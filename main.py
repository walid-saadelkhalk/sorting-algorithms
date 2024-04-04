import pygame
import random
import math

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cercle avec camemberts")

# Couleurs
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Paramètres du cercle
circle_center = (width // 2, height // 2)
circle_radius = min(width, height) // 3

# Nombre de camemberts
num_slices = 2000

# Calcul des positions des points de départ et d'arrivée de chaque camembert
slice_angles = [math.radians(i * (360 / num_slices)) for i in range(num_slices)]
slice_points = [(circle_center[0] + circle_radius * math.cos(angle), circle_center[1] + circle_radius * math.sin(angle)) for angle in slice_angles]
slice_colors = [random.choice([YELLOW, RED, BLUE]) for _ in range(num_slices)]

# Fonction principale
def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill((255, 255, 255))  # Fond blanc

        # Dessiner le cercle
        pygame.draw.circle(screen, (0, 0, 0), circle_center, circle_radius, 2)

        # Dessiner les camemberts
        for i in range(num_slices):
            start_angle = slice_angles[i]
            end_angle = slice_angles[(i + 1) % num_slices]
            color = slice_colors[i]
            start_point = circle_center
            end_point = slice_points[i]

            pygame.draw.arc(screen, color, (circle_center[0]-circle_radius, circle_center[1]-circle_radius, circle_radius*2, circle_radius*2), start_angle, end_angle, circle_radius)

        # Rafraîchir l'écran
        pygame.display.flip()

        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(60)

    pygame.quit()

main()
