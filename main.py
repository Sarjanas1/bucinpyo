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

START_MESSAGE = """ 👋🏻 Halo saya Adalah bot yang dibuat untuk orang yang bara anggap Special
Ketik mulai untuk memulai Bot ini :)

⚠️ Aturan pakai, jangan mengetik jika tidak disuruh mengetik!!

👨‍💻 Owner :
"""

START_BUTTON = [

    [  
        InlineKeyboardButton("me", url="https://t.me/fearznolimit"),              
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
    await app.send_message(message.chat.id, "Ketik nama kamu terlebih dahulu agar saya bisa cek apakah benar kamu orang yang bara tuju")

# REGEX CARI NAMA
@app.on_message(filters.regex("dorva|dorva"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, "benersih nama asli, cuma ga mau yang ini wleeeeeeeeee 😜")

@app.on_message(filters.regex("dorva|dorva|ova|va"))
async def actions_chat(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, "benersih nama asli, cuma ga mau yang ini wleeeeeeeeee 😜")


# ESEKUSI 1

@app.on_message(filters.regex("dira|nadira"))
async def regex_indri(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(2)
    TEXT = """
Nah ini nama yang bener hehehe !!!
Halo ayang 👋🏻 gimana hari ini? Asik tidak? saya harap sih asik selalu ya!!
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
Oke jadi di bot ini Aku (pacarkamu) Cuma mau sampein sedikit banyak eh gmna ya -,-, Intinya gini

coba Kamu ketik intinya
"""
    await app.send_message(message.chat.id, text=TEXT)

@app.on_message(filters.regex("inti|intinya"))
async def regexinti(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(2)
    TEXT = """
aku cuma mau Berterima Kasih Karena udah kenal sama aku
dan jadi pacar yang baik, sering cerita sama aku ya intinya terimakasih banyakk yakk!!!
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
👋🏻 Pertama aku mau berterimakasih banget udah ngehargain Karya Bot aku dan
Terimakasih banget udah Mau Buka bot ini udah Jadi alasan gua buka Chat WA
Selain Karna tugas :)

Intinya Terimakasih Banyak Untuk kamu
Pencet Tombol ** Lanjut ** kalo seru
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
Tetep jadi dira yang aku kenal ya!

Kamu tau ga kenapa aku bilang "tetep jadi dira yang aku kenal"?
Nih aku kasih tau kenapa ak bilang gitu, soalnya kalok kmu berubah aku yang nangis ehehehehe 
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
Jangan pernah dengerin orang yg berkata jelek tentang kamu!!
udah stop mikirin perkataan orang tentang apapun itu tentang kamu yaa!

POKOK NYA KAMU YANG TERBAIK DARI APAPUN ITU !!!
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
bub aku pertama kali kenal cewe dan langsung jadian aku harap kamu yang terbaik buat aku

pokok nya aku mau serius sama kamu jadii jangan hianatin aku ya hehe
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
aku baru pertama kali ngelakuin hubungan seperti ini bub heheh

dan aku berusaha mengenal karakter kamu mwehehe ILY BUB ♡
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
pokok aku minta maaf kalau ak banyak kurang nya hehe
dan kalau aku ada salah samju bilang ya jangan diem aja
biar aku bisa introspeksi diri supaya tidak mengulangi nya lagi

POKOK NYA SEKARANG AKU SENENG BANGET JADI PACAR KAMU ♡
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

Jadi intinya aku sayang sama kamu, mungkin bisa dibilang nyaman, kalo sayang pasti karena ya sayang banget
tapi ini rasanya beda dan kek pengen effort lebih buat kamu, ngerti ga sih -,- !!

pasti ngerti deh, aku akan berusaha nyari tau tentang kamu gitu, dll, sebenernya saya suka banget :)
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
Ini cuma ungkapan ya, jadi aku sayang banget sama kamu, cuma ya mau anu, apasih namanya, kek ngungkapin aja yang perasaan yang sebenarnya,

Jujur aku baru pertama kali buat ginian buat orang yang ak sayang hehhee
mau sesuatu yang beda, yang orang lain ga kepikiran, jadi ya bikin bot dari 0% sampe jadi gini, mu

Ga bagus sih, cuma ya yang penting tersampaikan aja, Btw Mau nanya dong? Jujur aja Kamu Sebalikanya ga Ke aku? 
Coba abis pencet tombol selesai

Bales yaaa,
ketik ** Iya ** atau ** Gak **
aku tunggu 😜
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
        await callback_query.message.delete(SELESAI)

# GA ATAU IYA

@app.on_message(filters.regex("engga|G|enggak|gak|ga"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, """
gapapa kok kalok engga hehehe santai aja 
Teeimakasih yaaaaa udah jawab, yang penting aku niat bikin ini buat kamu 

Btw aku mau nanya are u sad or happy?
bales ya !!""")

@app.on_message(filters.regex("iya|suka"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, """
Serius banget nih kamu suka aku? wtf semalem gua mimpi apa ya anjg wkwkwk
Terimakasih banget ya udah suka sama project aku ini wkwkw, sebenernya aku gatau jawaban kamu sih ini kan bot wkwkwk tapi gapapa aku seneng aja hehe!
oh iya aku mau nanya are u sad or happy?
Bales ya!""")

# SAD & happy

@app.on_message(filters.regex("sad|sedih|sedihh|sadd"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, """
Sedih? kok bisa sih aelahh ga seru !!
yang aku tau kamu itu anaknya periang dan susah sedih, 

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
Sebenernya project ini aku buat khusus buat kamu  semoga suka yaaa
aku juga bikin ini lumayan aga susah sih difirst time bikin bot sendiri ya gitu deh lumayan aga susah, tapi seru

Apalagi ada tujuannya, ya siapa lagi kalo bukan kamu
Makasih banget loh berkat kamu aku jadi banyak bgt pengalaman yang aku coba contoh nya bot ini
serius dulu aku ga berani ke bot lain selain zenitsu, dan berkat kamu aku berhasil

Aku harap kamu bisa kek aku, bukan bisa main bot tapi berhasil keluar dari Zona nyaman kamu yaaa

✏️ Everything will be fine, get rid of the fear in u, I'm here to show u something you've never seen before ♥️
ILove you and Thankyou So much hehehe ♥️
may you always be happy 😊

setelah ini kamu bisa kirim reaksi kamu setelah mainin bot ini ke aku loh, 

ini pokoknya harus :

😡 kirim ke pc aja ke own bot ini @fearznolimit kalo sudah ketik ** udah **
ada kejutan lain lohh makanya isi dulu!!
""")

# UDAH 
@app.on_message(filters.regex("udah|udh"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, """
makasih yak udah ngirim respon ke aku hehe terimakasih banget yaaaaa!!! btw aku mau kasih bonus ke ke kamu
sekarang cobain ketik kata dibawah ini ya :

👉🏻 jamet
👉🏻 cantik
👉🏻 secret
👉🏻 kepo
👉🏻 specialvideo

Jangan Berekpetasi lebih ya wkwkwk 😊
""")


# SEND JAMET

@app.on_message(filters.regex("jamet"))
async def foto_se(_, message):
    await app.send_photo(message.chat.id, "https://telegra.ph/file/045651156bb199ed2d3d4c.jpg", caption="maaap yaaaa wkwkwk, kalo mau lagi ketik ** lagi ** ")
  

@app.on_message(filters.regex("lagi"))
async def regex_foto(_, message):
    await app.send_photo(message.chat.id, "https://telegra.ph/file/cf568f083e574eb1e9d70.jpg", "hehehe")
    

# SEND IF U SAD

@app.on_message(filters.regex("kepo"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, """ 
Asal Lo Tau Ya Dek !!! disini ga ada apa apa wkwkwk

Susah kalo jadi orang penasaran 😜

""")

@app.on_message(filters.regex("secret"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, """ 
Disini aku mau ngasih tau, kalo kamu sedih coba deh ikutin cara ku
itung beras sih biasanya klo aku.
terus Jujur kalo aku lagi sedih kadang aku suka nonton Anime sih hehehe
tapi coba kamu ketik urfavsong deh dengerin yakk semoga lekas membaik
""")

# REGEX SEND MEDIA

@app.on_message(filters.regex("urfavsong"))
async def regex_song(_, message):
    await app.send_voice(message.chat.id, "https://t.me/buatdiranih/3", caption="semoga kamu suka")

@app.on_message(filters.regex("cantik"))
async def regex_cantik(_, message):
    await app.send_photo(message.chat.id, "https://t.me/buatdiranih/4", caption="ini gemassssssss tapi kalo kamu ketik ** imut ** lebih gemas lagi")

@app.on_message(filters.regex("cute"))
async def regex_cute(_, message):
    await app.send_photo(message.chat.id, "https://telegra.ph/file/bfd41ec19b507b08624a2.jpg", caption="hehe cute kann")

@app.on_message(filters.regex("imut"))
async def regex_imut(_, message):
    await app.send_photo(message.chat.id, "https://t.me/buatdiranih/5", caption="WKWKWKWKWK")

@app.on_message(filters.regex("specialvideo"))
async def regex_cantik(_, message):
    await app.send_video(message.chat.id, "https://t.me/buatdiranih/6", caption="INI BUAT KAMU BUB")


print('loading cuy')
print('•')
print('••')
print('•••')
print('bisa ion')
print('gaskeun ion!!')
app.run()
