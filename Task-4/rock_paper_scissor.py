import pygame
import sys
import random 

def main():
    pygame.init()

    white = (255, 255, 255)
    black = (0, 0, 0)

    global font
    font = pygame.font.SysFont(None, 16)

    global screen
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption('Rock Papper Scissor')
    clock = pygame.time.Clock()

    rock = pygame.image.load("Images\img1.png")
    paper = pygame.image.load("Images\img1.png")
    scissor = pygame.image.load("Images\img1.png")

    rock_r = pygame.transform.scale(rock, (130,130))
    paper_r = pygame.transform.scale(paper, (130,130))
    scissor_r = pygame.transform.scale(scissor, (130,130))

    reset_button = pygame.Rect(0, 515, 90, 30) 
    reset_button.centerx = 500//2

    user_choice = ''
    game_winner = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 20<= x <=150 and 350 <= y <= 480:
                    user_choice = 'rock'
                if 20+130+35 <= x <= 20+130+35+130 and 350 <= y <= 350+130:
                    user_choice = 'paper'
                if 20+130+35+130+35 <= x <= 20+130+35+130+35+130 and 350 <= y <= 350+130:
                    user_choice = 'scissor'
                game_winner = winner(user_choice)
                print(game_winner)

                if game_winner:
                    display_message("User_Win" , (20,20))
                elif not game_winner:
                    display_message("Computer  Win" , (20,20))


            screen.fill(white)
            screen.blit(rock_r, (20,350))
            screen.blit(paper_r, (185,350))
            screen.blit(scissor_r, (350,350))
            pygame.draw.rect(screen, (47, 153, 196), reset_button, border_radius=10)


        pygame.display.flip()




def winner(user_choice):
    l = ['rock', 'paper', 'scissor']
    com_choice = random.choice(l)
    if user_choice == 'rock' and com_choice =='scissor':
        return 1
    elif user_choice == 'paper' and com_choice =='rock':
        return 1
    elif user_choice == 'scissor' and com_choice =='paper':
        return 1
    else:
        return 0


def display_message(message, pos):
    text = font.render(message, True, (1,34,56))
    screen.blit(text, pos)


if __name__ == "__main__":
    main()