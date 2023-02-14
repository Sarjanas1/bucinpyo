# IMPORT BUKAN PYRO
import asyncio
from sys import version as pyver

# IMPORT CONFIG
import time
import config

# IMPORT PYRO
import pyrogram
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram import filters, idle
from pyrogram.errors import FloodWait
from pyrogram import enums

# IMPORT PYRO TYPES
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery 

app = pyrogram.Client(
    "RexaBot",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

# COMMAND START AND HELP

START_MESSAGE = """ 👋🏻 Halo saya Adalah bot yang dibuat untuk orang yang Rexa anggap Special
Ketik mulai untuk memulai Bot ini :)

👨‍💻 Owner :
"""
START_BUTTON = [
    [InlineKeyboardButton ('Rexa', url='https://t.me/JustRex')]
]

@app.on_message(filters.command("start") & filters.private)
def start(app, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_BUTTON)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
# MULAI 
@app.on_message(filters.regex("mulai"))
def chat_actions(app, message):
    app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(2)
    app.send_message(message.chat.id,"Ketik nama kamu terlebih dahulu agar saya bisa cek apakah benar kamu orang yang Rexa tuju")

# REGEX CARI NAMA
@app.on_message(filters.regex("jean"))
@app.on_message(filters.regex("jeann"))
def chat_actions(app, message):
    app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    app.send_message(message.chat.id,"benersih nama asli, cuma ga mau yang ini wleeeeeeeeee 😜")

@app.on_message(filters.regex("diva"))
@app.on_message(filters.regex("div"))
@app.on_message(filters.regex("diva"))
@app.on_message(filters.regex("dipa"))
def chat_actions(app, message):
    app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    app.send_message(message.chat.id,"benersih nama asli, cuma ga mau yang ini wleeeeeeeeee 😜")


# ESEKUSI 1

@app.on_message(filters.regex("indri"))
@app.on_messafe(filters.regex("indriasari))
def regex(app, message):
    app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(2)
    app.send_message(message.chat.id,""" Nah ini nama yang bener hehehe !!!
                                        Halo indri 👋🏻 gimana hari ini? Asik tidak? saya harap sih asik selalu ya!!
Gimana ? kaget ga, ternyata kamu orangnya!!! keknya sih engga muhehe

Hummm Kamu penasaran Gak aku mau ngomong apa? Kalo penasaran coba deh Ketik penasaran :)
""")

@app.on_message(filters.regex("penasaran"))
@app.on_messafe(filters.regex("pnasaran"))
def regex(app, message):
    app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(2)
    app.send_message(message.chat.id,""" Idih Kepo?? muhehehe becanda ya!!!
Oke jadi di bot ini Gua (Rexa) Cuma mau sampein sedikit banyak eh gmna ya -,-, Intinya gini

coba Kamu ketik intinya
""")


# REGEX SEND MEDIA
@app.on_message(filters.regex("foto"))
def regex(app, message):
    app.send_photo(message.chat.id,"https://graph.org/file/6fd592fa2e0cc9ecc07f7.jpg")

@app.on_message(filters.regex("f"))
def regex(app, message):
    app.send_video(message.chat.id,"https://t.me/blamemelikeatrash/164")
    

print('loading cuy')
print('•')
print('••')
print('•••')
print('bisa rex')
print('gaskeun rex!!')
app.run()
