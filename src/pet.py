from enum import Enum

class State(Enum):
    NORMAL = 0,
    HUNGRY = 1,
    BORING = 2,
    SLEEPY = 3,
    DISEASED = 4,
    HOT = 5,
    COLD = 6


class pet():

    def __init__(self, name):
        self.name = name
        self.hunger = 100
        self.sleep = 100
        self.fun = 100
        self.vitality = 100
        self.temperature = 25
        #self.vocab = self.vocab[:]
        self.state = [State.NORMAL]

    def __basal_hunger(self):
        if (self.hunger < 30):
            self.vitality -= (30 - self.hunger) * 0.8

    def __basal_metabolism(self):
        self.__basal_hunger()

    def clock_tick(self):
        self.hunger -= 1
        self.sleep -= 1
        self.fun -=1

        self.__basal_metabolism()

    def event(self, event):
        self.hunger += event.modifiers['hunger']
        self.sleep += event.modifiers['sleep']
        self.fun += event.modifiers['fun']
        self.vitality += event.modifiers['vitality']
        self.temperature += event.modifiers['temperature']

    def __str__(self):
        info = f'hunger: {self.hunger} \nsleep: {self.sleep} \nfun: {self.fun} \nvitality: {self.vitality} \ntemperature: {self.temperature}'
        info += '\n'
        return info