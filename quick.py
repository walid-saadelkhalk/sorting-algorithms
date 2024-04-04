from colors import HSV_to_RGB

def quick_sort(liste_hsv, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):
    n = len(liste_hsv)
    if n <= 1:
        return liste_hsv  # Cas de base : liste de taille 0 ou 1
    
    pivot = liste_hsv[n // 2]
    left = [x for x in liste_hsv if x < pivot]
    middle = [x for x in liste_hsv if x == pivot]
    right = [x for x in liste_hsv if x > pivot]

    # Appels récursifs de quick_sort pour trier les partitions gauche et droite
    left_sorted = quick_sort(left, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)
    right_sorted = quick_sort(right, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)

    # Concaténation des partitions triées et du pivot
    liste_hsv = left_sorted + middle + right_sorted
    
    # Conversion HSV en RGB
    HSV_to_RGB(liste_hsv, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)