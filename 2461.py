from telethon import TelegramClient
api_id = 1060200
api_hash = '43c8c02209d400e90a503cfca187aa19'
with TelegramClient('rebot', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('+44 7430 500470', 'Hello, myself!'))



from telethon import TelegramClient, events
api_id = 1060200
api_hash = '43c8c02209d400e90a503cfca187aa19'
client = TelegramClient('rebot', api_id, api_hash)
xmc_seed_nodes = '193.112.64.213\n111.230.177.177\n118.24.41.27\n123.206.77.55\nPorts:18081(18080) '
@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'Official website' in event.raw_text:
        await event.reply('http://monero-classic.org/')
    #if 'official website' in event.raw_text:
        await event.reply('http://monero-classic.org/')
    if 'xmc github' in event.raw_text:
        await event.reply('https://github.com/monero-classic')
    #if 'official website' in event.raw_text:
     #   await event.reply('http://monero-classic.org/')
    if 'xmc rpc' in event.raw_text:
        await event.reply('Related documents are in production：https://github.com/monero-classic/monero/wiki/Daemon-RPC-documentation')
    if 'xmc exchange' in event.raw_text:
        await event.reply('https://tradeogre.com/exchange/BTC-XMC')
    if 'xmc seed nodes' in event.raw_text:
        await event.reply(xmc_seed_nodes)
client.start()
client.run_until_disconnected()