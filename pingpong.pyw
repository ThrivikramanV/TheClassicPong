import pygame
import random
import sys

black=(0,0,0)
white=(255,255,255)
red=(200,0,0)
brightred=(255,0,0)
green=(0,200,0)
brightgreen=(0,255,0)
blue=(0,0,200)
brightblue=(0,0,255)
win_height=600
win_width=700
paddle_height=80
paddle_width=20
ball_rad=10
paddle_2_x=650
paddle_1_x=30
score=[0,0]
level=sys.argv[-1]

if level=='easy':
    extra_speed = 0
    paddle_shift=80
elif level=='hard' or level=='twoplayer':
    extra_speed = 2
    paddle_shift=0
else:
    extra_speed = 1
    paddle_shift=40

pygame.init()
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption('Ping Pong')
clock = pygame.time.Clock()

won = pygame.mixer.Sound('.\\sounds\\won.wav')
hit = pygame.mixer.Sound('.\\sounds\\hit.wav')
lost = pygame.mixer.Sound('.\\sounds\\lost.wav')

def message_display(text,colour,fontsize,pos_x,pos_y):
    font = pygame.font.Font('C:\\Windows\\Fonts\\comic.ttf',fontsize)
    textSurf = font.render(text, True, colour)
    textRect = textSurf.get_rect()
    textRect.center = (pos_x,pos_y)
    win.blit(textSurf,textRect)

def score_display(score):
    message_display(str(score[0]),white,40,(win_width/2)-50,30)
    message_display(str(score[1]),white,40,(win_width/2)+50,30)

def button(msg,x,y,width,height,active,inactive,func):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x < mouse[0] < x+width and y < mouse[1] < y+height:
        pygame.draw.rect(win,active,(x,y,width,height))
        if click[0]==1:
            if func=='continue':
                return False
            if func=='quit':
                pygame.quit()
                sys.exit()
    else:
        pygame.draw.rect(win,inactive,(x,y,width,height))

    message_display(msg,black,20,x+(width/2),y+(height/2))
    return True

def pause(ball_x,ball_y,paddle_1_y,paddle_2_y,score):
    run=True

    while run:
        win.fill(black)
        score_display(score)
        pygame.draw.rect(win,white,(paddle_2_x,paddle_2_y,paddle_width,paddle_height))
        pygame.draw.rect(win,white,(paddle_1_x,paddle_1_y,paddle_width,paddle_height))
        pygame.draw.circle(win,white,(int(ball_x),int(ball_y)),ball_rad)
        message_display('PAUSED',white,50,win_width/2,200)

        run=button('CONTINUE',200,400,120,50,green,brightgreen,'continue')
        button('QUIT',400,400,120,50,red,brightred,'quit')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    run=False

        pygame.display.update()
        clock.tick(30)

def game_over(paddle_1_y,paddle_2_y,score,txt):
    win.fill(black)
    pygame.draw.rect(win,white,(paddle_2_x,paddle_2_y,paddle_width,paddle_height))
    pygame.draw.rect(win,white,(paddle_1_x,paddle_1_y,paddle_width,paddle_height))
    score_display(score)
    message_display(txt,white,60,win_width/2,win_height/2)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
        
def game_loop(score):
    ball_x=win_width/2
    ball_y=win_height/2
    paddle_2_y=(win_height/2)-(paddle_height/2)
    paddle_1_y=(win_height/2)-(paddle_height/2)
    paddle_2_speed=0
    paddle_1_speed=0
    
    win.fill(black)
    score_display(score)
    pygame.draw.rect(win,white,(paddle_2_x,paddle_2_y,paddle_width,paddle_height))
    pygame.draw.rect(win,white,(paddle_1_x,paddle_1_y,paddle_width,paddle_height))
    pygame.draw.circle(win,white,(int(ball_x),int(ball_y)),ball_rad)
    pygame.display.update()

    pygame.time.delay(1000)

    samp=[1,2,3,4]
    count=random.choice(samp)
    if count==1:
        ball_speed_x = 5 + extra_speed
        ball_speed_y = 7 + extra_speed
    if count==2:
        ball_speed_x = 5 + extra_speed
        ball_speed_y = -(7 + extra_speed)
    if count==3:
        ball_speed_x = -(5 + extra_speed)
        ball_speed_y = 7 + extra_speed
    if count==4:
        ball_speed_x = -(5 + extra_speed)
        ball_speed_y = -(7 + extra_speed)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if level=='twoplayer':
                    if event.key == pygame.K_UP:
                        paddle_2_speed=-7
                    if event.key == pygame.K_w:
                        paddle_1_speed=-7
                    if event.key == pygame.K_DOWN:
                        paddle_2_speed=7
                    if event.key == pygame.K_s:
                        paddle_1_speed=7
                else:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                            paddle_2_speed=-7 
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            paddle_2_speed=7
                if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    pause(ball_x,ball_y,paddle_1_y,paddle_2_y,score)
            if event.type == pygame.KEYUP:
                if level=='twoplayer':
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        paddle_2_speed=0
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        paddle_1_speed=0
                else:
                    if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        paddle_2_speed=0

        win.fill(black)
        
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        
        if ball_y + ball_rad >= win_height:
            pygame.mixer.Sound.play(hit)
            ball_speed_y *= -1
        if ball_y - ball_rad <= 0:
            pygame.mixer.Sound.play(hit)
            ball_speed_y *= -1
        
        if ball_x + ball_rad <= 0:
            score[1]+=1
            if score[1]==3:
                pygame.mixer.Sound.play(won)
                if level=='twoplayer':
                    game_over(paddle_1_y,paddle_2_y,score,'Player 2 Won!')
                else:
                    game_over(paddle_1_y,paddle_2_y,score,'You Won!')
            game_loop(score)
        if ball_speed_x < 0 and ball_x - ball_rad <= paddle_1_x + paddle_width and ball_x - ball_rad >= paddle_1_x + 10:
            if paddle_1_y <= ball_y + ball_rad and paddle_1_y + paddle_height >= ball_y - ball_rad:
                pygame.mixer.Sound.play(hit)
                ball_speed_x *= -1
        
        if ball_x - ball_rad >= win_width:
            score[0]+=1
            if score[0]==3:
                if level=='twoplayer':
                    pygame.mixer.Sound.play(won)
                    game_over(paddle_1_y,paddle_2_y,score,'Player 1 Won!')
                else:
                    pygame.mixer.Sound.play(lost)
                    game_over(paddle_1_y,paddle_2_y,score,'You Lost:(')
            game_loop(score)
        if ball_speed_x > 0 and ball_x + ball_rad >=paddle_2_x and ball_x + ball_rad <=paddle_2_x + 10:
            if paddle_2_y <= ball_y + ball_rad and paddle_2_y + paddle_height >= ball_y - ball_rad:
                pygame.mixer.Sound.play(hit)
                ball_speed_x *= -1
        
        pygame.draw.circle(win,white,(int(ball_x),int(ball_y)),ball_rad)

        paddle_2_y += paddle_2_speed
        if paddle_2_y + paddle_height >= win_height:
            paddle_2_y = win_height - paddle_height
        if paddle_2_y <= 0:
            paddle_2_y = 0
        pygame.draw.rect(win,white,(paddle_2_x,paddle_2_y,paddle_width,paddle_height))

        if level=='twoplayer':
            paddle_1_y += paddle_1_speed
            if paddle_1_y + paddle_height >= win_height:
                paddle_1_y = win_height - paddle_height
            if paddle_1_y <= 0:
                paddle_1_y = 0
        else:
            paddle_1_y = ball_y - paddle_height/2
            if paddle_1_y + paddle_height + paddle_shift>= win_height:
                paddle_1_y = win_height - paddle_height - paddle_shift
            if paddle_1_y - paddle_shift <= 0:
                paddle_1_y = paddle_shift
        
        pygame.draw.rect(win,white,(paddle_1_x,paddle_1_y,paddle_width,paddle_height))

        score_display(score)
        
        pygame.display.update()
        clock.tick(30)
    
game_loop(score)
