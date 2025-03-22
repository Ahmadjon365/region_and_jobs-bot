from pack_buttons import send_regions, send_jobs
from config import dataBase
from database import DataBase

db = DataBase(dataBase)


def message_handler(update, context):
    chat_id = update.message.chat_id
    text = update.message.text
    if text == 'Regions':
        regions = db.get_all_regions()
        send_regions(context=context, regions=regions, chat_id=chat_id)
    elif text == 'Jobs':
        jobs = db.get_all_jobs()
        send_jobs(context=context, jobs=jobs, chat_id=chat_id)
