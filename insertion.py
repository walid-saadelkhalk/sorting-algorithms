from colors import HSV_to_RGB
from threading import Lock

'''
Insertion sort algorithm :
1. Start from the second element of the array.
2. Compare the second element with the first element.
3. If the second element is less than the first element, insert it at the correct position.
4. Compare the third element with the first and second elements and place it at the correct position.
5. Repeat the process until all elements are in the correct position.
'''

pygame_lock = Lock()


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