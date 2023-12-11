import os

from .payments import Payments

from mtnmomo.collection import Collection

from decouple import config

client = Collection(
    config={
        "COLLECTION_USER_ID": config("COLLECTION_USER_ID"),
        "COLLECTION_API_SECRET": config("COLLECTION_API_SECRET"),
        "COLLECTION_PRIMARY_KEY": config("COLLECTION_PRIMARY_KEY"),
    }
)


class MobileMoney(Payments):
    def __init__(self) -> None:
        super().__init__()

    def pay(self, number, amount):
        client.requestToPay(
            mobile=number,
            amount=amount,
            external_id="M-49403",
            payee_note="Pay for products",
            payer_message="okay",
            currency="EUR",
        )

    # def status(self, ex_id):
    #     return client.getTransactionStatus(transaction_id=ex_id)


# To be done
# API KEYS OBTAINED
