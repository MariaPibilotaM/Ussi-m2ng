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
#Ekraani suurused
laius = 520 
kõrgus = 520
#Tausta lisamine
taust = pygame.image.load("taust.bmp")
#Akna pinna tegemine
aken = pygame.display.set_mode((laius,kõrgus))
#Akna nimetuse panemine
pygame.display.set_caption("Ussimäng!")
aken.blit(taust, [0,0]) 

#Mängu lõpu pildid
#Üksikmängija või ussi võt
mäng_läbi_uss_pilt = pygame.image.load("Lõpp_uss.PNG")
pildi_laius = 736
pildi_kõrgus = 738
mäng_läbi_uss = pygame.transform.scale(mäng_läbi_uss_pilt, (round(pildi_laius * 0.6),round(pildi_kõrgus * 0.6)))
#Kana võit
mäng_läbi_kana_pilt = pygame.image.load("Lõpp_kana.PNG")
mäng_läbi_kana = pygame.transform.scale(mäng_läbi_kana_pilt, (round(pildi_laius * 0.6),round(pildi_kõrgus * 0.6)))
#Viigiga
mäng_läbi_viik_pilt = pygame.image.load("Lõpp_viik.PNG")
mäng_läbi_viik = pygame.transform.scale(mäng_läbi_viik_pilt, (round(pildi_laius * 0.6),round(pildi_kõrgus * 0.6)))
#Alguse pilt
algus_pilt = pygame.image.load("algus.PNG")
algus = pygame.transform.scale(algus_pilt, (round(pildi_laius * 0.6),round(pildi_kõrgus * 0.6)))

#Kasutajale akna näitamine
pygame.display.flip()

#Uss
x = 35
y = 35
laius_uss = 25
kõrgus_uss = 25
border = 10
surm = 0
x_muutus = 25
y_muutus = 0
keha = []

#Kana
kõrgus_kana= 25
laius_kana= 25
x_kana= 35
y_kana= 460
x_kana_muutus = 25
y_kana_muutus = 0
kana_keha = []
kanasurm = 0
usssurm = 0
skoor_uss = 0

#Toit
raadius = 10
x1 = randrange(border+raadius, laius-border-raadius, 25)
y1 = randrange(border+raadius, kõrgus-border-raadius, 25)

menüü = 0
tõeväärtus = True

#Mängu tsükkel
tõeväärtus = True
while tõeväärtus:
    pygame.display.update()
    pygame.time.delay(20)
    for event in pygame.event.get():
        
        #Kui kasutaja paneb aknast kinni
        if event.type == pygame.QUIT:
            tõeväärtus = False
    #Alguse menüü ning mängijate valimine
    if menüü == 0:
        pygame.display.flip()
        aken.blit(taust, [0,0])
        aken.blit(algus, (39,40))
        valik = pygame.key.get_pressed()
        if valik [pygame.K_2]:
            menüü = 2
        elif valik [pygame.K_1]:
            menüü = 1
        else:
            menüü = 0
        
    #Uss sööb toitu
    dist_uss = sqrt((x+(laius_uss / 2)-x1)*(x+(laius_uss / 2)-x1) + (y+(kõrgus_uss / 2)-y1)*(y+(kõrgus_uss / 2)-y1))
    dist_kana = sqrt((x_kana+(laius_kana / 2)-x1)*(x_kana+(laius_kana / 2)-x1) + (y_kana+(kõrgus_kana / 2)-y1)*(y_kana+(kõrgus_kana / 2)-y1))
    if dist_uss <= 15 and (menüü == 1 or menüü == 2):
        skoor_uss += 1
        if skoor_uss > highscore and menüü == 1:#Kui skoor suurem kui highscore ss highscore muutub scoreiks
            highscore = skoor_uss
        x1 = randrange(border+raadius, laius-border-raadius, 25)
        y1 = randrange(border+raadius, kõrgus-border-raadius, 25)
        keha.append((x, y, laius_uss, kõrgus_uss))#Sisestame uued kordinaadid kehale

    #Kana sööb toitu
    if dist_kana <= 15 and menüü == 2:
        x1 = randrange(border+raadius, laius-border-raadius, 25)
        y1 = randrange(border+raadius, kõrgus-border-raadius, 25)
        kana_keha.append((x_kana, y_kana, laius_kana, kõrgus_uss))
    
    #Ussi tagumisest otsast hakkavad kordinaadid ennemaks muutuma, ehk et viimane taguots muutub ruuduks, mis ta ees oli enne jne, kuni selleni mis enne pead on
    if menüü == 1 or menüü == 2:
        for i in range(len(keha)-1, 0, -1):
            keha[i] = keha[i-1]
            pygame.draw.rect(aken, (255,204,204), (keha[i]))
            
    #Kana tagumine ots muutub
    if menüü == 2:
        for j in range(len(kana_keha)-1, 0, -1):
            kana_keha[j] = kana_keha[j-1]
            pygame.draw.rect(aken, (200,200,200), (kana_keha[i]))
            
    #Enne pead ruut liigub pea kohale, sest järgnevalt liigub pea edasi
    if len(keha) > 0 and (menüü == 1 or menüü == 2):
        keha[0] = (x, y, laius_uss, kõrgus_uss)
        pygame.draw.rect(aken, (255,204,204), (keha[0]))
        
    #Kana pea edasi liikumine
    if len(kana_keha) > 0 and menüü == 2:
        kana_keha[0] = (x_kana, y_kana, laius_kana, kõrgus_kana)
        pygame.draw.rect(aken, (200,200,200), (kana_keha[0]))
        
    #Liikumine ja bordertest kinni pidamine  
    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT]and x > border and x_muutus != 25 and surm == 0 and (menüü == 1 or menüü == 2):
        x_muutus = -25
        y_muutus = 0
    elif keys [pygame.K_RIGHT]and x < (laius - laius_uss - border) and x_muutus != -25 and surm == 0 and (menüü == 1 or menüü == 2):
        x_muutus = 25
        y_muutus = 0
    elif keys [pygame.K_UP] and y > border and y_muutus != 25 and surm == 0 and (menüü == 1 or menüü == 2):
        y_muutus = -25
        x_muutus = 0
    elif keys [pygame.K_DOWN] and y < (kõrgus - laius_uss - border) and y_muutus != -25 and surm == 0 and (menüü == 1 or menüü == 2):
        y_muutus = 25
        x_muutus = 0
    if surm == 0 and (menüü == 2 or menüü == 1):
        x = x + x_muutus
        y = y + y_muutus

    #Kana liikumine
    keys_kana = pygame.key.get_pressed()
    if keys_kana [pygame.K_a]and x_kana > border and x_kana_muutus != 25 and surm == 0 and menüü == 2:
        x_kana_muutus = -25
        y_kana_muutus = 0
    elif keys_kana [pygame.K_d]and x_kana < (laius - laius_kana - border) and x_kana_muutus != -25 and surm == 0 and menüü == 2:
        x_kana_muutus = 25
        y_kana_muutus = 0
    elif keys_kana [pygame.K_w] and y_kana > border and y_kana_muutus != 25 and surm == 0 and menüü == 2:
        y_kana_muutus = -25
        x_kana_muutus = 0
    elif keys_kana [pygame.K_s] and y_kana < (kõrgus - laius_kana - border) and y_kana_muutus != -25 and surm == 0 and menüü == 2:
        y_kana_muutus = 25
        x_kana_muutus = 0
    if menüü == 2 and surm == 0:
        x_kana = x_kana + x_kana_muutus
        y_kana = y_kana + y_kana_muutus
    
    #Kehasse sõitmine kahemängijas
    if menüü == 2:
        for osa in kana_keha:
            dist = sqrt((x+(laius_uss / 2)-(osa[0]+(laius_kana / 2)))*(x+(laius_uss / 2)-(osa[0]+(laius_kana / 2))) + (y+(kõrgus_uss / 2)-(osa[1] +(kõrgus_kana / 2)))*(y+(kõrgus_uss / 2)-(osa[1] +(kõrgus_kana / 2))))
            if dist <= 15 and surm == 0:
                usssurm = 1
        for osa in keha:
            dist = sqrt((x_kana+(laius_uss / 2)-(osa[0]+(laius_kana / 2)))*(x_kana+(laius_uss / 2)-(osa[0]+(laius_kana / 2))) + (y_kana+(kõrgus_uss / 2)-(osa[1] +(kõrgus_kana / 2)))*(y_kana+(kõrgus_uss / 2)-(osa[1] +(kõrgus_kana / 2))))
            if dist <= 15 and surm == 0:
                kanasurm = 1
    
    #Seina kokkupõrge või uued x ja y kordinaadid on juba keha kordinaadi
    if x < border or x > (laius - laius_uss - border) or y < border or y > (laius - laius_uss - border) or (x, y, laius_uss, kõrgus_uss) in keha and surm == 0 and (menüü == 1 or menüü == 2):
        usssurm = 1
    if x_kana < border or x_kana > (laius - laius_kana - border) or y_kana < border or y_kana > (laius - laius_kana - border) or (x_kana, y_kana, laius_kana, kõrgus_kana) in kana_keha and surm == 0 and menüü == 2:
        kanasurm = 1
        
    #Peade kokkupõrge
    dist_pead = sqrt(((x+(laius_uss / 2)-(x_muutus/2))-(x_kana+(laius_uss / 2)-(x_kana_muutus/2)))*((x+(laius_uss / 2)-(x_muutus/2))-(x_kana+(laius_uss / 2)-(x_kana_muutus/2))) + ((y+(kõrgus_uss / 2)-(y_muutus/2))-(y_kana+(kõrgus_uss / 2)-(y_kana_muutus/2)))*((y+(kõrgus_uss / 2)-(y_muutus/2))-(y_kana+(kõrgus_uss / 2)-(y_kana_muutus/2))))
    if dist_pead <= 12.5 and surm == 0 and ((x_muutus == -x_kana_muutus != 0 and y == y_kana) or (y_muutus == -y_kana_muutus != 0 and x == x_kana)) and menüü == 2:
        kanasurm = 1
        usssurm = 1
    #Toidu lisamine   
    if surm == 0 and menüü > 0:
        pygame.draw.circle(aken, (248, 255, 1), (x1, y1), raadius)
        pygame.draw.rect(aken, (252,166,166), (x, y, laius_uss, kõrgus_uss))
        if menüü == 2:
            pygame.display.set_caption("""Ussimäng! KANA VS USS""")
            pygame.draw.rect(aken,(200,200,200),(x_kana, y_kana, laius_kana, kõrgus_kana))
        if menüü == 1:
            pygame.display.set_caption("Ussimäng! Skoor: " + str(skoor_uss) + " Parim skoor: " + str(highscore))
	            
    #Mäng läbi ja surm  
    if kanasurm == 1 or usssurm == 1 and menüü != 0:
        surm = 1  
    if surm == 1:
        restart = pygame.key.get_pressed()
        if restart [pygame.K_r]:
            menüü = 0
            surm = 0
            kanasurm = 0
            usssurm = 0

            aken = pygame.display.set_mode((laius,kõrgus))
        #Andmete taastamine    
        x = 35
        y = 35
        x_kana = 35
        y_kana = 460
        x_kana_muutus = 25
        y_kana_muutus = 0
        x_muutus = 25
        y_muutus = 0
        keha = []
        kana_keha = []
        skoor_uss = 0
        lõpp = pygame.display.set_mode((laius,kõrgus))
        if menüü == 2:
            if usssurm > kanasurm: #Kontrollime kas saavutati uus highscore ja väljastame vastava sõnumi
                pygame.display.set_caption("Läbi! Kana võitis!")
                aken.blit(mäng_läbi_kana, (39,40))
            if kanasurm > usssurm:
                pygame.display.set_caption("Läbi! Uss võitis!")
                aken.blit(mäng_läbi_uss, (39,40))
            if kanasurm == usssurm:
                pygame.display.set_caption("Läbi! Mäng jäi viiki")    
                aken.blit(mäng_läbi_viik, (39,40))
        if menüü == 1:
            if highscore > alghighscore: #Kontrollime kas saavutati uus highscore ja väljastame vastava sõnumi
                pygame.display.set_caption("Läbi! Saavutasid uue parima skoori! Uus parim skoor: " + str(highscore))
                f = open("highscore.txt", "w")
                f.write(str(highscore))
            if highscore <= alghighscore:
                pygame.display.set_caption("Läbi! Parim skoor jäi muutumata! Mängu skoor: " + str(skoor_uss) + " Parim skoor: " + str(highscore))
            aken.blit(mäng_läbi_uss, (39,40))

        

        
    pygame.display.update()
    if (menüü == 1 or menüü == 2) and surm == 0:
        aken.blit(taust, [0,0])
    time.sleep (100.0 / 1000.0)

pygame.quit()
