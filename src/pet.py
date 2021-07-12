from enum import Enum
import random
import json
import pygame

class State(Enum):
    NORMAL = 0,
    HUNGRY = 1,
    BORING = 2,
    SLEEPY = 3,
    DISEASED = 4,
    HOT = 5,
    COLD = 6,
    DEAD = 7,
    THIRST = 8,
    DIRTY = 9,
    HAPPY = 10,
    EGG = 11

class PetSprite(pygame.sprite.Sprite):
    def __init__(self, x,y,size):
        pygame.sprite.Sprite.__init__(self)

        self.velocity_x = 1
        self.velocity_y = 1
       
        self.egg = pygame.image.load_extended('../images/egg.png')
        self.sprites = []
        self.sprites.append(pygame.image.load_extended('../images/mermaid/normal.png'))
        self.sprites.append(pygame.image.load_extended('../images/mermaid/angry.png'))
        self.sprites.append(pygame.image.load_extended('../images/mermaid/angry_2.png'))
        self.sprites.append(pygame.image.load_extended('../images/mermaid/happy.png'))
       
        self.sprite_dead = pygame.image.load_extended('../images/TombStone.png')

        self.current_sprite = self.egg
        self.rect = self.current_sprite.get_rect()
        self.rect.center = (x,y)
        self.size = size
        

    def draw(self, screen):

        if self.velocity_x > 0:
            screen.blit(self.current_sprite, self.rect)
        else:
            screen.blit(pygame.transform.flip(self.current_sprite, True, False),self.rect)
    

    def update(self,priority_state):
        if priority_state == State.EGG:
            self.current_sprite = self.egg
            return
        if priority_state == State.DEAD:
            self.current_sprite = self.sprite_dead
            return
        if priority_state == State.HAPPY:
            self.current_sprite = self.sprites[3]
            return
        if priority_state == State.NORMAL:
            self.current_sprite = self.sprites[0]
        else:
            index = random.randint(1, 2)
            self.current_sprite = self.sprites[index]
        
        self.move()
            

    def move(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        if self.rect.x > self.size[0] - self.rect.width - 32:
            self.velocity_x = -self.velocity_x
        if self.rect.x < 0 + 32:
            self.velocity_x = -self.velocity_x
        if self.rect.y < 35 or self.rect.y > self.size[1] - self.rect.height -35:
            self.velocity_y = -self.velocity_y

class PetAttributes():

    def __init__(self, name):
        self.step = 0
        self.name = name
        self.age = -1
        with open('config.json') as file:
            config = json.load(file)

            self.hunger = config['attributes']['max_hunger']
            self.sleep = config['attributes']['max_sleep']
            self.fun = config['attributes']['max_fun']
            self.vitality = config['attributes']['max_vitality']
            self.temperature = config['attributes']['temperature']
            self.clean = config['attributes']['max_clean']
            self.thirst = config['attributes']['max_thrist']

            self.hunger_decay = config['attributes']['hunger_decay']
            self.thrist_decay = config['attributes']['thrist_decay']
            self.sleep_decay = config['attributes']['sleep_decay']
            self.fun_decay = config['attributes']['fun_decay']
            self.clean_decay = config['attributes']['clean_decay']

            self.poop_time = 0
            self.digestion_time = config['attributes']['digestion_time']
            self.poop = False

            self.birthday = config['attributes']['biological_birthday_clock']
        #self.vocab = self.vocab[:]
        self.states = [State.NORMAL]
    
    def __remove_state(self, state):
        if (state in self.states):
            self.states.remove(state)

    def __append_state(self, state):
        if (state not in self.states):
            self.states.append(state)

    def check_attribute(self,attribute, state):
        if attribute > 150:
            self.vitality -= 0.2

        if attribute < 25:
            self.__append_state(state)

            if attribute < 0:
                self.vitality -= 0.2
        else:
            self.__remove_state(state)

    def check_vitality(self):
        if self.vitality < 25:
            self.states.append(State.DISEASED)
        if self.vitality < 0:
            self.states.append(State.DEAD)

    def __basal_metabolism(self):
        self.step += 1

        self.__remove_state(State.HAPPY)
        self.check_attribute(self.hunger,State.HUNGRY)
        self.check_attribute(self.thirst,State.THIRST)
        self.check_attribute(self.sleep,State.SLEEPY)
        self.check_attribute(self.fun,State.BORING)
        self.check_attribute(self.clean,State.DIRTY)
       
        self.check_vitality()

        if self.age == -1 and self.step == 20:
            self.age = 0

        if self.step == self.birthday:
            self.age += 1
            self.step = 0

    def biological_clock(self):
        if State.DEAD not in self.states and self.age > -1:
            self.hunger -= self.hunger_decay
            self.thirst -= self.thrist_decay
            self.sleep -= self.sleep_decay
            self.fun -= self.fun_decay
            self.clean -= self.clean_decay

            if self.poop_time  > 0:
                self.poop_time -= 1
                if self.poop_time == 0:
                    self.poop = True
        self.__basal_metabolism()

    def modify(self, event):
        self.__append_state(event.state)
        modifiers = event.modifiers
        if 'hunger' in modifiers:
            self.hunger += modifiers['hunger']
            if modifiers['hunger'] > 0:
                self.poop_time = self.digestion_time
        if 'thirst' in modifiers:
            self.thirst += modifiers['thirst']
        if 'sleep' in modifiers:
            self.sleep += modifiers['sleep']
        if 'fun' in modifiers:
            self.fun += modifiers['fun']
        if 'vitality' in modifiers:
            self.vitality += modifiers['vitality']
        if 'temperature' in modifiers:
            self.temperature += modifiers['temperature']
        if 'clean' in modifiers:
            self.clean += modifiers['clean']

    def __str__(self):
        info = f'hunger: {self.hunger} \nsleep: {self.sleep} \nfun: {self.fun} \nvitality: {self.vitality} \ntemperature: {self.temperature} \nthirst: {self.thirst}'
        info += '\n'
        for index in range(len(self.states)):
            info += f'{self.states[index]} , ' 
        info += '\n'
        return info


class Pet():

    def __init__(self, name,size):
        x = size[0] / 2
        y = size[1] / 2
        self.attributes = PetAttributes(name)
        self.sprite = PetSprite(x,y,size)

    def update(self):
        if self.attributes.age < 0:
            self.sprite.update(State.EGG)
        else:
            state = self.attributes.states[-1]
            self.sprite.update(state)

    def change_route(self):
        change_x = random.randint(0, 1)
        change_y = random.randint(0, 1)
        if change_x == 1:
            self.sprite.velocity_x = -self.sprite.velocity_x
        
        if change_y == 1:
            self.sprite.velocity_y = -self.sprite.velocity_y
    
    def biological_clock(self):
        self.attributes.biological_clock()
        
    def event(self,event):
        if State.DEAD not in self.attributes.states:
            self.attributes.modify(event)
    
    def is_time_to_poop(self):
        return self.attributes.poop

    def poop(self):
        self.attributes.poop = False
        rect = self.sprite.rect
        x = rect.x + rect.height/2
        y = rect.y + rect.width/2
        poo = pygame.image.load('../images/poo.png')
        poo_rect = poo.get_rect()
        poo_rect.center = (x,y)
        return (poo,poo_rect)
       
