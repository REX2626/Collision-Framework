import sys
from time import perf_counter
import objects
import pygame

pygame.init()

WIN = pygame.display.set_mode((1200, 800))

delta_time = 1
while True:
    time1 = perf_counter()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    time2 = perf_counter()
    delta_time = time2 - time1