from colors import *
from bubble import *
from selection import *
from combes import *
from insertion import *
from heapify import *
from merge import *
from quick import *
import pygame

window = pygame.display.set_mode((1200, 300))
pygame.display.set_caption("Sorting Algorithms")


NUM_SECTIONS = 20
WHITE = (255, 255, 255)

liste_rgb = list_rgb(NUM_SECTIONS)
liste_hsv_selection, liste_hsv_bubble, liste_hsv_insertion, liste_hsv_merge, liste_hsv_quick, liste_hsv_heap, liste_hsv_combes = RGB_to_HSV(liste_rgb)

# Initialisation de pygame
pygame.init()

selection_sort(liste_hsv_selection, window, liste_rgb, 100, 100, 75, WHITE, NUM_SECTIONS)
bubble_sort_step(liste_hsv_bubble, window, liste_rgb, 270, 100, 75, WHITE, NUM_SECTIONS)
insertion_sort(liste_hsv_insertion, window, liste_rgb, 440, 100, 75, WHITE, NUM_SECTIONS)
merge_sort(liste_hsv_merge, window, liste_rgb, 610, 100, 75, WHITE, NUM_SECTIONS)
quick_sort(liste_hsv_quick, window, liste_rgb, 780, 100, 75, WHITE, NUM_SECTIONS)
heap_sort(liste_hsv_heap, window, liste_rgb, 950, 100, 75, WHITE, NUM_SECTIONS)
combes_sort(liste_hsv_combes, window, liste_rgb, 1120, 100, 75, WHITE, NUM_SECTIONS)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()