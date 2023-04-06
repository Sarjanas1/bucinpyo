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

START_MESSAGE = """ 👋🏻 Halo saya Adalah bot yang dibuat untuk orang yang Bion anggap Special
Ketik mulai untuk memulai Bot ini :)

⚠️ Aturan pakai, jangan mengetik jika tidak disuruh mengetik!!

👨‍💻 Owner :
"""

START_BUTTON = [

    [  
        InlineKeyboardButton("Bion", url="https://t.me/onlybionn"),              
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
    await app.send_message(message.chat.id, "Ketik nama kamu terlebih dahulu agar saya bisa cek apakah benar kamu orang yang Bion tuju")

# REGEX CARI NAMA
@app.on_message(filters.regex("jopa|jopaa"))
async def chat_actions(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, "benersih nama asli, cuma ga mau yang ini wleeeeeeeeee 😜")

@app.on_message(filters.regex("jopa|acey|casey|cey"))
async def actions_chat(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await app.send_message(message.chat.id, "benersih nama asli, cuma ga mau yang ini wleeeeeeeeee 😜")


# ESEKUSI 1

@app.on_message(filters.regex("aulia|yaya"))
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
Oke jadi di bot ini Aku (Bion) Cuma mau sampein sedikit banyak eh gmna ya -,-, Intinya gini

coba Kamu ketik intinya
"""
    await app.send_message(message.chat.id, text=TEXT)

@app.on_message(filters.regex("inti|intinya"))
async def regexinti(_, message):
    await app.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(2)
    TEXT = """
aku cuma mau Berterima Kasih Karena udah kenal sama aku
dan jadi pacar yang baik, sering cerita dll intinya terimakasih banyakk yakk!!!
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
Terimakasih banget udah Mau Bantu udah jadi Temen cerita sampe Jadi alasan gua buka Chat WA
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
Tetep jadi jopa yang aku kenal ya!

Kamu tau ga kenapa aku bilang "tetep jadi jopa yang aku kenal"?
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
Jangan terlalu gampang dengerin omomgan orang yg ngejek in kamu tau!!
udah stop mikirin perkataan orang tentang apapun itu tentang kamu yaa!

Kamu cantik kamu baik tapi jangan denger kata kata orang yg jelek jelekin kamu !!!
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
bub inget ga ? Waktu pertama kali kamu kenal aku? Malahan sebelum kenal saya deh
waktu di os wa dulu sebenarnya aku udah penasaran sama kamu, karena kamu lucu

tapi karena saya anaknya ga tau diri( ga tau diri maksudnya, padahal kamu dah punya pacar tetep ak chat)
jadi saya mencoba berani ngechat anda, tapi jujur aku anaknya ga berani ngechat, kalo suka ya suka aja diem diem hehehe
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
Nah lama kelamaaan kok ngobrol sama kamu asik, Dulu yang aku ngajak os itu
aku kira kamu ga bakal mau eh ternyata mau

sebenarnya itu trik biar ak bisa deketin km wkwk maap yaaa tapi yaudahlah kan ga terlalu cringe juga usahanya
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
Di suatu ketika aku cuek sama kamu karna ak pernah ngerasa ga di hargai
dan tau ga? kamu tau ga aku ngearasa aku ga di hargai karna apa?
pas kamu bilang galau pas kita lagi call rasanya kayak apa yaa eummm

Karena aku lebih baik marah nya cuek dari pada ngerespon kamu, maaf ya yang waktu itu
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
Sebenernya project ini udah lama cuma dipending atau ke distract sama kesibukan hehehe
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

😡 kirim ke pc aja ke own bot ini @onlybionn kalo sudah ketik ** udah **
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
👉🏻 bionn
👉🏻 specialvideo

Jangan Berekpetasi lebih ya wkwkwk 😊
""")


# SEND JAMET

@app.on_message(filters.regex("jamet"))
async def foto_se(_, message):
    await app.send_photo(message.chat.id, "https://telegra.ph/file/da27e3de339b8326c44b.jpg", caption="maaap yaaaa wkwkwk, kalo mau lagi ketik ** lagi ** ")
  

@app.on_message(filters.regex("lagi"))
async def regex_foto(_, message):
    await app.send_photo(message.chat.id, "https://telegra.ph/file/9b776c7644d2c53264edb.jpg", "hehehe")
    

# SEND IF U SAD

@app.on_message(filters.regex("bionn"))
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
    await app.send_voice(message.chat.id, "https://t.me/jopajamet/3", caption="semoga kamu suka, kalo mau tau liriknya ketik aja ** lirik **")

@app.on_message(filters.regex("cantik"))
async def regex_cantik(_, message):
    await app.send_video(message.chat.id, "https://t.me/jopajamet/4", caption="ini gemassssssss tapi kalo kamu ketik ** imut ** lebih gemas lagi")

@app.on_message(filters.regex("lirik"))
async def regex_lirik(_, message):
    await app.send_photo(message.chat.id, "https://telegra.ph/file/0f96e6e53f568496f84a5.jpg", caption="dengerin klo malem enak sih menurut ku")

@app.on_message(filters.regex("imut"))
async def regex_imut(_, message):
    await app.send_photo(message.chat.id, "https://t.me/jopajamet/5", caption="WKWKWKWKWK")

@app.on_message(filters.regex("specialvideo"))
async def regex_cantik(_, message):
    await app.send_video(message.chat.id, "https://t.me/jopajamet/6", caption="ini lagu yang bikin gua semangat terus, menurut gua sih enak")


print('loading cuy')
print('•')
print('••')
print('•••')
print('bisa ion')
print('gaskeun ion!!')
app.run()
