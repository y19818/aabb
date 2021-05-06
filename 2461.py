import schedule
import time
from telethon import TelegramClient, events
api_id = 1060200
api_hash = '43c8c02209d400e90a503cfca187aa19'
client = TelegramClient('rebot21', api_id, api_hash)
txt = '''
VNS is the first eco-platform project that fully integrates AMT value idea after years of accumulation of experiences of AMT Community. The idea connotations of VNS are closely related to the value reflections of AMT Community, which can be called the crystallization of thought of AMT Community over the years. AMT Community believes that the blockchain technology will certainly change human lifestyle, the communication of future society will evolve into value interconnection on the basis of the current information interconnection, and in the trust system constructed by blockchain, all kinds of people or things will deliver their value via the blockchain network, to form a rich ecology of value internet, to eventually increase the social production efficiency greatly.

The ONLY Official Website：
http://www.vnscoin.org/

Wallet：
Bitpie：https://bitpie.com/ （Recommended）
CoinID：https://www.coinid.pro/ 
BITKAN：https://bitkan.com/en/app

VNS Blockchain Explorer：
http://explorer.vnscoin.org/
http://vns.vnscoin.org/

VNS Pool：

Pool NO.1：http://www.vnspool.org/#/miners
Mine command：start /high VNSMiner.exe （The number of threads of Mining）http://59.175.238.51:18888/Your wallet address

Pool NO.2：http://www.wawapool.com/#/miners
Mine command：start /high VNSMiner.exe （The number of threads of Mining） http://118.25.228.226:8888/ Your wallet address

Pool NO.3：http://47.92.5.207/#/miners
Mine command：start /high VNSMiner.exe （The number of threads of Mining） http://47.92.5.207:8888/ Your wallet address

Pool NO.4：http://www.xiaomipool.com/#/miners
Mine command：start /high VNSMiner.exe （The number of threads of Mining） http://129.28.240.129:8888/ Your wallet address

Exchange：
CoinX：https://www.coinx.pro/ 
https://www.coinciyuan.com/
CEX：https://www.cex.com/
 https://www.cex.plus/
Hcoin：https://www.hcoin86.com/
CoinBig：https://www.coinbig.com/
bitrabbit：https://bitrabbit.com/
bituan：https://www.bituan.io/

If you want to play with VNS 
You can use the following links：
https://github.com/AMTcommunity/go-vnscoin'''
def add():

    async def main():
        await client.send_message('VNScoin_Official',txt)

    with client:
        client.loop.run_until_complete(main())
schedule.every(15).minutes.do(add)
while True:
    # 启动服务
    schedule.run_pending()
    time.sleep(1)