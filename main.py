import os.path
import sys

import pygame
from models import Model
from type import Type
import random

WIDTH, HEIGHT = 1500, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 40
WHITE = (255, 255, 255)

objects = []
num_objects = random.randint(25, 80)

for i in range(num_objects):
    o = Model(random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50))
    objects.append(o)


def changeImage(first:Model, second:Model):
    for i in list(Type):
        if i.name == second.type.name:
            first.type = i
    first.scaled_image = pygame.transform.scale(first.type.value, (second.WIDTH, second.HEIGHT))
def change(first:Model, second: Model):
    if first.type == Type.ROCK:
        if second.type == Type.PAPER:
            changeImage(first, second)
        elif second.type == Type.SCISSOR:
            changeImage(second, first)
    elif first.type == Type.PAPER:
        if second.type == Type.SCISSOR:
            changeImage(first, second)
        elif second.type == Type.ROCK:
            changeImage(second, first)
    elif first.type == Type.SCISSOR:
        if second.type == Type.ROCK:
            changeImage(first, second)
        elif second.type == Type.PAPER:
            changeImage(second, first)
def collision(first: Model, second:Model):
    if abs(second.rect.top - first.rect.bottom) < 10 and first.y_speed > 0:
         first.y_speed *= -1
    if abs(second.rect.bottom - first.rect.top) < 10 and first.y_speed < 0:
        first.y_speed *= -1
    if abs(second.rect.right - first.rect.left) < 10 and first.x_speed < 0:
         first.x_speed *= -1
    if abs(second.rect.left - first.rect.right) < 10 and first.x_speed > 0:
        first.x_speed *= -1

def draw():
    for i in range(num_objects):
        o = objects[i]
        o.rect.x += o.x_speed
        o.rect.y += o.y_speed
        if o.rect.right >= WIDTH or o.rect.left <= 0:
            o.x_speed *= -1
        if o.rect.bottom >= HEIGHT or o.rect.top <= 0:
            o.y_speed *= -1
        for j in range(i + 1, num_objects):
            second = objects[j]
            if o.rect.colliderect(second.rect):
                change(o, second)
                collision(o, second)
                collision(second, o)
        WINDOW.blit(o.scaled_image, (o.rect.x, o.rect.y))
    pygame.display.update()


pygame.mixer.init()
pygame.mixer.music.load(os.path.join('media', 'music.mp3'))
pygame.mixer.music.play(loops=-1)

while True:
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        clock.tick(FPS)
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
    WINDOW.fill(WHITE)
    draw()
