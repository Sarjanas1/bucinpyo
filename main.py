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
👋🏻 Pertama aku mau berterimakasih banget udah ngehargain Karya Bot saya dan
Terimakasih banget udah Mau Bantu udah jadi Temen cerita sampe Jadi alasan gua buka Chat Telegram
Selain Karna orderan Bot :)

Intinya Terimakasih Banyak Untuk kamu
Pencet Tombol Lanjut kalo seru
"""  
        KESATUTOMBOL = [
            [
                InlineKeyboardButton("HAPUS", callback_data="selesai"),
                InlineKeyboardButton("Lanjut", callback_data="kedua"),
            ],
        ]
        await callback_query.edit_message_text(
            KESATU, reply_markup=InlineKeyboardMarkup(KESATUTOMBOL)
        )

    if query[0] == "kedua":
        KEDUA = """
‼️ Aku pengen bilang ini !!!
Stop jadi orang ga enakan ! pelan pelan aja keluar dari zona nyaman kamu yang selalu di lakuin seenaknya!

Kesel wei !! Ngeliat kamu digituin terus sama orang orang, kenapasih !! emang ga cape?
ya jadi orang baik emang ga salah cuma jangan terus terusan kamu yang di jajah! Ngerti ga? Pokoknya kurang kurangin rasa ga enakannya ya !! 🙎‍♂️🙎‍♂️
""" 
        KEDUATOMBOL = [
            [
                InlineKeyboardButton("Balik ke 1", callback_data="kesatu"),
                InlineKeyboardButton("Lanjut", callback_data="ketiga"),
                ]
            ]
        await callback_query.edit_message_text(
            KEDUA, reply_markup=InlineKeyboardMarkup(KEDUATOMBOL)
        )

    if query[0] == "ketiga":
        KETIGA = """
Siap siap !!!!!! 😡😡
Saya mau ngomelin lagi !!!
Jangan terlalu gampang diandelin tau ga! Ayah mu bener ngomong kek gitu, jangan batu napa sih!!
udah stop terlalu care buat orang lain, Care nya kediri sendiri aja sih ah elahhhhhhhhhhhh!

Kamu cantik kamu baik tapi jgn mau di perlakukan seenaknya sama orang! inget !!!
"""
        KETIGATOMBOL = [
            [
                InlineKeyboardButton("Balik ke 2", callback_data="kedua"),
                InlineKeyboardButton("Lanjut", callback_data="keempat"),
                ]
            ]
        await callback_query.edit_message_text(
            KETIGA, reply_markup=InlineKeyboardMarkup(KETIGATOMBOL)
        )

    if query[0] =="keempat":
        KEEMPAT = """
Dip inget ga ? Waktu pertama kali kamu kenal aku? Malahan sebelum kenal saya deh
waktu di os LF dulu sebenarnya aku udah penasaran sama kamu, karena bio nya bekasi hehehe

tapi karena saya anaknya pemalu dan sombong ( sombong karna saya bisa kalo gabisa saya ga sombong)
jadi saya ga tertarik buat chat, tapi jujur aku anaknya ga berani ngechat, kalo suka ya suka aja diem diem hehehe
"""
        KEEMPATTOMBOL = [
            [
                InlineKeyboardButton("Balik ke 3", callback_data="ketiga"),
                InlineKeyboardButton("Lanjut", callback_data="kelima"),
                ]
            ]
        await callback_query.edit_message_text(
            KEEMPAT, reply_markup=InlineKeyboardMarkup(KEEMPATTOMBOL)
        )

    if query[0] =="kelima":
        KELIMA = """
Nah lama kelamaaan kok ngobrol sama kamu asik, Dulu tuh bikin Bot whatsapp sengaja biar kamu tau nomer wasap ku hehe
dan akhirnya kamu kepancing kan buat diwasap sampe kita bikin group

sebenarnya itu trik biar ak bisa deketik km wkwk maap yaaa tapi yaudahlah kan ga terlalu cringe juga usahanya
"""
        KELIMATOMBOL = [
           [
               InlineKeyboardButton("Balik ke 4", callback_data="keempat"),
               InlineKeyboardButton("Lanjut", callback_data="keenam"),
               ]
            ]
        await callback_query.edit_message_text(
            KELIMA, reply_markup=InlineKeyboardMarkup(KELIMATOMBOL)
        )

    if query[0] =="keenam":
        KEENAM = """
lama kelamaan kita mulai ga kontekan tuh, sebenernya emang jarang sih, apalagi waktu ada problem sama sirkel kamu itu, tapi its okay, aku paham kamu lagi asik sama mereka
dan tau ga? aku tu sebenernya kek ngerasa kehilangan, kek mikirnya gini "Duh keknya bakal gagal deh gua deketin si jean" gitu dalem hati
dan setiap hari tuh selalu ngomong gini dalam hati "Gua bisa ga ya sama jean" "jean suka ga ya sama gua" heheh cringe tapi yaudahlah

Karena gua lebih suka diem diem suka daripada langsung ngomong, gua juga orangnya ga asal, jadi harus pastiin dulu apa bener bener perasaan gua ada ga buat lu hehehe
"""
        KEENAMTOMBOL = [
            [
                InlineKeyboardButton("Balik ke 5", callback_data="kelima"),
                InlineKeyboardButton("Lanjut", callback_data="ketujuh"),
                ]
            ]
        await callback_query.edit_message_text(KEENAM, reply_markup=InlineKeyboardMarkup(KEENAMTOMBOL)
        )

    if query[0] =="ketujuh":
        KETUJUH = """
Keknya aku harus jujur sama kamu, hehehe 

Jadi intinya aku suka kamu, mungkin bisa dibilang nyaman, kalo sayang pasti karena kita temenan
tapi ini rasanya beda dan kek pengen effort buat kamu, ngerti ga sih -,- !!

pasti ngerti deh, kek setiap hari nyari tau tentang kamu gitu, dll, sebenrnya saya suka banget :)
"""
        KETUJUHTOMBOL = [
            [
                InlineKeyboardButton("Balik ke 6", callback_data="keenam"),
                InlineKeyboardButton("Lanjut", callback_data="kedelapan"),
                ]
            ]
        await callback_query.edit_message_text(KETUJUH, reply_markup=InlineKeyboardMarkup(KETUJUHTOMBOL)
        )

    if query[0] =="kedelapan":
        KEDELAPAN = """
Ini cuma ungkapan ya, jadi aku ga nembak kamu, cuma ya mau anu, apasih namanya, kek ngungkapin aja yang perasaan yang sebenarnya,

Saya ga pengen dibales kek apalah cuma mau confess aja sih ke kamu, yaaa maap ya caranya aga cringe lewat bot, hehe tapi aku anaknya emamg gini
mau sesuatu yang beda, yang orang lain ga kepikiran, jadi ya bikin bot dari 0% sampe jadi gini, mu

Ga bagus sih, cuma ya yang penting tersampaikan aja, Btw Mau nanya dong? Jujur aja Kamu Sebalikanya ga Ke saya? 
Coba abis pencet tombol selesai, bales ya ketik Iya atau Gak aku tunggu 😜
"""
        KEDELAPANTOMBOL = [
            [
                InlineKeyboardButton("Balik ke 7", callback_data="ketujuh"),
                InlineKeyboardButton("Selesai", callback_data="selesai"),
                ]
            ]
        await callback_query.edit_message_text(KEDELAPAN, reply_markup=InlineKeyboardMarkup(KEDELAPANTOMBOL)
        )

    if query[0] =="selesai":
        SELESAI = """
Selesai
"""
        SELESAITOMBOL = [
            [
                InlineKeyboardButton("Balik ke 8", callback_data="kedelapan"),
                InlineKeyboardButton("SELESAI", callback_data="selesai"),
                ]
            ]
        await callback_query.message.delete(KESEMBILAN)

# GA ATAU IYA

@app.on_message(filters.regex("engga|G|enggak|gak|ga"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, """
gapapa kok santai saya mengerti, apalagi kamu punya trauma aku ngerti banget kok
Teeimakasih yaaaaa udah jawab, tenang aja pesan ini ga diliat rexa kok, jadi kamu aman hehe

Btw aku mau nanya are u sad or happy?
bales ya !!""")

@app.on_message(filters.regex("ya|iya|suka|y|yak|iyak"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, """
Serius banget nih kamu suka aku? wtf semalem gua mimpi apa ya anjg wkwkwk
Terimakasih banget ya udah suka saya wkwkw, sebenernya aku gatau jawaban kamu sih ini kan bot wkwkwk tapi gapapa aku seneng aja hehe!
oh iya aku mau nanya are u sad or happy?
Bales ya!""")

@app.on_message(filters.regex("ya|iya|suka|y|yak|iyak"))
async def regex_foto(_, message):
    await app.send_sticker(message.chat.id, "CAACAgUAAx0EZ77D7QAC4wpj7OcOfwWCQX2j_kH0Wk0oqgmKpgACJQUAAn3dOVa0npVTk7sv9R4E")


# SAD & happy

@app.on_message(filters.regex("sad|sedih|sedihh|sadd"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, """
Sedih? kok bisa sih aelahh ga seru !!
yang aku tau dipa itu anaknya periang dan susah sedih, 

tapi gapapa kok kan ga harus bahagia, jujur aku ga bisa ngehibur, cuma kalo kamu mau cerita gapapa chat aku aja
oh iya sebenernya ada lagi sih wkwk, coba deh ketik mau""")

@app.on_message(filters.regex("happy|hppy|seneng|bahagia|hapy"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, """
Kamu lagi happy ? jangan bilang happy karena udah aku buatin bot hehehe, keknya gamungkin deh
oh iya malah bagus kalo kamu lagi happy gini, semoga selalu happy yaaaa, oh iya ada lagi loh sebenernya wkwk, coba kamu ketik mau """)


# MAU !!!!
@app.on_message(filters.regex("mau|Mau"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, """ 
ini sebenernya gaterlalu penting sih, aku cuma pengen bilang semangat terus buat kamu 😊,

don't be afraid of the future because Im sure u can pass it all ! Ganbatte neee!!
Sebenernya project ini udah lama cuma dipending atau ke distract sama kesibukan hehehe
aku juga bikin ini lumayan aga susah sih difirst time bikin bot sendiri ya gitu deh lumayan aga susah, tapi seru

Apalagi ada tujuannya, ya siapa lagi kalo bukan kamu
Makasih banget loh berkat kamu aku jadi banyak bgt bikin bot game, yang tadinya ketakutan keluar dari zona nyaman bot ku
sserius dulu aku ga berani ke bot lain selain hikari, dan berkat kamu aku berhasil

Aku harap kamu bisa kek aku, bukan jago bot tapi berhasil keluar dari Zona nyaman kamu yaaa
everything will be fine, get rid of the fear in u, I'm here to show u something you've never seen before ♥️
ILove you and Thankyou So much hehehe ♥️
may you always be happy 😊

setelah ini kamu bisa kirim reaksi kamu setelah mainin bot ini ke aku loh, ketik aja yaaa apa yang kamu mau sampein ke aku, abis itu kalo udah ketik udah
""")

# UDAH 
@app.on_message(filters.regex("udah|udh"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, """
makasih yak udah ngirim respon ke aku hehe terimakasih banget yaaaaa!!! btw aku mau kasih bonus ke ke kamu
sekarang cobain ketik kata dibawah ini :

• jamet
• lagi
• ifusad
• secret
• secretvideo
Jangan Berekpetasi lebih ya wkwkwk 😊
""")


# SEND JAMET

@app.on_message(filters.regex("jamet"))
async def foto_se(_, message):
    await app.send_photo(message.chat.id, "https://telegra.ph/file/f0246bd66f054ed2ac570.jpg")
  

@app.on_message(filters.regex("lagi"))
async def regex_foto(_, message):
    await app.send_photo(message.chat.id, "https://graph.org/file/46b2aa7693a28e510f5e0.jpg")
    

# SEND IF U SAD

@app.on_message(filters.regex("ifusad"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, """ 
Jujur kalo aku lagi sedih kadang aku suka nonton Theater Jkt48 sih hehehe tapi coba kamu ketik urfavsong deh dengerin yakk semoga mood mu membaik 
""")

# REGEX SEND MEDIA

@app.on_message(filters.regex("urfavsong"))
async def regex_foto(_, message):
    await app.send_voice(message.chat.id, "https://t.me/ifusadcallme/4", caption="semoga kamu suka")
    

print('loading cuy')
print('•')
print('••')
print('•••')
print('bisa rex')
print('gaskeun rex!!')
app.run()
