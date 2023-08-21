from fastapi import FastAPI
from app.services.blockchain import get_wallet_balance, format_wallet
from app.services.mongoDB import get_wallet_history, save_wallet_balance
from app.models.WalletBalance import WalletBalance, WalletHistory
from typing import List

app = FastAPI()

@app.get("/wallet/balance/")
async def get_wallet_balance_endpoint(wallet: str) -> dict:
    wallet = format_wallet(wallet)

    # Get data from blockchain
    balance = await get_wallet_balance(wallet)

    # Get previous historical data
    history = await get_wallet_history(wallet)

    # Create Wallet Balance Instance
    wallet_balance = WalletBalance(wallet=wallet, balance=balance['ether'], balance_usd=balance['usd'])

    # Save wallet Balance Instance
    await save_wallet_balance(wallet_balance)
    return {'history':history, **wallet_balance.dict()}

@app.get("/wallet/history/")
async def get_wallet_history_endpoint(wallet: str) -> List[WalletHistory]:
    wallet = format_wallet(wallet)
    
    history = await get_wallet_history(wallet)
    return history
