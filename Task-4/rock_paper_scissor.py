from msilib.schema import Font
import pygame
import sys
import random 


def main():
    global Your_score
    Your_score = 0
    global Computer_score
    Computer_score = 0

    pygame.init()

    white = (255, 255, 255)
    black = (0, 0, 0)

    #font Style
    global font, Font
    font = pygame.font.SysFont('Arial', 20 , bold= True, italic= True)
    Font = pygame.font.SysFont('Georgia', size= 22, bold=True)

    global screen
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption('Rock Papper Scissor')

    #Texts
    text = font.render("Pick your Move", True, (0,0,0))
    text_rect = text.get_rect()
    text_rect.center = (250, 325)


    #Images
    rock = pygame.image.load("Images/img2.png")
    paper = pygame.image.load("Images/img1.png")
    scissor = pygame.image.load("Images/img3.png")

    #Resized images.
    rock_r = pygame.transform.scale(rock, (130,130))
    paper_r = pygame.transform.scale(paper, (130,130))
    scissor_r = pygame.transform.scale(scissor, (130,130))


    #Button for the reset
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
                elif 20+130+35 <= x <= 20+130+35+130 and 350 <= y <= 350+130:
                    user_choice = 'paper'
                elif 20+130+35+130+35 <= x <= 20+130+35+130+35+130 and 350 <= y <= 350+130:
                    user_choice = 'scissor'
                else:
                    continue

                game_winner, com_choice = winner(user_choice)

                if game_winner == 'Computer Win':
                    Computer_score += 1
                elif game_winner == 'You Win':
                    Your_score += 1
                print(f'{game_winner},{user_choice}')

                if game_winner:
                    print(com_choice)
                elif not game_winner:
                    print(com_choice)

            score_text , score_text_rect = update_score(game_winner)

            screen.fill(white)
            screen.blit(score_text, score_text_rect)
            screen.blit(text, text_rect)
            screen.blit(rock_r, (20,350))
            screen.blit(paper_r, (185,350))
            screen.blit(scissor_r, (350,350))
            pygame.draw.rect(screen, (47, 153, 196), reset_button, border_radius=10)


        pygame.display.flip()


def update_score(Winner):
    #Variable to Score the Score.
    global Computer_score
    global Your_score

    if winner == "Computer Win":
        Computer_score += 1
    elif winner == "You Win":
        Your_score += 1

    #text 
    score_text = Font.render(f"You : {Your_score}    {Computer_score} : Computer",True , (0,0,0))
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (250, 50)
    return score_text, score_text_rect


def winner(user_choice):
    l = ['rock', 'paper', 'scissor']
    com_choice = random.choice(l)
    if user_choice == 'rock' and com_choice =='scissor':
        return "You Win",com_choice
    elif user_choice == 'paper' and com_choice =='rock':
        return 'You Win', com_choice
    elif user_choice == 'scissor' and com_choice =='paper':
        return 'You Win', com_choice
    elif user_choice == com_choice:
        return 'Draw',com_choice
    else:
        return 'Computer Win', com_choice


def display_message(message, pos):
    text = Font.render(message, True, (0,0,0))
    screen.blit(text, pos)


if __name__ == "__main__":
    main()