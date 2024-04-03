from sortinganth import *
import pygame
import random

HEIGHT = 600
WIDTH = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithms")

def list_red():
    liste_red = []  # Définissez localement la liste liste_red
    for i in range(10):
        liste_red.append(random.randint(0, 255))
    return liste_red

def list_blue():
    liste_blue = []  # Définissez localement la liste liste_blue
    for i in range(10):
        liste_blue.append(random.randint(0, 255))
    return liste_blue

def list_green():
    liste_green = []  # Définissez localement la liste liste_green
    for i in range(10):
        liste_green.append(random.randint(0, 255))
    return liste_green

def list_rgb():
    liste_rgb = []
    liste_red = list_red()
    liste_blue = list_blue()
    liste_green = list_green()
    for i in range(10):
        liste_rgb.append((liste_red[i], liste_blue[i], liste_green[i]))
    return liste_rgb

liste_rgb = list_rgb()
liste_hsv = RGB_to_HSV(liste_rgb)

WHITE = (255, 255, 255)
NUM_SECTIONS = 10

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
        liste_hsv = bubble_sort_step(liste_hsv)
        HSV_to_RGB(liste_hsv, liste_rgb, window, WIDTH, HEIGHT, WHITE, NUM_SECTIONS)
        index += 1

    pygame.quit()