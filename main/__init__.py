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
BOT_TOKEN = "6783282067:AAEy5SBcI3_5sJbTN2LASAZVZJT9jhbsCPk"
SESSION = "BQCMLuIASYK9cT9x0JahiFdPXz5-rGKjZl6OYcY1lN7Iu_ptg58BTgEoBkqyIKqI5nb8PL-P5G5V8RTpUPuVE1fmEAwrG8gl6c28uiz6OKp2qm3kKyBwOJl-Z6sLAVylt02ZXP7AzHA43xXrVeWaXlqdWRObBgxUrrAVXG_nDhmZbmyauo_KHQMMhcLZq7wqr2uZtBecmzj5aDAjYZLMOuT8AFCOWXtAzljnJxYtpQGngNh0FqZAib_f5QEV3FzkVLLxZJHI2kww5YjhkzUIwwhUyfQ5e1eBBJENLHq1SerVT-4h-mYM8TSdlyxLzz61J6wkQw8uX5uEtwbo1FRaB-HDgOJ9HQAAAAGX-jAhAA"
FORCESUB = "forcesubpavo4"
AUTH = 6844723233
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
