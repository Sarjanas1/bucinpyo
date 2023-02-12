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

@app.on_message(filters.command('start') & filters.private)
def command(app, message):
    app.send_message(message.chat.id,"ppp bang.")
    
print('bisa rex')
app.run()
