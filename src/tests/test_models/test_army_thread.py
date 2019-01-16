import pytest

from src.models.army import Army
from src.models.army_thread import ArmyThread

class TestArmyThread:
    @pytest.fixture
    def army_t(self):
        return ArmyThread('green', 3, 's')

    @pytest.fixture()
    def army_one(self):
        return Army('red', 3, 's')

    @pytest.fixture()
    def army_two(self):
        return Army('blue', 3, 's')

    def test_run(self):
        pass