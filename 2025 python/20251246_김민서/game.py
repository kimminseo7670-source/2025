import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("화살 피하기")
  
WHITE = (255, 255, 255)

RED = (255, 0, 0)


clock = pygame.time.Clock()



#배경 이미지
raw_bg_image = pygame.image.load("background.png")
BACKGROUND_IMAGE = pygame.transform.scale(raw_bg_image, (WIDTH, HEIGHT))

#화살 이미지
raw_arrow_image = pygame.image.load("arrow.png")
ARROW_IMAGE = pygame.transform.scale(raw_arrow_image, (20, 60))

#스티브 이미지
raw_steve_image = pygame.image.load("steve.png")
STEVE_IMAGE = pygame.transform.scale(raw_steve_image, (25, 25))


#클래스 정의

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = STEVE_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5 

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, speed):
        super().__init__()
        
        # 화살 회전 및 이미지 설정
        degrees = -math.degrees(angle) #.degrees : 라디안을 도(degree)단위로 바꾸기
        correction_angle = -90 #화살 이미지가 90도(위쪽 방향)를 향하고 있기 때문에 0도로 설정하기 
        self.image = pygame.transform.rotate(ARROW_IMAGE, degrees + correction_angle) # .rotate 화살 돌리기
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    
        self.dx = math.cos(angle) * speed  #삼각함수 (x = cos(angle) * r)  (y = sin(angle) * r) 여기서 r은 speed(이동 거리)와 같음
        self.dy = math.sin(angle) * speed #대각선(빗변 r)으로 갈 때 필요한 가로(x), 세로(y) 이동량  구하기

    def update(self):
        self.rect.centerx +=self.dx #이동거리 업데이트
        self.rect.centery +=self.dy 
        
        margin = 1000 #멀리 간 화살 삭제하기 (.kill)
        if (self.rect.right < -margin or self.rect.left > WIDTH + margin or 
            self.rect.bottom < -margin or self.rect.top > HEIGHT + margin):
            self.kill()


def spawn_random_arrow(group, player_rect):
    side = random.choice(['top', 'bottom', 'left', 'right'])
    buffer = 100 #화면안에서 뜬금없이 나오면 어색하기 때문에 여유공간 만들기
    
    if side == 'top':
        spawn_x = random.randint(0, WIDTH)
        spawn_y = -buffer
    elif side == 'bottom':
        spawn_x = random.randint(0, WIDTH)
        spawn_y = HEIGHT + buffer
    elif side == 'left':
        spawn_x = -buffer
        spawn_y = random.randint(0, HEIGHT)
    elif side == 'right':
        spawn_x = WIDTH + buffer
        spawn_y = random.randint(0, HEIGHT)
    
    # 조준하기 
    target_dx = player_rect.centerx - spawn_x #(도착점 - 출발점) 방향과 거리 구하기 
    target_dy = player_rect.centery - spawn_y 
    target_angle = math.atan2(target_dy, target_dx) #atan : 아크탄젠트(탄젠트 함수의 역함수)  atan2 : 360e도 방향 구분
    #아크탄젠트는 각도를 반환하기 때문에 목표물이 몇도에 위치하는지 알 수 있음
    
    arrow = Arrow(spawn_x, spawn_y, target_angle, speed=4)
    group.add(arrow)

#원형 패턴으로 화살 생성하기
def spawn_circle_pattern(group, player_rect):
    center_x, center_y = player_rect.center 
    radius = 700 #화면 밖에서 나오도록 반지름을 크게 잡음
    num_arrows = 15 #화살 개수
    
    for i in range(num_arrows): 
        angle = math.radians((360 / num_arrows) * i) #반복문 돌면서 각도 조정(0도,24도,48도 ...)
        spawn_x = center_x + radius * math.cos(angle)
        spawn_y = center_y + radius * math.sin(angle)
        
        #조준하기 (위와 같음)
        target_angle = math.atan2(center_y - spawn_y, center_x - spawn_x)
        
        arrow = Arrow(spawn_x, spawn_y, target_angle, speed=3)
        group.add(arrow)



def main():
    running = True
    game_over = False
    
    all_sprites = pygame.sprite.Group()
    arrows = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    
    start_ticks = pygame.time.get_ticks() #시작 시간
    last_basic_arrow_time = 0 #마지막으로 화살이 발사된 시간
    next_phase_time = 5000 #원형 화살이 나올 시간 (처음에는 5초에 나옴)
    phase_interval = 3000   #원형 화살 간격 시간
    
    font = pygame.font.SysFont(None, 36)
    big_font = pygame.font.SysFont(None, 70)
    final_score = 0.0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r: #R을 눌러 재시작하기 
                        game_over = False
                        all_sprites.empty()
                        arrows.empty()
                        player = Player()
                        all_sprites.add(player)
                        start_ticks = pygame.time.get_ticks()
                        last_basic_arrow_time = 0
                        next_phase_time = 5000

        if not game_over:
            all_sprites.update()
            current_ticks = pygame.time.get_ticks() - start_ticks
            
            #랜덤 화살
            if current_ticks - last_basic_arrow_time > 500: #0.5초가 지났으면 / 마지막으로 화살 쏜지 0.5초가 지났으면
                spawn_random_arrow(arrows, player.rect) #화살 쏘기
                all_sprites.add(arrows)
                last_basic_arrow_time = current_ticks #마지막 화살 쏜 시간 덮어쓰기
            
            #원형 패턴
            if current_ticks > next_phase_time: #발사시간을 넘었으면 
                spawn_circle_pattern(arrows, player.rect) #원형 화살 발사
                all_sprites.add(arrows)
                next_phase_time += phase_interval #다음 원형 화살 발사시간 설정

            #충돌 체크
            if pygame.sprite.spritecollide(player, arrows, False, pygame.sprite.collide_circle_ratio(0.6)):
                #.collide_circle_ratio(0.6) : 이미지를 사각형 말고 원으로 인식 후 원 크기를 60%로 줄임,게임의 재미를 위해 완벽하게 닿아야만 충돌로 인식
                game_over = True
                final_score = current_ticks / 1000

        #화면 설정
        
       
        screen.blit(BACKGROUND_IMAGE, (0, 0)) #.bilt  붙이기

        if not game_over:
            all_sprites.draw(screen)
            current_score = (pygame.time.get_ticks() - start_ticks) / 1000
            #시간 보이기
            main_text = font.render(f"score: {current_score:.1f}s", True, WHITE)
           
            screen.blit(main_text, (10, 10))
            
        else:
            all_sprites.draw(screen)
            
            game_over_str = "GAME OVER"
            score_str = f"score: {final_score:.1f} sec"
            restart_str = " Press 'R' to Restart"
            
            #Game Over

            go_main = big_font.render(game_over_str, True, RED)
            go_rect = go_main.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))

            screen.blit(go_main, go_rect)
            
            #Score
            
            score_main = font.render(score_str, True, WHITE)
            score_rect = score_main.get_rect(center=(WIDTH//2, HEIGHT//2))
            
            screen.blit(score_main, score_rect)
            
            #Restart
          
            restart_main = font.render(restart_str, True, WHITE)
            restart_rect = restart_main.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
           
            screen.blit(restart_main, restart_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()