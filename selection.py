from colors import HSV_to_RGB
from timer import chrono
from threading import Lock

'''
Selection sort algorithm :
1. Find the minimum element in the list.
2. Swap the minimum element with the first element.
3. Repeat the process for the remaining elements.
'''

pygame_lock = Lock()

def selection_sort(time_start, liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):
    for i in range(len(liste_hsv)):
        min_index = i
        for j in range(i+1, len(liste_hsv)):
            if liste_hsv[j] < liste_hsv[min_index]:
                min_index = j
        liste_hsv[i], liste_hsv[min_index] = liste_hsv[min_index], liste_hsv[i]
        with pygame_lock:
            HSV_to_RGB(time_start,liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)
