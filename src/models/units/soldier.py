from random import randint

from src.models.units.unit import Unit
from src.const import TIME_DIVIDER

class Soldier(Unit):
    """Class, which represents Soldier unit. Operator in vehicle units"""
    def __init__(self, number: int):
        self._health = 100
        self._is_alive = True
        self._number = number
        self._experience = 1
        self.recharge = self.set_recharge()

    @property
    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return self._is_alive

    @is_alive.setter
    def is_alive(self, value = False):
        self._is_alive = value

    @property
    def experience(self):
        return self._experience

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, dmg: float):
        if self.health - dmg <= 0:
            self._health = 0
            self.is_alive = False
        else:
            self._health = round(self.health - dmg, 2)


    def damage(self) -> float:
        """Damage unit can inflict. Depends on soldier experience. Damage is rounded because of possibility
           innacuracies associated with floating numbers"""
        return round(0.05 + self.experience / 100, 2)

    def under_attack(self, damage: float) -> None:
        if self.is_alive:
            self.health = damage

    def set_recharge(self):
        return round(randint(1, 10) / TIME_DIVIDER, 3) #Decrease recharging time in order to reduce programm running time

    def increase_exp(self):
        if self.experience < 50:
            self._experience += 1

    def compute_att_succ_prob(self):
        return round(0.5 * (1 + self.health / 100) * randint(50 + self.experience, 100) / 100, 2)

    def __repr__(self):
        return f'Soldier #{self._number}'

if __name__ == '__main__':
    soldier = Soldier(1)
    print(soldier.health)
    soldier._health = 10
    soldier._experience = 50
    print(soldier.compute_att_succ_prob())

