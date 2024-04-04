from colors import *
from bubble import *
from selection import *
from combes import *
import pygame
import time

window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Sorting Algorithms")


NUM_SECTIONS = 1000
WHITE = (255, 255, 255)

liste_rgb = list_rgb(NUM_SECTIONS)
liste_hsv = RGB_to_HSV(liste_rgb)


# Initialisation de pygame
pygame.init()

# Boucle principale du jeu
running = True
index = 0
clock = pygame.time.Clock()
draw_sorting(window, liste_rgb, 150, 150, 100, WHITE, NUM_SECTIONS)
draw_sorting(window, liste_rgb, 450, 150, 100, WHITE, NUM_SECTIONS)
draw_sorting(window, liste_rgb, 750, 150, 100, WHITE, NUM_SECTIONS)
liste_hsv_bubble = bubble_sort_step(liste_hsv)
HSV_to_RGB(liste_hsv_bubble, window, liste_rgb, 150, 150, 100, WHITE, NUM_SECTIONS)
liste_hsv_selection = selection_sort(liste_hsv)
HSV_to_RGB(liste_hsv_selection, window, liste_rgb, 450, 150, 100, WHITE, NUM_SECTIONS)
liste_hsv_combes = combes_sort(liste_hsv)
HSV_to_RGB(liste_hsv_combes, window, liste_rgb, 750, 150, 100, WHITE, NUM_SECTIONS)
index += 1 


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Trier une étape de la liste si le tri n'est pas terminé

    clock.tick(60)
pygame.quit()

