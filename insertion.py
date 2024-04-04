from colors import HSV_to_RGB
from threading import Lock

# Créer un verrou
pygame_lock = Lock()
from timer import chrono

def insertion_sort(time_start, liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):
    n = len(liste_hsv)
    for i in range(n):
        for j in range(0, n - i):
            key = liste_hsv[i]
            j = i-1
            while j >= 0 and key < liste_hsv[j]:
                liste_hsv[j + 1] = liste_hsv[j]
                j -= 1
            liste_hsv[j + 1] = key
            with pygame_lock:
                HSV_to_RGB(time_start, liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)