from motor.motor_asyncio import AsyncIOMotorClient
from app.models.WalletBalance import WalletBalance, WalletHistory

MONGODB_URL = "mongodb://my_mongo:27017"
DB_NAME = "wallet_balance"

def connect_to_mongodb():
    client = AsyncIOMotorClient(MONGODB_URL)
    return client[DB_NAME]



async def get_wallet_history(wallet: str):
    db = connect_to_mongodb()
    collection = db[DB_NAME]

    cursor = collection.find({'wallet':wallet})

    # Convert the cursor to a list of documents
    documents = await cursor.to_list(length=None)
    
    history = []
    for document in documents:
        history.append(WalletHistory(timestamp=document['last_updated'], value=document['balance']))

    return history

async def save_wallet_balance(wallet_balance: WalletBalance):
    db = connect_to_mongodb()
    collection = db[DB_NAME]
    await collection.insert_one(wallet_balance.dict())
