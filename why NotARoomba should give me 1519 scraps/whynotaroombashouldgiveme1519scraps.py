import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
slide = 1
running = True
font = pygame.font.Font(None, size = (35))
slide1 = pygame.image.load("slide1.png")
slide2 = pygame.image.load("slide2.png")
slide3 = pygame.image.load("slide3.png")
slide4 = pygame.image.load("slide4.png")
slide5 = pygame.image.load("slide5.png")
slide6 = pygame.image.load("slide6.png")
slide7 = pygame.image.load("slide7.png")
slide8 = pygame.image.load("slide8.png")
slide9 = pygame.image.load("slide9.png")
slide10 = pygame.image.load("slide10.png")
slide11 = pygame.image.load("slide11.png")
slide12 = pygame.image.load("slide12.png")
text = font.render("Move with Left and Right arrows",True, (0,0,0))
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    slide += 1
                if event.key == pygame.K_LEFT:
                    slide -= 1
    keys = pygame.key.get_pressed()
    
    
    
    if slide == 1:
        screen.blit(slide1, (0,0))
        screen.blit(text, (453, 20))
    if slide == 2:
        screen.blit(slide2, (0,0))
    if slide == 3:
        screen.blit(slide3, (0,0))
    if slide == 4:
        screen.blit(slide4, (0,0))
    if slide == 5:
        screen.blit(slide5, (0,0))
    if slide == 6:
        screen.blit(slide6, (0,0))
    if slide == 7:
        screen.blit(slide7, (0,0))
    if slide == 8:
        screen.blit(slide8, (0,0))
    if slide == 9:
        screen.blit(slide9, (0,0))
    if slide == 10:
        screen.blit(slide10, (0,0))
    if slide == 11:
        screen.blit(slide11, (0,0))
    if slide == 12:
        screen.blit(slide12, (0,0))
    clock.tick(60)
    pygame.display.flip()
        
pygame.quit()