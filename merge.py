from colors import HSV_to_RGB

from threading import Lock

# Créer un verrou
pygame_lock = Lock()

def merge_sort(liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):
    n = len(liste_hsv)
    if n > 1:
        mid = n // 2
        left_half = liste_hsv[:mid]
        right_half = liste_hsv[mid:]

        merge_sort(left_half, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)
        merge_sort(right_half, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                liste_hsv[k] = left_half[i]
                with pygame_lock:
                    HSV_to_RGB(liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)
                i += 1
            else:
                liste_hsv[k] = right_half[j]
                with pygame_lock:
                    HSV_to_RGB(liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)
                j += 1
            k += 1

        while i < len(left_half):
            liste_hsv[k] = left_half[i]
            with pygame_lock:
                HSV_to_RGB(liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)
            i += 1
            k += 1

        while j < len(right_half):
            liste_hsv[k] = right_half[j]
            with pygame_lock:
                HSV_to_RGB(liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)
            j += 1
            k += 1

