from src.models.units.buggy import Buggy

class TestBuggy:
    def test_set_recharge(self):
        buggy = Buggy(1)
        recharge = buggy.set_recharge()
        assert recharge >= 0.012 and recharge <= 0.025