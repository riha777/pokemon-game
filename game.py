import pygame
pygame.init()
import pokemon
import moves

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pokemon Battle!')

WORD_FONT = pygame.font.SysFont('italics', 40)

input_box = pygame.Rect(300,300,200,50) #class if starts with a capital letter, if not then a function
user_name = ""
active = False #to track if input_box is active

def main(user_name):
    while True:
        screen.fill((255,255,255))
        print(f'Welcome {user_name}')
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def welcome_screen():
    global user_name, active
    
    while True:
        screen.fill((0,0,0))
        welcome_text = WORD_FONT.render('Welcome to Pokemon Battle!', True, (255,255,255))
        screen.blit(welcome_text, (100,100))
        instructions = WORD_FONT.render('Enter your username then press enter.', True, (255,255,255))
        screen.blit(instructions,(200,200))

        pygame.draw.rect(screen,(200,200,200), input_box)
        text_surface = WORD_FONT.render(user_name, True, (0,0,0))
        screen.blit(text_surface, (input_box.x + 8, input_box.y + 5))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(active)
                if input_box.collidepoint(event.pos):
                    active = True
                    print(active)
                else:
                    active = False 
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        main(user_name)
                    else:
                        user_name += event.unicode
                        print(user_name)

welcome_screen()

        



