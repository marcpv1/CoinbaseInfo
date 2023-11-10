from coinbase.wallet.client import Client
from coinbase.wallet.model import Transaction
#from forex_python.converter import CurrencyRates
import sys
import json
import httplib
import urllib
import json

sys.path.insert(0,'/home/pi/coinbase_git')
import config_coin_mpv
import config_coin_arg

if (len(sys.argv)>0):
   user = sys.argv[1]

if (user=='mpv'):
    api_key = config_coin_mpv.api_key
    api_secret = config_coin_mpv.api_secret
   
if (user=='arg'):
    api_key = config_coin_arg.api_key
    api_secret = config_coin_arg.api_secret


client = Client(api_key, api_secret)
currency_EUR = 'BTC-EUR'
currency_USD = 'BTC-USD'
currencyEURUSD='EUR-USD'
currency_LINK='LINK-EUR'
currency_LINK_USD='LINK-USD'
currency_ETH='ETH-EUR'
currency_ETH_USD='ETH-USD'
currency_ADA='ADA-EUR'
currency_ADA_USD='ADA-USD'
currency_SOL='SOL-EUR'
currency_SOL_USD='SOL-USD'

total = 0
COIN_wallet=0

COINS=["BTC","ETH", "LINK"]

#accounts = client.get_accounts()
#print(accounts.data)

class Moneda(object):
    def __init__(self, code, URL1, URL2):
        self.code = code
        self.URL1 = URL1
        self.URL2 = URL2

llista_moneda = []

llista_moneda.append(Moneda("BTC" ,"<a href=\"https://coinmarketcap.com/es/currencies/bitcoin/\" target=\"_blank\">"    ,  "<img src=\"https://assets.bitstamp.net/widgets/s/widgets/widgets/img/btc.5e2d1332.svg\" width=\"40\" height=\"40\"></a>"))
llista_moneda.append(Moneda("ETH","<a href=\"https://coinmarketcap.com/es/currencies/ethereum/\" target=\"_blank\">"    ,  "<img src=\"https://assets.bitstamp.net/dashboard/s/widgets/dashboard/44cfa606c6c2ace5de7d6a29ff2bb998.svg\" width=\"40\" height=\"40\"></a>"))
llista_moneda.append(Moneda("LINK" ,"<a href=\"https://coinmarketcap.com/es/currencies/chainlink/\" target=\"_blank\">" ,  "<img src=\"https://assets.bitstamp.net/dashboard/s/widgets/dashboard/98015f33f9e7bcb0acc781f022646f8f.svg\" width=\"40\" height=\"40\"></a>"))

        
for moneda in llista_moneda:

    COIN=moneda.code
    
    COIN_account = client.get_account(COIN)
    COIN_accountdict = json.loads(json.dumps(COIN_account))
    COIN_balance = COIN_accountdict['balance']['amount']
    
    cadena = '<br/>'
    cadena = cadena + moneda.URL1
    cadena = cadena + moneda.URL2
    cadena = cadena + " " + COIN_accountdict['currency']['name']
    print(cadena) 
    
    print("<br>1 " + str(COIN) + ": " + str(COIN_balance))
    preu = client.get_spot_price(currency_pair=COIN + "-USD")
    _preu = str(round(float(preu.amount),2))
    print("<br>1 " + str(COIN) + " " + str(_preu) + " $")    
        
    preu = client.get_spot_price(currency_pair=COIN + "-EUR")
    _preu = str(round(float(preu.amount),2))
    
    total = float(COIN_balance) * float(preu.amount)
    print("<br>TOTAL " + str(round(float(total),2))  + " &euro;" + "<br>")
    COIN_wallet+=round(float(total),2)
    
print("<br>TOTAL: " + str(COIN_wallet) + " &euro;")
    
