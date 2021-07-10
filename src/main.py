from pet import  Pet, State
from event import Event, simple_actions
from datetime import datetime, timedelta
from animation import  ItemAnimation
from modules.enviroment.weather import weather
import pygame
import pygame_gui
import sys

UPDATE_PET = pygame.USEREVENT + 1
CHANGE_ROUTE = pygame.USEREVENT + 2
BIOLOGICAL_CLOCK = pygame.USEREVENT + 3 
if __name__ == "__main__":
    #weather()
   
    pygame.init()
    x = 480
    y = 320
    size = x, y
    white = 255,255,255,255
    teal = 72,209,204
    black = 0,0,0
    pet = Pet("manolo",size)
    screen = pygame.display.set_mode(size)
    screen.fill(teal)
    bg = pygame.image.load('../images/bg/voodoo_cactus_underwater.jpg')
    pygame.draw.rect(screen,black,(0,0,x,34)) 
    pygame.draw.rect(screen,black,(0,y - 34,x,34)) 
    manager = pygame_gui.UIManager(size,'theme.json')

    button_layout_rect = pygame.Rect(30,20,32,32)
    hunger = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(1,y - 33,32,32), text='',manager=manager,object_id='#comer')
    thirst = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(33,y - 33,32,32), text='',manager=manager,object_id='#beber')
    fun = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(65,y - 33,32,32), text='',manager=manager,object_id='#jugar')
    vitality = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(97,y -33,32,32), text='',manager=manager,object_id='#curar')
    caramelo = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(129,y -33,32,32), text='',manager=manager,object_id='#caramelo')
    shower = pygame_gui.elements.UIButton(relative_rect = pygame.Rect(161,y -33,32,32), text='',manager=manager,object_id='#shower')

    time = pygame_gui.elements.UILabel(relative_rect = pygame.Rect(x - 150, 1,150,32), text='',manager=manager,object_id="#infoText")
    info = pygame_gui.elements.UILabel(relative_rect = pygame.Rect(1, 1,150,32), text='',manager=manager,object_id="#infoText")
    secret_info = pygame_gui.elements.UILabel(relative_rect = pygame.Rect(20,50,350,250), visible =False, text='cosas',manager=manager,object_id="#infoText")

 
    clock = pygame.time.Clock()
    pygame.time.set_timer(UPDATE_PET, 25)
    pygame.time.set_timer(CHANGE_ROUTE, 1000)
    pygame.time.set_timer(BIOLOGICAL_CLOCK,1000)

    poops = []
    animations = []

    actions = {
        'hunger' : Event('hunger',simple_actions['hunger'],State.HAPPY),
        'thirst' : Event('thirst',simple_actions['thirst'],State.HAPPY),
        'fun' : Event('fun',simple_actions['fun'],State.HAPPY),
        'vitality' : Event('vitality',simple_actions['vitality'],State.HAPPY),
        'sweet' : Event('sweet',simple_actions['sweet'],State.HAPPY),
        'clean' : Event('clean',simple_actions['clean'],State.HAPPY)
    }
    item_animation = ItemAnimation()
    while (True):
        clock.tick(60)
        time_delta = pygame.time.get_ticks()/1000.0
        
        time.set_text(datetime.now().strftime("%d/%m/%Y, %H:%M"))
        info.set_text(f'{pet.attributes.name}   Edad: {pet.attributes.age}')
    
        
        for event in pygame.event.get():
            if event.type == UPDATE_PET:
                    pet.update()
                    print(pet.attributes)

            if event.type == CHANGE_ROUTE:
                    pet.change_route()
                    
            if event.type == BIOLOGICAL_CLOCK:
                    pet.biological_clock()
                    print(pet.attributes)
                    secret_info.set_text(str(pet.attributes))
                    if pet.is_time_to_poop():
                        poops.append(pet.poop())
                   
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == hunger:
                        pet.event(actions['hunger'])
                        animations.append(item_animation.return_animation(1,x/2,y/2))
                    if event.ui_element == thirst:
                        pet.event(actions['thirst'])
                        animations.append(item_animation.return_animation(2,x/2,y/2))
                    if event.ui_element == fun:
                        pet.event(actions['fun'])
                        animations.append(item_animation.return_animation(3,x/2,y/2))
                    if event.ui_element == vitality:
                        pet.event(actions['vitality'])
                        animations.append(item_animation.return_animation(4,x/2,y/2))
                    if event.ui_element == caramelo:
                        pet.event(actions['sweet'])
                        animations.append(item_animation.return_animation(5,x/2,y/2))
                    if event.ui_element == shower:
                        pet.event(actions['clean'])
                        poops = []
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    secret_info.visible = not secret_info.visible 
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            manager.process_events(event)
        for animation in animations:
            if animation.active == True:
                    animation.update()
            else:
                animations.remove(animation)

        screen.fill(teal)
        screen.blit(bg,(0,0))
        for poop in poops:
            screen.blit(poop[0], poop[1])
 
    
              
        pet.sprite.draw(screen)
        for animation in animations:
            animation.draw(screen)
        
        pygame.draw.rect(screen,black,(0,0,x,34)) 
        pygame.draw.rect(screen,black,(0,y - 34,x,34)) 
        manager.update(time_delta)
        manager.draw_ui(screen)

        pygame.display.update()

   
