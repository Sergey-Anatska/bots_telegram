import telebot
import logging
from telebot import types
from telebot.types import WebAppInfo


bot = telebot.TeleBot("6582505003:AAFHjvJKzyN1ZRnHiXeGZnAhE5mMcQ2cnhc")

btn_costs = types.InlineKeyboardButton('Узнать цены', callback_data='costs')
btn_states = types.InlineKeyboardButton('Где действует полис?', callback_data='states')
btn_border = types.InlineKeyboardButton('Как пересечь границу?', callback_data='border')
btn_car = types.InlineKeyboardButton('Легковой автомобиль', callback_data='car')
btn_moto = types.InlineKeyboardButton('Мотоцикл', callback_data='moto')
btn_bus = types.InlineKeyboardButton('Автобус', callback_data='bus')
btn_link = types.InlineKeyboardButton('Перейти на сайт',  url='https://greencard.agency/')
btn_crm_form = types.InlineKeyboardButton('ОФОРМИТЬ ПОЛИС',
                                          web_app=WebAppInfo(url='https://b24-u594l7.bitrix24.site/crm_form_f7oxx/'))
btn_manager = types.InlineKeyboardButton('Соеденить с оператором', url='https://t.me/GreenCardAgency_bot')
btn_main_menu = types.InlineKeyboardButton('Главное меню', callback_data='main_menu')
btn_pay_when = types.InlineKeyboardButton('Когда платить', callback_data='pay_when')
btn_pay_where = types.InlineKeyboardButton('Как платить', callback_data='pay_where')
btn_what_is = types.InlineKeyboardButton('Что это за страховка', callback_data='what_is')
btn_subject = types.InlineKeyboardButton('Предмет страхования', callback_data='subject')
btn_not_covered = types.InlineKeyboardButton('Что НЕ покрывает', callback_data='not_covered')
btn_restrictions = types.InlineKeyboardButton('Ограничения', callback_data='restrictions')
btn_start_end = types.InlineKeyboardButton('Время действия', callback_data='start_end')

def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(btn_costs)
    markup.row(btn_states, btn_border)
    markup.row(btn_what_is)
    markup.row(btn_crm_form, btn_link)
    bot.send_message(message.chat.id, 'Чем я могу помочь?',
                     reply_markup=markup)


@bot.message_handler(commands=['start'])
def hi_here(message):
    bot.send_message(message.chat.id, f'Добрый день, {message.from_user.first_name} {message.from_user.last_name}')
    bot.send_message(message.chat.id, f'Я телеграм-БОТ агентства <b>Green Card</b>.', parse_mode='HTML')
    main(message)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):

    markup_main = types.InlineKeyboardMarkup()
    markup_main.row(btn_crm_form)
    markup_main.row(btn_main_menu, btn_manager)

    if callback.data == 'costs':
        bot.send_message(callback.message.chat.id, 'Минимальный срок страхования 1 месяц')
        bot.send_message(callback.message.chat.id, 'Стоимость будет указана за 1 месяц.')
        bot.send_message(callback.message.chat.id,
                         'Что-бы узнать стоимость за 2 или 3 месяца, необходимо просто умножить ' 
                         'сумму на количество месяцев.')
        bot.send_message(callback.message.chat.id, f'<u><b>ВНИМАНИЕ!</b></u>', parse_mode='HTML')
        bot.send_message(callback.message.chat.id,
                         'При оформлении договора страхования на легковой автомобиль сразу на год, получите <u><b>'
                         'скидку до 48%</b></u>', parse_mode='HTML')
        markup = types.InlineKeyboardMarkup()
        markup.row(btn_pay_when, btn_pay_where)
        markup.row(btn_car)
        markup.row(btn_moto, btn_bus)
        bot.send_message(callback.message.chat.id, 'На какой вид транспорта Вы хотите оформить страховку?',
                         reply_markup=markup)

    elif callback.data == 'car':
        bot.send_message(callback.message.chat.id, 'Стоимость полиса на легковой автомобиль 185,4 злотых по курсу'
                         ' на день оплаты', reply_markup=markup_main)

    elif callback.data == 'moto':
        bot.send_message(callback.message.chat.id, 'Стоимость полиса на Мотоцикл 65 евро по курсу'
                         ' на день оплаты', reply_markup=markup_main)

    elif callback.data == 'bus':
        bot.send_message(callback.message.chat.id, 'Стоимость полиса на Автобус 240 евро по курсу'
                         ' на день оплаты', reply_markup=markup_main)

    elif callback.data == 'main_menu':
        main(callback.message)

    elif callback.data == 'states':
        bot.send_message(callback.message.chat.id, 'Действие полиса распространяется на все страны <b>Евросоюза</b>,'
                         ' а так же на <b>Швейцарию</b>', parse_mode='HTML')
        bot.send_message(callback.message.chat.id, 'Вот перечень стран, где действует полис:')
        bot.send_message(callback.message.chat.id, 'АВСТРИЯ, <i>БЕЛЬГИЯ</i>, БОЛГАРИЯ, <i>ВЕНГРИЯ</i>, ГРЕЦИЯ, '
                         '<i>ГЕРМАНИЯ</i>, ДАНИЯ, <i>ЭСТОНИЯ</i>, ИРЛАНДИЯ, <i>ИСЛАНДИЯ</i>, ИСПАНИЯ, <i>ИТАЛИЯ</i>,'
                         ' КИПР, <i>ЛИТВА</i>, ЛАТВИЯ, <i>ЛЮКСЕМБУРГ</i>, МАЛЬТА, <i>НИДЕРЛАНДЫ</i>, НОРВЕГИЯ,'
                         ' <i>ПОЛЬША</i>, ПОРТУГАЛИЯ, <i>РУМЫНИЯ</i>, СЛОВАКИЯ, <i>СЛОВЕНИЯ</i>, ФИНЛЯНДИЯ,'
                         ' <i>ЧЕШСКАЯ</i> РЕСПУБЛИКА, <i>ФРАНЦИЯ</i>, ХОРВАТИЯ, <b><i>ШВЕЙЦАРИЯ</i></b>, ШВЕЦИЯ',
                         parse_mode='HTML', reply_markup=markup_main)
        bot.send_message(callback.message.chat.id,
                         'Независимо от того, в какой стране приобретен указанный выше полис, он будет действовать'
                         ' во всех странах.')
        bot.send_message(callback.message.chat.id,
                         'Например Вы приобрели польский полис, с ним Вы без проблем проедете через границу'
                         ' Беларусь - Литва', reply_markup=markup_main)

    elif callback.data == 'border':
        bot.send_message(callback.message.chat.id,
                         'С 1 июня 2023 года прекращено сотрудничество между 31-ой европейской страной и странами'
                         ' Российская Федерация и Республика Беларусь по международному страхованию «Зеленая карта».'
                         'В связи с прекращением действия соглашения по «Зеленой карте» с 01 июня 2023 года пересечение'
                         ' границы возможно с договором пограничного страхования (Договор обязательного страхования'
                         ' гражданской ответственности водителей транспортных средств для нерезидентов).')
        bot.send_message(callback.message.chat.id,
                         '<b>Для пересечения границы</b> и прибывания в странах ЕС и Швейцарии на автомобиле '
                         'зегистрированном за границами ЕС или Швейцарии вы должны иметь при себе договор ' 
                         'обязательного страхования ответственности владельцев транспортных средсв нерезидента '
                         '(в просторечии: "Зеленая карта")\nПолис <b>в обязательном порядке необходимо распечатать</b>'
                         ' на простой белой бумаге', parse_mode='HTML')
        bot.send_message(callback.message.chat.id,
                         'Договор пограничного страхования заключенный в одной из стран Европейского союза или'
                         ' Швейцарии действует на территории всего Европейского союза и Швейцарии. Данный полис можно'
                         ' приобрести при посредничестве нашей компании. Договор оформляется в электронном виде. Но '
                         'его в обязательном порядке надо распечатать и иметь при себе.')
        bot.send_message(callback.message.chat.id,
                         'Независимо от того, в какой стране приобретен указанный выше полис, он будет действовать'
                         ' во всех странах.')
        bot.send_message(callback.message.chat.id,
                         'Например Вы приобрели польский полис, с ним Вы без проблем проедете через границу'
                         ' Беларусь - Литва', reply_markup=markup_main)

    elif callback.data == 'pay_when':
        bot.send_message(callback.message.chat.id,
                         'После оформления заявки, она будет отправлена в страховую компанию на акцептацию.\n'
                         ' Данный процесс может занять несколько часов.\n Только после того как страховая даст'
                         ' разрешение на продажу полиса, на вашу почту будет направлен счет на оплату',
                         parse_mode='HTML', reply_markup=markup_main)

    elif callback.data == 'pay_where':
        bot.send_message(callback.message.chat.id,
                         'Оплата полиса производится на польскую карту.\n Если у Вас беларуская карта - необходимо'
                         ' будет произвести перевод <b>с карты на карту</b> через Ваш интернет-банкинг.\n Если у ваш '
                         'банк под санкциями, можете скачать приложение БНБ банка и оформить виртуальную карту "123" '
                         'и с нее оплатить за страховку \n С европейских платежных карт необходимо будет произвести '
                         '<b>перевод на польский расчетный счет</b>', parse_mode='HTML', reply_markup=markup_main)

    elif callback.data == 'what_is':
        markup = types.InlineKeyboardMarkup()
        markup.row(btn_subject, btn_not_covered)
        markup.row(btn_start_end, btn_restrictions)
        markup.row(btn_main_menu)
        bot.send_message(callback.message.chat.id,
                         'Страхование гражданской ответственности владельцев автотранспортных средств ( ОC ) '
                         'является обязательным страхованием, применимым в ситуации, когда владелец или водитель '
                         'транспортного средства причиняет ущерб другим лицам, и в соответствии с применимым '
                         'законодательством несет за это гражданскую ответственность.\nОбязательство заключить договор '
                         'страхования гражданской ответственности распространяется на всех владельцев транспортных '
                         'средств, т.е. как владельцев, так и пользователей ( например, когда транспортное средство '
                         'сдано в аренду или в так называемом "пользовании" ',
                         parse_mode='HTML', reply_markup=markup)

    elif callback.data == 'subject':
        markup = types.InlineKeyboardMarkup()
        markup.row(btn_what_is, btn_not_covered)
        markup.row(btn_start_end, btn_restrictions)
        markup.row(btn_main_menu)
        bot.send_message(callback.message.chat.id,
                         'Страховая защита охватывает гражданскую ответственность владельца и/или водителя '
                         'механического транспортного средства, указанного в полисе, за ущерб, причиненный третьим '
                         'лицам в связи с движением этого транспортного средства.\nСтраховая компания несет '
                         'ответственность в пределах установленной в страховом договоре гарантированной суммы, которая '
                         'в отношении одного события, независимо от числа пострадавших, не может быть менее следующей '
                         'в эквиваленте:\n- 5 210 000 евро - в случае ущерба личности\n- 1 050 000 евро - в случае '
                         'ущерба имуществу\n\nЗа ущерб, причиненный в других странах, кроме Республики Польша, на '
                         'территории которых действует страховая защита, страховая компания несет ответственность в '
                         'пределах гарантированной суммы, установленной законами этой страны, но не менее суммы, '
                         'указанной выше. Подробное описание объекта и объема страхования содержится в Уставе.',
                         parse_mode='HTML', reply_markup=markup)

    elif callback.data == 'not_covered':
        markup = types.InlineKeyboardMarkup()
        markup.row(btn_subject, btn_what_is)
        markup.row(btn_start_end, btn_restrictions)
        markup.row(btn_main_menu)
        bot.send_message(callback.message.chat.id,
                         '- транспортных средств, отличных от механических транспортных средств в смысле Закона;\n'
                         '- ущерба, заключающегося в повреждении, уничтожении или утрате имущества, причиненного '
                         'водителем механического транспортного средства владельцу этого транспортного средства;\n'
                         '- ущерба, связанного с загрязнением или заражением окружающей среды.\n\nПодробная информация '
                         'о объеме страховой защиты, которая не распространяется на указанные случаи, содержится в '
                         'Уставе.', parse_mode='HTML', reply_markup=markup)

    elif callback.data == 'restrictions':
        markup = types.InlineKeyboardMarkup()
        markup.row(btn_subject, btn_not_covered)
        markup.row(btn_start_end, btn_what_is)
        markup.row(btn_main_menu)
        bot.send_message(callback.message.chat.id,
                         'Страховая компания имеет право требовать от водителя возврата выплаченной компенсации по '
                         'страхованию гражданской ответственности (ОСАГО) неризидента ЕС, если водитель:\n- нанес '
                         'ущерб умышленно, будучи в нетрезвом состоянии, после употребления алкоголя или наркотических '
                         'средств;\n- приобрел право владения автомобилем в результате совершения преступления;\n'
                         '- не обладал необходимыми правами для управления автомобилем;\n- сбежал с места происшествия.'
                         '\n\nПодробная информация, а также другие ограничения и исключения, которые дают право '
                         'отказать в выплате компенсации и других пособий или снизить их размер, содержатся в Уставе.',
                         parse_mode='HTML', reply_markup=markup)

    elif callback.data == 'start_end':
        markup = types.InlineKeyboardMarkup()
        markup.row(btn_subject, btn_not_covered)
        markup.row(btn_what_is, btn_restrictions)
        markup.row(btn_main_menu)
        bot.send_message(callback.message.chat.id,
                         'Страховая защита начинается после заключения страхового договора, с даты, указанной в '
                         'полисе и согласованной сторонами. Договор может быть заключен на любой срок до 364 дней но не '
                         'менее 30 дней.\nСтраховой договор расторгается:\n- по истечении срока, на который он был '
                         'заключен;\n- с момента документированной утраты автомобиля на постоянной основе;\n- с даты '
                         'выдачи свидетельства о списании автомобиля.\n\nПодробная информация о сроке страховой защиты '
                         'содержится в Уставе.', parse_mode='HTML', reply_markup=markup)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as ex:
            logger.error(ex)
