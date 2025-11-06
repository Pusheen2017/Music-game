import pygame, os, random
from enum import Enum

class BUTTONS(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4  

ppos = {
    BUTTONS.RED: (55,45),
    BUTTONS.GREEN: (122,47),
    BUTTONS.BLUE: (122,120),
    BUTTONS.YELLOW: (55,120)
}

class Gra:
    def __init__(self):
        self.running = True #flaga działania gry
        self.screen = pygame.display.set_mode((286, 249)) #okno gry
        pygame.display.set_caption("Memory Game")
        self.BASE_DIR = os.path.dirname(__file__) #katalog do ładowania obrazków
        #img_path = os.path.join(self.BASE_DIR, "memo.png")
        # ładujemy obraz po ustawieniu ekranu
        #self.image = pygame.image.load(img_path).convert_alpha()
        self.screen.fill((255, 255, 255))
        #self.screen.blit(self.image, (0, 0))
        pygame.display.flip()
        self.clock = pygame.time.Clock()
        pygame.fastevent.init()
        print("pygame.fastevent.init()")
        self.music()

    #def run_loop(self):
    #    pygame.time.delay(500) #5000 milisekund = 5 sekund swyczajnych
    
   
                    
    def events(self):
        self.eventsWithTime(1)
    
    def music(self):
        # losowanie niejednorazowe przy starcie — drukujemy każdą wartość
        img_path = os.path.join(self.BASE_DIR, "memo.png")
        image = pygame.image.load(img_path).convert_alpha()
        
        for _ in range(10):
            n = random.randint(1, 4)
            selected_path = str
            pos = (int, int)
            #print("działa")
            if n == 1:
                print("Wylosowano 1")
                selected_path = "podświetlNaCzerwono.png"
                pos=ppos[BUTTONS.RED]
            elif n == 2:
                print("Wylosowano 2")
                selected_path = "podświetlNaZielono.png"
                pos=(122,47)
            elif n == 3:
                print("Wylosowano 3")
                selected_path = "podświetlNaNiebiesko.png"
                pos=(122,120)
            else:
                print("Wylosowano 4")
                selected_path = "podświetlNaŻółto.png"
                pos=(55,120)         
            self.screen.blit(image, (0, 0))#Najpierw użyj tej funkcji, żeby rysować
            img_path = os.path.join(self.BASE_DIR, selected_path)
            image0 = pygame.image.load(img_path).convert_alpha()
            self.screen.blit(image0, pos)#A potem użyj tego.
            pygame.display.flip()
            self.eventsWithTime(100)
        self.screen.blit(image, (0, 0))
        pygame.display.flip()
    
    def eventsWithTime(self, sleepTime):
        strartTime = pygame.time.get_ticks()
        while self.running and pygame.time.get_ticks() - strartTime < sleepTime:
            pygame.fastevent.init()
            event = pygame.fastevent.poll()
            img_path = os.path.join(self.BASE_DIR, "memo.png")
            image0 = pygame.image.load(img_path).convert_alpha()
            pos = (int, int)
            
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_w:#Jeżeli klawisz w naciśnięty
                    print("Naciśnięto W")
                    img_path = os.path.join(self.BASE_DIR, "podświetlNaCzerwono.png")
                    pos = (55,45)
                elif event.key == pygame.K_a:
                    print("Naciśnięto A")
                    img_path =  os.path.join(self.BASE_DIR, "podświetlNaNiebiesko.png")
                    pos=(122,120)
                elif event.key == pygame.K_s:
                    print("Naciśnięto S")
                    img_path =  os.path.join(self.BASE_DIR, "podświetlNaZielono.png")
                    pos=(122,47)
                elif event.key == pygame.K_d:
                    print("Naciśnięto D")
                    img_path =  os.path.join(self.BASE_DIR, "podświetlNaŻółto.png")
                    pos=(55,120)
                if self.running:
                    image = pygame.image.load(img_path).convert_alpha()
                    self.screen.blit(image0, (0, 0))#Najpierw użyj tej funkcji, żeby rysować
                    self.screen.blit(image, pos) #A potem użyj tego.
                    pygame.display.flip()
                    
    #główna pętla programu
    def run(self):
        while self.running:
            #self.clock.tick(60)
            self.eventsWithTime(500)
            self.events()  

if __name__ == "__main__":
    game = Gra()
    game.run()