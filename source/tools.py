import os
import pygame as pg
from abc import ABC, abstractmethod

keybinding = {"action": pg.K_s, "jump": pg.K_SPACE, "left": pg.K_LEFT, "right": pg.K_RIGHT, "down": pg.K_DOWN}

class State():
    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.next = None
        self.persist = {}

    @abstractmethod
    def startup(self, current_time, persist):
        '''abstract method'''

    def cleanup(self):
        self.done = False
        return self.persist

    @abstractmethod
    def update(self, surface, keys, current_time):
        '''abstract method'''

class Control():
    pass