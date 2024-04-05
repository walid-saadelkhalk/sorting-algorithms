from colors import HSV_to_RGB
from threading import Lock

'''
Bubble sort algorithm : 
1. Start from the first element, compare it with the next element of the array.
2. If the first element is greater than the next element of the array, swap them.
3. If the first element is less than the next element, move to the next element.
'''


pygame_lock = Lock()

def bubble_sort_step(time_start, liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):
    n = len(liste_hsv)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if abs(liste_hsv[j][0] - liste_hsv[j + 1][0]) > 180:
                liste_hsv[j], liste_hsv[j + 1] = liste_hsv[j + 1], liste_hsv[j]
            elif liste_hsv[j][0] > liste_hsv[j + 1][0]:
                liste_hsv[j], liste_hsv[j + 1] = liste_hsv[j + 1], liste_hsv[j]
            with pygame_lock:
                HSV_to_RGB(time_start,liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)
