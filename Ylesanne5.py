import pygame
pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

#ekraani seaded
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Ping-Pong")
screen.fill(lBlue)
clock = pygame.time.Clock()
posX, posY = 0, 0
ballspeedX, ballspeedY = 3, 4
padspeed = 4

#ball
ball = pygame.Rect(posX, posY, 20, 20)
ballImage = pygame.image.load("ball.png")
ballImage = pygame.transform.scale(ballImage, [ball.width, ball.height])

#pad
pad = pygame.Rect(posX, posY, 120, 20)
padImage = pygame.image.load("pad.png")
padImage = pygame.transform.scale(padImage, [pad.width, pad.height])

score = 0

gameover = False
while not gameover:
    clock.tick(60)
    screen.fill(lBlue)
    #mängu sulgemine ristist
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    # ball liikumine
    ball = pygame.Rect(posX, posY, 20, 20)
    screen.blit(ballImage, ball)

    posX += ballspeedX
    posY += ballspeedY

    if posX > screenX - ballImage.get_rect().width or posX < 0:
        ballspeedX = -ballspeedX

    if posY > screenY - ballImage.get_rect().height or posY < 0:
        ballspeedY = -ballspeedY

    # pad liikumine
    pad.x += padspeed
    pad.y = screenY * 0.75
    if pad.left <= 0 or pad.right >= screenX:
        padspeed = -padspeed

    if ball.colliderect(pad) and ballspeedY > 0:
        ballspeedY = -ballspeedY
        score += 1
        print(score) # lisab skoori ühe punkti võrra ning väljastab selle terminali

    screen.blit(padImage, pad)
    pygame.display.flip()


