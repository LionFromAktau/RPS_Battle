import enum
import os
import pygame
class Type(enum.Enum):
    SCISSOR = pygame.image.load(os.path.join('media', 'scissor.png'))
    ROCK = pygame.image.load(os.path.join('media', 'rock.png'))
    PAPER = pygame.image.load(os.path.join('media', 'paper.png'))