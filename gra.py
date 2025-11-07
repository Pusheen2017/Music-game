import pygame, os, random
from enum import Enum
from pygame import color as color

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

ppath = {
    BUTTONS.RED: ("podświetlNaCzerwono.png"),
    BUTTONS.GREEN: ("podświetlNaZielono.png"),
    BUTTONS.BLUE: ("podświetlNaNiebiesko.png"),
    BUTTONS.YELLOW: ("podświetlNaŻółto.png")
}

class Gra:
    def __init__(self):
        self.running = True #flaga działania gry
        self.screen = pygame.display.set_mode((286, 249)) #okno gry
        pygame.display.set_caption("Memory Game")
        self.clock = pygame.time.Clock()
        pygame.fastevent.init()
        self.music()

    def drawBase(self):
        img_path = os.path.join(os.path.dirname(__file__), "memo.png")
        image = pygame.image.load(img_path).convert_alpha()
        self.screen.blit(image, (0, 0))
        pygame.display.flip()
        
    def drawSelected(self, button: BUTTONS):
        self.drawBase()
        img_path = os.path.join(os.path.dirname(__file__), ppath[button])
        image = pygame.image.load(img_path).convert_alpha()
        self.screen.blit(image, ppos[button])
        pygame.display.flip()

    #def run_loop(self):
    #    pygame.time.delay(500) #5000 milisekund = 5 sekund swyczajnych
    
   
                    
    def events(self):
        self.eventsWithTime(1)
    
    def music(self):
        # losowanie niejednorazowe przy starcie — drukujemy każdą wartość
        #img_path = os.path.join(self.BASE_DIR, "memo.png")
        #image = pygame.image.load(img_path).convert_alpha()
        
        for _ in range(10):
            n = random.randint(1, 4)
            pos = (int, int)
            #print("działa")
            if n == 1:
                print("Wylosowano 1")
                self.drawSelected(BUTTONS.RED)
            elif n == 2:
                print("Wylosowano 2")
                self.drawSelected(BUTTONS.GREEN)
            elif n == 3:
                print("Wylosowano 3")
                self.drawSelected(BUTTONS.BLUE)
            else:
                print("Wylosowano 4")
                self.drawSelected(BUTTONS.YELLOW)
            self.eventsWithTime(1000)
    
    def eventsWithTime(self, sleepTime):
        strartTime = pygame.time.get_ticks()
        while self.running and pygame.time.get_ticks() - strartTime < sleepTime:
            pygame.fastevent.init()
            event = pygame.fastevent.poll()
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_w:#Jeżeli klawisz w naciśnięty
                    print("Naciśnięto W")
                    self.drawSelected(BUTTONS.RED)
                elif event.key == pygame.K_d:
                    print("Naciśnięto D")
                    self.drawSelected(BUTTONS.BLUE)
                elif event.key == pygame.K_a:
                    print("Naciśnięto A")
                    self.drawSelected(BUTTONS.GREEN)
                elif event.key == pygame.K_s:
                    print("Naciśnięto S")
                    self.drawSelected(BUTTONS.YELLOW)
                    
    #główna pętla programu
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.eventsWithTime(1000)
            self.drawBase()
            self.events()  

if __name__ == "__main__":
    game = Gra()
    game.run()