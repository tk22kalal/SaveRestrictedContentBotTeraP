#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 27326793
API_HASH = "2e122c532cc3c2a3b62d18ef0bd35ff4"
BOT_TOKEN = "6808721007:AAGeXwj2QigEX_YxDjU_VxC_kecDdSuIiT0"
SESSION = "BACMLuIAUpu4UNOACwdTJudZsa5Akso54yDf7FaYlfvX8y5UJtFLjK7V4_8v1sHotgHT1iosV_MRLujigNpCg8KOJm34i0zy9zHoC-hEiw0r04o4mr4n8cQiB_L3mgBcrga2TdA0ypMz744YXSol8hrtoeLljbUcPomztTCbIRe7hWFrnK95pfi1-uOumSEG6KhyDU8t5-_UhtAryPBD-2-ngfEkzIh-RjHI2UyIsjU36gYiXad4HFAZz8nYL6iM73xDhAIvoxb8XJ6_gvq1zKEOsKYXSYhpRvm3q7VQoP_GDjDRYQlyp_iyt6jdBaDinB63YRNq3hMRE5vyr3oww0afSfUNbgAAAAF8vK0nAA"
AUTH = 6387707175
FORCESUB = "forcesubc"
DB_CHANNEL = -1002216207474
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
