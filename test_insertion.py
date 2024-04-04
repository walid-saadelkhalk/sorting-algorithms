import pygame
import random
import math
import time

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cercle avec camemberts")

# Couleurs
GREEN = (0, 255, 0)
RED = (255, 0, 0) 
BLUE = (0, 0, 255)
# Paramètres du cercle
circle_center = (width // 2, height // 2)
circle_radius = min(width, height) // 3

# Nombre de camemberts
num_slices = 200

# Calcul des positions des points de départ et d'arrivée de chaque camembert
slice_angles = [math.radians(i * (360 / num_slices)) for i in range(num_slices)]
slice_points = [(circle_center[0] + circle_radius * math.cos(angle), circle_center[1] + circle_radius * math.sin(angle)) for angle in slice_angles]
slice_colors = [random.choice([GREEN, RED, BLUE]) for _ in range(num_slices)]

# Tri des couleurs par insertion
def insertion_sort_color(color_list):
    for i in range(1, len(color_list)):
        key = color_list[i]
        j = i - 1
        while j >= 0 and color_priority(color_list[j]) > color_priority(key):
            color_list[j + 1] = color_list[j]
            j -= 1
            # Affichage à l'écran après chaque échange
            draw_slices()
            time.sleep(0.01)
        color_list[j + 1] = key

# Définir la priorité des couleurs
def color_priority(color):
    if color == GREEN:
        return 0
    elif color == RED:
        return 1
    elif color == BLUE:
        return 2

# Dessiner les camemberts
def draw_slices():
    screen.fill((255, 255, 255))  # Fond blanc
    pygame.draw.circle(screen, (0, 0, 0), circle_center, circle_radius, 2)
    for i in range(num_slices):
        start_angle = slice_angles[i]
        end_angle = slice_angles[(i + 1) % num_slices]
        color = slice_colors[i]
        pygame.draw.arc(screen, color, (circle_center[0]-circle_radius, circle_center[1]-circle_radius, circle_radius*2, circle_radius*2), start_angle, end_angle, circle_radius)
    pygame.display.flip()

# Tri des couleurs
insertion_sort_color(slice_colors)

# Fonction principale
def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(60)

    pygame.quit()

main()


# total_list = [range(len(red)), range(len(green)), range(len(blue))]