import telebot
import requests
from telebot import types

token = '5406309028:AAEW7yQajJqmSR7M9vA0pjEwT2AHLZRK1Dg'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.chat.id,
                         "Добрый день!  В компании Теремок сейчас открыта позиция Повар-кассир в г. Москва. Если вакансия интересна, то дальше мы расскажем об условиях работы.")
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='Success1')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='Refuse1')
        keyboard.add(key_no)
        bot.send_message(message.from_user.id, text='Интересна ли вам вакансия?', reply_markup=keyboard)

    if message.text == "/second":
        bot.send_message(message.chat.id,
                         "Здравствуйте! Вы были записаны на собеседование в сеть ресторанов «Теремок». К сожалению, вы не пришли на собеседование😔. Мы можем сейчас Вас повторно записать к нам на собеседование.")
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='Success3')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='Refuse3')
        keyboard.add(key_no)
        bot.send_message(message.from_user.id, text='Вы готовы приехать на собеседование?', reply_markup=keyboard)

    if message.text == "/third":
        bot.send_message(message.chat.id,
                         "Здравствуйте! 👋 Вас приветствует сеть ресторанов «Теремок».  Ранее мы с вами связывались и общались по вакансии Повар-кассир.")
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='Success1')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='Refuse1')
        keyboard.add(key_no)
        bot.send_message(message.from_user.id, text='Продолжим диалог?', reply_markup=keyboard)

def reason_handler(message):
    bot.send_message(message.chat.id, text="Спасибо за ваш ответ!")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Success1":
        photo = open('test_starting_pic.jpeg', 'rb')
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='Success2')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='Refuse2')
        keyboard.add(key_no)
        bot.send_message(call.message.chat.id, text="Отлично! Мы предлагаем:\nЗ/П от 49 000 до 82 000 руб., всегда есть подработка.\nРаботу рядом с домом.\nГрафик работы на выбор: 3/3; гибкий от 6 часов в день; вахта – 20/10 или 30/10.\nКомпенсацию проживания в общежитии в размере 9 000 руб., или ЖКХ до 5 000 руб.\nОплата проезда в первый месяц работы.\nОплата проезда из региона до Москвы по факту предоставления именного билета.\nПомощь в оформлении мед. книжки.\nБесплатное, вкусное и полезное питание, комфортная спецодежда.\nКарьерный рост до Администратора ресторана.\n")
        bot.send_photo(call.message.chat.id, photo=photo)
        photo.close()
        bot.send_message(call.message.chat.id, text="Что нужно делать:\nЗаниматься приготовлением блюд русской кухни.\nПриветствовать гостя, помогать в выборе блюд, расчитывать его на кассе.\n")
        bot.send_message(call.message.chat.id, text="Рассматриваем без опыта работы, предусмотрено бесплатное обучение, стипендия 15000 руб.\n")
        bot.send_message(call.message.chat.id, text="Устраивают ли вас предложенные условия?\n", reply_markup=keyboard)

    if call.data == "Success2":
        bot.send_message(call.message.chat.id, text="Ответьте на 2 вопроса, чтобы узнать вас получше.\n")
        keyboard = types.InlineKeyboardMarkup()
        key_age1 = types.InlineKeyboardButton(text='Младше 18 лет', callback_data='BadAge')
        keyboard.add(key_age1)
        key_age2 = types.InlineKeyboardButton(text='От 18 до 65 лет', callback_data='GoodAge')
        keyboard.add(key_age2)
        key_age3 = types.InlineKeyboardButton(text='Старше 65 лет', callback_data='BadAge')
        keyboard.add(key_age3)
        bot.send_message(call.message.chat.id, text='Укажите, пожалуйста, ваш возраст:\n', reply_markup=keyboard)

    if call.data == "GoodAge":
        keyboard = types.InlineKeyboardMarkup()
        key_age1 = types.InlineKeyboardButton(text='Россия / Беларусь', callback_data='GoodFinal')
        keyboard.add(key_age1)
        key_age2 = types.InlineKeyboardButton(text='Армения / Казахстан / Киргизия / Украина', callback_data='BadFinal')
        keyboard.add(key_age2)
        key_age3 = types.InlineKeyboardButton(text='Другое', callback_data='BadFinal')
        keyboard.add(key_age3)
        bot.send_message(call.message.chat.id, text='Укажите, пожалуйста, ваше гражданство:\n', reply_markup=keyboard)

    if call.data == "BadAge":
        keyboard = types.InlineKeyboardMarkup()
        key_age1 = types.InlineKeyboardButton(text='Россия / Беларусь', callback_data='BadFinal')
        keyboard.add(key_age1)
        key_age2 = types.InlineKeyboardButton(text='Армения / Казахстан / Киргизия / Украина',
                                              callback_data='BadFinal')
        keyboard.add(key_age2)
        key_age3 = types.InlineKeyboardButton(text='Другое', callback_data='BadFinal')
        keyboard.add(key_age3)
        bot.send_message(call.message.chat.id, text='Укажите, пожалуйста, ваше гражданство:\n', reply_markup=keyboard)

    if call.data == "BadFinal":
        bot.send_message(call.message.chat.id, text="Спасибо за предоставленную информацию!\nМы передадим ваши данные на рассмотрение специалистам.\nВ случае положительного решения мы с вами свяжемся в течение двух рабочих дней.\n")

    if call.data == "GoodFinal":
        photo2 = open('test_teremok_route.jpeg', 'rb')
        photo3 = open('test_teremok_entrance.jpeg', 'rb')
        bot.send_photo(call.message.chat.id, photo2)
        bot.send_photo(call.message.chat.id, photo3)
        photo2.close()
        photo3.close()
        bot.send_message(call.message.chat.id, text="Отлично!\nПриходите на собеседование в будни с 09:00 до 17:00.\nм. Парк Культуры, ул. Зубовский бульвар дом 22/39 (7 мин., пешком).\nДеловой Центр \'Пречистенка\' (два льва у входа). Из стеклянных дверей направо, второй лифт, на лифте на 5 этаж.\nПо возможности возьмите с собой паспорт, ИНН, СНИЛС, трудовую книжку, если есть - документ об образовании и медицинскую книжку.\nТелефон для связи +7 495 736 96 95 или 8 800 333 31 20 (звонок бесплатный!)")

    if call.data == "Refuse2":
        keyboard = types.InlineKeyboardMarkup()
        key_decl21 = types.InlineKeyboardButton(text='Мне неудобен график', callback_data='Decline2-1')
        keyboard.add(key_decl21)
        key_decl22 = types.InlineKeyboardButton(text='Низкая зарплата', callback_data='Decline2-2')
        keyboard.add(key_decl22)
        key_decl23 = types.InlineKeyboardButton(text='Обязанности не совпали с ожиданием', callback_data='Decline2-3')
        keyboard.add(key_decl23)
        key_decl24 = types.InlineKeyboardButton(text='Было интересно узнать детали, работу не ищу', callback_data='Decline2-4')
        keyboard.add(key_decl24)
        key_decl25 = types.InlineKeyboardButton(text='Не готов проходить обучение', callback_data='Decline2-5')
        keyboard.add(key_decl25)
        key_decl26 = types.InlineKeyboardButton(text='Другая причина', callback_data='Decline2-6')
        keyboard.add(key_decl26)
        bot.send_message(call.message.chat.id, text="Пожалуйста, подскажите, почему Вы не готовы продолжать диалог?", reply_markup=keyboard)

    if call.data == "Decline2-1" or call.data == "Decline2-2" or call.data == "Decline2-3" or call.data == "Decline2-4" or call.data == "Decline2-5":
        bot.send_message(call.message.chat.id, "Спасибо за Ваш ответ!")

    if call.data == "Decline2-6":
        bot.send_message(call.message.chat.id, "Возможно, у Вас остались вопросы по вакансии или вы пересмотрели своё решение\nЕсли вы готовы рассмотреть нашу вакансию, можете связаться с нами по номеру +7 495 736 96 95 или 8 800 333 31 20 (звонок бесплатный!) или приехать в офис на собеседование по адресу м. Парк Культуры, ул. Зубовский бульвар дом 22/39 (7 мин., пешком).")
        photo = open('test_teremok_route.jpeg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        photo.close()

    if call.data == "Refuse1":
        keyboard = types.InlineKeyboardMarkup()
        key_decl1 = types.InlineKeyboardButton(text='Мне не подходит должность', callback_data='Decline1')
        keyboard.add(key_decl1)
        key_decl2 = types.InlineKeyboardButton(text='Не хочу работать в общепите', callback_data='Decline2')
        keyboard.add(key_decl2)
        key_decl3 = types.InlineKeyboardButton(text='Не подходит город', callback_data='Decline3')
        keyboard.add(key_decl3)
        key_decl4 = types.InlineKeyboardButton(text='Ищу работу не для себя', callback_data='Decline4')
        keyboard.add(key_decl4)
        key_decl5 = types.InlineKeyboardButton(text='Другая причина', callback_data='Decline5')
        keyboard.add(key_decl5)
        bot.send_message(call.message.chat.id, text="Пожалуйста, подскажите, почему Вам не интересна эта вакансия?", reply_markup=keyboard)

    if call.data == "Decline1" or call.data == "Decline2" or call.data == "Decline3" or call.data == "Decline4":
        bot.send_message(call.message.chat.id, "Спасибо за Ваш ответ!")

    if call.data == "Decline5":
        reason = bot.send_message(call.message.chat.id, "Какую вакансию вы ищете? (Напишите, пожалуйста, свой вариант одним соообщением)")
        bot.register_next_step_handler(reason, reason_handler)

    # Splitter : CASE 2

    if call.data == "Success3":
        photo2 = open('test_teremok_route.jpeg', 'rb')
        photo3 = open('test_teremok_entrance.jpeg', 'rb')
        bot.send_photo(call.message.chat.id, photo2)
        bot.send_photo(call.message.chat.id, photo3)
        photo2.close()
        photo3.close()
        bot.send_message(call.message.chat.id,
                         text="Приходите на собеседование в будни с 09:00 до 17:00.\nм. Парк Культуры, ул. Зубовский бульвар дом 22/39 (7 мин., пешком).\nДеловой Центр \'Пречистенка\' (два льва у входа). Из стеклянных дверей направо, второй лифт, на лифте на 5 этаж.\nПо возможности возьмите с собой паспорт, ИНН, СНИЛС, трудовую книжку, если есть - документ об образовании и медицинскую книжку.\n")
        bot.send_message(call.message.chat.id, text="Мы ждем Вас и благодарим за уделённое время! 😊\nПри возникновении вопросов обращаться по телефону +74957369395 или 8 800 333 31 20 (звонок бесплатный).")

    if call.data == "Refuse3":
        keyboard = types.InlineKeyboardMarkup()
        key_decl31 = types.InlineKeyboardButton(text='Мне неудобен график', callback_data='Decline3-1')
        keyboard.add(key_decl31)
        key_decl32 = types.InlineKeyboardButton(text='Низкая зарплата', callback_data='Decline3-2')
        keyboard.add(key_decl32)
        key_decl33 = types.InlineKeyboardButton(text='Обязанности не совпали с ожиданием', callback_data='Decline3-3')
        keyboard.add(key_decl33)
        key_decl34 = types.InlineKeyboardButton(text='Было интересно узнать детали, работу не ищу',
                                                callback_data='Decline3-4')
        keyboard.add(key_decl34)
        key_decl35 = types.InlineKeyboardButton(text='Не готов проходить обучение', callback_data='Decline3-5')
        keyboard.add(key_decl35)
        key_decl36 = types.InlineKeyboardButton(text='Другая причина', callback_data='Decline3-6')
        keyboard.add(key_decl36)
        bot.send_message(call.message.chat.id, text="Пожалуйста, подскажите, почему Вы не готовы продолжать диалог?",
                         reply_markup=keyboard)

    if call.data == "Decline3-1" or call.data == "Decline3-2" or call.data == "Decline3-3" or call.data == "Decline3-4" or call.data == "Decline3-5":
        bot.send_message(call.message.chat.id, "Спасибо за Ваш ответ! ")

    if call.data == "Decline3-6":
        bot.send_message(call.message.chat.id,
                         "Возможно, у Вас остались вопросы по вакансии или вы пересмотрели своё решение\nЕсли вы готовы рассмотреть нашу вакансию, можете связаться с нами по номеру +7 495 736 96 95 или 8 800 333 31 20 (звонок бесплатный!) или приехать в офис на собеседование по адресу м. Парк Культуры, ул. Зубовский бульвар дом 22/39 (7 мин., пешком).")
        photo = open('test_teremok_route.jpeg', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        photo.close()



bot.polling(none_stop=True)