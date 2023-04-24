import random

from type import Type
import pygame




class Model:
    def __init__(self, x_coordinate, y_coordinate):
        self.type = random.choice(list(Type))
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.x_speed, self.y_speed = 1, 1
        self.WIDTH, self.HEIGHT = 80, 60
        self.scaled_image = pygame.transform.scale(self.type.value, (self.WIDTH, self.HEIGHT))
        self.rect = pygame.Rect(self.x_coordinate, self.y_coordinate, self.WIDTH, self.HEIGHT)

    # def collision(self, second:Model):
    #     if abs(second.rect.top - self.rect.bottom) < 10 and self.y_speed > 0:
    #         self.y_speed *= -1
    #     if abs(second.rect.bottom - self.rect.top) < 10 and self.y_speed < 0:
    #         self.y_speed *= -1
    #     if abs(second.rect.right - self.rect.left) < 10 and self.x_speed < 0:
    #         self.x_speed *= -1
    #     if abs(second.rect.left - self.rect.right) < 10 and self.x_speed > 0:
    #         self.x_speed *= -1