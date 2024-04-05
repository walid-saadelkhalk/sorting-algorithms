from colors import HSV_to_RGB
from threading import Lock

'''
Merge sort algorithm :
1. Divide the list into two halves.
2. Divide the two halves into two halves.
3. Repeat the process until all elements are divided into individual elements.
4. Sort the elements of the first half and the second half.
5. Merge the sorted halves.
6. Repeat the process until all elements are merged into a single sorted list.
'''


pygame_lock = Lock()

def merge_sort(time_start, liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):
    n = len(liste_hsv)
    if n > 1:
        mid = n // 2
        left_half = liste_hsv[:mid]
        right_half = liste_hsv[mid:]

        merge_sort(time_start, left_half, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)
        merge_sort(time_start, right_half, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                liste_hsv[k] = left_half[i]
                with pygame_lock:
                    HSV_to_RGB(time_start,liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)
                i += 1
            else:
                liste_hsv[k] = right_half[j]
                with pygame_lock:
                    HSV_to_RGB(time_start,liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)
                j += 1
            k += 1

        while i < len(left_half):
            liste_hsv[k] = left_half[i]
            with pygame_lock:
                HSV_to_RGB(time_start,liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)
            i += 1
            k += 1

        while j < len(right_half):
            liste_hsv[k] = right_half[j]
            with pygame_lock:
                HSV_to_RGB(time_start,liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)
            j += 1
            k += 1

