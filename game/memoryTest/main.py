import pygame

# 초기화 (필수)
pygame.init()

# 화면 크기
screen_width = 640
screen_height = 360
screen = pygame.display.set_mode((screen_width, screen_height))

# 폰트 정의
start_font = pygame.font.Font('./font/NanumGothic.ttf', 30)
text_font = pygame.font.Font('./font/NanumGothic.ttf', 20)

# 색상 표
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)

start_button = pygame.Rect(screen_width / 2 - 60, screen_height / 2 - 40, 120, 40)

# 화면 타이틀 설정
pygame.display.set_caption('기억력 테스트')

def display_main_screen():
    # 시작 버튼 그리기
    pygame.draw.rect(screen, WHITE, start_button, 1)
    msg = start_font.render('Start', True, WHITE)
    msg_rect = msg.get_rect(center=start_button.center)
    screen.blit(msg, msg_rect)

def display_game_screen():
    interval = 60           # 간격
    division_line = 480     # 구분선(점수 및 단계)

    # 배경색 지정
    screen.fill(BLACK)

    # 화면 구분선 그리기 (세로줄)
    for i in range(0, screen_width, interval):
        if i <= division_line:
            pygame.draw.line(screen, WHITE, [i, 0], [i, 360], 1)

    # 화면 구분선 그리기 (가로줄)
    for i in range(0, screen_height, interval):
        pygame.draw.line(screen, WHITE, [0, i], [division_line, i], 1)

    screen.blit(text_font.render('Grade', True, WHITE), (division_line + 10, 120))     # 단계
    screen.blit(text_font.render('Score', True, WHITE), (division_line + 10, 60))      # 점수


def click_start_button(click_position):
    global start
    if start_button.collidepoint(click_position):
        start = True

running = True  # 이벤트 루프 여부
start = False   # 게임시작 여부

# 이벤트 루프 (루프가 없다면 창이 유지되지 않음)
while running:

    click_position = None   # 클릭 위치

    for event in pygame.event.get():
        # 게임 나가기
        if event.type == pygame.QUIT:  # 게임 종료 시
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:    # 마우스 위치
            click_position = pygame.mouse.get_pos()

    # 마우스 클릭 시
    if click_position:
        click_start_button(click_position)

    # 시작 화면
    if start:
        display_game_screen()
    else:
        display_main_screen()

    # 화면 업데이트
    pygame.display.update()


# 게임 종료
pygame.quit()
