from random import randint

from src.const import TIME_DIVIDER
from src.models.units.soldier import Soldier
from src.models.units.vehicle import Vehicle


class Tank(Vehicle):
    def __init__(self, number):
        super().__init__(number)
        self._recharge = self.set_recharge()
        self._operators = [Soldier(1),
                          Soldier(2),
                          Soldier(3)]


    def __repr__(self) -> str:
        return f"Tank #{self.number}"

    def set_recharge(self) -> float:
        return round(randint(15, 35) / TIME_DIVIDER, 3)

    def damage(self):
        sum_oper_exp = 0
        for operator in self._operators:
            sum_oper_exp += (operator.experience / 100)
        return round(0.2 + sum_oper_exp, 2)

tank = Tank(1)
print(tank._recharge)
tank._recharge = 20
print((tank._recharge))