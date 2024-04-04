from colors import HSV_to_RGB

def insertion_sort(liste_hsv, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):
    n = len(liste_hsv)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            key = liste_hsv[i]
            j = i-1
            while j >= 0 and key < liste_hsv[j]:
                liste_hsv[j + 1] = liste_hsv[j]
                j -= 1
            liste_hsv[j + 1] = key
            HSV_to_RGB(liste_hsv, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)