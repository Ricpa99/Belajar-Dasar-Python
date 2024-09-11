import pygame

pygame.init()
dimensi = 500

layar = pygame.display.set_mode((dimensi,dimensi))

x = 250
y = 250
panjang = 20
lebar = 20
dimensi_layar_x = dimensi - panjang
dimensi_layar_y = dimensi - panjang
sped = 1.05
run = True
p = 35
l = 35
while run:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("close")
            run = False
    

    # mengambil key dari keybord
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and x > 0:
        x -= sped
    if key[pygame.K_RIGHT] and x < dimensi_layar_x:
        x += sped
    if key[pygame.K_UP] and y > 0:
        y -= sped
    if key[pygame.K_DOWN] and y < dimensi_layar_y:
        y += sped
    # pygame.draw.rect(layar, ("#463e86"), (x,y))
    layar.fill("#c9c2ff")
    pygame.draw.rect(layar, ("#463e86"), (x,y,lebar,panjang))
    pygame.display.update()

pygame.quit()