import pytest

from src.models.army import Army
from src.models.squad import Squad

class TestArmy:
    @pytest.fixture()
    def army_one(self)-> Army:
        army = Army('red', 2, 's')
        army._squads = [Squad('tank', 'red', 's', 1), Squad('buggy', 'red', 's', 2)]
        # army_power() = 1.52
        return army

    @pytest.fixture()
    def army_two(self) -> Army:
        army = Army('green', 4, 'w')
        army._squads = [Squad('tank', 'green', 'w', 1), Squad('tank', 'green', 'w', 2),
                        Squad('soldier', 'green', 'w', 3), Squad('soldier', 'green', 'w', 4)]
        for soldier in army._squads[3]._units:
            soldier._experience = 50
        # army_power() = 7.94
        return army

    @pytest.fixture()
    def army_three(self)-> Army:
        army = Army('blue', 2, 'r')
        army._squads = [Squad('soldier', 'blue', 'r', 1), Squad('soldier', 'blue', 'r', 2)]
        army._squads[0].increase_exp() #now squad #1 is more powerfull, therefore if attacking squad attack mode is
                                       # 'weakest' it will choose squad #2, if attacking squad attack mode is 'strongest
                                       # it will choose squad #1
        # army_power() = 1.3
        return army

    @pytest.fixture()
    def armies(self, army_one, army_two, army_three) -> list:
        return [army_one, army_two, army_three]

    def test_create_army(self):
        army = Army('green', 5, 'w')
        assert len(army._squads) == 5

    def test_is_alive(self, capfd):
        army = Army('green', 5, 'w')
        assert army.is_alive() == True
        army = Army('green', 1, 'w')
        assert army.is_alive() == True
        army._squads = []
        assert army.is_alive() == False

        out, err = capfd.readouterr()
        assert out == f'{army} was totally destroyed\n'

    def test_alive_squads(self):
        army = Army('green', 5, 'w')
        army.alive_squads()
        assert len(army._squads) == 5
        army._squads[4].under_attack(10000)
        army.alive_squads()
        assert len(army._squads) == 4
        army._squads[0].under_attack(10000)
        army.alive_squads()
        assert len(army._squads) == 3

    def test_get_strongest_squad(self, army_one, army_two, army_three):
        assert army_one.get_strongest_squad() == army_one._squads[0]
        assert army_two.get_strongest_squad() == army_two._squads[3]
        assert army_three.get_strongest_squad() == army_three._squads[0]

    def test_get_weakest_squad(selfself, army_one, army_two, army_three):
        assert army_one.get_weakest_squad() == army_one._squads[1]
        assert army_two.get_weakest_squad() == army_two._squads[2]
        assert army_three.get_weakest_squad() == army_three._squads[1]


    def test_choice_army_to_attack(self,army_one, army_two, army_three, armies):
        assert army_one.choice_army_to_attack(armies) == army_two   # army_one attack type is strongest, it must chooses
                                                                    #  the strongest army to attack
        assert army_two.choice_army_to_attack(armies) == army_three # army_two attack type is weakest, it must chooses
                                                                    #  the weakest army to attack
        random_army = army_three.choice_army_to_attack(armies)
        assert random_army == army_one or random_army == army_two   # army_three attack type is random, we check that
                                                                    # it has choosen armmy to attack at all
        assert random_army != army_three                            # there is checking, army can't choses itself
                                                                    # as army to attack

    def test_choice_target(self, army_one, army_two, army_three):
        assert army_one.choice_target(army_two) == army_two._squads[3] # army_one attack mode is 'strongest', therefore
                                                                       # it choses the strongest squad of army_two
        assert army_two.choice_target(army_one) == army_one._squads[1] # army_two attack mode is 'weakest', therefore
                                                                       # it choses the weakest squad of army_one
        assert army_three.choice_target(army_one) in army_one._squads  # army_three attack mode is 'random', check it
                                                                       # makes choice

    def test_attack(self, army_one, army_two, army_three):
        army_two.attack([army_one, army_three, army_two])
        assert army_three._squads[1]._units[1]._health < 100
        army_two._att_type = 's'                                   # if change army_two attack mode to 'strongest'
        army_two.attack([army_one, army_three, army_two])                    # it will choose more powerfull army_one to attack
        assert army_one._squads[0]._units[0]._health < 100         # and, accordingly, the most poerfull Tank squad #1

    def test_army_power(self, army_one, army_two, army_three):
        assert army_one.army_power() == 1.52
        assert army_two.army_power() == 7.94
        assert army_three.army_power() == 1.3
        army_one._squads[0].increase_exp()
        assert army_one.army_power() == 1.64
        army_one._squads[0].increase_exp()
        assert army_one.army_power() == 1.76
