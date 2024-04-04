from colors import *
from bubble import *
from selection import *
from combes import *
import pygame

window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Sorting Algorithms")


NUM_SECTIONS = 50
WHITE = (255, 255, 255)

liste_rgb = list_rgb(NUM_SECTIONS)
liste_hsv = RGB_to_HSV(liste_rgb)


# Initialisation de pygame
pygame.init()

# Boucle principale du jeu
running = True
index = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Trier une étape de la liste si le tri n'est pas terminé
    if index < NUM_SECTIONS:
        window.fill((255, 255, 255))
        bubble_sort_step(liste_hsv, window, liste_rgb, 150, 150, 100, WHITE, NUM_SECTIONS)
        selection_sort(liste_hsv, window, liste_rgb, 450, 150, 100, WHITE, NUM_SECTIONS)
        combes_sort(liste_hsv, window, liste_rgb, 750, 150, 100, WHITE, NUM_SECTIONS)
        index += 1

pygame.quit()