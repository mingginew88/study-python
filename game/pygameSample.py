import pygame


#########################################
# 인프런 강의 - 파이썬 무료 강의 (활용편1) - 추억의 오락실 게임 만들기 (3시간)
# https://www.inflearn.com/course/%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%99%9C%EC%9A%A9%ED%8E%B8-1/dashboard
#########################################

# 초기화 (필수)
pygame.init()

# 화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('PYGAME')

# FPS
clock = pygame.time.Clock()

# 배경 이미지 로드
background = pygame.image.load('./images/background.png')

# 캐릭터 설정
character = pygame.image.load('./images/character.png')
character_size = character.get_rect().size
character_width = character_size[0]     # 캐릭터 가로 사이즈
character_height = character_size[1]    # 캐릭터 세로 사이즈
character_x_pos = (screen_width - character_width) / 2     # 화면 가로 중간 위치
character_y_pos = screen_height - character_height         # 화면 세로 하단 위치

# 이동좌표
to_x = 0
to_y = 0

# 이동속도
character_speed = 0.5

# enemy 설정
enemy = pygame.image.load('./images/enemy.png')
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]     # enemy 가로 사이즈
enemy_height = enemy_size[1]    # enemy 세로 사이즈
enemy_x_pos = (screen_width - enemy_width) / 2     # 화면 가로 중간 위치
enemy_y_pos = (screen_height - enemy_height) /2    # 화면 세로 중간 위치

running = True

# 폰트 정의
# 폰트 객체 생성(폰트, 크기)
font = pygame.font.Font(None, 40)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()

# 이벤트 루프 (루프가 없다면 창이 유지되지 않음)
while running:
    # 게임 화면 초당 프레임 수 설정
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창닫을 경우
            running = False

        if event.type == pygame.KEYDOWN:    # 키 확인
            if event.key == pygame.K_LEFT:      # 좌
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:   # 우
                to_x += character_speed
            elif event.key == pygame.K_UP:      # 상
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:    # 하
                to_y += character_speed

        if event.type == pygame.KEYUP:   # 방향키를 떼는 경우 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 최종 위치 수정
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print('충돌!!!')
        running = False

    # 배경 그리기
    screen.blit(background, (0, 0))
    # screen.fill((255, 0, 255))

    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    # enemy 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 타이머 설정
    # 경과 시간
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000    # ms -> 초단위로 변경

    timer = font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))     # 시간, anti_alis = True, 글자색
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        print('Time Out')
        running = False

    # 화면 다시 그리기
    pygame.display.update()
    
# 대기
pygame.time.delay(2000)     # 2초 대기

# 종료
pygame.quit()


