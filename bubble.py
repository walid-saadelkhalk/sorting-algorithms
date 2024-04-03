def bubble_sort_step(liste_hsv):
    n = len(liste_hsv)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            # Comparaison tenant compte de la différence circulaire entre les valeurs de teinte
            if abs(liste_hsv[j][0] - liste_hsv[j + 1][0]) > 180:
                # Si la différence circulaire est supérieure à 180 degrés, échangez les valeurs
                liste_hsv[j], liste_hsv[j + 1] = liste_hsv[j + 1], liste_hsv[j]
            elif liste_hsv[j][0] > liste_hsv[j + 1][0]:
                # Sinon, comparez directement les valeurs de teinte
                liste_hsv[j], liste_hsv[j + 1] = liste_hsv[j + 1], liste_hsv[j]
    return liste_hsv