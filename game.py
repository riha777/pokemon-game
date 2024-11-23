import pygame
import random
from pokemon import Pokemon
from water import WaterPokemon
from fire import FirePokemon
from grass import GrassPokemon


# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 800,400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pokemon Battle!')

WORD_FONT = pygame.font.SysFont('script', 40)  # Use the default font

input_box = pygame.Rect(300, 300, 200, 50)
user_name = ""
active = False  # To track if input_box is active
flame_active = False # to track if the flame is active 

# Create Pokémon instances
#pokemon = Pokemon('Sharamender', 100, 100, 5, 200, 200, "1.png")
#pokemon_two = Pokemon("Bob", 100, 100, 5, 400, 200, "2.png")
flame_image = pygame.image.load("images/fire_image.png")
flame_image = pygame.transform.scale(flame_image, (60,60))
bg = pygame.image.load("images/bg1.png")
bulbasaur = GrassPokemon('Bulbasaur', 100, 15, ['winewhip', 'razorleaf'], 200, 200, "images/bulbasaur1.png")
charmender = FirePokemon('Charmender', 100, 20, ['flamethrower', 'firespin'], 350, 200, "images/charmender1.png")
squirtle = WaterPokemon('Squirtle', 100, 10, ['watergun', 'bubble'], 500, 200, "images/squirtle1.png")

opponent_choices = [charmender, squirtle, bulbasaur]



def choose_pokemon(): 
    print('Choosing a Pokemon')
    choosen_pokemon = None 
    screen.fill((255,255,255))
    while choosen_pokemon is None:
        bulbasaur.render(screen)
        charmender.render(screen)
        squirtle.render(screen)  # these commands are for displaying the Pokemons 
        instructions_text = WORD_FONT.render('Choose your Pokemon!', True, (0,0,0))
        screen.blit(instructions_text, (190,100))

        # checking for mouse clicks 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)

                # check if user clicked on each pokemon 
                if 200 <= mouse_pos [0] <= 300 and 200 <= mouse_pos[1] <= 300:
                    choosen_pokemon = bulbasaur

                if 300 <= mouse_pos[0] <= 400 and 200 <= mouse_pos[1] <= 300:
                    choosen_pokemon = charmender

                if 500 <= mouse_pos[0] <= 600 and 200 <= mouse_pos[1] <= 300:
                    choosen_pokemon = squirtle 

                opponent_choices.remove(choosen_pokemon)
                opponent_pokemon = random.choice(opponent_choices)




        pygame.display.flip()
    return choosen_pokemon, opponent_pokemon


def player_turn(choosen_pokemon, opponent_pokemon):
    pass

def opponent_turn(choosen_pokemon, opponent_pokemon):
    pass 

# function to animate flames
def flame_attack_animation(screen, attacker):

    flame_color = ((255,69,0)) # flame is orange
    flame_radius = 10
    flame_x, flame_y = attacker.x_pos-50, attacker.y_pos 
    #pygame.draw.circle(screen, flame_color, (flame_x, flame_y), flame_radius)
    screen.blit(flame_image,(flame_x, flame_y))
    if flame_active:
        flame_x -= 10
        print(flame_x)
    pygame.display.flip()
    print(f'{attacker.name} used a flame attack! ')


def main(user_name, choosen_pokemon, opponent_pokemon):
    turn = "player" #start with the player's turn 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if turn == "player":
                player_turn(choosen_pokemon, opponent_pokemon)
                turn = "opponent"
            elif turn == "opponent":
                opponent_turn(opponent_pokemon, choosen_pokemon)
                turn = "player"

        screen.fill((255, 255, 255))
        screen.blit(bg, (0, 0))  # Draw background image
        choosen_pokemon.render(screen)
        opponent_pokemon.render(screen)
        #pokemon.render(screen)
        #pokemon_two.render(screen)
        #bulbasaur.render(screen)
        #charmender.render(screen)
        #squirtle.render(screen)

# we cannot call the method defined inside the class without the object
        choosen_pokemon.health_bar(screen, 50, 50, "green")
        opponent_pokemon.health_bar(screen, 600, 50, "red")

        # movement of the keys 
        keys = pygame.key.get_pressed()
        choosen_pokemon.move(keys, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
        if keys[pygame.K_SPACE]:
            flame_active = True
            flame_attack_animation(screen, choosen_pokemon)          
            
        #pokemon_two.move(keys, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)

        # Display welcome message
        welcome_message = WORD_FONT.render(f'Welcome {user_name}', True, (0, 0, 0))
        screen.blit(welcome_message, (300, 50))

        pygame.display.flip()

def welcome_screen():
    global user_name, active

    while True:
        screen.fill((0, 0, 0))
        welcome_text = WORD_FONT.render('Welcome to Pokemon Battle!', True, (255, 255, 255))
        screen.blit(welcome_text, (190, 100))
        instructions = WORD_FONT.render('Enter your username then press enter.', True, (255, 255, 255))
        screen.blit(instructions, (120, 200))
        

        pygame.draw.rect(screen, (200, 200, 200), input_box)
        text_surface = WORD_FONT.render(user_name, True, (0, 0, 0))
        screen.blit(text_surface, (input_box.x + 8, input_box.y + 5))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        choosen_pokemon, opponent_pokemon = choose_pokemon()
                        main(user_name, choosen_pokemon, opponent_pokemon)
                    elif event.key == pygame.K_BACKSPACE:  # Handle backspace
                        user_name = user_name[:-1]
                    else:
                        user_name += event.unicode


welcome_screen()


