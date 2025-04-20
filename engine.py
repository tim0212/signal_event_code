"""단어 수락은 Tab키로, 단어 취소는 ESC 키로, 단어 입력은 Enter 키로 진행합니다."""

import pygame, sys, os, keyboard
from sign import Signals

x = 100
y = x * (9/16)

class Act:
    def __init__(self):
        self.sign = Signals()

    def attack(self):
        print("attack")

    def attack2(self):
        pass

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((x, y))
        self.clock = pygame.time.Clock()
        self.sign = Signals()
        self.act = Act()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.sign.signal(send="attack", list_num=0)
                    if event.key == pygame.K_2:
                        self.sign.signal(send="defence", list_num=1)

                if event.type == pygame.KEYUP:
                    pass


            #screen setttings
            pygame.display.flip()
            self.screen.fill("black")
            self.clock.tick(60)

            if self.sign.signal(reseve="attack", list_num=0): self.act.attack(); self.sign.clear(list_num=0)
            if self.sign.signal(reseve="defence", list_num=1): self.act.attack2(); self.sign.clear(list_num=1)

if __name__ == "__main__":
    game = Game()
    game.run()