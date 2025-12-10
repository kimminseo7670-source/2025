#1. "황금 사과" 아이템 추가 (특수 효과)
# [spawn_apple 함수 수정]
def spawn_apple():
    # ... (기존 위치/속도 설정 코드 동일) ...
    
    # 10% 확률로 황금 사과, 나머지는 일반 사과
    item_type = "gold" if random.random() < 0.1 else "normal"
    
    # 딕셔너리에 'type' 정보 추가
    apples.append({"rect": rect, "vx": vx, "vy": vy, "type": item_type})

# [메인 루프의 충돌 처리 부분 수정]
    if player.rect.colliderect(rect):
        if apple["type"] == "gold":
            score += 5        # 점수 대박
            print("황금 사과! 점수 +5")
            # 여기에 '무적 모드'나 '속도 증가' 코드를 넣을 수도 있습니다.
        else:
            score += 1
            print("일반 사과! 점수 +1")
        continue

# [그리기 부분 수정]
    for apple in apples:
        if apple["type"] == "gold":
            # 황금 사과는 노란색 동그라미로 표시 (이미지가 있다면 이미지 사용)
            pygame.draw.circle(screen, (255, 215, 0), apple["rect"].center, 20)
        else:
            screen.blit(apple_img, apple["rect"])

#2. 점수에 따른 난이도 상승 (똥 분열하기)
# [메인 루프의 사과 충돌 처리 부분]
    if player.rect.colliderect(rect):
        score += 1
        
        # 5점마다 새로운 똥 추가
        if score % 5 == 0:
            # 화면 랜덤한 위치에 새 적 생성
            new_enemy = Enemy(random.randint(0, WIDTH), random.randint(0, HEIGHT))
            # 플레이어 바로 옆에 생기면 억울하니까 위치 조정 (옵션)
            if abs(new_enemy.rect.x - player.rect.x) < 100: 
                new_enemy.rect.x += 200
                
            all_sprites.add(new_enemy)
            enemy_group.add(new_enemy)
            print(f"경고! 똥이 {len(enemy_group)}개가 되었습니다!")
            
        continue

#3. 장르 변경: "하늘에서 똥이 비처럼 내려와"
# [Enemy 클래스 전면 수정]
class Enemy(pygame.sprite.Sprite):
    def __init__(self):  # x, y를 밖에서 받지 않고 안에서 랜덤 생성
        super().__init__()
        self.image = poop_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 40)
        self.rect.y = random.randint(-100, -40) # 화면 위쪽 안 보이는 곳
        self.speed_y = random.randint(3, 6)     # 떨어지는 속도 랜덤

    def update(self):
        self.rect.y += self.speed_y
        
        # 바닥에 닿으면 다시 위로 올려보내기 (재활용)
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - 40)
            self.rect.y = random.randint(-100, -40)
            self.speed_y = random.randint(3, 6) # 속도 다시 설정
            
# [초기화 부분]
# 처음에 똥 5개를 미리 만들어둠
for i in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemy_group.add(enemy)