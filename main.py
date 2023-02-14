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
@app.on_message(filters.regex("indriasari"))
def regex(app, message):
    app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(2)
    app.send_message(message.chat.id,""" Nah ini nama yang bener hehehe !!!
Halo indri 👋🏻 gimana hari ini? Asik tidak? saya harap sih asik selalu ya!!
Gimana ? kaget ga, ternyata kamu orangnya!!! keknya sih engga muhehe

Hummm Kamu penasaran Gak aku mau ngomong apa? Kalo penasaran coba deh Ketik penasaran :)
""")

@app.on_message(filters.regex("penasaran"))
@app.on_message(filters.regex("pnasaran"))
def regex(app, message):
    app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(2)
    app.send_message(message.chat.id,""" Idih Kepo?? muhehehe becanda ya!!!
Oke jadi di bot ini Gua (Rexa) Cuma mau sampein sedikit banyak eh gmna ya -,-, Intinya gini

coba Kamu ketik intinya
""")

@app.on_message(filters.regex("intinya"))
@app.on_message(filters.regex("inti"))
def regex(app, message):
    app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(2)
    app.send_message(message.chat.id,""" Gua cuma mau Berterima Kasih Karena udah kenal sama aku
dan jadi temen baik, sering cerita dll intinya terimakasih banyakk yakk!!!
sebenernya ada lagi tapi aku gamau ngeliat kamu cape typing jadi kita main tombol aja yak !!

Sekarang kamu pencet -> /akukepo
""")


# CALLBACK TOMBOL YA INI !!

AKUKEPO = "Cieeeee Kepo Bgt ya anda, heheh langsung aja klik tombol dibawah :)"

AKUKEPOTOMBOL = [
    [InlineKeyboardButton ('KLIK DISINI', callback_data="KESATU")]
]

@app.on_message(filters.command("akukepo") & filters.private)
def akukepo(app, message):
    message.reply(
        text = AKUKEPO,
        reply_markup = InlineKeyboardMarkup(AKUKEPOTOMBOL)
    )

@app.on_callback_query()
def callback_query(Client, CallbackQuery):
    if CallbackQuery.data == "KLIK DISINI":

        KESATU = """ Pertama aku mau berterimakasih banget udah ngehargain Karya Bot saya dan
Terimakasih banget udah Mau Bantu udah jadi Temen cerita sampe Jadi alasan gua buka Chat Telegram
Selain Karna orderan Bot :)

Intinya Terimakasih Banyak Untuk kamu
Pencet Tombol Lanjut kalo seru

"""  
 
        KESATUTOMBOL = [
            [
                [InlineKeyboardButton ('KEMBALI KE MENU', callback_data="KEMBALI KE MENU"),
                [InlineKeyboardButton ('LANJUT', callback_data="KEDUA")
            ]
        ]

        CallbackQuery.edit_message_text(
           KESATU,
           reply_markup = InlineKeyboardMarkup(KESATUTOMBOL)
        )

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
