import pygame
pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ping-Pong")
clock = pygame.time.Clock()

# algseisud
ballspeedX, ballspeedY = 3, 4
padspeed = 3

# ball
ball = pygame.Rect(100, 100, 20, 20)
ballImage = pygame.image.load("ball.png")
ballImage = pygame.transform.scale(ballImage, [ball.width, ball.height])

# pad (aseta see allapoole ekraani keskele)
pad = pygame.Rect(100, int(screenY * 0.75), 120, 20)
padImage = pygame.image.load("pad.png")
padImage = pygame.transform.scale(padImage, [pad.width, pad.height])

# game loop
gameover = False
while not gameover:
    clock.tick(60)
    screen.fill(lBlue)

    # sündmused
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    # ball liikumine
    ball.x += ballspeedX
    ball.y += ballspeedY

    # seinte põrkamine
    if ball.left <= 0 or ball.right >= screenX:
        ballspeedX = -ballspeedX
    if ball.top <= 0:
        ballspeedY = -ballspeedY

    # pad liikumine
    pad.x += padspeed
    if pad.left <= 0 or pad.right >= screenX:
        padspeed = -padspeed

    # põrkumine padiga (ainult kui liigub alla)
    if ball.colliderect(pad) and ballspeedY > 0:
        ballspeedY = -ballspeedY

    # joonista
    screen.blit(ballImage, ball)
    screen.blit(padImage, pad)

    pygame.display.flip()
