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
BOT_TOKEN = "6543286597:AAEjMjtxJO2he-RXV--TqpYtB7VM3deTwsg"
SESSION = "BQCMLuIAtEIImsYe1VYMNKKzamFqjUisb--vHvxkHP5_G_qLEnh_8krIN1u8pnm6WoWqMllvjzqFMZBfl4OXCQgG1i5B9UlUsycqnujmLNdMG4F9C0j4Uh3Xfc0NijTbQ0PAOAiqTBQTvzdc5Zw1jgJcZVHBfrjQ-p6JQI-vzoeGT2vzchzILg7cZAY1M8vYceLsI7CG9t1uEcOK5ieMo6wpz-6pDOt3tRwH2Eta4cxDuuZbEeMlh2qB4gwfvOiJRj_LTG5GV6xe0WaPl18SEC5YCNqiHog0X1TLykqP7yRTqnI9ETzTBgks0Gd1b1LAs6xiBPO-bx1u9sN3Owm7zyv2kBQ4BQAAAAG4gn41AA"
FORCESUB = "forcesubcl"
AUTH = 7390527029
DB_CHANNEL = -1002178432875
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
