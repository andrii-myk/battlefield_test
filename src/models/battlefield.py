from .army import Army
from .army_thread import ArmyThread


class Battlefield():
    def __init__(self, num_armies: int, num_squads: int, att_mode: str):
        self._num_armies = num_armies
        self._num_squads = num_squads
        self._att_mode = att_mode
        self._colors = ('red', 'green', 'yellow', 'blue', 'orange', 'lime', 'cyan', 'magenta', 'purple', 'grey',
                        'white', 'pink', 'apricot', 'beige', 'mint', 'lavender', 'maroon', 'brown', 'olive',
                        'teal', 'navy', 'black')
        self._armies = self.create_armies()

    @property
    def num_armies(self):
        return self._num_armies

    @property
    def num_squads(self):
        return self._num_squads

    @property
    def att_mode(self):
        return self._att_mode

    def create_armies(self):
        armies = []
        for i in range(self.num_armies):
            armies.append(Army(self._colors[i % len(self._colors)], self.num_squads, self.att_mode))
        return armies

    def start_battle(self):
        armies_threads = []
        for army in self._armies:
            armies_threads.append(ArmyThread(army, self._armies))

        for thread in armies_threads:
            print(f"{thread.getName()} is started")
            thread.start()

        while True:
            if len(self._armies) == 1:
                print(f'{self._armies[0]} has won battle')
                # for thread in armies_threads:
                #     thread.join()
                armies_threads = []
                self._armies = []
                break
