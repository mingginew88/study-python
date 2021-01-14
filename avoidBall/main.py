import pygame
import sys
from time import sleep
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

padWidth = 480      # 넓이
padHeight = 640     # 높이
highScore = 0       # 최고점수

ballImg = ['./image/redBall.png', './image/blueBall.png', './image/yellowBall.png']     # 공 이미지

# 점수 작성
def writeScore(count):
    global gamePad, highScore
    font = pygame.font.Font('./font/NanumGothic.ttf', 20)
    text = font.render('피한 갯수 : ' + str(count), True, BLACK)
    if count > highScore:
        highScore = count
    highScoreText = font.render('최고 점수 : ' + str(highScore), True, BLACK)

    gamePad.blit(text, (220, 0))
    gamePad.blit(highScoreText, (350, 0))

# 메세지 작성
def writeMessage(text):
    global gamePad
    textFont = pygame.font.Font('./font/NanumGothic.ttf', 80)
    text = textFont.render(text, True, RED)
    textPos = text.get_rect()
    textPos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textPos)
    pygame.display.update()
    sleep(1)
    runGame()

# 게임 종료
def gameOver():
    global gamePad
    writeMessage('Game Over')

# 배경에 사물 그리기
def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))
    gamePad.blit(obj, (x, y))

# 게임 초기 설정
def initGame():
    global gamePad, clock, background, character
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('avoiding ball') # 게임명
    background = pygame.image.load('./image/background_white.png') # 배경이미지
    character = pygame.image.load('image/character.png') # 캐릭터이미지
    clock = pygame.time.Clock()

# 게임 실행
def runGame():
    global gamePad, clock, background, character

    #캐릭터 크기
    characterSize = character.get_rect().size
    characterWidth = characterSize[0]
    characterHeight = characterSize[1]

    #캐릭터 초기 위치
    x = padWidth * 0.4
    y = padHeight * 0.9
    characterX = 0

    # 공 생성
    ball = pygame.image.load(random.choice(ballImg))
    ballSize = ball.get_rect().size
    ballWidth = ballSize[0]
    ballHeight = ballSize[1]

    # 공 초기 위치
    ballX = random.randrange(0, padWidth - ballWidth)
    ballY = 0
    ballSpeed = 2

    # 피한 공 갯수
    ballPassed = 0

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:  # 게임종료
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:  # 방향키 누르는 경우
                if event.key == pygame.K_LEFT:  # 좌측 이동
                    characterX -= 5
                elif event.key == pygame.K_RIGHT:  # 우측 이동
                    characterX += 5

            if event.type in [pygame.KEYUP]:  # 방향키 떼는 경우
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # 멈춤
                    characterX = 0

        drawObject(background, 0, 0)    # 배경 그리기

        # 캐릭터 위치조정
        x += characterX
        if x < 0:
            x = 0
        elif x > padWidth - characterWidth:
            x = padWidth - characterWidth

        # 게임 오버
        if y < ballY + ballHeight:
            if (ballX > x and ballX < x + characterWidth) or (
                    ballX + ballWidth > x and ballX + ballWidth < x + characterWidth):
                gameOver()

        drawObject(character, x, y)     # 캐릭터 그리기

        # 공 위치조정
        ballY += ballSpeed # 공 위치 변경
        if ballY > padHeight:
            # 새 공 생성
            ball = pygame.image.load(random.choice(ballImg))
            ballSize = ball.get_rect().size
            ballWidth = ballSize[0]
            ballHeight = ballSize[1]
            ballX = random.randrange(0, padWidth - ballWidth)
            ballY = 0
            ballPassed += 1
            ballSpeed += 0.02 * ballPassed
            if ballSpeed >= 10:
                ballSpeed = 10

        writeScore(ballPassed)

        drawObject(ball, ballX, ballY)

        # gamePad.fill(WHITE)       # 게임화면
        pygame.display.update()     # 게임화면 다시 그림

        clock.tick(60)  # 초당 프레임

    pygame.quit()   # pygame 종료

initGame()
runGame()
