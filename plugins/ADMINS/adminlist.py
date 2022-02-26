

import html

from Stella import StellaCli
from plugins.helper import custom_filter
from plugins.helper.disable import disable


@StellaCli.on_message(custom_filter.command(commands=('adminlist'), disable=True))
@disable
async def admin_list(client, message):
    chat_title = message.chat.title 
    chat_id = message.chat.id 

    data_list = await StellaCli.get_chat_members(
        chat_id=chat_id,
        filter='administrators'
        )
    ADMINS_LIST = []
    for user in data_list:
        if user.user.username is not None:
            ADMINS_LIST.append(f'- <a href=tg://user?id={user.user.username}>{user.user.first_name}</a> id `{user.user.id}`\n')
        else:
            ADMINS_LIST.append(f'- <a href=tg://user?id={user.user.id}>{user.user.first_name}</a> id `{user.user.id}`\n')


    admin_header = f"Admins in {html.escape(chat_title)}:\n"
    
    for admin in ADMINS_LIST:
        admin_header += admin
    await message.reply(
        (
            f"{admin_header}\n\n"
            "__These are the updated values.__"
        ),
        quote=True
    )
        
