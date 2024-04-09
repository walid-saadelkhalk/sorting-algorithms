import pygame
import math
import threading
from timer import chrono

draw_lock = threading.Lock()

def draw_sorting(time_start, font, message, window, liste_rgb, a, b, radius, WHITE, NUM_SECTIONS):
    with draw_lock:
        sort_message = font.render(message, True, (255,255,255))
        sort_rect = sort_message.get_rect()
        sort_rect.center = (a, b + radius + 20)
    
    seconds = chrono(time_start)
    time_message = font.render(str(seconds), True, (255,255,255))
    time_rect = time_message.get_rect()
    time_rect.center = (a, b + radius + 80)

    window.fill((0, 0, 0), time_rect)
    
    # Paramètres du cercle
    circle_center = (a, b)
    circle_radius = radius

    window.blit(sort_message, sort_rect)
    window.blit(time_message, time_rect)

    pygame.draw.circle(window, WHITE, circle_center, circle_radius, 1)
    # Ajuster la taille de liste_rgb pour correspondre à NUM_SECTIONS
    liste_rgb = liste_rgb[:NUM_SECTIONS]
    # Calcul des positions des points de départ et d'arrivée de chaque camembert
    slice_angles = [math.radians(i * (360 / NUM_SECTIONS)) for i in range(NUM_SECTIONS)]
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