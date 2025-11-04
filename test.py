import pygame, os, random

class Gra:
    def __init__(self):
        pygame.init()
        self.running = True  # flaga działania gry
        self.screen = pygame.display.set_mode((286, 249))  # okno gry
        pygame.display.set_caption("Memory Game")

        self.BASE_DIR = os.path.dirname(__file__)  # katalog do ładowania obrazków
        self.screen.fill((255, 255, 255))
        pygame.display.flip()

        self.clock = pygame.time.Clock()
        pygame.fastevent.init()
        print("pygame.fastevent.init()")

        self.music()  # uruchamiamy sekwencję startową

    def show_highlight(self, filename, pos):
        """Wyświetla tło + podświetlenie koloru przez chwilę"""
        base_path = os.path.join(self.BASE_DIR, "memo.png")
        base = pygame.image.load(base_path).convert_alpha()

        path = os.path.join(self.BASE_DIR, filename)
        image = pygame.image.load(path).convert_alpha()

        # rysowanie
        self.screen.blit(base, (0, 0))
        self.screen.blit(image, pos)
        pygame.display.flip()

        # chwila podświetlenia
        pygame.time.delay(500)

        # powrót do planszy bazowej
        self.screen.blit(base, (0, 0))
        pygame.display.flip()

    def music(self):
        """Losowo podświetla pola przy starcie gry"""
        img_path = os.path.join(self.BASE_DIR, "memo.png")
        image = pygame.image.load(img_path).convert_alpha()

        for _ in range(10):
            n = random.randint(1, 4)
            if n == 1:
                print("Wylosowano 1")
                self.show_highlight("podświetlNaCzerwono.png", (55, 45))
            elif n == 2:
                print("Wylosowano 2")
                self.show_highlight("podświetlNaZielono.png", (122, 47))
            elif n == 3:
                print("Wylosowano 3")
                self.show_highlight("podświetlNaNiebiesko.png", (122, 120))
            else:
                print("Wylosowano 4")
                self.show_highlight("podświetlNaŻółto.png", (55, 120))

        self.screen.blit(image, (0, 0))
        pygame.display.flip()

    def eventsWithTime(self, sleepTime):
        """Odczytuje zdarzenia przez określony czas"""
        startTime = pygame.time.get_ticks()
        while self.running and pygame.time.get_ticks() - startTime < sleepTime:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_w:
                        print("Naciśnięto W")
                        self.show_highlight("podświetlNaCzerwono.png", (55, 45))
                    elif event.key == pygame.K_a:
                        print("Naciśnięto A")
                        self.show_highlight("podświetlNaZielono.png", (122, 47))
                    elif event.key == pygame.K_d:
                        print("Naciśnięto S")
                        self.show_highlight("podświetlNaNiebiesko.png", (122, 120))
                    elif event.key == pygame.K_s:
                        print("Naciśnięto D")
                        self.show_highlight("podświetlNaŻółto.png", (55, 120))
            pygame.time.delay(10)

    def events(self):
        self.eventsWithTime(1)

    def run(self):
        """Główna pętla gry"""
        while self.running:
            self.eventsWithTime(500)
            self.events()

if __name__ == "__main__":
    game = Gra()
    game.run()
