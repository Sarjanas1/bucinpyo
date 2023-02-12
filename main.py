import asyncio
from sys import version as pyver

import pyrogram
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram import filters, idle
from pyrogram.errors import FloodWait
from pyrogram.types import Message

import config

from pyrogram import Client, filters

app = pyrogram.Client(
    "RexaBot",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

@app.on_message(filters.regex("p"))
def regex(app, message):
    app.send_message(message.chat.id,"ppp bang.")
    if len(message.regex) < 2:
                return await message.reply_text(
                    "**Usage**:\n/broadcastusers [MESSAGE] or [Reply to a Message]"
                )
            query = message.text.split(None, 1)[1]

@app.on_message(filters.regex("foto"))
def regex(app, message):
    app.send_photo(message.chat.id,"https://graph.org/file/6fd592fa2e0cc9ecc07f7.jpg")

@app.on_message(filters.regex("f"))
def regex(app, message):
    app.send_video(message.chat.id,"https://t.me/blamemelikeatrash/164")
    
print('bisa rex')
app.run()
