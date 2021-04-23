from random import randrange

import pygame

# 초기화 (필수)
pygame.init()

# 화면 타이틀 설정
pygame.display.set_caption('기억력 테스트')

running = True  # 이벤트 루프 여부
start = False   # 게임시작 여부
hidden = False  # 숨김 여부
next = False    # 다음게임

# 화면 크기
screen_width = 640
screen_height = 360
screen = pygame.display.set_mode((screen_width, screen_height))

# 폰트 정의
start_font = pygame.font.Font('./font/NanumGothic.ttf', 30)
text_font = pygame.font.Font('./font/NanumGothic.ttf', 20)
number_font = pygame.font.Font(None, 50)

# 색상표
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)

# 버튼 위치 리스트
number_buttons = []

interval = 60  # 간격
division_line = 480  # 구분선(점수 및 단계)

# start_button = pygame.Rect(screen_width / 2 - 60, screen_height / 2 - 40, 120, 40)
start_button = pygame.Rect(division_line, 300, 120, 40)

start_ticks = None  # 시간 계산 (현재 시간 정보를 저장)
display_time = None # 숫자를 보여주는 시간

score = 0    # 점수
level = 1    # 단계

def display_main_screen():
    # 시작 버튼 그리기
    pygame.draw.rect(screen, BLACK, start_button, 1)
    msg = start_font.render('Start', True, WHITE)
    msg_rect = msg.get_rect(center=start_button.center)
    screen.blit(msg, msg_rect)


def display_game_screen():
    global hidden, level

    # 배경색 지정
    screen.fill(BLACK)

    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed_time > display_time:
            hidden = True

    # 화면 구분선 그리기 (세로줄)
    for i in range(0, screen_width, interval):
        if i <= division_line:
            pygame.draw.line(screen, WHITE, [i, 0], [i, 360], 1)

    # 화면 구분선 그리기 (가로줄)
    for i in range(0, screen_height, interval):
        pygame.draw.line(screen, WHITE, [0, i], [division_line, i], 1)

    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:
            # 흰 사각형 틀 그리기
            pygame.draw.rect(screen, WHITE, rect)
        else:
            # 숫자 그리기
            cell_text = number_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)

    screen.blit(text_font.render('Level', True, WHITE), (division_line + 10, 120))     # 단계
    screen.blit(text_font.render('Score', True, WHITE), (division_line + 10, 60))      # 점수


def click_start_button(click_position):
    global start, start_ticks

    if start:
        check_number_buttons(click_position)
    elif start_button.collidepoint(click_position):
        start = True
        # 타이머 시작 (현재 시간을 저장)
        start_ticks = pygame.time.get_ticks()

def check_number_buttons(click_position):
    global start, hidden, level

    for button in number_buttons:
        if button.collidepoint(click_position):
            if button == number_buttons[0]:
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else:
                game_over()
            break

    if len(number_buttons) == 0:
        start = False
        hidden = False
        level += 1
        set_game(level)


def set_game(level):
    global display_time
    display_time = 3     # 1초 미만이면 1초로 처리

    number_count = (level // 3) + 5
    number_count = min(number_count, 48)

    shuffle_number(number_count)


def shuffle_number(number_count):
    rows = 8
    columns = 6
    number = 1

    grid = [[0 for col in range(columns)] for row in range(rows)]

    while number <= number_count:
        row_idx = randrange(0, rows)
        column_idx = randrange(0, columns)

        if grid[row_idx][column_idx] == 0:
            grid[row_idx][column_idx] = number
            number += 1

            center_x = (row_idx * interval) + (interval / 2)
            center_y = (column_idx * interval) + (interval / 2)

            button = pygame.Rect(0, 0, interval, interval)
            button.center = (center_x, center_y)

            number_buttons.append(button)


# 게임 종료
def game_over():
    global running
    running = False

    msg = text_font.render(f"Your level is {level}", True, WHITE)
    msg_rect = msg.get_rect(center=(screen_width / 2, screen_height / 2))

    screen.fill(BLACK)
    screen.blit(msg, msg_rect)


set_game(1)

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


pygame.time.delay(5000)

# 게임 종료
pygame.quit()
