import os

from payments import Payments

from mtnmomo.collection import Collection

client = Collection({
    "COLLECTION_USER_ID": os.environ.get("COLLECTION_USER_ID"),
    "COLLECTION_API_SECRET": os.environ.get("COLLECTION_API_SECRET"),
    "COLLECTION_PRIMARY_KEY": os.environ.get("COLLECTION_PRIMARY_KEY"),
})

class MobileMoney(Payments):
    def __init__(self) -> None:
        super().__init__()
        
    def pay(self, number, amount, id):
        return super().pay()
    
# To be done
# API KEYS OBTAINED