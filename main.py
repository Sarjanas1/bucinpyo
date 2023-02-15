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

    [  
        InlineKeyboardButton("Rexa", url="https://t.me/JustRex"),              
    ],            
]            
@app.on_message(filters.command("start") & filters.private)
async def start(_, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_BUTTON)
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

# MULAI 
@app.on_message(filters.regex("mulai"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(2)
    await app.send_message(message.chat.id, "Ketik nama kamu terlebih dahulu agar saya bisa cek apakah benar kamu orang yang Rexa tuju")

# REGEX CARI NAMA
@app.on_message(filters.regex("jean|jeann"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, "benersih nama asli, cuma ga mau yang ini wleeeeeeeeee 😜")

@app.on_message(filters.regex("diva|div|dipa|diva"))
async def actions_chat(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, "benersih nama asli, cuma ga mau yang ini wleeeeeeeeee 😜")


# ESEKUSI 1

@app.on_message(filters.regex("indriasari|indri"))
async def regex_indri(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(2)
    TEXT = """
Nah ini nama yang bener hehehe !!!
Halo indri 👋🏻 gimana hari ini? Asik tidak? saya harap sih asik selalu ya!!
Gimana ? kaget ga, ternyata kamu orangnya!!! keknya sih engga muhehe

Hummm Kamu penasaran Gak aku mau ngomong apa? Kalo penasaran coba deh Ketik penasaran :)
"""
    await app.send_message(message.chat.id, text=TEXT)

@app.on_message(filters.regex("pnasaran|penasaran"))
async def regexpena(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(2)
    TEXT = """
Idih Kepo?? muhehehe becanda ya!!!
Oke jadi di bot ini Gua (Rexa) Cuma mau sampein sedikit banyak eh gmna ya -,-, Intinya gini

coba Kamu ketik intinya
"""
    await app.send_message(message.chat.id, text=TEXT)

@app.on_message(filters.regex("inti|intinya"))
async def regexinti(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(2)
    TEXT = """
Gua cuma mau Berterima Kasih Karena udah kenal sama aku
dan jadi temen baik, sering cerita dll intinya terimakasih banyakk yakk!!!
sebenernya ada lagi tapi aku gamau ngeliat kamu cape typing jadi kita main tombol aja yak !!

Sekarang kamu pencet -> /akukepo
""" 
    await app.send_message(message.chat.id, text=TEXT)


# CALLBACK TOMBOL YA INI !

AKUKEPO = "Cieeeee Kepo Bgt ya anda, heheh langsung aja klik tombol dibawah :)"

AKUKEPOTOMBOL = [

    [  
        InlineKeyboardButton("KLIK DISINI", callback_data="kesatu"),              
    ],            
]            

@app.on_message(filters.command("akukepo") & filters.private)
async def akukepo(_, message):
    await message.reply(
        text = AKUKEPO,
        reply_markup = InlineKeyboardMarkup(AKUKEPOTOMBOL)
    )

@app.on_callback_query(filters.regex("^kesatu|kedua|ketiga|keempat|kelima|keenam|ketujuh|kedelapan|kesembilan|selesai"))
async def kesatu(_, callback_query):
    query = callback_query.data.split()
    if query[0] == "kesatu":
        KESATU = """
Pertama aku mau berterimakasih banget udah ngehargain Karya Bot saya dan
Terimakasih banget udah Mau Bantu udah jadi Temen cerita sampe Jadi alasan gua buka Chat Telegram
Selain Karna orderan Bot :)

Intinya Terimakasih Banyak Untuk kamu
Pencet Tombol Lanjut kalo seru
"""  
        KESATUTOMBOL = [
            [
                InlineKeyboardButton("KEMBALI KE MENU", callback_data="akukepo"),
                InlineKeyboardButton("LANJUT", callback_data="kedua"),
            ],
        ]
        await callback_query.edit_message_text(
            KESATU, reply_markup=InlineKeyboardMarkup(KESATUTOMBOL)
        )

    if query[0] == "kedua":
        KEDUA = """
TES 2
""" 
        KEDUATOMBOL = [
            [
                InlineKeyboardButton("KEMBALI KE SATU", callback_data="kembali_ke_satu"),
                InlineKeyboardButton("LANJUT", callback_data="ketiga"),
                ]
            ]
        await callback_query.edit_message_text(
            KEDUA, reply_markup=InlineKeyboardMarkup(KEDUATOMBOL)
        )

    if query[0] == "ketiga":
        KETIGA = """
TES 3
"""
        KETIGATOMBOL = [
            [
                InlineKeyboardButton("KEMBALI KE DUA", callback_data="kedua"),
                InlineKeyboardButton("LANJUT", callback_data="keempat"),
                ]
            ]
        await callback_query.edit_message_text(
            KETIGA, reply_markup=InlineKeyboardMarkup(KETIGATOMBOL)
        )

    if query[0] =="keempat":
        KEEMPAT = """
TES 4
"""
        KEEMPATTOMBOL = [
            [
                InlineKeyboardButton("KEMBALI KETIGA", callback_data="ketiga"),
                InlineKeyboardButton("LANJUT", callback_data="kelima"),
                ]
            ]
        await callback_query.edit_message_text(
            KEEMPAT, reply_markup=InlineKeyboardMarkup(KEEMPATTOMBOL)
        )

    if query[0] =="kelima":
        KELIMA = """
TES 5
"""
        KELIMATOMBOL = [
           [
               InlineKeyboardButton("KEMBALI KEEMPAT", callback_data="keempat"),
               InlineKeyboardButton("LANJUT", callback_data="keenam"),
               ]
            ]
        await callback_query.edit_message_text(
            KELIMA, reply_markup=InlineKeyboardMarkup(KELIMATOMBOL)
        )

    if query[0] =="keenam":
        KEENAM = """
TES 6
"""
        KEENAMTOMBOL = [
            [
                InlineKeyboardButton("KEMBALI KELIMA", callback_data="kelima"),
                InlineKeyboardButton("LANJUT", callback_data="ketujuh"),
                ]
            ]
        await callback_query.edit_message_text(KEENAM, reply_markup=InlineKeyboardMarkup(KEENAMTOMBOL)
        )

    if query[0] =="ketujuh":
        KETUJUH = """
TES 7
"""
        KETUJUHTOMBOL = [
            [
                InlineKeyboardButton("KEMBALI KEENAM", callback_data="keenam"),
                InlineKeyboardButton("LANJUT", callback_data="kedelapan"),
                ]
            ]
        await callback_query.edit_message_text(KETUJUH, reply_markup=InlineKeyboardMarkup(KETUJUHTOMBOL)
        )

    if query[0] =="kedelapan":
        KEDELAPAN = """
TES 8
"""
        KEDELAPANTOMBOL = [
            [
                InlineKeyboardButton("KEMBALI KEDELAPAN", callback_data="ketujuh"),
                InlineKeyboardButton("SELESAI", callback_data="kesembilan"),
                ]
            ]
        await callback_query.edit_message_text(KEDELAPAN, reply_markup=InlineKeyboardMarkup(KEDELAPANTOMBOL)
        )

    if query[0] =="kesembilan":
        KESEMBILAN = """
TES 9
"""
        KESEMBILANTOMBOL = [
            [
                InlineKeyboardButton("KEMBALI KEDELAPAN", callback_data="kedelapan"),
                InlineKeyboardButton("SELESAI", callback_data="selesai"),
                ]
            ]
        await callback_query.message.delete(KESEMBILAN)

# REGEX SEND MEDIA
@app.on_message(filters.regex("foto"))
async def regex_foto(_, message):
    await app.send_photo(message.chat.id, "https://graph.org/file/6fd592fa2e0cc9ecc07f7.jpg")

@app.on_message(filters.regex("f"))
async def regex_v(_, message):
    await app.send_video(message.chat.id, "https://t.me/blamemelikeatrash/164")
    

print('loading cuy')
print('•')
print('••')
print('•••')
print('bisa rex')
print('gaskeun rex!!')
app.run()
