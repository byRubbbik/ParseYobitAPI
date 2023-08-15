import requests
import datetime


class CryptoInfo:
    def __init__(self, coin1='usdt', coin2='usd', limit=150) -> None:
        self.coin1 = coin1
        self.coin2 = coin2
        self.limit = limit
        
        self.responseInfo = requests.get(url='https://yobit.net/api/3/info')
        self.responseTicker = requests.get(url=f'https://yobit.net/api/3/ticker/{self.coin1}_{self.coin2}?ignore_invalid=1')
        self.responseDepth = requests.get(url=f'https://yobit.net/api/3/depth/{self.coin1}_{self.coin2}?limit={self.limit}&ignore_invalid=1')
        self.responseTrades = requests.get(url=f'https://yobit.net/api/3/trades/{self.coin1}_{self.coin2}?limit={self.limit}&ignore_invalid=1')

    def getInfo(self):
        with open('info.txt', 'w', encoding='utf-8') as file:
            file.write(self.responseInfo.text)

        return 0

    def getTicker(self):
        with open('ticker.txt', 'w', encoding='utf-8') as file:
            file.write(self.responseTicker.text)
        
        return 0
    
    def getDepth(self):

        with open('depth.txt', 'w', encoding='utf-8') as file:
            file.write(self.responseDepth.text)

        bids = self.responseDepth.json()[f'{self.coin1}_usd']['bids']
        total_bids_amount = 0

        for item in bids:
            price = item[0]
            coin_amount = item[1]

            total_bids_amount += price * coin_amount

        return print(total_bids_amount)
    
    def getTrades(self):
        with open('trades.txt', 'w', encoding='utf-8') as file:
            file.write(self.responseTrades.text)

        return 0


if __name__ == '__main__':
    s = CryptoInfo(coin1='usdt', coin2='usd', limit=200)
    s.getInfo()
    s.getDepth()
    s.getTicker()
    s.getTrades()
