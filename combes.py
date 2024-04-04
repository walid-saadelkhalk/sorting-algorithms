from colors import HSV_to_RGB

def combes_sort(liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):
    """
    Trie une étape de la liste par le tri de Combes
    """
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
        HSV_to_RGB(liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)