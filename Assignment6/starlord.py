import pygame, sys
pygame.init()

size = width, height = 320, 240
black = 0,0,0
screen = pygame.display.set_mode(size)

star1 = pygame.image.load("c:\\python\\star1.png")
star1rect = star1.get_rect()
speed = [1,1]
BLAM = pygame.image.load("c:\\python\\BLAM.png")
BLAM = pygame.transform.scale(BLAM, (100,75))
BLAMrect = BLAM.get_rect()
collide = False

star2 = pygame.image.load("c:\\python\\star2.png")
star2rect = star2.get_rect()

star2rect.x = 40
star2rect.y =200
speed2 =[1,1]

while 1:
    screen.fill(black)
    screen.blit(star1,star1rect)
    screen.blit(star2,star2rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif pygame.key.get_pressed()[pygame.K_1]:
            print("1 pressed")
        elif pygame.key.get_pressed()[pygame.K_UP]:
            print("Up Arrow Pressed")
            speed = [speed[0]+1, speed[1]+1]
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            print("Down Arrow Pressed")
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            print("LEFT Arrow Pressed")
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            print("RIGHT Arrow Pressed")
        elif pygame.key.get_pressed()[pygame.K_m]:
            print("OMG You pressed the m key")

    star1rect = star1rect.move(speed)
    star2rect = star2rect.move(speed2)
    print("({0},{1})".format(star1rect.x,star1rect.y))

    if star1rect.left < 0 or star1rect.right > width:
        speed[0] = -speed[0]
    if star2rect.left < 0 or star2rect.right > width:
        speed2[0] = -speed2[0]
    if star1rect.top < 0 or star1rect.bottom > height:
        speed[1] = -speed[1]
    if star2rect.top < 0 or star2rect.bottom > height:
        speed2[1] = -speed2[1]

    if star1rect.colliderect(star2rect):
        speed[0] = - speed[0]
        speed[1] = - speed[1]
        speed2[0] = - speed2[0]
        speed2[1] = - speed2[1]
        collide = True
    if collide == True:
        screen.blit(BLAM,(star1rect.x,star1rect.y))
        pygame.time.delay(80)
        collide = False
    


    pygame.time.delay(80)

    
    
    pygame.display.flip()

