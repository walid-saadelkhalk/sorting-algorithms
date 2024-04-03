import cv2
import numpy as np
import random

def list_red():
    liste_red = []  # Définissez localement la liste liste_red
    for i in range(100):
        liste_red.append(random.randint(0, 255))
    return liste_red

def list_blue():
    liste_blue = []  # Définissez localement la liste liste_blue
    for i in range(100):
        liste_blue.append(random.randint(0, 255))
    return liste_blue

def list_green():
    liste_green = []  # Définissez localement la liste liste_green
    for i in range(100):
        liste_green.append(random.randint(0, 255))
    return liste_green

def list_rgb():
    liste_rgb = []
    liste_red = list_red()
    liste_blue = list_blue()
    liste_green = list_green()
    for i in range(100):
        liste_rgb.append((liste_red[i], liste_blue[i], liste_green[i]))
    return liste_rgb

liste_rgb = list_rgb()

def rgb_to_hsv(rgb):
    r, g, b = rgb
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    hsv = cv2.cvtColor(np.uint8([[[(b, g, r)]]]), cv2.COLOR_BGR2HSV)[0][0]
    return hsv[0], hsv[1], hsv[2]

# # Liste des couleurs RGB
# liste_rgb = [(0, 146, 194), (2, 78, 63), (17, 5, 198)]

# Convertir les couleurs RGB en couleurs HSV et trier par teinte
liste_hsv = [rgb_to_hsv(rgb) for rgb in liste_rgb]
liste_hsv_sorted = sorted(liste_hsv, key=lambda x: x[0])

# Convertir les couleurs HSV triées en couleurs RGB
liste_rgb_sorted = [cv2.cvtColor(np.uint8([[[h, s, v]]]), cv2.COLOR_HSV2RGB)[0][0] for h, s, v in liste_hsv_sorted]

print(liste_rgb_sorted)