from msilib.schema import Font
import pygame
import sys
import random 


def main():
    pygame.init()

    #font Style
    global font, Font
    b_font = pygame.font.SysFont('Arial', size= 14,bold=True)
    heading_font = pygame.font.SysFont('Arial', size=30, bold=True)
    font = pygame.font.SysFont('Arial', size= 18, bold=True, italic=True)
    Font = pygame.font.SysFont('Georgia', size= 24, bold=True)

    #screen
    screen = pygame.display.set_mode((500, 510))
    pygame.display.set_caption('Rock Paper Scissor')

    clock = pygame.time.Clock()

    #Texts for Pick you move
    text = font.render("Pick your Move", True, (0,0,0))
    text_rect = text.get_rect()
    text_rect.center = (250, 275)

    #Images
    rock = pygame.image.load("Images/img2.png")
    paper = pygame.image.load("Images/img1.png")
    scissor = pygame.image.load("Images/img3.png")

    #Resized images.
    rock_r = pygame.transform.scale(rock, (130,130))
    paper_r = pygame.transform.scale(paper, (130,130))
    scissor_r = pygame.transform.scale(scissor, (130,130))

    #Rock paper Scissor heading.
    heading = pygame.Rect(0,0,500,50)
    heading_font = heading_font.render('Rock  Paper  Scissor', True, (255,255,255))
    heading_font_rect = heading_font.get_rect()
    heading_font_rect.center = (250, 25)

    #Button for the reset
    reset_button = pygame.Rect(0, 450, 110, 30) 
    reset_button.centerx = 500//2
    text_b = b_font.render("Play Again", True , (0,0,0))
    text_b_rect = text_b.get_rect()
    text_b_rect.center = (250, 465)

    #varibale to store the data
    user_choice = ''
    com_choice = ''
    game_winner = ''
    global Your_score, Computer_score
    Your_score = 0
    Computer_score = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            screen.fill((255,255,255))

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 20<= x <=150 and 290 <= y <= 290+130:
                    user_choice = 'rock'
                elif 20+130+35 <= x <= 20+130+35+130 and 290 <= y <= 290+130:
                    user_choice = 'paper'
                elif 20+130+35+130+35 <= x <= 20+130+35+130+35+130 and 290 <= y <= 290+130:
                    user_choice = 'scissor'
                elif 190 <= x <=190+110 and 450 <= y <= 450+30:
                    Your_score, Computer_score, user_choice, com_choice,game_winner = 0, 0, '', '',''
                    continue
                else:
                    continue
                
                game_winner, com_choice = winner(user_choice)

                if game_winner == 'Computer Win':
                    Computer_score += 1
                elif game_winner == 'You Win':
                    Your_score += 1

            score_text , score_text_rect,choice_text, choice_text_rect, winner_text, winner_text_rect = update_score(game_winner, user_choice, com_choice)
            

            pygame.draw.rect(screen, (0,0,0) , heading)
            pygame.draw.rect(screen, (47, 153, 197), reset_button, border_radius=10)
            screen.blit(heading_font, heading_font_rect)
            screen.blit(score_text, score_text_rect)
            screen.blit(choice_text, choice_text_rect)
            screen.blit(winner_text, winner_text_rect)
            screen.blit(text, text_rect)
            screen.blit(rock_r, (20,290))
            screen.blit(paper_r, (185,290))
            screen.blit(scissor_r, (350,290))
            screen.blit(text_b, text_b_rect)


        pygame.display.update()
        clock.tick(60)


def update_score(Winner, user_choice, computer_choice):
    #Variable to Score the Score.
    global Computer_score
    global Your_score

    winner_text = Font.render(f"{Winner}",True , (255,0,0))
    winner_text_rect = winner_text.get_rect()
    winner_text_rect.center = (250, 190)

    choice_text = Font.render(f"     {user_choice}                    {computer_choice}     ",True , (0,0,0))
    choice_text_rect = choice_text.get_rect()
    choice_text_rect.center = (250, 135)

    score_text = Font.render(f"    You : {Your_score}     v/s     {Computer_score} : Computer",True , (0,0,0))
    score_text_rect = score_text.get_rect()
    score_text_rect.center = (250, 90)
    #text 
    return score_text, score_text_rect , choice_text, choice_text_rect, winner_text, winner_text_rect

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

if __name__ == "__main__":
    main()