import pygame
from pygame import mixer
import os
pygame.font.init()
pygame.mixer.init()
szeles, magas= 1550,900
hatter= pygame.transform.scale(pygame.image.load(os.path.join('kepekeszene','Hatter.png')), (szeles,magas))
MENU= pygame.transform.scale(pygame.image.load(os.path.join('kepekeszene','menuhatter.png')), (szeles,magas))
Feher=(255,255,255)
Fekete=(0,0,0)
Barna=(128,0,0)
Kijelzo= pygame.display.set_mode((szeles,magas))

Macskahang=pygame.mixer.Sound('kepekeszene\Cicaserult.mp3')
Rokahang=pygame.mixer.Sound("kepekeszene\Rokaserult.mp3") 

macskault=False
rokault=False

 
pygame.display.set_caption("Cats vs Foxes") #címe az Kijelzodownak
gyors=4
fps=60
lovedekgy=6
lovedekm, lovedeksz=80,75
multiszeles, multimagas=120,55  
Lszam=4 #mennyi lehet a képernyőn egyszerre
lultiszam=1
stealszeles, stealmagas=90,85
ikonszeles, ikonmagas=80, 65
Eletiras=pygame.font.SysFont('comicsans', 35 )
Gyoztesiras = pygame.font.SysFont('comicsans', 100)
Szamlaloiras= pygame.font.SysFont('comicsans', 45)
Menuiras=pygame.font.SysFont('comicsans', 65 )

allatokmagas, allatokszeles= 180, 180
Elvalaszto=pygame.Rect(szeles//2-2.5, 0,5, magas)
Mlovet_kep=pygame.image.load(os.path.join('kepekeszene','Egér.png'))
Mlovedekmeret= pygame.transform.scale(Mlovet_kep,(lovedeksz,lovedekm))
Multi_kep=pygame.image.load(os.path.join('kepekeszene','Multi.png'))
Multi_merete=pygame.transform.scale(Multi_kep,(multiszeles, multimagas))
Rlovet_kep=pygame.image.load(os.path.join('kepekeszene','Gomba.png'))
Rlovedekmeret= pygame.transform.scale(Rlovet_kep,(lovedeksz,lovedekm))
Rulti_kep=pygame.image.load(os.path.join('kepekeszene','Rulti.png'))
Rulti_merete=pygame.transform.scale(Rulti_kep,(multiszeles, multimagas))
Muikon_kep=pygame.image.load(os.path.join('kepekeszene','Muikon.png'))
Muikon_merete= pygame.transform.scale(Muikon_kep,(ikonszeles,ikonmagas))
Ruikon_kep=pygame.image.load(os.path.join('kepekeszene','Ruikon.png'))
Ruikon_merete= pygame.transform.scale(Ruikon_kep,(ikonszeles,ikonmagas))
cicaeredmeny=0
rokaeredmeny=0
menumagas=450
menuszeles=430
Macskaserult=pygame.USEREVENT+1
Rokaserult=pygame.USEREVENT+2
Macskaultiserult=pygame.USEREVENT+3
Rokaultiserult=pygame.USEREVENT+4
# Macska=pygame.image.load('macska.png') ez így müködhetne ha 1 mappába van viszont ha nem akkor
Macska_kep = pygame.image.load(os.path.join('kepekeszene','Macska.png')) #ez kell így mivel más op-nak más lehet az elérési utvonala és a kiugrálás máshogy folyhat le
Macska_meret=pygame.transform.scale(Macska_kep,(allatokszeles,allatokmagas))
Macska_menun=pygame.transform.scale(Macska_kep,(menuszeles,menumagas))
Roka_kep = pygame.image.load(os.path.join('kepekeszene','Roka.png')) #ez kell így mivel más op-nak más lehet az elérési utvonala és a kiugrálás máshogy folyhat le
Roka_meret=pygame.transform.scale(Roka_kep,(allatokszeles,allatokmagas))
Roka_menun=pygame.transform.scale(Roka_kep,(menuszeles,menumagas))

def macskamozgas(lenyomotb, MacskaJ):
    if lenyomotb[pygame.K_a] and MacskaJ.x-gyors>0: #macska balra + nem engedi kilépni a képből a többi is ezt fogja tenni
        MacskaJ.x-=gyors
    if lenyomotb[pygame.K_d] and MacskaJ.x+gyors+MacskaJ.width< Elvalaszto.x: #macska jobbra jobrol indul emiatt átmenne ha nem lenne a width -15 az Elvalasztohóz hogy ne menjen rá
        MacskaJ.x+=gyors
    if lenyomotb[pygame.K_s] and MacskaJ.y+gyors+ MacskaJ.width<magas: #macska le
        MacskaJ.y+=gyors
    if lenyomotb[pygame.K_w] and MacskaJ.y-gyors>50: #macska fel
        MacskaJ.y-=gyors
        
def Rokamozgas(lenyomotb, RokaJ):
    if lenyomotb[pygame.K_LEFT] and RokaJ.x-gyors>Elvalaszto.x+Elvalaszto.width: #Roka balra ugyan az mint a macskánál 
        RokaJ.x-=gyors
    if lenyomotb[pygame.K_RIGHT] and RokaJ.x+gyors+RokaJ.width<szeles-5  : #Roka jobbra
        RokaJ.x+=gyors
    if lenyomotb[pygame.K_DOWN]and RokaJ.y+gyors+RokaJ.width<magas: #Roka le
        RokaJ.y+=gyors
    if lenyomotb[pygame.K_UP] and RokaJ.y-gyors>50: #Roka fel
        RokaJ.y-=gyors
        

def draw(RokaJ, MacskaJ, Mlovedek, Rlovedek, Rokaelet, Macskaelet,cicaeredmeny,rokaeredmeny,Multilovedek,Rultilovedek,Msebzodotdb, Rsebzodotdb): #rajzolás a Kijelzodora, macska Roka azért van behiva mivel igy ahogy majd mozgatjuk máshova fogja rajzolni
    Kijelzo.blit(hatter, (0,0))
    pygame.draw.rect(Kijelzo, Fekete,Elvalaszto)
    Cicaeletereje=Eletiras.render("Életeid: " + str(Macskaelet), 1,Feher)
    Rokaeletereje=Eletiras.render("Életeid: " + str(Rokaelet),1 ,Feher)
    Cicaszamlalo=Szamlaloiras.render(str(cicaeredmeny),1,Feher)
    Rokaszamlalo=Szamlaloiras.render(str(rokaeredmeny),1,Feher)
    Kijelzo.blit(Cicaszamlalo, (Elvalaszto.x-50,10))
    Kijelzo.blit(Rokaszamlalo, (Elvalaszto.x+25,10))
    Kijelzo.blit(Cicaeletereje, (10,10))
    Kijelzo.blit(Rokaeletereje, (szeles-Rokaeletereje.get_width()-10, 10))
    Kijelzo.blit(Macska_meret, (MacskaJ.x,MacskaJ.y)) #hogy RÁ rajzoljunk valamire kordináta (.x és.y lefogja követni majd hogy hogy mozgunk)
    Kijelzo.blit(Roka_meret, (RokaJ.x,RokaJ.y))
    if Msebzodotdb%4==0 and Msebzodotdb!=0:
       Kijelzo.blit(Ruikon_merete, (1400, 70))
       
    if Rsebzodotdb%4==0 and Rsebzodotdb!=0:
       Kijelzo.blit(Muikon_merete, (30,70))

    for Macskatuze in Mlovedek:
        Kijelzo.blit(Mlovedekmeret, (Macskatuze.x, Macskatuze.y))
        
    for macskasteal in Multilovedek:
        Kijelzo.blit(Multi_merete, (macskasteal.x, macskasteal.y))
        
        
    for Rokatuze in Rlovedek:
        Kijelzo.blit(Rlovedekmeret, (Rokatuze.x, Rokatuze.y))
        
    for Rokasteal in Rultilovedek:
            Kijelzo.blit(Rulti_merete, (Rokasteal.x, Rokasteal.y))
        
    
        
    pygame.display.update() #alapból fekete lenne és nem töltené be mi van rajta az update ezen segít  
def Kiiras(iras, jatekvar):
        jatekvar=True
        seged= Gyoztesiras.render(iras,1,Feher)
        x = szeles / 2 - seged.get_width() / 2
        y = magas / 2 - seged.get_height() / 2
        Kijelzo.blit(seged, (x, y))
        pygame.display.update()
        pygame.time.delay(3000)
        jatekvar=False
def Kepeseg(MacskaJ,RokaJ, jatekvar, Msebzodotdb, Rsebzodotdb, Multilovedek, Rultilovedek,rokault,macskault):
     if jatekvar==False:
        for Macskasteal in Multilovedek:
            Macskasteal.x += lovedekgy+1
            if RokaJ.colliderect(Macskasteal):
               pygame.event.post(pygame.event.Event(Rokaultiserult))
               Multilovedek.remove(Macskasteal)
               macskault=False
            elif Macskasteal.x > szeles:
                Multilovedek.remove(Macskasteal)
                macskault=False
                
               
                
                
        for Rokasteal in Rultilovedek:
            Rokasteal.x -= lovedekgy+1
            if MacskaJ.colliderect(Rokasteal):
                pygame.event.post(pygame.event.Event(Macskaultiserult))
                Rultilovedek.remove(Rokasteal)
                rokault=False
            elif Rokasteal.x < 0:
                Rultilovedek.remove(Rokasteal)
                rokault=False
                
def Utes(Mlovedek,Rlovedek,MacskaJ,RokaJ, jatekvar):
    if jatekvar==False:
        for Macskatuze in Mlovedek:
            Macskatuze.x += lovedekgy
            if RokaJ.colliderect(Macskatuze):
                pygame.event.post(pygame.event.Event(Rokaserult))
                Mlovedek.remove(Macskatuze)
            elif Macskatuze.x > szeles:
                Mlovedek.remove(Macskatuze)
                
                
        for Rokatuze in Rlovedek:
            Rokatuze.x-=lovedekgy
            if MacskaJ.colliderect(Rokatuze):
                pygame.event.post(pygame.event.Event(Macskaserult))
                Rlovedek.remove(Rokatuze)
            elif Rokatuze.x < 0:
                Rlovedek.remove(Rokatuze)
        
def menu():
    while True:
        for event in pygame.event.get():
            pygame.mixer.music.load('kepekeszene\menu_song.mp3')  
            pygame.mixer.music.play(-1)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key==pygame.K_KP_ENTER:
                    return True,mixer.stop()
                elif event.key == pygame.K_2 or event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        Kijelzo.blit(MENU, (0,0))
        StartSzoveg = Menuiras.render("1. Start", 1, Barna)
        KilepSzoveg = Menuiras.render("2. Exit", 1, Barna)
        Kijelzo.blit(StartSzoveg, (szeles//2 - StartSzoveg.get_width()//2, magas//2 - 75))
        Kijelzo.blit(KilepSzoveg, (szeles//2 - KilepSzoveg.get_width()//2, magas//2 + 75))
        Kijelzo.blit(Macska_menun, (szeles//2 - Macska_menun.get_width()//2-450, magas//2-150))
        Kijelzo.blit(Roka_menun, (szeles//2 - Roka_menun.get_width()//2+450, magas//2-150))
        pygame.display.update()
def main(cicaeredmeny,rokaeredmeny,rokault,macskault):
    pygame.mixer.music.stop()
    pygame.mixer.music.load('kepekeszene\game_song.mp3')  
    pygame.mixer.music.play(-1)
    RokaJ= pygame.Rect(1250,300, allatokszeles, allatokmagas) #röviden hitbox és amivel írányitani fogjuk a kutyát majd
    MacskaJ=pygame.Rect(100,300, allatokszeles, allatokmagas)
    clock =pygame.time.Clock()
    Mlovedek=[] 
    Rlovedek=[]
    Multilovedek=[] 
    Rultilovedek=[]
    Gyozelem =""
    Macskaelet =10
    Rokaelet =10
    Msebzodotdb=0
    Rsebzodotdb=0
    teljeskepernyo=False
    jatekvar=False
    run=True
    while run:
        if Rsebzodotdb%4==0:
            macskault=True
        else:
            macskault=False
        if Msebzodotdb%4==0:
            rokault=True
        else:
            rokault=False
        clock.tick(fps) #60 fps-sel fusson mindig
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run=False 
                pygame.quit()
            if event.type== pygame.KEYDOWN and jatekvar==False:#he egyszer lenyomtunk egy gombot
                if event.key== pygame.K_LCTRL  and len(Mlovedek)<Lszam: #max Lszam mennyiségű lövedék lehet a képernyőn
                    Macskatuze = pygame.Rect(
                        MacskaJ.x + MacskaJ.width, MacskaJ.y + MacskaJ.height//2 - 2, lovedeksz, lovedekm)
                    Mlovedek.append(Macskatuze)
                if event.key==pygame.K_LSHIFT and macskault==True:
                        Macskasteal = pygame.Rect(
                            MacskaJ.x + MacskaJ.width, MacskaJ.y + MacskaJ.height//2 - 2,stealszeles,stealmagas)
                        Multilovedek.append(Macskasteal)
                if event.key== pygame.K_RCTRL and len(Rlovedek)<Lszam:
                    Rokatuze = pygame.Rect(
                        RokaJ.x, RokaJ.y + RokaJ.height // 2 - 2,lovedeksz,lovedekm)
                    Rlovedek.append(Rokatuze)
                if event.key==pygame.K_RSHIFT and rokault==True:
                        Rokasteal = pygame.Rect(
                            RokaJ.x, RokaJ.y + RokaJ.height//2 - 2,stealszeles,stealmagas)
                        Rultilovedek.append(Rokasteal)
                if event.key==pygame.K_f:
                    teljeskepernyo=not teljeskepernyo
                    if teljeskepernyo==True:
                        pygame.display.set_mode((szeles, magas), pygame.FULLSCREEN)
                    else:
                        pygame.display.set_mode((szeles, magas))
                if event.key==pygame.K_ESCAPE:
                    run=False
                    pygame.quit()
            if event.type == Rokaserult:
                Rokaelet=Rokaelet-1
                Rsebzodotdb+=1
                Rokahang.play()
            if event.type==Rokaultiserult:
                Macskaelet+=1
                Rokaelet-=2
                Rsebzodotdb+=2
                Rokahang.play()
             
            if event.type == Macskaserult:
                Macskaelet=Macskaelet-1
                Msebzodotdb+=1
                Macskahang.play()
            if event.type== Macskaultiserult:
                Macskaelet=Macskaelet-2
                Rokaelet=Rokaelet+1
                Msebzodotdb+=2
                Macskahang.play()
                
        if Rokaelet <= 0:
            Gyozelem = "Macska nyert!"
            cicaeredmeny=cicaeredmeny+1
        if Macskaelet <= 0:
            Gyozelem = "Róka nyert!"
            rokaeredmeny=rokaeredmeny+1
        if Gyozelem != "":
            Kiiras(Gyozelem, jatekvar)
            jatekvar=False
            pygame.mixer.music.stop()
            pygame.mixer.music.load('kepekeszene\menu_song.mp3')  
            pygame.mixer.music.play(-1)
            jatekvar=True
            break
        lenyomotb=pygame.key.get_pressed() #megnézni milyen gombok vannak lenyomva 
        macskamozgas(lenyomotb,MacskaJ)
        Rokamozgas(lenyomotb,RokaJ)
        draw(RokaJ, MacskaJ, Mlovedek, Rlovedek, Rokaelet, Macskaelet, cicaeredmeny, rokaeredmeny,Multilovedek,Rultilovedek,Msebzodotdb, Rsebzodotdb)
        Utes(Mlovedek,Rlovedek,MacskaJ,RokaJ, jatekvar)
        Kepeseg(MacskaJ,RokaJ, jatekvar, Msebzodotdb, Rsebzodotdb, Multilovedek, Rultilovedek,rokault, macskault)
        
    return cicaeredmeny, rokaeredmeny, rokault,macskault
    
    
if __name__ == "__main__": #nincs importálva de ez megoldja hogy helyesen fusson le és akkor fusson le a def main amikor mi szeretnénks
    while True:
        if menu():
            cicaeredmeny,rokaeredmeny =main(cicaeredmeny, rokaeredmeny,rokault, macskault)