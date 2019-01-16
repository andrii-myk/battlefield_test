from random import randint

from src.const import TIME_DIVIDER
from src.models.units.vehicle import Vehicle

class Buggy(Vehicle):
    def __init__(self, number):
        super().__init__(number)
        self._recharhe = self.set_recharge()

    def __repr__(self) -> str:
        return f"Buggy #{self.number}"

    def set_recharge(self) -> float:
        return round(randint(12, 25) /TIME_DIVIDER, 3)