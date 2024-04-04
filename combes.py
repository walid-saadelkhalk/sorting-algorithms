from colors import HSV_to_RGB
from timer import chrono

def combes_sort(time_start, liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):
    """
    Trie une étape de la liste par le tri de Combes
    """
    seconds = chrono(time_start)
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
        HSV_to_RGB(seconds, liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)