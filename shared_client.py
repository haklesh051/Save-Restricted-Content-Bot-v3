from telethon import TelegramClient
from telethon.errors import FloodWaitError
from config import API_ID, API_HASH, BOT_TOKEN, STRING
from pyrogram import Client
import asyncio
import sys

client = TelegramClient("telethonbot", API_ID, API_HASH)
app = Client("pyrogrambot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
userbot = Client("4gbbot", api_id=API_ID, api_hash=API_HASH, session_string=STRING)

async def start_client():
    # Start Telethon Bot
    try:
        if not client.is_connected():
            await client.start(bot_token=BOT_TOKEN)
            print("✅ Telethon bot started")
    except FloodWaitError as e:
        print(f"⛔ Telethon FloodWait: wait {e.seconds} seconds")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Telethon failed: {e}")
        sys.exit(1)

    # Start Pyrogram Bot
    try:
        await app.start()
        print("✅ Pyrogram bot started")
    except Exception as e:
        print(f"❌ Pyrogram bot error: {e}")
        sys.exit(1)

    # Start Userbot (if STRING present)
    if STRING:
        try:
            await userbot.start()
            print("✅ Userbot started")
        except Exception as e:
            print(f"❌ Userbot error: Session invalid or expired: {e}")
            sys.exit(1)

    return client, app, userbot
