from colors import HSV_to_RGB
from threading import Lock

'''
Quick sort algorithm :
1. Choose a pivot element from the list.
2. Partition the list such that all elements less than the pivot are on the left and all elements greater than the pivot are on the right.
3. Recursively sort the left and right sublists.
4. Combine the sorted sublists.
'''


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