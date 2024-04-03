import pygame
import math

def RGB_to_HSV(list_rgb):
    list_hsv = []
    for r, g, b in list_rgb:
        r, g, b = r / 255, g / 255, b / 255
        cmax = max(r, g, b)
        cmin = min(r, g, b)
        delta = cmax - cmin
        if delta == 0:
            h = 0
        elif cmax == r:
            h = 60 * (((g - b) / delta) % 6)
        elif cmax == g:
            h = 60 * ((b - r) / delta + 2)
        elif cmax == b:
            h = 60 * ((r - g) / delta + 4)
        if cmax == 0:
            s = 0
        else:
            s = 1
        v = cmax
        list_hsv.append((h, s, v))
    return list_hsv

def HSV_to_RGB(liste_hsv, liste_rgb, window, WIDTH, HEIGHT, WHITE, NUM_SECTIONS):
    liste_rgb.clear()
    for h, s, v in liste_hsv:
        c = v * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = v - c
        if 0 <= h < 60:
            r, g, b = c, x, 0
        elif 60 <= h < 120:
            r, g, b = x, c, 0
        elif 120 <= h < 180:
            r, g, b = 0, c, x
        elif 180 <= h < 240:
            r, g, b = 0, x, c
        elif 240 <= h < 300:
            r, g, b = x, 0, c
        elif 300 <= h < 360:
            r, g, b = c, 0, x
        liste_rgb.append((int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)))
        draw_sorting(window, liste_rgb, WIDTH, HEIGHT, WHITE, NUM_SECTIONS)

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

def draw_sorting(window, liste_rgb, WIDTH, HEIGHT, WHITE, NUM_SECTIONS):
    window.fill((0, 0, 0))
    # Paramètres du cercle
    circle_center = (WIDTH // 2, HEIGHT // 2)
    circle_radius = min(WIDTH, HEIGHT) // 3
    # Ajuster la taille de liste_rgb pour correspondre à NUM_SECTIONS
    liste_rgb = liste_rgb[:NUM_SECTIONS]
    # Calcul des positions des points de départ et d'arrivée de chaque camembert
    slice_angles = [math.radians(i * (360 / NUM_SECTIONS)) for i in range(NUM_SECTIONS)]
    slice_points = [(circle_center[0] + circle_radius * math.cos(angle), circle_center[1] + circle_radius * math.sin(angle)) for angle in slice_angles]
    # Dessiner les camemberts
    for i in range(len(liste_rgb)):  # Utilisez la longueur de liste_rgb
        start_angle = slice_angles[i]
        end_angle = slice_angles[(i + 1) % NUM_SECTIONS]
        color_rgb = liste_rgb[i]  # Récupérer la couleur RVB à partir de liste_rgb
        # Convertir la couleur RVB en tuple d'entiers
        color_tuple = (int(color_rgb[0]), int(color_rgb[1]), int(color_rgb[2]))
        # Dessiner le camembert avec la couleur spécifiée
        pygame.draw.arc(window, color_tuple, (circle_center[0]-circle_radius, circle_center[1]-circle_radius, circle_radius*2, circle_radius*2), start_angle, end_angle, circle_radius)
    pygame.display.update()
        