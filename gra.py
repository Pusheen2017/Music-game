import pygame, os, random

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
                pos=(55,45)
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
            self.screen.blit(image, (0, 0))
            img_path = os.path.join(self.BASE_DIR, selected_path)
            image0 = pygame.image.load(img_path).convert_alpha()
            self.screen.blit(image0, pos)
            pygame.display.flip()
            self.eventsWithTime(1000)
        self.screen.blit(image, (0, 0))
        pygame.display.flip()
    
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
                elif event.key == pygame.K_w:
                    print("Naciśnięto W")
                    self.selected_path = "podświetlNaCzerwono.png"
                    pygame.time.delay(1000)
                    self.selected_path = "memo.png"
                elif event.key == pygame.K_a:
                    print("Naciśnięto A")
                    self.selected_path = "podświetlNaZielono.png"
                    pygame.time.delay(1000)
                    self.selected_path = "memo.png"
                elif event.key == pygame.K_s:
                    print("Naciśnięto S")
                    self.selected_path = "podświetlNaNiebiesko.png"
                    pygame.time.delay(1000)
                    self.selected_path = "memo.png"
                elif event.key == pygame.K_d:
                    print("Naciśnięto D")
                    self.selected_path = "podświetlNaŻółto.png"
                    pygame.time.delay(1000)
                    self.selected_path = "memo.png"
                    
    #główna pętla programu
    def run(self):
        while self.running:
            #self.clock.tick(60)
            self.eventsWithTime(500)
            self.events()  

if __name__ == "__main__":
    game = Gra()
    game.run()