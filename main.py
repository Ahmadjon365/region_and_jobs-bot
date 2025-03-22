from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from pack_buttons import send_menu
from inlines import inline_handler
from messages import message_handler
from config import token


def start(update, context):
    send_menu(context=context, chat_id=update.message.chat_id)


def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
