import pygame
from creature import Creature
from item import Item
from slider import Slider
from random import randint
from const import *

pygame.init()
pygame.display.set_caption('Flocking Simulation')
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

factors = {
    'View Range': 150,
    'Avoid Range': 50,
    'Alignment': 0.05,
    'Cohesion': 0.005,
    'Separation': 0.05,
    'Avoidance': 0.05,
    'Seeking': 0.05,
    'Max Speed': 10
}

creatures = [Creature(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)) for _ in range(150)]
obstacles = []
foods = [Item(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)) for _ in range(3)]
sliders = []

table = [
    {'name': 'Alignment', 'min': 0, 'max': 0.1},
    {'name': 'Cohesion', 'min': 0, 'max': 0.01},
    {'name': 'Separation', 'min':0, 'max':0.1},
    {'name': 'Avoidance', 'min':0, 'max':0.1},
    {'name': 'Seeking', 'min':0, 'max':0.1},
    {'name': 'Max Speed', 'min':0, 'max':20},
]
for i, info in enumerate(table):
    sliders.append(Slider((235 + i * 250, 980), (200, 4), info['min'], info['max'], factors[info['name']], info['name']))

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if event.button == 1:
                pass
                # foods.append(Item(x, y))
            elif event.button == 3:
                obstacles.append(Item(x, y))
    
    screen.fill(COLOR_BACKGROUND)
    for creature in creatures:
        creature.update(creatures, obstacles, foods, factors)
        pygame.draw.polygon(screen, COLOR_CREATURE, creature.body_points(), 2)
    for obstacle in obstacles:
        pygame.draw.circle(screen, COLOR_OBSTACLE, (obstacle.pos.x, obstacle.pos.y), 10, 0)
    for food in foods:
        pygame.draw.circle(screen, COLOR_FOOD, (food.pos.x, food.pos.y), 10, 0)

    mouse = pygame.mouse.get_pos()

    for slider in sliders:
        slider.draw(screen)
        factors[slider.name] = slider.get_value()

    pygame.display.update()

