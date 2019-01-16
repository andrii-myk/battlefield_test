from time import sleep


from src.models.units.buggy import Buggy
from src.models.units.soldier import Soldier
from src.models.units.tank import Tank


class Squad():
    "Represents units squad"
    def __init__(self, unit_type: str, color: str, att_strategy: str, number: int):
        self._is_alive = True
        self._unit_type = unit_type
        self._color = color
        self._att_strategy = att_strategy
        self._number = number
        self._readiness = True
        self._units = self.create_squad()
        self._att_succ_prob = None
        self._recharge = self.get_squad_avg_recharge()

    @property
    def is_alive(self):
        self.alive_units()
        if self._units:  # if there are at least one unit in squad
            return True
        else:
            return False

    @is_alive.setter
    def is_alive(self, value=False):
        self._is_alive = value

    @property
    def readiness(self):
        return self._readiness

    @readiness.setter
    def readiness(self, value = False):
        self._readiness = value

    def create_squad(self)-> list:
        l = []
        if self._unit_type == "soldier":
            for i in range(1, 11):
                l.append(Soldier(i))
        elif self._unit_type== "tank":
            for i in range(1, 5):
                l.append(Tank(i))
        else:
            for i in range(1, 6):
                l.append(Buggy(i))
        return l

    def compute_att_succ_prob(self):
        if self.is_alive:
            multiple_att_prob = 1
            for unit in self._units:
                multiple_att_prob *= unit.compute_att_succ_prob()
            return multiple_att_prob ** (1 / len(self._units)) #GAVG works really bad for different size squads

    def attack(self, enemy_squad) -> None:
        if self._readiness:
            if self.compute_att_succ_prob() >= enemy_squad.compute_att_succ_prob():
                enemy_squad.under_attack(self.damage())
                self.increase_exp()
                print(f"{self} has attacked {enemy_squad}")
            else:
                print(f"{self} has failured to attack {enemy_squad}")
            self.readiness = False
            self.recharging()

    def recharging(self) -> None:
        sleep(self._recharge)
        self.readiness = True

    def increase_exp(self) -> None:
        for unit in self._units:
            unit.increase_exp()

    def damage(self) -> float:
        tot_damage = 0
        for unit in self._units:
            tot_damage += unit.damage()
        return round(tot_damage, 3)

    def under_attack(self, damage) -> None:
        if self.is_alive:
            damage_to_unit = damage / len(self._units)
            for unit in self._units:
                unit.under_attack(damage_to_unit)

    def alive_units(self) -> None:
        self._units =  list([unit for unit in self._units if unit.is_alive])

    def get_squad_avg_recharge(self) -> float:
        avg_recharge = 0
        for unit in self._units:
            avg_recharge += unit.recharge
        return round(avg_recharge / len(self._units), 3)

    def __repr__(self) -> str:
        if self.is_alive:
            return f"{self._units[0].__class__.__name__} squad #{self._number} of the {self._color} army"
