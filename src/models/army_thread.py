from threading import Thread


from .army import Army


class ArmyThread(Thread):
    """Represents a bunch of units """
    def __init__(self, army: Army, armies: list):
        super().__init__()
        self._armies = armies
        self._army = army

    def run(self):
        while True:
            if self._army.is_alive() and len(self._armies) > 1:
                try:
                    self._army.attack(self._armies)
                except Exception as e:
                    print('error in attack')
                    self._army._squads = []
                    continue
            else:
                #print(f'{self._army} was totally destroyed!!!')
                self._armies.pop(self._armies.index(self._army))
                break

    def __del__(self):
        print(f"{self.getName()} is stopped")

