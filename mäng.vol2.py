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


#Kasutajale akna näitamine
pygame.display.flip()

x = 50
y = 50
laius = 30
kõrgus = 30
vel = 5

tõeväärtus = True
while tõeväärtus:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        
        #Kui kasutaja paneb aknast kinni
        if event.type == pygame.QUIT:
            tõeväärtus = False

    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT]:
        x -= vel
    if keys [pygame.K_RIGHT]:
        x += vel
    if keys [pygame.K_UP]:
        y -= vel
    if keys [pygame.K_DOWN]:
        y += vel
    

    aken.fill((153, 255, 51))
    #Ristküliku joonistamine

    pygame.draw.rect(aken, (199,0,157), (x, y, laius, kõrgus))
    pygame.display.update()
                     
pygame.quit()
