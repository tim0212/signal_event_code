# signal이 보내는걸 칮고 싶으면 F3후 signal:원하는 신호 이름 <-으로 적어

import pygame, sys, os, keyboard
from ingame_code import *

x = 1440
y = x * (9/16)

class Gain_mudule:
    def __init__(self, shared_sign):
        self.sign = shared_sign
        self.ally = Ally()
        self.act = Act()
        self.enemy = Enermy()
        self.load = Load()

class Signal_control:
    def __init__(self, shared_sign, mudule_act):
        self.sign = shared_sign
        self.mudule_act = mudule_act

    def control(self):
        if self.sign.signal(reseve="attack", list_num=0): # signal:attack
            self.mudule_act.attack()
            self.sign.clear(list_num=0)

        if self.sign.signal(reseve="unique attack", list_num=1): # signal:unique attack
            self.mudule_act.attack2()
            self.sign.clear(list_num=1)

class ImageButton:
    def __init__(self, image_path, position=(0, 0), convert_alpha=False, surface=None):
        self.surface = surface or pygame.display.get_surface()

        # 이미지 경로 설정
        button_folder = "개발중\턴제 게임\graphics\\button"
        path = os.path.join(button_folder, image_path)

        # 이미지 로드
        self.image = pygame.image.load(path)
        if convert_alpha:
            self.image = self.image.convert_alpha()

        self.rect = self.image.get_rect(topleft=position)

    def draw(self):
        self.surface.blit(self.image, self.rect.topleft)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class Button:
    def __init__(self, screen, share_sign):
        self.shared_sign = share_sign

        self.attack_button = ImageButton(image_path="attack.png", position=(100, 100), surface=screen)
        self.U_attack_button = ImageButton(image_path="unique_attack.png", position=(100, 150), surface=screen)

    def button_ctrl(self, event):
        if self.attack_button.is_clicked(event): # i
            self.shared_sign.signal(send="attack", list_num=0) # siganl:attack

        if self.U_attack_button.is_clicked(event):
            self.shared_sign.signal(send="unique attack", list_num=1) # signal:unique attack

    def draws(self):
        self.attack_button.draw()
        self.U_attack_button.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((x, y))
        self.clock = pygame.time.Clock()

        self.shared_sign = Signals()
        self.shared_act = Act()

        self.module = Gain_mudule(self.shared_sign)
        self.signal_control = Signal_control(self.shared_sign, self.shared_act)

        self.button = Button(self.screen, self.shared_sign)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_1:
                        self.shared_sign.signal(send="attack", list_num=0) # signal:attack

                    if event.key == pygame.K_2:
                        self.shared_sign.signal(send="unique attack", list_num=1) # signal:unique attack

                self.button.button_ctrl(event)

            self.screen.fill("black")

            self.button.draws()
            self.signal_control.control()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
