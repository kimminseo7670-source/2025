#1. 아이템(Power-up) 시스템 추가하기

# [추가할 클래스]

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(green)  # 초록색 아이템
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.speed_y = 3

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > screen_height:
            self.kill()

# [Player 클래스 수정: shoot 메서드]
    def shoot(self):
        # 레벨이 1이면 1발, 2면 2발 발사
        if self.bullet_level == 1:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
        elif self.bullet_level >= 2:
            bullet1 = Bullet(self.rect.left, self.rect.top)
            bullet2 = Bullet(self.rect.right, self.rect.top)
            all_sprites.add(bullet1, bullet2)
            bullets.add(bullet1, bullet2)

# [게임 루프 수정: 충돌 처리 부분]
    # 적이 죽을 때 10% 확률로 아이템 생성
    if random.random() < 0.1: 
        item = Item(alien.rect.centerx, alien.rect.centery)
        all_sprites.add(item)
        items.add(item) # items 그룹을 미리 만들어둬야 함

    # 플레이어가 아이템을 먹었을 때
    hits = pygame.sprite.spritecollide(player, items, True)
    for hit in hits:
        player.bullet_level += 1



#2. 적의 공격 패턴 다양화 (총을 쏘는 외계인)
# [추가할 클래스] 적의 총알
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(red)  # 빨간색 총알
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speed_y = 4  # 아래로 내려옴

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > screen_height:
            self.kill()

# [Alien 클래스 수정: update 메서드]
    def update(self):
        self.rect.y += self.speed_y
        # ... 기존 이동 코드 ...
        
        # 1% 확률로 총알 발사
        if random.random() < 0.01:
            bullet = EnemyBullet(self.rect.centerx, self.rect.bottom)
            all_sprites.add(bullet)
            enemy_bullets.add(bullet) # 충돌 검사를 위해 그룹 필요

# [게임 루프 추가] 플레이어와 적 총알의 충돌 검사
    if pygame.sprite.spritecollide(player, enemy_bullets, True):
        lives -= 1
        if lives <= 0:
            game_over = True


#4. 난이도 시스템 (점수에 따른 레벨업)
# 게임 루프 내 update 부분 근처
    
    # 10마리 잡을 때마다 난이도 상승
    # (Alien 생성 시 speed_y 범위를 변수로 관리하면 좋습니다)
    
    if kill_count > 10 and kill_count < 20:
        # 적들의 속도를 전반적으로 올리거나
        # 적 생성 주기를 빠르게 조정
        pass