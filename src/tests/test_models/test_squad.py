from src.models.squad import Squad
from src.models.units.tank import Tank
from src.models.units.soldier import Soldier
from src.models.units.buggy import Buggy

class TestSquad:
    def test_create_squad(self):
        squad = Squad('tank', 'green', 's', 12)
        assert isinstance(squad._units[0], Tank)
        assert len(squad._units) == 4

        squad = Squad('soldier', 'green', 's', 1)
        assert isinstance(squad._units[0], Soldier)
        assert len(squad._units) == 10

        squad = Squad('zzz', 'green', 's', 1)
        assert isinstance(squad._units[0], Buggy)
        assert len(squad._units) == 5

    def test_compute_att_succ_prob(self):
        squad = Squad('tank', 'green', 's', 12)
        for tank in squad._units:
           for operator in tank._operators:
               operator._experience = 50
        assert squad.compute_att_succ_prob() == 1.0

        squad = Squad('soldier', 'green', 's', 1)
        for soldier in squad._units:
            soldier._experience = 50
        assert squad.compute_att_succ_prob() == 1.0

    def test_attack(self, capfd):
        tank_squad = Squad('tank', 'green', 's', 12)
        tank_squad_2 = Squad('tank', 'green', 's', 1)
        for tank in tank_squad._units:
           for operator in tank._operators:
               operator._experience = 50
        tank_squad.attack(tank_squad_2)
        out, err = capfd.readouterr()
        assert out == f'{tank_squad} has attacked {tank_squad_2}\n'

        tank_squad_2 = Squad('tank', 'green', 's', 1)

        tank_squad_2.attack(tank_squad)
        out, err = capfd.readouterr()
        assert out == f'{tank_squad_2} has failured to attack {tank_squad}\n'
        #assert tank_squad_2._readiness == False

    def test_increase_exp(self):
        tank_squad = Squad('tank', 'green', 's', 12)
        tank_squad.increase_exp()
        assert tank_squad._units[0]._operators[0]._experience == 2
        tank_squad.increase_exp()
        assert tank_squad._units[0]._operators[0]._experience == 3
        tank_squad._units[0]._operators[0]._experience = 50
        tank_squad.increase_exp()
        assert tank_squad._units[0]._operators[0]._experience == 50
        tank_squad.increase_exp()
        assert tank_squad._units[0]._operators[0]._experience == 50

    def test_damage(self):
        tank_squad = Squad('tank', 'green', 's', 12)
        assert tank_squad.damage() == 0.92
        for tank in tank_squad._units:
           for operator in tank._operators:
               operator._experience = 50
        assert tank_squad.damage() == 6.8

        buggy_squad = Squad('buggy', 'green', 's', 1)
        assert buggy_squad.damage() == 0.6
        for buggy in buggy_squad._units:
            for operator in buggy._operators:
                operator._experience = 30
        assert buggy_squad.damage() == 3.5

        soldier_squad = Squad('soldier', 'green', 's', 1)
        assert soldier_squad.damage() == 0.6
        for soldier in soldier_squad._units:
            soldier._experience = 40
        assert soldier_squad.damage() == 4.5

    def test_under_attack(self):
        tank_squad = Squad('tank', 'green', 's', 14)
        tank_squad.under_attack(80)
        assert tank_squad._units[0].health == 88
        tank_squad.under_attack(800)
        assert tank_squad._units[0].health == 0

    def test_alive_units(self):
        tank_squad = Squad('tank', 'green', 's', 14)
        tank_squad._units[0]._health = 0
        tank_squad.alive_units()
        assert len(tank_squad._units) == 3


    def test_is_alive(self):
        tank_squad = Squad('tank', 'green', 's', 14)
        tank_squad._units = []
        assert tank_squad.is_alive == False

    def test_get_squad_avg_recharge(self):
        tank_squad = Squad('tank', 'green', 's', 14)
        #for tank in tank_squad._units:
        #   tank._recharge = 0.02                #didn't work
        assert tank_squad.get_squad_avg_recharge() <= 0.035

    def test_get_readiness(self):
        tank_squad = Squad('tank', 'green', 's', 14)
        assert tank_squad.readiness == True
        tank_squad.readiness = False
        assert tank_squad.readiness == False






