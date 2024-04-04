from colors import HSV_to_RGB
from threading import Lock

# Créer un verrou
pygame_lock = Lock()

def combes_sort(time_start, liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):
    """
    Trie une étape de la liste par le tri de Combes
    """
    n = len(liste_hsv)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = max(1, int(gap / 1.3))
        swapped = False
        for i in range(n - gap):
            if liste_hsv[i] > liste_hsv[i + gap]:
                liste_hsv[i], liste_hsv[i + gap] = liste_hsv[i + gap], liste_hsv[i]
                swapped = True
        with pygame_lock:
            HSV_to_RGB(time_start,liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)
