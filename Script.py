class script(object):

    START_TXT = (
        "<b>Hey {},</b>\n\n"
        "<blockquote><b>"
        "Send me a file or add me as an admin to any channel to instantly generate file links.\n\n"
        "Invite me to your channel and I’ll instantly create download links for any media you share. "
        "I’ll also add the right buttons to each post with a URL, making access seamless."
        "</b></blockquote>\n\n"
        "<blockquote><b>"
        "<a href='https://t.me/File_to_link_Go_bot?startchannel&admin=post_messages+edit_messages+delete_messages'>➜ Add To Channel</a>"
        "</b></blockquote>"
    )

    RESTART_TXT = (
        "<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !\n\n"
        "📅 Dᴀᴛᴇ : <code>{}</code>\n"
        "⏰ Tɪᴍᴇ : <code>{}</code>\n"
        "🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>\n"
        "🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : <code>v4.6.00 [ Stable ]</code>"
        "</b>"
    )

    HELP_TXT = (
        "<blockquote><b>"
        "You don't need many commands to use this bot.\n\n"
        "Just send me files and I will give you direct download & streaming links.\n\n"
        "You can also use me in your channel — just add me as admin and see my power 💥\n\n"
        "For more info use /help\n"
        "About bot use /about"
        "</b></blockquote>"
    )

    ADMIN_CMD_TXT = (
        "<blockquote><b>"
        "# Admin Only Commands 👑\n\n"
        "/ban - Ban a user/channel\n"
        "/unban - Unban a user/channel\n"
        "/broadcast - Send broadcast message\n"
        "/pin_broadcast - Send & pin broadcast\n"
        "/restart - Restart the bot\n"
        "/stats - Show bot statistics\n"
        "/blocked - List blocked users\n"
        "</b></blockquote>"
    )

    HELP2_TXT = (
        "<blockquote><b>"
        "HOW TO USE FILE TO LINK BOT\n\n"
        "BASIC USAGE:\n"
        "• SEND ANY FILE OR MEDIA\n"
        "• BOT GENERATES PERMANENT DOWNLOAD & STREAM LINKS\n"
        "• PASTE STREAM LINK INTO ANY VIDEO PLAYER\n\n"
        "KEY FEATURES:\n"
        "• PERMANENT LINKS\n"
        "• DIRECT DOWNLOAD\n"
        "• VIDEO STREAMING\n"
        "• CHANNEL SUPPORT\n"
        "• UNLIMITED FILE SIZE\n\n"
        "CHANNEL USAGE:\n"
        "1. ADD BOT AS ADMIN\n"
        "2. SEND FILES\n"
        "3. LINKS AUTO-GENERATED\n\n"
        "⚠️ IMPORTANT NOTES:\n"
        "• LINKS NEVER EXPIRE\n"
        "• ADULT CONTENT STRICTLY PROHIBITED\n\n"
        "📮 HELP & SUPPORT:\n"
        "• UPDATES & SUPPORT: @ind_gamer_1\n\n"
        "<u>REPORT BUGS TO "
        "<a href='https://t.me/ind_gamer_1'>DEVELOPER</a></u>"
        "</b></blockquote>"
    )

    CAPTION = "<b>🎬 <a href='{}'>{}</a></b>"

    LOG_TEXT = (
        "<b>#NEW_USER {}\n\n"
        "ID : <code>{}</code>\n"
        "NAME : {}"
        "</b>"
    )

    ABOUT_TXT = (
        "<blockquote><b>"
        "╔══❰ {} ❱═════❍\n"
        "║╭━━━━━━━━━━━━━━━━━━➣\n"
        "║┣⪼ 🤖 BOT NAME : {}\n"
        "║┣⪼ 👦 DEVELOPER : <a href='https://t.me/ind_gamer_1'>OWNER</a>\n"
        "║┣⪼ ❣️ UPDATES : <a href='https://t.me/ind_gamer_1'>@ind_gamer_1</a>\n"
        "║┣⪼ ⏲️ UPTIME : {}\n"
        "║┣⪼ 📡 HOSTING : KOYEB\n"
        "║┣⪼ 🗣️ LANGUAGE : PYTHON\n"
        "║┣⪼ 📚 LIBRARY : PYROGRAM\n"
        "║┣⪼ 🗒️ VERSION : {} [STABLE]\n"
        "║╰━━━━━━━━━━━━━━━➣\n"
        "╚══════════════════❍"
        "</b></blockquote>"
    )

    AUTH_TXT = (
        "<b>"
        "HEY {}! 👋\n\n"
        "TO CONTINUE USING THIS BOT, PLEASE JOIN OUR UPDATES CHANNEL 💬\n\n"
        "SERVER LOAD IS HIGH, ACCESS IS LIMITED TO CHANNEL MEMBERS ONLY 🚀"
        "</b>"
    )

    CAPTION_TXT = (
        "<b>{file_name}</b>\n\n"
        "Size : <b>{file_size}</b>\n"
        "Year : <b>{year}</b>\n"
        "Quality : <b>{quality}</b>\n"
        "Language : <b>{language}</b>\n\n"
        "➠ Stream Link : <a href='{stream_link}'>Click Here</a>\n\n"
        "➠ Download Link : <a href='{download_link}'>Click Here</a>\n\n"
        "➠ Telegram File : <a href='{telegram_file}'>Click Here</a>"
    )

    VERIFICATION_TEXT = (
        "<b>HEY {},\n\n"
        "<u>YOU ARE NOT VERIFIED TODAY.\n"
        "TAP THE VERIFY LINK AND GET UNLIMITED ACCESS FOR 24 HOURS.</u>"
        "</b>"
    )

    VERIFIED_COMPLETE_TEXT = (
        "<b>HEY {},\n\n"
        "YOU ARE NOW VERIFIED FOR TODAY ☺️\n"
        "ENJOY UNLIMITED MOVIE & SERIES LINKS 💥"
        "</b>"
    )

    VERIFIED_LOG_TEXT = (
        "<b><u>☄ USER VERIFIED SUCCESSFULLY ☄</u>\n\n"
        "⚡️ NAME : {} [ <code>{}</code> ]\n"
        "📆 DATE : <code>{}</code>\n\n"
        "#VERIFIED_COMPLETED"
        "</b>"
    )
