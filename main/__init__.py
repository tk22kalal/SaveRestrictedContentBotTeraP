#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24058425
API_HASH = "694b063e55c24287a3d30aed90191373"
BOT_TOKEN = "7482584259:AAHbnDAq7nBXsC50if9rK0dOivlLG9XlvcQ"
SESSION = "BQCMLuIAhzhCjSe5570KRaB_uThKmEJ13nMn4o3BCSdQPIGrkv_RyfrEG63Icb3VbM0SeNR5hQhGWFz-tEVu_6Rf4XLSQ02MOkx8VEE1zbkeOP7JonMk6P8tzTYwjIOosfRZoG2xA53PvlpCrjZKwpad2xhVZleTlYlv80Ocjgld65f5TRklL992eKgR1sm3Gy9TtJoqoFE_bhdrZTxfvIrCyTKDVCy0Gsicm60cvAvKA1zx5iwpuAMpZDot4HSRlvljlT10jhGF1q1yQgGUcvqsbFhaRuVQYIRlxwQDnuBFFnw07bz-gKjSDbEogBIpNkFM3MsZcWOZjk0Oz_KnhyuwZLfzzwAAAAGX-jAhAA"
AUTH = 6844723233
FORCESUB = "forcesubpavo4"
DB_CHANNEL = -1002010535930
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
