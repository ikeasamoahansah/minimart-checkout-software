import os

from payments.payments import Payments

from mtnmomo.collection import Collection

client = Collection({
    "COLLECTION_USER_ID": os.environ.get("COLLECTION_USER_ID"),
    "COLLECTION_API_SECRET": os.environ.get("COLLECTION_API_SECRET"),
    "COLLECTION_PRIMARY_KEY": os.environ.get("COLLECTION_PRIMARY_KEY"),
})

class MobileMoney(Payments):
    def __init__(self) -> None:
        super().__init__()
        
    def pay(self, number, amount, ex_id, note, message):
        return client.requestToPay(
            mobile=number,
            amount=amount,
            external_id=ex_id,
            payee_note=note,
            payer_message=message,
            currency="EUR"
        )
    
    def status(self, ex_id):
        return client.getTransactionStatus(
            transaction_id=ex_id
        )
    
# To be done
# API KEYS OBTAINED