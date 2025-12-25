from os import environ, getenv
from Script import script

# 🚀 Bot Configuration
SESSION = environ.get('SESSION', 'Govar x')  # Session name
API_ID = int(environ.get('API_ID', '28408609'))
API_HASH = environ.get('API_HASH', 'd6ddeafb0c189d91b8197ad49103e806')
BOT_TOKEN = environ.get('BOT_TOKEN', '8560596492:AAGl745Wqaz5EPDmLyWfsNow1-g0bRzmOBE')

# 👑 Owner & Admins
ADMINS = [int(i) for i in environ.get('ADMINS', '5665480584').split()]
AUTH_CHANNEL = [int(i) for i in environ.get("AUTH_CHANNEL", "").split()]
OWNER_USERNAME = environ.get("OWNER_USERNAME", 'ind_gamer_1')
BOT_USERNAME = environ.get("BOT_USERNAME", 'File_to_link_Go_bot')

# 🔗 Channel & Support Links
CHANNEL = environ.get('CHANNEL', 'https://t.me/All_Animes_in_teluguu_vs')
SUPPORT = environ.get('SUPPORT', 'https://t.me/All_Animes_in_teluguu_vs')
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', 'https://t.me/All_Animes_in_teluguu_vs')
HOW_TO_OPEN = environ.get('HOW_TO_OPEN', 'https://t.me/All_Animes_in_teluguu_vs')

# 📢 Log Channels
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", '-1002599753693'))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", '-1002599753693'))
PREMIUM_LOGS = int(environ.get("PREMIUM_LOGS", '-1002599753693'))
VERIFIED_LOG = int(environ.get('VERIFIED_LOG', '-1002599753693'))
SUPPORT_GROUP = int(environ.get("SUPPORT_GROUP", "-1002599753693"))

# ✅ Feature Toggles
VERIFY = False  # Enable user verification
FSUB = environ.get("FSUB", True)  # Force Subscribe
ENABLE_LIMIT = environ.get("ENABLE_LIMIT", True)
BATCH_VERIFY = False
IS_SHORTLINK = False
MAINTENANCE_MODE = environ.get("MAINTENANCE_MODE", False)
PROTECT_CONTENT = environ.get('PROTECT_CONTENT', False)
PUBLIC_FILE_STORE = environ.get('PUBLIC_FILE_STORE', True)
BATCH_PROTECT_CONTENT = environ.get('BATCH_PROTECT_CONTENT', False)

# 🔗 Shortlink Configuration
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')

# 💾 Database Configuration
DB_URL = environ.get('DATABASE_URI', "mongodb+srv://teddugovardhan544_db_user:WVjIA96jQ31net0j@cluster0.kwkkleo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get('DATABASE_NAME', "File-to-mm")

# 📸 Media & Images
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/3b53e1b446ae9a3c45b5b-f0a2d8f6f543c97e77.jpg')
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/3b53e1b446ae9a3c45b5b-f0a2d8f6f543c97e77.jpg")
AUTH_PICS = environ.get('AUTH_PICS', 'https://graph.org/file/3b53e1b446ae9a3c45b5b-f0a2d8f6f543c97e77.jpg')
PICS = environ.get('PICS', 'https://graph.org/file/3b53e1b446ae9a3c45b5b-f0a2d8f6f543c97e77.jpg')
FILE_PIC = environ.get('FILE_PIC', 'https://graph.org/file/3b53e1b446ae9a3c45b5b-f0a2d8f6f543c97e77.jpg')

# 📝 Captions
FILE_CAPTION=📁 <b>File Name:</b> {file_name}
BATCH_FILE_CAPTION=📦 <b>File Name:</b> {file_name}
CHANNEL_FILE_CAPTION=📢 <b>File Name:</b> {file_name}

# ⏱️ Time & Limits
PING_INTERVAL = int(environ.get("PING_INTERVAL", 1200))
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', 60))
RATE_LIMIT_TIMEOUT = int(environ.get("RATE_LIMIT_TIMEOUT", 600))
MAX_FILES = int(environ.get("MAX_FILES", 50))
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 60))  # Hours

# ⚙️ Worker & App Config
WORKERS = int(environ.get('WORKERS', 10))
MULTI_CLIENT = False
NAME = environ.get('name', 'Govar x')

# 🌐 Web Server
ON_HEROKU = 'DYNO' in environ
APP_NAME = environ.get('APP_NAME') if ON_HEROKU else None

PORT = int(environ.get('PORT', 2626))
NO_PORT = str(environ.get("NO_PORT", "true")).lower() in ("true", "1", "yes")
HAS_SSL = str(environ.get("HAS_SSL", "true")).lower() in ("true", "1", "yes")

# URL Generation
BIND_ADDRESS = environ.get("WEB_SERVER_BIND_ADDRESS", "file-link-fr1i.onrender.com/")   ##without https:// paste the base url here 
FQDN = environ.get("FQDN", BIND_ADDRESS)
if not FQDN.startswith("http"):
    PROTOCOL = "https" if HAS_SSL else "http"
    PORT_SEGMENT = "" if NO_PORT else f":{PORT}"
    
    # Clean up trailing slashes for consistency
    FQDN = FQDN.rstrip('/')
    URL = f"{PROTOCOL}://{FQDN}{PORT_SEGMENT}/"
else:
    URL = FQDN
