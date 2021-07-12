from os import listdir
from numpy import random
import pygame;

class Animation:

    def __init__(self,image, x, y):
        self.active = True
        self.image = image  
        self.rect = image.get_rect()
        self.rect.center = (x,y)
        self.step = 0
        self.x = 0
        
    def update(self):
        if self.step < 50:
            y = self.x**2 
            self.rect.x += self.x
            self.rect.y += y
            print(self.rect.x)
            print(self.rect.y)
            self.x += 0.1
            self.step += 1
        else:
            self.active = False
    
    def draw(self,screen):
         screen.blit(self.image, self.rect)

class ItemAnimation():
 
    def __init__(self):
        self.path_foods = '../images/items/food/'
        self.path_potions = '../images/items/potions/'
        self.path_sweets = '../images/items/sweet/'
        self.path_drinks = '../images/items/drink/'
        self.path_toys = '../images/items/toys/'

        self.foods = [pygame.image.load_extended(self.path_foods + food) for food in listdir(self.path_foods)]
        self.potions = [pygame.image.load_extended(self.path_potions + potion) for potion in listdir(self.path_potions)]
        self.sweets = [pygame.image.load_extended(self.path_sweets + sweet) for sweet in listdir(self.path_sweets)]
        self.drinks = [pygame.image.load_extended(self.path_drinks + drink) for drink in listdir(self.path_drinks)]
        self.toys = [pygame.image.load_extended(self.path_toys + toy) for toy in listdir(self.path_toys)]
        

    def return_animation(self,item,x,y):
        if item == 1:
            current_food = random.choice(self.foods)
            return Animation(current_food,x,y)
        if item == 2:
            current_drink = random.choice(self.drinks)
            return Animation(current_drink,x,y)
        if item == 3:
            current_toy = random.choice(self.toys)
            return Animation(current_toy,x,y)
        if item == 4:
            current_potion = random.choice(self.potions)
            return Animation(current_potion,x,y)
        if item == 5:
            current_sweet= random.choice(self.sweets)
            return Animation(current_sweet,x,y)