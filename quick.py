from colors import HSV_to_RGB
from threading import Lock

# Créer un verrou
pygame_lock = Lock()


def quick_sort(liste_hsv):
    if len(liste_hsv) <= 1:
        return liste_hsv
    
    pivot = liste_hsv[len(liste_hsv) // 2]
    left = [x for x in liste_hsv if x < pivot]
    middle = [x for x in liste_hsv if x == pivot]
    right = [x for x in liste_hsv if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_step(time_start, liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):
    liste_hsv = quick_sort(liste_hsv)
    with pygame_lock:
        HSV_to_RGB(time_start, liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)