import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
game_active = True

def ball_anime():
    global ball_speed_x,ball_speed_y
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y
    if ball_rect.top <= 0 or ball_rect.bottom >= 720:
            ball_speed_y *= -1
    if ball_rect.colliderect(player1_rect) or ball_rect.colliderect(player2_rect):
             ball_speed_x *= -1
def player_anime():
    player1_rect.y += player1_mov
    if player1_rect.top <= 0:
            player1_rect.topleft = (0,0)
    if player1_rect.bottom >= 720:
            player1_rect.bottomleft= (0,720)
ball_surf = pygame.image.load('Ball.png').convert_alpha()
ball_rect = ball_surf.get_rect(center = (640,360) )
ball_speed_x = 7
ball_speed_y = 7

player1_surf = pygame.image.load('Paddle.png').convert_alpha()
player1_rect = player1_surf.get_rect(midleft = (0,360))
player1_mov = 0

player2_surf = pygame.image.load('Paddle.png').convert_alpha()
player2_rect = player2_surf.get_rect(midright = (1280,360))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1_mov -= 2
                    
                if event.key == pygame.K_s:
                    player1_mov += 2
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player1_mov += 2
                    
                if event.key == pygame.K_s:
                    player1_mov -= 2
    
    if game_active:
        screen.fill('Black')
        pygame.draw.aaline(screen,'White',(0,360),(1280,360),1280)
        pygame.draw.aaline(screen,'White',(640,0),(640,720),720)
        
        ball_anime()
        player_anime()
        
        screen.blit(ball_surf, ball_rect)
        
        screen.blit(player1_surf, player1_rect)
        screen.blit(player2_surf, player2_rect)
        
        # if ball_rect.left <= 0 or ball_rect.right >= 1280:
        #     ball_speed_x *= -1
    pygame.display.update()
    clock.tick(60)