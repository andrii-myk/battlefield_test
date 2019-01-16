from src.models.units.vehicle import Vehicle

class TestVehicle():
    def test_compute_att_succ_prob(self):
        vehicle = Vehicle(1)
        vehicle._operators[0]._experience = 50
        vehicle._operators[1]._experience = 50
        assert vehicle.compute_att_succ_prob() == 1.0
        vehicle._health = 40
        assert vehicle.compute_att_succ_prob() == 0.9
        vehicle._health = 10
        assert vehicle.compute_att_succ_prob() == 0.85
        #vehicle._operators[0]._health = 10
        #assert vehicle.compute_att_succ_prob() == 0.7

    def test_compute_total_health(self):
        vehicle = Vehicle(1)
        assert vehicle.total_health == 100
        vehicle._health = 10
        assert vehicle.total_health == 70
        vehicle._operators[0]._health = 40
        assert vehicle.total_health == 50
        vehicle._operators[1]._health = 10
        assert vehicle.total_health == 20


    def test_alive_operators(self):
        vehicle = Vehicle(1)
        vehicle.alive_operators()
        assert len(vehicle._operators) == 2
        vehicle._operators[0]._health = 0
        vehicle.alive_operators()
        assert len(vehicle._operators) == 1

    def test_is_alive(self):
        vehicle = Vehicle(1)
        assert vehicle.is_alive == True
        vehicle._health = 0
        assert vehicle.is_alive == False
        assert len(vehicle._operators) == 0
        vehicle = Vehicle(2)
        vehicle._operators[0]._health = 0
        vehicle._operators[1]._health = 0
        assert vehicle.is_alive == False
        assert vehicle._health == 0

    def test_damage(self):
        vehicle = Vehicle(1)
        assert vehicle.damage() == 0.12
        vehicle._operators[0]._experience = 20
        assert vehicle.damage() == 0.31
        vehicle._operators[1]._experience = 20
        assert vehicle.damage() == 0.5
        vehicle._operators[0]._experience = 50
        vehicle._operators[1]._experience = 50
        assert vehicle.damage() == 1.1

    def test_increase_exp(self):
        vehicle = Vehicle(1)
        for i in range(1, 50):
            assert vehicle._operators[0].experience == i
            vehicle.increase_exp()
        for _ in range(10):
            assert vehicle._operators[0].experience == 50
            vehicle.increase_exp()

    def test_set_recharge(self):
        vehicle = Vehicle(1)
        recharge = vehicle.set_recharge()
        assert (recharge >= 0.01 and recharge <= 0.02)

    def test_under_attack(self):
        vehicle = Vehicle(1)
        vehicle.under_attack(10)
        assert vehicle.health == 94
        oper_health = vehicle._operators[0].health
        assert oper_health == 97.5 or oper_health == 98.5

