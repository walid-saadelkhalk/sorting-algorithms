from colors import *
from bubble import *
from selection import *
from combes import *
from insertion import *
from heapify import *
from merge import *
from quick import *
import pygame
import time

# Initialisation de pygame
pygame.init()
window = pygame.display.set_mode((1200, 300))
pygame.display.set_caption("Sorting Algorithms")

NUM_SECTIONS = 20
WHITE = (255, 255, 255)
font = pygame.font.Font(None, 36)
time_start = time.time()

liste_rgb = list_rgb(NUM_SECTIONS)
liste_hsv_selection, liste_hsv_bubble, liste_hsv_insertion, liste_hsv_merge, liste_hsv_quick, liste_hsv_heap, liste_hsv_combes = RGB_to_HSV(liste_rgb)

selection_sort(time_start, liste_hsv_selection, font, 'Selection', window, liste_rgb, 100, 100, 75, WHITE, NUM_SECTIONS)
bubble_sort_step(time_start, liste_hsv_bubble, font, 'Bubble', window, liste_rgb, 270, 100, 75, WHITE, NUM_SECTIONS)
insertion_sort(time_start, liste_hsv_insertion, font, 'Insertion', window, liste_rgb, 440, 100, 75, WHITE, NUM_SECTIONS)
merge_sort(time_start, liste_hsv_merge, font, 'Merge', window, liste_rgb, 610, 100, 75, WHITE, NUM_SECTIONS)
quick_sort(time_start, liste_hsv_quick, font, 'Quick', window, liste_rgb, 780, 100, 75, WHITE, NUM_SECTIONS)
heap_sort(time_start, liste_hsv_heap, font, 'Heap', window, liste_rgb, 950, 100, 75, WHITE, NUM_SECTIONS)
combes_sort(time_start, liste_hsv_combes, font, 'Combes', window, liste_rgb, 1120, 100, 75, WHITE, NUM_SECTIONS)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()