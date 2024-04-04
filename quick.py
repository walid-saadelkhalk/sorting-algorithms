from colors import HSV_to_RGB

def quick_sort(liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):
    n = len(liste_hsv)
    if n <= 1:
        return liste_hsv  # Cas de base : liste de taille 0 ou 1
    
    pivot = liste_hsv[n // 2]
    left = [x for x in liste_hsv if x < pivot]
    middle = [x for x in liste_hsv if x == pivot]
    right = [x for x in liste_hsv if x > pivot]

    # Appels récursifs de quick_sort pour trier les partitions gauche et droite
    left_sorted = quick_sort(left, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)
    right_sorted = quick_sort(right, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)

    # Vérifier si la partition gauche est vide
    if left_sorted is None:
        left_sorted = []

    # Vérifier si la partition droite est vide
    if right_sorted is None:
        right_sorted = []

    # Concaténation des partitions triées et du pivot
    liste_hsv = left_sorted + middle + right_sorted
    
    # Conversion HSV en RGB
    HSV_to_RGB(liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)