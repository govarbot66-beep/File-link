import os
import re
import json
import base64
from struct import pack

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import ChannelInvalid, UsernameInvalid, UsernameNotModified
from pyrogram.file_id import FileId

from info import LOG_CHANNEL, ADMINS, PUBLIC_FILE_STORE, BOT_USERNAME


# ================= ACCESS CONTROL =================
async def allowed(_, __, message: Message):
    if PUBLIC_FILE_STORE:
        return True
    if message.from_user and message.from_user.id in ADMINS:
        return True
    return False


# ================= FILE ID HELPERS =================
def encode_file_id(s: bytes) -> str:
    r = b""
    n = 0
    for i in s + bytes([22]) + bytes([4]):
        if i == 0:
            n += 1
        else:
            if n:
                r += b"\x00" + bytes([n])
                n = 0
            r += bytes([i])
    return base64.urlsafe_b64encode(r).decode().rstrip("=")


def encode_file_ref(file_ref: bytes) -> str:
    return base64.urlsafe_b64encode(file_ref).decode().rstrip("=")


def unpack_new_file_id(new_file_id: str):
    decoded = FileId.decode(new_file_id)
    file_id = encode_file_id(
        pack(
            "<iiqq",
            int(decoded.file_type),
            decoded.dc_id,
            decoded.media_id,
            decoded.access_hash
        )
    )
    file_ref = encode_file_ref(decoded.file_reference)
    return file_id, file_ref


# ================= BATCH HANDLER =================
@Client.on_message(filters.command(["batch", "pbatch"]) & filters.create(allowed))
async def gen_link_batch(bot: Client, message: Message):

    if len(message.command) != 3:
        return await message.reply(
            "❌ Use correct format:\n"
            "<code>/batch https://t.me/ind_gamer_1/10 https://t.me/ind_gamer_1/30</code>"
        )

    cmd, first, last = message.command

    regex = re.compile(
        r"(https://)?(t\.me|telegram\.me|telegram\.dog)/(c/)?([\w\d_]+)/(\d+)"
    )

    def parse(link):
        m = regex.match(link)
        if not m:
            return None, None
        chat = m.group(4)
        msg_id = int(m.group(5))
        if chat.isnumeric():
            chat = int("-100" + chat)
        return chat, msg_id

    f_chat, f_msg = parse(first)
    l_chat, l_msg = parse(last)

    if not f_chat or not l_chat:
        return await message.reply("❌ Invalid Telegram link")

    if f_chat != l_chat:
        return await message.reply("❌ Both links must be from the same channel")

    try:
        chat_id = (await bot.get_chat(f_chat)).id
    except ChannelInvalid:
        return await message.reply("❌ Make me admin in @ind_gamer_1")
    except (UsernameInvalid, UsernameNotModified):
        return await message.reply("❌ Invalid username")
    except Exception as e:
        return await message.reply(f"❌ Error: {e}")

    status = await message.reply("⏳ Generating batch link...")

    outlist = []
    total_range = l_msg - f_msg + 1
    saved = 0

    async for msg in bot.iter_messages(
        chat_id,
        min_id=f_msg - 1,
        max_id=l_msg
    ):
        if not msg.media:
            continue

        try:
            media = getattr(msg, msg.media.value)
            outlist.append({
                "file_id": media.file_id,
                "caption": msg.caption.html if msg.caption else "",
                "title": getattr(media, "file_name", ""),
                "size": media.file_size,
                "protect": cmd == "pbatch"
            })
            saved += 1
        except:
            pass

        if saved % 20 == 0:
            await status.edit(
                f"📦 Batch Progress\n"
                f"Total Range: `{total_range}`\n"
                f"Saved Files: `{saved}`"
            )

    if not outlist:
        return await status.edit("❌ No media files found in given range")

    filename = f"batch_{message.from_user.id}_{message.id}.json"
    with open(filename, "w") as f:
        json.dump(outlist, f)

    post = await bot.send_document(
        LOG_CHANNEL,
        filename,
        file_name="Batch.json",
        caption="📁 Batch generated"
    )

    os.remove(filename)

    file_id, _ = unpack_new_file_id(post.document.file_id)

    await status.edit(
        f"✅ Batch link generated successfully!\n"
        f"Files: `{saved}`\n\n"
        f"🔗 https://t.me/{BOT_USERNAME}?start=BATCH-{file_id}"
)
