from loguru import logger
import random

from help import Account, send_message, sleeping_between_wallets, intro, outro
from settings import bot_status, shuffle, bot_id, bot_token, module
from zkfair_module import zkFairSwap, OrbiterBridge




def main():
    with open('proxies.txt', 'r') as file:  # login:password@ip:port в файл proxy.txt
        proxies = [row.strip() for row in file]
    with open('wallets.txt', 'r') as file:
        wallets = [row.strip() for row in file]
    send_list = []
    intro(wallets)
    count_wallets = len(wallets)

    if len(proxies) == 0:
        proxies = [None] * len(wallets)
    if len(proxies) != len(wallets):
        logger.error('Proxies count doesn\'t match wallets count. Add proxies or leave proxies file empty')
        return

    data = [(wallets[i], proxies[i]) for i in range(len(wallets))]

    if shuffle:
        random.shuffle(data)

    for idx, (wallet, proxy) in enumerate(data, start=1):
        if ':' in wallet:
            private_key, addressokx = wallet.split(':')[0], wallet.split(':')[1]
        else:
            private_key = wallet
            addressokx = None

        account = Account(idx, private_key, proxy, "Scroll")
        print(f'{idx}/{count_wallets} : {account.address}\n')
        send_list.append(f'{account.id}/{count_wallets} : [{account.address}]({"https://debank.com/profile/" + account.address})')


        try:
            if module == 1:
                send_list.append(zkFairSwap(id=account.id, private_key=account.private_key, proxy=account.proxy, rpc="zkFair").main())
            if module == 2:
                send_list.append(OrbiterBridge(account.id, account.private_key, account.proxy, 'zkFair').bridge(from_chain='zkFair', to_chain='Optimism'))
            if module == 3:
                send_list.append(zkFairSwap(account.id, account.private_key, account.proxy, 'Optimism').send_to_okex(addressokx=addressokx))


        except Exception as e:
            logger.error(f'{idx}/{count_wallets} Failed: {str(e)}')
            sleeping_between_wallets()

        if bot_status == True:
            if account.id == count_wallets:
                send_list.append(f'\nSubscribe: https://t.me/CryptoMindYep')
            send_message(bot_token, bot_id, send_list)
            send_list.clear()

        if idx != count_wallets:
            sleeping_between_wallets()
            print()


    outro()
main()