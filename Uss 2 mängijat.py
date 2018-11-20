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

#USS 2 koodnimega KANA
kõrgus_kana= 25
laius_kana= 25
x_kana= 25
y_kana= 25
x_kana_muutus = 25
y_kana_muutus = 0
keha_uss_2 = []

#Toit
raadius = 10
x1 = randrange(border+raadius, laius-border-raadius, 25)
y1 = randrange(border+raadius, kõrgus-border-raadius, 25)
skoor_uss = 0
skoor_kana = 0

tõeväärtus = True
while tõeväärtus:
    pygame.time.delay(20)
    for event in pygame.event.get():
        
        #Kui kasutaja paneb aknast kinni
        if event.type == pygame.QUIT:
            tõeväärtus = False
            
    #Uss sööb toitu
    dist_uss = sqrt((x+(laius_uss / 2)-x1)*(x+(laius_uss / 2)-x1) + (y+(kõrgus_uss / 2)-y1)*(y+(kõrgus_uss / 2)-y1))
    dist_kana = sqrt((x_kana+(laius_kana / 2)-x1)*(x_kana+(laius_kana / 2)-x1) + (y_kana+(kõrgus_kana / 2)-y1)*(y_kana+(kõrgus_kana / 2)-y1))
    if dist_uss <= 15:
        skoor_uss += 1
        if skoor_uss > highscore:#Kui skoor suurem kui highscore ss highscore muutub scoreiks
            highscore = skoor_uss
        x1 = randrange(border+raadius, laius-border-raadius, 25)
        y1 = randrange(border+raadius, kõrgus-border-raadius, 25)
        keha.append((x, y, laius_uss, kõrgus_uss))#Sisestame uued kordinaadid kehale

    #Kana sööb toitu
    if dist_kana <= 15:
        skoor_kana += 1
        if skoor_kana > highscore:
            highscore = skoor_kana
        x1 = randrange(border+raadius, laius-border-raadius, 25)
        y1 = randrange(border+raadius, kõrgus-border-raadius, 25)
        
    #Uss 2 läheb ussi 1 vastu
    dist_2_1 = sqrt((x_kana+(laius_kana / 2)-x)*(x_kana+(laius_kana / 2)-x) + (y_kana+(kõrgus_kana / 2)-y)*(y_kana+(kõrgus_kana / 2)-y))
    if dist_2_1 <= 15:
        skoor_kana = skoor_kana + 1
        skoor_uss = skoor_uss - 1
        surm == 1
    #Uss 1 läheb ussi 2 vastu
    dist_1_2 = sqrt((x+(laius_uss / 2)-x_kana)*(x+(laius_uss / 2)-x_kana) + (y+(kõrgus_uss / 2)-y_kana)*(y+(kõrgus_uss / 2)-y_kana))
    if dist_1_2 <= 15:
        skoor_kana = skoor_kana - 1
        skoor_uss = skoor_uss + 1
        surm == 1

    
    #Ussi tagumisest otsast hakkavad kordinaadid ennemaks muutuma, ehk et viimane taguots muutub ruuduks, mis ta ees oli enne jne, kuni selleni mis enne pead on
    for i in range(len(keha)-1, 0, -1):
        keha[i] = keha[i-1]
        pygame.draw.rect(aken, (255,204,204), (keha[i]))
    #Uss nr 2 tagumine ots muutub
    for j in range(len(keha_uss_2)-1, 0, -1):
        keha_uss_2[j] = keha_uss_2[j-1]
        
    #Enne pead ruut liigub pea kohale, sest järgnevalt liigub pea edasi
    if len(keha) > 0:
        keha[0] = (x, y, laius_uss, kõrgus_uss)
        pygame.draw.rect(aken, (255,204,204), (keha[0]))
        
    #Uss 2 pea edasi liikumine
    if len(keha_uss_2) > 0:
        keha_uss_2[0] = (x_kana, y_kana, laius_kana, kõrgus_kana)
        pygame.draw.rect(aken, (200,200,200), (keha_uss_2[0]))
        
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

    #Uss nr 2 liikumine
    keys_kana = pygame.key.get_pressed()
    if keys_kana [pygame.K_a]and x_kana > border and x_kana_muutus != 25:
        x_kana_muutus = -25
        y_kana_muutus = 0
    elif keys_kana [pygame.K_d]and x_kana < (laius - laius_kana - border) and x_kana_muutus != -25:
        x_kana_muutus = 25
        y_kana_muutus = 0
    elif keys_kana [pygame.K_w] and y_kana > border and y_kana_muutus != 25:
        y_kana_muutus = -25
        x_kana_muutus = 0
    elif keys_kana [pygame.K_s] and y_kana < (kõrgus - laius_kana - border) and y_kana_muutus != -25:
        y_kana_muutus = 25
        x_kana_muutus = 0
    x_kana = x_kana + x_kana_muutus
    y_kana = y_kana + y_kana_muutus



    
    #Seina kokkupõrge või uued x ja y kordinaadid on juba keha kordinaadi. Mäng läbi
    if x < border or x > (laius - laius_uss - border) or y < border or y > (laius - laius_uss - border) or (x, y, laius_uss, kõrgus_uss) in keha:
        surm = 1
        x_muutus = 0
        y_muutus = 0
        x_kana_muutus = 0
        y_kana_muutus = 0
        f = open("highscore.txt", "w")
        f.write(str(highscore))
    if x_kana < border or x_kana > (laius - laius_kana - border) or y_kana < border or y_kana > (laius - laius_kana - border):
        surm = 1
        x_kana_muutus = 0
        y_kana_muutus = 0
        x_muutus = 0
        y_muutus = 0
        f = open("highscore.txt", "w")
        f.write(str(highscore))
    if surm == 1:
        lõpp = pygame.display.set_mode((laius,kõrgus))
        if highscore > alghighscore: #Kontrollime kas saavutati uus highscore ja väljastame vastava sõnumi
            pygame.display.set_caption("Läbi! Saavutasid uue parima skoori! Uus parim skoor: " + str(highscore))
        if highscore <= alghighscore and skoor_kana > skoor_uss:
            pygame.display.set_caption("Läbi! Parim skoor jäi muutumata! USS 2: " + str(skoor_kana) + "  USS 1: " + str(skoor_uss) + "  PARIM: " + str(highscore))
        if highscore <= alghighscore and skoor_kana < skoor_uss:
            pygame.display.set_caption("Läbi! Parim skoor jäi muutumata! USS 1: " + str(skoor_uss) + "  USS 2: " + str(skoor_kana) + "  PARIM: " + str(highscore))    
        
        aken.blit(mäng_läbi, (39,40))
           
    pygame.draw.rect(aken, (252,166,166), (x, y, laius_uss, kõrgus_uss))
    pygame.draw.rect(aken,(200,200,200),(x_kana, y_kana, laius_kana, kõrgus_kana))
    if surm == 0:
        pygame.draw.circle(aken, (248, 255, 1), (x1, y1), raadius)
        pygame.display.set_caption("Ussimäng! Skoor uss: " + str(skoor_uss) + "Skoor kana:" + str(skoor_kana) + " Parim skoor: " + str(highscore))
    pygame.display.update()
    aken.fill((153, 255, 51))
    time.sleep (100.0 / 1000.0)

pygame.quit()
