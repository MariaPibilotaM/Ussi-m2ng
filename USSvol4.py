import pygame
from math import sqrt
from random import randrange
import time

try:#Võtame failist highscore ja faili puudumisel oletame, et highscore on 0
    highscore = int(open("highscore.txt").read())
except:
    highscore = 0
alghighscore = highscore

pygame.init()
laius = 520 #Suurused
kõrgus = 520
aken = pygame.display.set_mode((laius,kõrgus)) #Akna pinna tegemine
pygame.display.set_caption("Ussimäng!")
aken.fill((153, 255, 51)) #Värv

#Mäng läbi pilt
mäng_läbi = pygame.image.load("uus_lopp.png")
pildi_laius = 736
pildi_kõrgus = 735
mäng_läbi = pygame.transform.scale(mäng_läbi, (round(pildi_laius * 0.6),round(pildi_kõrgus * 0.6)))

#Kasutajale akna näitamine
pygame.display.flip()

#Uss
x = 260
y = 260
laius_uss = 25
kõrgus_uss = 25
border = 10
surm = 0
x_muutus = 25
y_muutus = 0
keha = []

#Toit
raadius = 10
x1 = randrange(border+raadius, laius-border-raadius, 25)
y1 = randrange(border+raadius, kõrgus-border-raadius, 25)
skoor = 0

tõeväärtus = True
while tõeväärtus:
    pygame.time.delay(20)
    for event in pygame.event.get():
        
        #Kui kasutaja paneb aknast kinni
        if event.type == pygame.QUIT:
            tõeväärtus = False
            
    #Uss sööb toitu
    dist = sqrt((x+(laius_uss / 2)-x1)*(x+(laius_uss / 2)-x1) + (y+(kõrgus_uss / 2)-y1)*(y+(kõrgus_uss / 2)-y1))
    if dist <= 15:
        skoor += 1
        if skoor > highscore:#Kui skoor suurem kui highscore ss highscore muutub scoreiks
            highscore = skoor
        x1 = randrange(border+raadius, laius-border-raadius, 25)
        y1 = randrange(border+raadius, kõrgus-border-raadius, 25)
        keha.append((x, y, laius_uss, kõrgus_uss))#Sisestame uued kordinaadid kehale
    
    #Ussi tagumisest otsast hakkavad kordinaadid ennemaks muutuma, ehk et viimane taguots muutub ruuduks, mis ta ees oli enne jne, kuni selleni mis enne pead on
    for i in range(len(keha)-1, 0, -1):
        keha[i] = keha[i-1]
        pygame.draw.rect(aken, (255,204,204), (keha[i]))
        
    #Enne pead ruut liigub pea kohale, sest järgnevalt liigub pea edasi
    if len(keha) > 0:
        keha[0] = (x, y, laius_uss, kõrgus_uss)
        pygame.draw.rect(aken, (255,204,204), (keha[0]))
        
    #Liikumine ja bordertest mitte välja liikumine  
    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT]and x > border and x_muutus != 25:
        x_muutus = -25
        y_muutus = 0
    elif keys [pygame.K_RIGHT]and x < (laius - laius_uss - border) and x_muutus != -25:
        x_muutus = 25
        y_muutus = 0
    elif keys [pygame.K_UP] and y > border and y_muutus != 25:
        y_muutus = -25
        x_muutus = 0
    elif keys [pygame.K_DOWN] and y < (kõrgus - laius_uss - border) and y_muutus != -25:
        y_muutus = 25
        x_muutus = 0
    x = x + x_muutus
    y = y + y_muutus
    
    #Seina kokkupõrge või uued x ja y kordinaadid on juba keha kordinaadi. Mäng läbi
    if x < border or x > (laius - laius_uss - border) or y < border or y > (laius - laius_uss - border) or (x, y, laius_uss, kõrgus_uss) in keha:
        surm = 1
        x_muutus = 0
        y_muutus = 0
        f = open("highscore.txt", "w")
        f.write(str(highscore))
    if surm == 1:
        lõpp = pygame.display.set_mode((laius,kõrgus))
        if highscore > alghighscore: #Kontrollime kas saavutati uus highscore ja väljastame vastava sõnumi
            pygame.display.set_caption("Läbi! Saavutasid uue parima skoori! Uus parim skoor: " + str(highscore))
        if highscore <= alghighscore:
            pygame.display.set_caption("Läbi! Parim skoor jäi muutumata! Mängu skoor: " + str(skoor) + " Parim skoor: " + str(highscore))
        
        aken.blit(mäng_läbi, (39,40))
           
    pygame.draw.rect(aken, (252,166,166), (x, y, laius_uss, kõrgus_uss))
    if surm == 0:
        pygame.draw.circle(aken, (248, 255, 1), (x1, y1), raadius)
        pygame.display.set_caption("Ussimäng! Skoor: " + str(skoor) + " Parim skoor: " + str(highscore))
    pygame.display.update()
    aken.fill((153, 255, 51))
    time.sleep (100.0 / 1000.0)

pygame.quit()
