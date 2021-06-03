class event():

    def __init__(self,name,modifiers,type = 1):
        self.name = name
        self.type = type
        self.modifiers = modifiers
        # {'hunger' : hunger, 
        # 'sleep' : sleep, 
        # 'fun' : fun, 
        # 'vitality' : vitality,
        # 'temperature' : temperature}