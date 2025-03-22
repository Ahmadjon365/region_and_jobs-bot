from telegram import ReplyKeyboardMarkup, KeyboardButton

def send_menu(context, chat_id):
    butt = [
        [KeyboardButton('Regions'), KeyboardButton('Jobs')]
    ]
    context.bot.send_message(
        chat_id=chat_id,
        text='Menu:',
        reply_markup=ReplyKeyboardMarkup(keyboard=butt, resize_keyboard=True)
    )
