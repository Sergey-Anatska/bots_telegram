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
btn_trailer = types.InlineKeyboardButton('Прицеп к легковому авто', callback_data='trailer')
btn_crm_form = types.InlineKeyboardButton('ОФОРМИТЬ ПОЛИС',
                                          web_app=WebAppInfo(url='https://b24-u594l7.bitrix24.site/crm_form_wx0h6/'))
btn_manager = types.InlineKeyboardButton('Соеденить с оператором', url='https://t.me/GreenCardAgency_bot')
btn_main_menu = types.InlineKeyboardButton('Главное меню', callback_data='main_menu')
btn_pay_when = types.InlineKeyboardButton('Когда платить', callback_data='pay_when')
btn_pay_where = types.InlineKeyboardButton('Как платить', callback_data='pay_where')


def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(btn_costs)
    markup.row(btn_states, btn_border)
    markup.row(btn_crm_form)
    bot.send_message(message.chat.id, 'Чем я могу помочь?',
                     reply_markup=markup)


@bot.message_handler(commands=['start'])
def hiHere(message):
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
                         ' Данный процесс может занять несколько рабочих дней.\n Только после того как страховая даст'
                         ' разрешение на продажу полиса, на вашу почту будет направлен счет на оплату',
                         parse_mode='HTML', reply_markup=markup_main)
    elif callback.data == 'pay_where':
        bot.send_message(callback.message.chat.id,
                         'Оплата полиса производится на польскую карту.\n Если у Вас беларуская карта - необходимо'
                         ' будет произвести перевод <b>с карты на карту</b> через Ваш интернет-банкинг.\n Если у Вас '
                         'российская карта, вам необходимо <b>открыть счет в Wise</b> и произвести перевод с Wise на '
                         'польский расчетный счет. \n С европейских платежных карт необходимо будет произвести '
                         '<b>перевод на польский расчетный счет</b>', parse_mode='HTML', reply_markup=markup_main)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as ex:
            logger.error(ex)
