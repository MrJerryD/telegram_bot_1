import telebot
from config import token
# тут токен
telebot.apihelper.ENABLE_MIDDLEWARE = True # активировали middleware_handler (3) обработчик левого текста

mybot = telebot.TeleBot(token)
name = ''

# обработчик сообщение, написали в декораторе комманды которые пишем в боте при обращении
@mybot.message_handler(commands=['start'])
def start_message(message):
    mybot.send_message(message.chat.id, 'Hello! My dure friend')
    markup_keyboard = telebot.types.ReplyKeyboardMarkup()
    btn_1 = telebot.types.KeyboardButton('hi')
    btn_2 = telebot.types.KeyboardButton('/help')
    btn_3 = telebot.types.KeyboardButton('/voice')
    btn_4 = telebot.types.KeyboardButton('Шо клацаешь')
    markup_keyboard.row(btn_1, btn_2, btn_3)
    markup_keyboard.row(btn_4)
    mybot.send_message(message.chat.id, 'Here some setting: ', reply_markup=markup_keyboard)

    with open('filefile.txt', 'a') as f:
        print(message.te/xt, file=f)
        print(message.from_user.username, file=f)\


@mybot.message_handler(commands=['help'])
def help_message(message):
    mybot.send_message(message.chat.id, "Here commands what we have\n/start\n/help\nyou can send voice\ntext 'hi', after text your name")
    # print(message.from_user.username)
    # print(type(message))


@mybot.message_handler(content_types=['voice'])
def voice_message(message):
    mybot.send_message(message.chat.id, 'Wow, but I cannot talk')


@mybot.message_handler(content_types=['text'])
def hello_mess(message):
    if message.text.lower() == 'hi':
        mybot.send_message(message.chat.id, 'sup')
        mybot.send_message(message.chat.id, 'What is your name?')
        mybot.register_next_step_handler(message, req_name)
def req_name(message):
    global name
    name = message.text
    mybot.send_message(message.chat.id, f'Glad to see you {name}')

    # клавиатура inline (отображаются где смски приходят)
    my_kyeboard = telebot.types.InlineKeyboardMarkup()
    key_one = telebot.types.InlineKeyboardButton(text='text', callback_data='1')
    key_two = telebot.types.InlineKeyboardButton(text='text_2', callback_data='2')
    my_kyeboard.add(key_one, key_two)
    mybot.send_message(message.chat.id, '_text_', reply_markup=my_kyeboard)
# для клавы
@mybot.callback_query_handler(func=lambda call: True)
def call_back_kyeboard(call):
    if call.data == '1':
        mybot.send_message(call.message.chat.id, ':)')
    if call.data == '2':
        mybot.send_message(call.message.chat.id, ':|')




# перехватил смс с левыми словами, не командамми
# middleware_handler - выполняется каждый раз при запросе бота
# @mybot.middleware_handler(update_types=['message'])
# def mes_up(bot_instance, message): # bot_instance обязательно, без ошибка
#     if not message.text.startswith('/'): #and 'hi'.lower()):
#         mybot.send_message(message.chat.id, ' WHATUFC IS THAT? - ' + message.text)
#         print(message.json)
        # print(message)
        # print(type(message))

mybot.infinity_polling() # заустили бота | infinity_polling - раз в n секунд опрашивает сервера тг на новые сообщения
