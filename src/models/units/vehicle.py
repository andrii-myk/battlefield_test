from random import randint, choice

from src.const import TIME_DIVIDER
from src.models.units.unit import Unit
from src.models.units.soldier import Soldier


class Vehicle(Unit):
    """Class which represents base vehicle object"""
    def __init__(self, number):
        super().__init__()
        self.number = number
        self._health = 100
        self._is_alive = True
        self._operators = [Soldier(1),
                           Soldier(2)]
        self.recharge = self.set_recharge()
        self._total_health = 100

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, dmg):
        if self.health - dmg <= 0:
            self._health = 0
            self.is_alive = False
        else:
            self._health = round(self.health - dmg, 2)

    @property
    def is_alive(self):
        self.alive_operators()
        if self.health > 0 and self._operators: #if vehicle has healthpoints and there are alive operators
            return True
        elif not self._operators:
            self._health = 0
            return False
        else:
            self._operators = []
            return False

    @is_alive.setter
    def is_alive(self, value=False):
        self._is_alive = value

    @property
    def total_health(self):
        self.compute_total_health()
        return self._total_health

    def compute_att_succ_prob(self) -> float:
        if self.is_alive:
            self.compute_total_health()
            mult_atack_success = 1
            for operator in self._operators:
                mult_atack_success *= operator.compute_att_succ_prob()
            return round(0.5 * (1 + self.total_health / 100) * (mult_atack_success ** (1 / len(self._operators))), 2) # GAVG

    #compute total_health and set it to object property
    def compute_total_health(self) -> None:
        temp_health = 0
        for operator in self._operators:
            temp_health += operator.health
        self._total_health =  (self.health + temp_health) / (len(self._operators) + 1)

    def alive_operators(self):
        self._operators =  list([x for x in self._operators if x.is_alive])

    def damage(self) -> float:
        sum_oper_exp = 0
        for operator in self._operators:
            sum_oper_exp += (operator.experience /100)
        return round(0.1 + sum_oper_exp, 2)

    def increase_exp(self) -> None:
        for operator in self._operators:
            operator.increase_exp()

    def set_recharge(self) -> float:
        return round(randint(10, 20) / TIME_DIVIDER, 3)

    def under_attack(self, damage) -> None:
        if self.is_alive:
            self.health = damage * 0.6
            temp_operator = choice(self._operators)
            temp_operator.under_attack(damage * 0.25)
            for operator in self._operators:
                if temp_operator is operator:
                    continue
                else:
                    operator.under_attack(damage * 0.15)
