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

# Couleurs avec leur longueur d'onde dans le spectre visible
colors = {
    "VIOLET": (138, 43, 226),   # ~420-450 nm (Ultraviolet)
    "BLEU": (0, 0, 255),         # ~450-495 nm
    "CYAN": (0, 255, 255),       # ~495-570 nm
    "VERT": (0, 255, 0),         # ~570-590 nm
    "JAUNE": (255, 255, 0),      # ~590-620 nm
    "ORANGE": (255, 165, 0),     # ~620-750 nm
    "ROUGE": (255, 0, 0)         # ~620-750 nm (Infrarouge)
}

# Fonction pour trier les couleurs en fonction de leur longueur d'onde
def sort_colors_by_wavelength(colors):
    # Trier les couleurs en fonction de la longueur d'onde (croissante)
    sorted_colors = sorted(colors.items(), key=lambda item: wavelength_range(item[0]))
    return [color[1] for color in sorted_colors]

# Définir la plage de longueur d'onde pour chaque couleur
def wavelength_range(color):
    if color == "VIOLET":
        return 420
    elif color == "BLEU":
        return 470
    elif color == "CYAN":
        return 525
    elif color == "VERT":
        return 580
    elif color == "JAUNE":
        return 605
    elif color == "ORANGE":
        return 665
    elif color == "ROUGE":
        return 700

# Tri des couleurs par longueur d'onde
sorted_colors = sort_colors_by_wavelength(colors)

# Paramètres du cercle
circle_center = (width // 2, height // 2)
circle_radius = min(width, height) // 3

# Nombre de camemberts
num_slices = 100

# Calcul des positions des points de départ et d'arrivée de chaque camembert
slice_angles = [math.radians(i * (360 / num_slices)) for i in range(num_slices)]
slice_points = [(circle_center[0] + circle_radius * math.cos(angle), circle_center[1] + circle_radius * math.sin(angle)) for angle in slice_angles]
slice_colors = random.choices(sorted_colors, k=num_slices)  # Choix aléatoire des couleurs triées

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

# Tri des camemberts
def insertion_sort_color(color_list):
    for i in range(1, len(color_list)):
        key = color_list[i]
        j = i - 1
        while j >= 0 and sorted_colors.index(color_list[j]) > sorted_colors.index(key):
            color_list[j + 1] = color_list[j]
            j -= 1
            # Affichage à l'écran après chaque échange
            draw_slices()
            time.sleep(0.01)
        color_list[j + 1] = key

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

# Tri des couleurs des camemberts par longueur d'onde
insertion_sort_color(slice_colors)

# Exécution du programme
if __name__ == "__main__":
    draw_slices()  # Dessiner les camemberts avant de commencer à trier
    main()  # Lancer la boucle principale
