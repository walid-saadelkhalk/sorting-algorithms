from colors import *
from bubble import *
from selection import *
from combes import *
import pygame
import threading

window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Sorting Algorithms")


NUM_SECTIONS = 1000
WHITE = (255, 255, 255)

liste_rgb = list_rgb(NUM_SECTIONS)
liste_hsv = RGB_to_HSV(liste_rgb)
index = 0
running = True


# Initialisation de pygame
pygame.init()


def bubble_sort_thread():
    global liste_hsv
    liste_hsv_bubble = bubble_sort_step(liste_hsv)
    HSV_to_RGB(liste_hsv_bubble, window, liste_rgb, 150, 150, 100, WHITE, NUM_SECTIONS)

def selection_sort_thread():
    global liste_hsv
    liste_hsv_selection = selection_sort(liste_hsv)
    HSV_to_RGB(liste_hsv_selection, window, liste_rgb, 450, 150, 100, WHITE, NUM_SECTIONS)

def combes_sort_thread():
    global liste_hsv
    liste_hsv_combes = combes_sort(liste_hsv)
    HSV_to_RGB(liste_hsv_combes, window, liste_rgb, 750, 150, 100, WHITE, NUM_SECTIONS)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Trier une étape de la liste si le tri n'est pas terminé
    if index < NUM_SECTIONS:
        # Créer et démarrer un thread pour chaque algorithme de tri
        bubble_thread = threading.Thread(target=bubble_sort_thread)
        selection_thread = threading.Thread(target=selection_sort_thread)
        combes_thread = threading.Thread(target=combes_sort_thread)

        bubble_thread.start()
        selection_thread.start()
        combes_thread.start()
        index += 1

        # Attendre que tous les threads se terminent
        bubble_thread.join()
        selection_thread.join()
        combes_thread.join()


pygame.quit()
