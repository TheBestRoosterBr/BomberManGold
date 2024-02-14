import random

import pygame

from Configuration import Configuration


class Particle:
    def __init__(self, position):
        self.position = [position[0], position[1]]
        self.color = (255, 0, 0)

        self.direction = (random.randint(0, 30), random.randint(0, 30))
        self.size = (3, 3)

    def update(self):
        self.position[0] += self.direction[0] - 15
        self.position[1] += self.direction[1] - 15

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1]))



class SangueAnimation:
    def __init__(self, position):
        self.life_time = Configuration.get_config().game_fps * 4
        self.time = 0

        self.particles = []
        for i in range(100):
            self.particles.append(Particle(position))

    def update(self, screen):
        self.time += 1
        if self.time >= self.life_time:
            self.particles.clear()
            return True
        for particle in self.particles:
            particle.update()
            particle.draw(screen)

        return False
