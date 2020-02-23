import telebot
import config
import datetime as dt
import random as r
from telebot import types
import time

bot = telebot.TeleBot(config.token)
print("redy!")
@bot.message_handler(commands=['start','help'])
def start_command(message):
    print("@" + message.chat.username + " Start using bot!")
    mark = types.InlineKeyboardMarkup(row_width=1)
    help_c = types.InlineKeyboardButton('Помощь',callback_data='help')
    cb_c = types.InlineKeyboardButton('Предложения и замечяния',callback_data='callback')
    mark.add(help_c,cb_c)
    bot.send_message(message.chat.id, "Привет, я бот который в любой момент может выслать тебе расписание!\
    	Для того что-бы получить расписание напиши мне дату или день недели!",reply_markup=mark)
    if message.text == 'Помощь':
    	bot.send_message(message.chat.id, "Напиши \"/help\"")
    elif message.text == 'Предложения и замечяния':
    	bot.send_message(message.chat.id, 'У тебя есть замечяние или предложение, тогда напиши комманду\
    		\"/callback\", и мы обязательно прочтем твой отзыв!')
@bot.message_handler(commands=['callback'])
def callback(message):
    cbmessage = bot.send_message(message.chat.id,"Напиши мне отзыв, и его прочитает мой творец!")
    bot.register_next_step_handler(cbmessage, callback_data)
def callback_data(message):
    msg = message.text
    print(msg)
    chat_id = -1001432681447
    bot.send_message(-1001432681447,"---------")
    bot.send_message(-1001432681447,msg)
    try:
        bot.send_message(-1001432681447,message.chat.username)
    except:
        bot.send_message(-1001432681447,"unknow username!")
    bot.send_message(-1001432681447,"---------")
    bot.send_message(message.chat.id,"Спасибо, ваше мнение очень важно для нас!")

@bot.message_handler(commands=['group_id'])
def send_group_id(message):
    bot.send_message(message.chat.id,message.chat.id)


@bot.message_handler(content_types=['audio','video','documnet','photo'])
def sorry_content_type_err(message):
	bot.send_message(message.chat.id, "Извини но я понимаю только текст! Напиши \"/help\" если нужна помощь!")
##################
@bot.message_handler(commands=['htMath'])
def new_hometask(message):
    bot.send_message(message.chat.id, "Новое дз?")
    newdz = bot.send_message(message.chat.id, "Присылай его мне")
    bot.register_next_step_handler(newdz, set_new_ht)
def set_new_ht(message):
    ht = open("hometaskMath.dat","w") 
    ht.write(message.text)
    ht.close()
    bot.send_message(message.chat.id, "Ок, запомню!")
#####################
@bot.message_handler(commands=['htEng'])
def new_hometask(message):
    bot.send_message(message.chat.id, "Новое дз?")
    newdz = bot.send_message(message.chat.id, "Присылай его мне")
    bot.register_next_step_handler(newdz, set_new_ht)
def set_new_ht(message):
    ht = open("hometaskEng.dat","w") 
    ht.write(message.text)
    ht.close()
    bot.send_message(message.chat.id, "Ок, запомню!")
####################
@bot.message_handler(commands=['htInr'])
def new_hometask(message):
    bot.send_message(message.chat.id, "Новое дз?")
    newdz = bot.send_message(message.chat.id, "Присылай его мне")
    bot.register_next_step_handler(newdz, set_new_ht)
def set_new_ht(message):
    ht = open("hometaskInr.dat","w") 
    ht.write(message.text)
    ht.close()
    bot.send_message(message.chat.id, "Ок, запомню!")
#####################
@bot.message_handler(commands=['htHist'])
def new_hometask(message):
    bot.send_message(message.chat.id, "Новое дз?")
    newdz = bot.send_message(message.chat.id, "Присылай его мне")
    bot.register_next_step_handler(newdz, set_new_ht)
def set_new_ht(message):
    ht = open("hometaskHist.dat","w") 
    ht.write(message.text)
    ht.close()
    bot.send_message(message.chat.id, "Ок, запомню!")
#####################
@bot.message_handler(commands=['htBio'])
def new_hometask(message):
    bot.send_message(message.chat.id, "Новое дз?")
    newdz = bot.send_message(message.chat.id, "Присылай его мне")
    bot.register_next_step_handler(newdz, set_new_ht)
def set_new_ht(message):
    ht = open("hometaskBio.dat","w") 
    ht.write(message.text)
    ht.close()
    bot.send_message(message.chat.id, "Ок, запомню!")
#####################
@bot.message_handler(commands=['htGeo'])
def new_hometask(message):
    bot.send_message(message.chat.id, "Новое дз?")
    newdz = bot.send_message(message.chat.id, "Присылай его мне")
    bot.register_next_step_handler(newdz, set_new_ht)
def set_new_ht(message):
    ht = open("hometaskGeo.dat","w") 
    ht.write(message.text)
    ht.close()
    bot.send_message(message.chat.id, "Ок, запомню!")
#####################
@bot.message_handler(commands=['htFiz'])
def new_hometask(message):
    bot.send_message(message.chat.id, "Новое дз?")
    newdz = bot.send_message(message.chat.id, "Присылай его мне")
    bot.register_next_step_handler(newdz, set_new_ht)
def set_new_ht(message):
    ht = open("hometaskFiz.dat","w") 
    ht.write(message.text)
    ht.close()
    bot.send_message(message.chat.id, "Ок, запомню!")


@bot.message_handler(content_types=['sticker'])
def send_random_sticker(message):
    pic1 = open('images/st1.webp', 'rb')
    pic2 = open('images/st2.webp', 'rb')
    pic3 = open('images/st3.webp', 'rb')
    pic4 = open('images/st4.jpg', 'rb')
    pic5 = open('images/st5.jpg', 'rb')
    pic6 = open('images/st6.jpg', 'rb')
    pic7 = open('images/st7.jpg', 'rb')
    pic8 = open('images/st8.jpg', 'rb')
    pc = [pic1,pic2,pic3,pic4,pic5,pic6,pic7,pic8]
    pic = r.choice(pc)
    bot.send_sticker(message.chat.id, pic)
    print("@"+message.chat.username + " take sticker from bot!")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    if message.text == u"Понедельник" or message.text == u"понедельник":#MONDAY########
        """md = open('images/schedule/monday.png', 'rb')
       	markup = types.ReplyKeyboardMarkup(row_width=2)
       	math1 = types.KeyboardButton('Математика')
       	hist1 = types.KeyboardButton('История')
       	eng1 = types.KeyboardButton('Английский')
       	pe = types.KeyboardButton('Физ - ра')
       	markup.add(math1,hist1,eng1,pe)
       	bot.send_photo(message.chat.id, md, reply_markup=markup)"""
        ##############                    MATH
        MDinlinekeyb = types.InlineKeyboardMarkup(row_width=1)
        firstless = types.InlineKeyboardButton("1. Математика", callback_data='math_cd')
        secondless = types.InlineKeyboardButton("2. Математика", callback_data='math_cd')
        thirdless = types.InlineKeyboardButton("3. Английский", callback_data='eng_cd')
        forthless = types.InlineKeyboardButton("4. Английский", callback_data='eng_cd')
        fivsless = types.InlineKeyboardButton("5. История", callback_data='hist_cd')
        sixsless = types.InlineKeyboardButton("6. История", callback_data='hist_cd')
        MDinlinekeyb.add(firstless,secondless,thirdless,forthless,fivsless,sixsless)
        bot.send_message(message.chat.id, "<b>ПОНЕДЕЛЬНИК</b>",parse_mode='html',reply_markup=MDinlinekeyb)
        ##############
    #if message.text == u"Математика":
        global MDhometaskMath, MDhometaskEng, MDhometaskInr, MDhometaskFiz, MDhometaskHist, MDhometaskBio, MDhometaskNem, MDhometaskGeo, MDhometaskUkrL\
            , MDhometaskUkrM, MDhometaskArt, MDhometaskChmstr, MDhometaskGeom
        MDhtm = open("MDhometask/MDhometaskMath.dat","r", encoding="utf8")
       	MDhometaskMath = MDhtm.readline()
        MDhtm.close()
        #######################
        MDhte = open("MDhometask/MDhometaskEng.dat","r", encoding="utf8")
        MDhometaskEng = MDhte.readline()
        MDhte.close()
        #######################
        MDhti = open("MDhometask/MDhometaskInr.dat","r", encoding="utf8")
        MDhometaskInr = MDhti.readline()
        MDhti.close()
        #######################
        MDhthist = open("MDhometask/MDhometaskHist.dat","r", encoding="utf8")
        MDhometaskHist = MDhthist.readline()
        MDhthist.close()
        #######################
        MDhtfiz = open("MDhometask/MDhometaskFiz.dat","r", encoding="utf8")
        MDhometaskFiz = MDhtfiz.readline()
        MDhtfiz.close()
        #######################
        MDhtbio = open("MDhometask/MDhometaskBio.dat","r", encoding="utf8")
        MDhometaskBio = MDhtbio.readline()
        MDhtbio.close()
        #######################
        MDhtnem = open("MDhometask/MDhometaskNem.dat","r", encoding="utf8")
        MDhometaskNem = MDhtnem.readline()
        MDhtnem.close()
        #######################
        MDhtgeo = open("MDhometask/MDhometaskGeo.dat","r", encoding="utf8")
        MDhometaskGeo = MDhtgeo.readline()
        MDhtgeo.close()
        #######################
        MDhtukrl = open("MDhometask/MDhometaskUkrL.dat","r", encoding="utf8")
        MDhometaskUkrL = MDhtukrl.readline()
        MDhtukrl.close()
        #######################
        MDhtukrm = open("MDhometask/MDhometaskUkrM.dat","r", encoding="utf8")
        MDhometaskUkrM = MDhtukrm.readline()
        MDhtukrm.close()
        #######################
        MDhtart = open("MDhometask/MDhometaskArt.dat","r", encoding="utf8")
        MDhometaskArt = MDhtart.readline()
        MDhtart.close()
        #######################
        MDhtchmstr = open("MDhometask/MDhometaskChmstr.dat","r", encoding="utf8")
        MDhometaskChmstr = MDhtchmstr.readline()
        MDhtchmstr.close()
        #######################
        MDhtgeom = open("MDhometask/MDhometaskGeom.dat","r", encoding="utf8")
        MDhometaskGeom = MDhtgeom.readline()
        MDhtgeom.close()
       	#htm.close()
       	#bot.send_message(message.chat.id, "Каб: 104")
       	#bot.send_message(message.chat.id, "Преподователь: Антонина Александровна")
       	#bot.send_message(message.chat.id, "ДЗ:"+hometask)

        print("@"+message.chat.username + "-Mondey")
    elif message.text == u"Вторник" or message.text == u"вторник":#THUESDAY############
        """tsd = open('images/schedule/Thuesday.png', 'rb')
        bot.send_photo(message.chat.id, tsd)"""
        ##############                    Art - Pe
        TUinlinekeyb = types.InlineKeyboardMarkup(row_width=1)
        firstless = types.InlineKeyboardButton("1. Физика", callback_data='fiz_cd')
        secondless = types.InlineKeyboardButton("2. Физика", callback_data='fiz_cd')
        thirdless = types.InlineKeyboardButton("3. Укр. Мова", callback_data='ukrm_cd')
        forthless = types.InlineKeyboardButton("4. Укр. Мова", callback_data='ukrm_cd')
        fivsless = types.InlineKeyboardButton("5. Физ - ра", callback_data='pe_cd')
        sixsless = types.InlineKeyboardButton("6. Искуство", callback_data='art_cd')
        TUinlinekeyb.add(firstless,secondless,thirdless,forthless,fivsless,sixsless)
        bot.send_message(message.chat.id, "<b>ВТОРНИК</b>",parse_mode='html',reply_markup=TUinlinekeyb)
        ##############

        print("@"+message.chat.username + "-Tuesday")
    elif message.text == u"Среда" or message.text == u"среда":#WEDENSDAY###############
        """wd = open('images/schedule/Wedensday.png', 'rb')
        bot.send_photo(message.chat.id, wd)"""
        ##############                    NEM
        WDinlinekeyb = types.InlineKeyboardMarkup(row_width=1)
        firstless = types.InlineKeyboardButton("1. Укр. Литература", callback_data='ukrl_cd')
        secondless = types.InlineKeyboardButton("2. Укр. Литература", callback_data='ukrl_cd')
        thirdless = types.InlineKeyboardButton("3. Немецкий", callback_data='nem_cd')
        forthless = types.InlineKeyboardButton("4. Немецкий", callback_data='nem_cd')
        fivsless = types.InlineKeyboardButton("5. Информатика", callback_data='inform_cd')
        sixsless = types.InlineKeyboardButton("6. Информатика", callback_data='inform_cd')
        WDinlinekeyb.add(firstless,secondless,thirdless,forthless,fivsless,sixsless)
        bot.send_message(message.chat.id, "<b>СРЕДА</b>",parse_mode='html',reply_markup=WDinlinekeyb)
        ##############
        print("@"+message.chat.username + "-Wedensday")
    elif message.text == u"Четверг" or message.text == u"четверг":#THURSDAY############
        """trd = open('images/schedule/Thursday.png', 'rb')
        bot.send_photo(message.chat.id, trd)"""
        ##############                    GEO
        TRinlinekeyb = types.InlineKeyboardMarkup(row_width=1)
        firstless = types.InlineKeyboardButton("1. История", callback_data='hist_cd')
        secondless = types.InlineKeyboardButton("2. История", callback_data='hist_cd')
        thirdless = types.InlineKeyboardButton("3. Математика", callback_data='math_cd')
        forthless = types.InlineKeyboardButton("4. Математика", callback_data='math_cd')
        fivsless = types.InlineKeyboardButton("5. Английский", callback_data='eng_cd')
        sixsless = types.InlineKeyboardButton("6. Английский", callback_data='eng_cd')
        TRinlinekeyb.add(firstless,secondless,thirdless,forthless,fivsless,sixsless)
        bot.send_message(message.chat.id, "<b>ЧЕТВЕРГ</b>",parse_mode='html',reply_markup=TRinlinekeyb)
        ##############
        print("@"+message.chat.username + "-Thursday")
    elif message.text == u"Пятница" or message.text == u"пятница":#FRIDAY##############
        """fd = open('images/schedule/Friday.png', 'rb')
        bot.send_photo(message.chat.id, fd)"""
        ##############                    FIZ
        FRinlinekeyb = types.InlineKeyboardMarkup(row_width=1)
        firstless = types.InlineKeyboardButton("1. Биология", callback_data='bio_cd')
        secondless = types.InlineKeyboardButton("2. Биология", callback_data='bio_cd')
        thirdless = types.InlineKeyboardButton("3. География", callback_data='geo_cd')
        forthless = types.InlineKeyboardButton("4. География", callback_data='geo_cd')
        fivsless = types.InlineKeyboardButton("5. Химия", callback_data='chm_cd')
        sixsless = types.InlineKeyboardButton("6. Химия", callback_data='chm_cd')
        FRinlinekeyb.add(firstless,secondless,thirdless,forthless,fivsless,sixsless)
        bot.send_message(message.chat.id, "<b>ПЯТНИЦА</b>",parse_mode='html',reply_markup=FRinlinekeyb)
        ##############
    
        print("@"+message.chat.username + "-Friday")
    elif message.text == "Субота" or message.text == "субота":
        bot.send_message(message.chat.id, "Сегодня субота, можешь отдохнуть!!!)))")
    elif message.text == "Воскресенье" or message.text == "воскресенье":
        bot.send_message(message.chat.id, "Сегодня ВОСКРЕСЕНЬЕ отдыхай!!!!!!)))")
    else:
    	#bot.send_message(message.chat.id,"『  Прости я непонял  』")
        bot.send_message(message.chat.id, "Кажется ты написал...")
        bot.send_message(message.chat.id,"『  " + message.text + "  』")
        print("11")
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            global hometaskMath, hometaskEng, hometaskInr
            if call.data == 'math_cd':
                bot.send_message(call.message.chat.id, "<u>МАТЕМАТИКА</u>",parse_mode='html')
                bot.send_message(call.message.chat.id, "Каб: 104")
                bot.send_message(call.message.chat.id, "Преподователь: Антонина Александровна")
                global MDhometaskMath, MDhometaskEng, MDhometaskInr, MDhometaskFiz, MDhometaskHist, MDhometaskBio, MDhometaskNem, MDhometaskGeo, MDhometaskUkrL\
            , MDhometaskUkrM, MDhometaskArt, MDhometaskChmstr, MDhometaskGeom
                bot.send_message(call.message.chat.id, "ДЗ:" + MDhometaskMath)
            elif call.data == 'eng_cd':
                bot.send_message(call.message.chat.id, "<u>АНГЛИЙСКИЙ</u>",parse_mode='html')
                bot.send_message(call.message.chat.id, "Каб: 104")
                bot.send_message(call.message.chat.id, "Преподователь: Светлана Анатольевна")
                global MDhometaskEng, MDhometaskInr, MDhometaskFiz, MDhometaskHist, MDhometaskBio, MDhometaskNem, MDhometaskGeo, MDhometaskUkrL\
            , MDhometaskUkrM, MDhometaskArt, MDhometaskChmstr, MDhometaskGeom
                bot.send_message(call.message.chat.id, "ДЗ:" + MDhometaskEng)
            elif call.data == 'inform_cd':
                bot.send_message(call.message.chat.id, "<u>ИНФОРМАТИКА</u>",parse_mode='html')
                bot.send_message(call.message.chat.id, "Каб: 301")
                bot.send_message(call.message.chat.id, "Преподователь: Дмитрий Владимирович")
                global MDhometaskInr, MDhometaskFiz, MDhometaskHist, MDhometaskBio, MDhometaskNem, MDhometaskGeo, MDhometaskUkrL\
            , MDhometaskUkrM, MDhometaskArt, MDhometaskChmstr, MDhometaskGeom
                bot.send_message(call.message.chat.id, "ДЗ:" + MDhometaskInr)
            elif call.data == 'help':
                bot.send_message(call.message.chat.id, "<u>ПОМОЩЬ</u>", parse_mode='html')
                bot.send_message(call.message.chat.id, "Мой <pre>творец</pre> создал меня для того что-бы я давал вам расписание на любой рабочий день недели!", parse_mode='html')
                bot.send_message(call.message.chat.id, "Просто напиши <i>Понедельник</i> или <i>вторник</i>, и я пришлю тебе расписание на этот день!", parse_mode='html')
                bot.send_message(call.message.chat.id, "Мой творец - <b><code>@tesla33IO</code></b>", parse_mode='html')
            elif call.data == 'callback':
                bot.send_message(call.message.chat.id, "<b>Для связи с творцом напиши кооманду <i>/callback</i> или напиши ему лично(<i>@tesla33IO</i>)</b>", parse_mode='html')
            elif call.data == "fiz_cd":
                bot.send_message(call.message.chat.id, "<u>ФИЗИКА</u>",parse_mode='html')
                bot.send_message(call.message.chat.id, "Каб: 304")
                bot.send_message(call.message.chat.id, "Преподователь: Ирина Сергеевна")
                global MDhometaskFiz, MDhometaskHist, MDhometaskBio, MDhometaskNem, MDhometaskGeo, MDhometaskUkrL\
            , MDhometaskUkrM, MDhometaskArt, MDhometaskChmstr, MDhometaskGeom
                bot.send_message(call.message.chat.id, "ДЗ:" + MDhometaskFiz)
            elif call.data == 'hist_cd':
                bot.send_message(call.message.chat.id, "<u>ИСТОРИЯ</u>",parse_mode='html')
                bot.send_message(call.message.chat.id, "Каб: 104")
                bot.send_message(call.message.chat.id, "Преподователь: Вера Александровна")
                global MDhometaskHist, MDhometaskBio, MDhometaskNem, MDhometaskGeo, MDhometaskUkrL\
            , MDhometaskUkrM, MDhometaskArt, MDhometaskChmstr, MDhometaskGeom
                bot.send_message(call.message.chat.id, "ДЗ:" + MDhometaskHist)
            elif call.data == 'ukrm_cd':
                bot.send_message(call.message.chat.id, "<u>УКР. МОВА</u>",parse_mode='html')
                bot.send_message(call.message.chat.id, "Каб: 104")
                bot.send_message(call.message.chat.id, "Преподователь: Инна Ивановна")
                global MDhometaskBio, MDhometaskNem, MDhometaskGeo, MDhometaskUkrL\
            , MDhometaskUkrM, MDhometaskArt, MDhometaskChmstr, MDhometaskGeom
                bot.send_message(call.message.chat.id, "ДЗ:" + MDhometaskUkrM)
            elif call.data == 'ukrl_cd':
                bot.send_message(call.message.chat.id, "<u>УКР. ЛИТЕРАТУРА</u>",parse_mode='html')
                bot.send_message(call.message.chat.id, "Каб: 104")
                bot.send_message(call.message.chat.id, "Преподователь: Инна Ивановна")
                global MDhometaskBio, MDhometaskNem, MDhometaskGeo, MDhometaskUkrL\
            ,MDhometaskArt, MDhometaskChmstr
                bot.send_message(call.message.chat.id, "ДЗ:" + MDhometaskUkrL)
            elif call.data == 'art_cd':
                bot.send_message(call.message.chat.id, "<u>ИСКУСТВО</u>",parse_mode='html')
                bot.send_message(call.message.chat.id, "Каб: 118")
                bot.send_message(call.message.chat.id, "Преподователь: Юлия Валентиновна")
                global MDhometaskBio, MDhometaskNem, MDhometaskGeo\
            ,MDhometaskArt, MDhometaskChmstr
                bot.send_message(call.message.chat.id, "ДЗ:" + MDhometaskArt)
            elif call.data == 'pe_cd':
                bot.send_message(call.message.chat.id, "Просто возьми форму!")
            elif call.data == 'nem_cd':
                bot.send_message(call.message.chat.id, "<u>НЕМЕЦКИЙ</u>",parse_mode='html')
                bot.send_message(call.message.chat.id, "Каб: 104")
                bot.send_message(call.message.chat.id, "Преподователь: Валерия Сергеевна")
                global MDhometaskBio, MDhometaskNem, MDhometaskGeo\
            ,MDhometaskChmstr
                bot.send_message(call.message.chat.id, "ДЗ:" + MDhometaskNem)
            elif call.data == 'bio_cd':
                bot.send_message(call.message.chat.id, "<u>БИОЛОГИЯ</u>",parse_mode='html')
                bot.send_message(call.message.chat.id, "Каб: 104")
                bot.send_message(call.message.chat.id, "Преподователь: Елена Михайловна")
                global MDhometaskBio,MDhometaskGeo,MDhometaskChmstr
                bot.send_message(call.message.chat.id, "ДЗ:" + MDhometaskBio)
            elif call.data == 'geo_cd':
                bot.send_message(call.message.chat.id, "<u>ГЕОГРАФИЯ</u>",parse_mode='html')
                bot.send_message(call.message.chat.id, "Каб: 104")
                bot.send_message(call.message.chat.id, "Преподователь: Елена Еагеньевна")
                global MDhometaskGeo, MDhometaskChmstr
                bot.send_message(call.message.chat.id, "ДЗ:" + MDhometaskGeo)
            elif call.data == 'chm_cd':
                bot.send_message(call.message.chat.id, "<u>ХИМИЯ</u>",parse_mode='html')
                bot.send_message(call.message.chat.id, "Каб: 308")
                bot.send_message(call.message.chat.id, "Преподователь: Светлана Анатольевна")
                global MDhometaskChmstr
                bot.send_message(call.message.chat.id, "ДЗ:" + MDhometaskChmstr)
    except:
        pass

if __name__ == '__main__':
    bot.polling(none_stop=True)

