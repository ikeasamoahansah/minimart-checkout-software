from mtnmomo.collection import Collection

class Payments:
    def __init__(self) -> None:
        pass

    def pay(self):
        pass


class MobileMoney(Payments):
    def __init__(self) -> None:
        super().__init__()
        
    def pay(self, number, amount, id):
        return super().pay()