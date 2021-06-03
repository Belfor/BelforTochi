from pet import pet
from event import event
from datetime import datetime, timedelta


if __name__ == "__main__":
    
    instanteFinal = datetime.now() + timedelta(seconds=2)
    modifiers = {'hunger' : -50, 
        'sleep' : 100, 
        'fun' : 100, 
        'vitality' : 500,
        'temperature' : 30}
    manolo = pet("manolo")
    comer = event("comer", modifiers = modifiers)

    while (True):
        instanteInicial = datetime.now()
        tiempo = instanteFinal - instanteInicial # Devuelve un objeto 
        segundos = tiempo.seconds
        if (segundos == 0):

            print(manolo)
            manolo.clock_tick()
            instanteFinal = datetime.now() + timedelta(seconds=2)
            manolo.event(comer)
            segundos = 0
