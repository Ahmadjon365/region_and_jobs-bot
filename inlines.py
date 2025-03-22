from pack_buttons import send_regions, send_countries, send_jobs, send_salary_job, send_country_flag
from database import DataBase
from config import dataBase
db = DataBase(dataBase)

def inline_handler(update, context):
    query = update.callback_query
    message_id = query.message.message_id
    chat_id = query.message.chat_id

    data = str(query.data).split('_')
    print(data)
    if data[0] == 'region':
        if data[1].isdigit():
            countries = db.get_countries_by_region(int(data[1]))
            send_countries(context=context, countries=countries, chat_id=chat_id,
                           message_id=message_id)
        elif data[1] == 'back':
            regions = db.get_all_regions()
            send_regions(context=context, regions=regions, chat_id=chat_id,
                         message_id=message_id)
    if data[0] == 'country':
        if data[1] in [
            "AR", "AU", "BE", "BR", "CA", "CH", "CN", "DE", "DK", "EG",
            "FR", "HK", "IL", "IN", "IT", "JP", "KW", "MX", "NG", "NL",
            "SG", "UK", "US", "ZM", "ZW"]:
            country = db.get_country_by_id(data[1])
            flag = country[0]['flags']
            text_flag = f"The flag of this country is {flag}"

            send_country_flag(context=context, text_flag=text_flag, chat_id=chat_id,
                              message_id=message_id)
        elif data[1] == 'back':
            regions = db.get_all_regions()
            send_regions(context=context, regions=regions, chat_id=chat_id,
                         message_id=message_id)
    if data[0] == 'job':
        if data[1].isdigit():
            job = db.get_job_by_id(int(data[1]))
            min_salary = job[0]['min_salary']
            max_salary = job[0]['max_salary']
            text_salary = f"The salary for this job is from {min_salary} to {max_salary}"

            send_salary_job(context=context, text_salary=text_salary, chat_id=chat_id,
                            message_id=message_id)
        elif data[1] == 'back':
            jobs = db.get_all_jobs()
            send_jobs(context=context, jobs=jobs, chat_id=chat_id,
                                message_id=message_id)
    if data[0] == 'close':
        msg = query.message.edit_text(
            text='⏳',
            reply_markup=None
        )
        context.bot.delete_message(chat_id=chat_id, message_id=msg.message_id)
