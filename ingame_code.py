"""원하는 단어 찾기 = f3, 기호 전체이름 바꾸기 = ctrl + f2"""

import pygame, sys, os
from sign import *
from load import Load

class externae_mudule:
    def __init__(self):
        self.module_load = Load()
        self.sign = Signals()

class Act(externae_mudule):
    def __init__(self):
        super().__init__()

    def attack(self):
        print("attack")

    def attack2(self):
        print("attack2")

class Ally(externae_mudule):
    def __init__(self):
        super().__init__()


class Enermy(externae_mudule):
    def __init__(self):
        super().__init__()

