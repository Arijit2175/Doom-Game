from sprite_object import *
from random import randint, random, choice

class NPC(AnimatedSprite):
    def __init__(self, game, path='assets/sprites/npc/Imp/imp_0.png', pos=(10.5, 5.5),
                 scale=0.6, shift=0.38, animation_time=180):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_images = self.get_images(self.path + '/attack')
        self.death_images = self.get_images(self.path + '/death')
        self.walk_images = self.get_images(self.path + '/walk')
        self.idle_images = self.get_images(self.path + '/idle')
        self.pain_images = self.get_images(self.path + '/pain')

        