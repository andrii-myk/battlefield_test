from random import randint, choice
from src.models.squad import Squad
from src.logger.logger import logger

class Army():
    def __init__(self, color: str, number_of_squads: int, att_type: str):
        self._color = color
        self._number_of_squads = number_of_squads
        self._att_type = att_type
        self._unit_types = ('soldier', 'tank', 'buggy')
        self._squads = self.create_army()

    def create_army(self):
        army = []
        for i in range(1, self._number_of_squads + 1):
            army.append(Squad(choice(self._unit_types), self._color, self._att_type, i))
        return army

    def get_strongest_squad(self):
        best_squad = self._squads[0]
        for squad in self._squads:
            if squad.damage() > best_squad.damage():
                best_squad = squad
        return best_squad

    def get_weakest_squad(self):
        weakest_squad: Squad = self._squads[-1]
        for squad in self._squads:
            if squad.damage() < weakest_squad.damage():
                weakest_squad = squad
        return weakest_squad

    def choice_army_to_attack(self, armies: list):
        for army in armies:
            if not army.is_alive():
                armies.pop(armies.index(army))
        if len(armies) > 1:
            target_army = None
            listt = armies[:]
            listt.pop(armies.index(self))
            listt.sort(key= lambda x: x.army_power())
            if self._att_type == 'w':
                target_army = listt[0]
            elif self._att_type == 's':
                target_army = listt[-1]
            else:
                target_army = choice(listt)
            return target_army

    def choice_target(self, enemy_army):
        target = None
        if self._att_type == 'w':
            target = enemy_army.get_weakest_squad()
        elif self._att_type == 's':
            target = enemy_army.get_strongest_squad()
        else:
            target = enemy_army._squads[randint(0, len(enemy_army._squads))]
        return target

    def alive_squads(self):
        self._squads = list([squad for squad in self._squads if squad.is_alive])

    def is_alive(self):
        self.alive_squads()
        if len(self._squads) > 0:
            return True
        else:
            print(f"{self} was totally destroyed")
            logger.debug(f"{self} was totally destroyed")
            return False

    def attack(self, armies: list):
        if self.is_alive():
            enemy_army = self.choice_army_to_attack(armies)
            for squad in self._squads:
                if squad.readiness:
                    squad.attack(self.choice_target(enemy_army))
                else:
                    continue

    def army_power(self):
        power = 0
        for squad in self._squads:
            power += squad.damage()
        return round(power, 2)

    def __repr__(self):
        return f"{self._color.capitalize()} army"

