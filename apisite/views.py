from django.shortcuts import render
from django.http import HttpResponse
from coinmarketcapapi import CoinMarketCapAPI

def index(request):
    cmc = CoinMarketCapAPI('a60407f9-fc24-409f-a3d0-f1200c0203c4')
    symbol_list = ['BTC', 'ETH', 'USDT', 'BNB', 'USDC', 'XRP', 'ADA', 'DOGE', 'TRX', 'MATIC']
    context = {}
    symbo_price = {}
    symbo = []
    price = []
    for Sym in symbol_list:
        result = cmc.tools_priceconversion(amount=1, symbol=Sym, convert='JPY')
        inte = result.data[0]['quote']['JPY']['price']
        symbo_price[f"{Sym}"] = inte

    context = {
        "data_list": symbo_price
               }
    return render(request, 'apisite/index.html', context)