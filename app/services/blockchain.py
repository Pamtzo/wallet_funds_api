from web3 import Web3
import requests

# https://chainlist.org/chain/1
w3 = Web3(Web3.HTTPProvider("https://eth.llamarpc.com"))

def format_wallet(wallet: str)-> str:
    return Web3.to_checksum_address(wallet)

async def get_wallet_balance(wallet: str) -> dict:
    # Use Web3.py to fetch wallet balance
    balance_wei = w3.eth.get_balance(wallet)
    balance_ether = w3.from_wei(balance_wei, 'ether')

    # Use CoinGecko API to fetch Ether price in USD
    coingecko_url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'ethereum',
        'vs_currencies': 'usd'
    }
    response = requests.get(coingecko_url, params=params)
    ether_price_usd = response.json()['ethereum']['usd']

    balance_usd = float(balance_ether) * ether_price_usd

    return {
        'ether': float(balance_ether),
        'usd': float(balance_usd)
    }
