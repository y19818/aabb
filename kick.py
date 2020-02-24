from telethon import TelegramClient, events

api_id = 1060200
api_hash = '43c8c02209d400e90a503cfca187aa19'
client = TelegramClient('rebot', api_id, api_hash)
name = []
result = {}
list_chat = [352416960,1224781314,1001224781314]
@client.on(events.NewMessage)
async def my_event_handler(event):

    if 'https' in event.raw_text :
        chat = await event.get_chat()
        sender = await event.get_sender()
        chat_id = abs(event.chat_id)
        if   chat_id in list_chat:
            sender_id = event.sender_id
            name.append(sender_id)
    for i in set(name):
        result[i] = name.count(i)
        if result[sender_id]  == 1 :
            await event.reply('请不要在群内发送无关链接，警告两次之后会被自动踢出群聊')
        if result[sender_id]  == 2 :
            await event.reply('请不要在群内发送无关链接，警告一次之后会被自动踢出群聊')
        if result[sender_id]  == 3 :
            await client.kick_participant(chat_id, sender_id)



    print(name)

    print(result)

    print(chat_id)

    print(sender_id)


client.start()
client.run_until_disconnected()