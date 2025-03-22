from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def send_salary_job(context, text_salary, chat_id, message_id=None):
    keyboard = [[InlineKeyboardButton(text="Back", callback_data="job_back")]]

    if message_id:
        context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=f"<b>{text_salary}</b>",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard),
            parse_mode="HTML"
        )
    else:
        context.bot.send_message(
            chat_id=chat_id,
            text=f"<b>{text_salary}</b>",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard),
            parse_mode="HTML"
        )
