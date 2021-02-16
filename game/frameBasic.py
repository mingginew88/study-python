import pygame

###############################################################
# 초기화 (필수)
pygame.init()

# 화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('게임명')

# FPS
clock = pygame.time.Clock()
###############################################################

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 이미지, 속도, 폰트, 시간 등)

running = True

# 이벤트 루프 (루프가 없다면 창이 유지되지 않음)
while running:
    # 게임 화면 초당 프레임 수 설정
    dt = clock.tick(60)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창닫을 경우
            running = False

    # 3. 게임 캐릭터 위치 정의
    # 4. 충돌 처리
    # 5. 화면 그리기

    # 화면 다시 그리기
    pygame.display.update()

# 종료
pygame.quit()


