# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 26862233  # Get this value from my.telegram.org/apps
    API_HASH = "28ba253a514409ad88fe84902590b6c0"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "mongodb+srv://smkthebotz:7jcBnVS8WgBod1fO@cluster0.ciut5k2.mongodb.net/?retryWrites=true&w=majority"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1002053184012
    MESSAGE_DUMP = -1002053184012

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://smkthebotz:7jcBnVS8WgBod1fO@cluster0.ciut5k2.mongodb.net/?retryWrites=true&w=majority"

    # Support chat and support ID
    SUPPORT_CHAT = "SMKSUPPORTGROUP"
    SUPPORT_ID = -1002093662679

    # Database name
    DB_NAME = "cluster0"

    # Bot token
    TOKEN = "6914941062:AAH64uhnFX0YCy3wfi981D_hTBd1mcRzXOY"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 5340652544
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = []  # Sudo users
    DEV_USERS = []  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
