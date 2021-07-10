from pet import State
simple_actions = { 'hunger' : {'hunger': 20 },
            'thirst' : {'thirst': 20},
            'sleep' : {'sleep': 20},
            'fun' : {'fun': 20},
            'vitality' : {'vitality': 20},
            'clean' : {'clean': 20},
            'sweet' : {'hunger': 20 , 'fun': 20}
}
        
class Event():

    def __init__(self,name,modifiers,state,type = 1):
        self.name = name
        self.type = type
        self.modifiers = modifiers
        self.state = state
