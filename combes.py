from colors import HSV_to_RGB
from threading import Lock

'''
Combes sort algorithm :
The Comb sort algorithm is an improvement over the Bubble sort algorithm.
1. The Comb sort algorithm improves on the Bubble sort algorithm by using a gap of size more than 1.
2. The gap starts with a large value and shrinks by a factor of 1.3 in every iteration until it reaches 1.
3. Compares elements that are far apart and then reduces the gap between them.
4. Swaps elements if they are in the wrong order.
5. Repeats the process until the gap becomes 1 and no swaps are needed.
'''

pygame_lock = Lock()

def combes_sort(time_start, liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):

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
