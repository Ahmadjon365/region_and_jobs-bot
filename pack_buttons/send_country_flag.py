from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def send_country_flag(context, text_flag, chat_id, message_id=None):
    keyboard = [[InlineKeyboardButton(text="Back", callback_data="country_back")]]

    if message_id:
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=f"<b>{text_flag}</b>",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard),
            parse_mode="HTML"
        )
    else:
        context.bot.send_message(
            chat_id=chat_id,
            text=f"<b>{text_flag}</b>",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard),
            parse_mode="HTML"
        )
