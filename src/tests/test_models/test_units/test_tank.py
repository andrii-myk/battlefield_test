from src.models.units.tank import Tank

class TestTank:
    def test_set_recharge(self):
        tank = Tank(1)
        recharge = tank.set_recharge()
        assert recharge >= 0.015 and recharge <= 0.35

    def test_compute_att_succ_prob(self):
        tank = Tank(1)
        tank._operators[0]._experience = 50
        tank._operators[1]._experience = 50
        tank._operators[2]._experience = 50
        assert tank.compute_att_succ_prob() == 1.0
        tank._health = 60
        assert tank.compute_att_succ_prob() == 0.95
        tank._health = 20
        assert tank.compute_att_succ_prob() == 0.9
