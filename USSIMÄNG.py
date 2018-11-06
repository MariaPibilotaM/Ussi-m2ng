import pygame

#Tööle rakendamine
pygame.init()

#Akna pinna tegemine
laius = 500
kõrgus = 500

aken = pygame.display.set_mode((laius,kõrgus))

pygame.display.set_caption("Ussimäng")

#Akna värv
aken.fill((153, 255, 51))

#Mäng läbi pilt
mäng_läbi = pygame.image.load("game-over.png")
pildi_laius = 528
pildi_kõrgus = 528

#Mäng läbi pildi suuruse muutmine
mäng_läbi = pygame.transform.scale(mäng_läbi, (round(pildi_laius * 0.35),round(pildi_kõrgus * 0.35)))

#Kasutajale akna näitamine
pygame.display.flip()

x = 250
y = 250
laius_uss = 30
kõrgus_uss = 30
vel = 10

tõeväärtus = True
while tõeväärtus:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        
        #Kui kasutaja paneb aknast kinni
        if event.type == pygame.QUIT:
            tõeväärtus = False

    #Liikumine ja mitte äärtesse minek   
    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT]and x > vel:
        x -= vel
    if keys [pygame.K_RIGHT]and x < (laius - laius_uss - vel) :
        x += vel
    if keys [pygame.K_UP] and y > vel:
        y -= vel
    if keys [pygame.K_DOWN] and y < (kõrgus - laius_uss - vel):
        y += vel
        
    #Äärde liikumine ja mäng läbi pilt
    if (keys [pygame.K_DOWN] or [pygame.K_UP] or [pygame.K_LEFT]or [pygame.K_RIGHT])and ( x == vel or x == (laius - laius_uss - vel) or y == vel or y == (laius - laius_uss - vel)):
        #Mäng läbi pildi asukoht ja kuvamine
        aken.blit(mäng_läbi, (250-(round(pildi_laius*0.35/2)),250-(round(pildi_kõrgus*0.35/2))))
        pygame.display.update()
        
    #Ristküliku joonistamine
    pygame.draw.rect(aken, (199,0,157), (x, y, laius_uss, kõrgus_uss))
    pygame.display.update()
    aken.fill((153, 255, 51))

    

pygame.quit()
