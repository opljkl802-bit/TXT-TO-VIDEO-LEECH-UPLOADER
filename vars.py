

from os import environ

API_ID = int(environ.get("API_ID","30296254", ""))
API_HASH = environ.get("API_HASH","c2b5306f4ccd2d795405a026c10b4c62", "")
BOT_TOKEN = environ.get("BOT_TOKEN","8697727988:AAHFPX-fMxt61jqOyFlJEbLJO7EwR1TEP4M", "")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "gkfjldlkfvoifg")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/gkfjldlkfvoifg")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("6320092636", "").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("7660916897", ""))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")





