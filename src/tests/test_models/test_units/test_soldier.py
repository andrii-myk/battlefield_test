import pytest

from src.models.units.soldier import Soldier


class TestSoldier():
    def test_increment_experience(self):
        soldier = Soldier(1)
        soldier._experience = 50
        soldier.increase_exp()
        soldier.increase_exp()
        assert soldier.experience == 50
        soldier.increase_exp()
        soldier.increase_exp()
        assert soldier.experience == 50

    def test_damage(self):
        soldier = Soldier(1)
        assert soldier.damage() == 0.06
        soldier._experience = 30
        assert soldier.damage() == 0.35
        soldier._experience = 50
        assert soldier.damage() == 0.55

    def test_is_alive(self):
        soldier = Soldier(1)
        assert soldier.is_alive == True
        soldier.under_attack(50)
        assert soldier.is_alive == True
        soldier.under_attack(52)
        assert soldier.is_alive == False

    def test_under_attack(self):
        soldier = Soldier(1)
        soldier.under_attack(50)
        assert soldier.health == 50
        soldier.under_attack(40.25)
        assert soldier.health == 9.75
        soldier.under_attack(0.61)
        assert soldier.health == 9.14
        soldier.under_attack(8.77)
        assert soldier.health == 0.37
        soldier.under_attack(0.01)
        assert soldier.health == 0.36
        soldier.under_attack(0.13)
        assert soldier.health == 0.23

    def test_set_recharge(self):
        soldier = Soldier(1)
        x = soldier.set_recharge()
        print(2)
        assert (x >= 0.001 and  x <= 0.01)

    def test_compute_att_succ_prob(self):
        soldier = Soldier(1)
        soldier._experience = 50
        assert soldier.compute_att_succ_prob() == 1.0
        soldier._health = 50
        assert soldier.compute_att_succ_prob() == 0.75
        soldier._health = 10
        assert soldier.compute_att_succ_prob() == 0.55
