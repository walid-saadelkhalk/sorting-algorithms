from colors import HSV_to_RGB
from timer import chrono

def insertion_sort(time_start, liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):
    seconds = chrono(time_start)
    n = len(liste_hsv)
    for i in range(n):
        for j in range(0, n - i):
            key = liste_hsv[i]
            j = i-1
            while j >= 0 and key < liste_hsv[j]:
                liste_hsv[j + 1] = liste_hsv[j]
                j -= 1
            liste_hsv[j + 1] = key
            HSV_to_RGB(seconds, liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)