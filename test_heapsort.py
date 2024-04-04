import pygame
import random
import math

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cercle avec camemberts")

# Fonction pour dessiner un camembert
def draw_slice(color, center, radius, start_angle, end_angle):
    rect = pygame.Rect(center[0] - radius, center[1] - radius, radius * 2, radius * 2)
    pygame.draw.arc(screen, color, rect, start_angle, end_angle, 10)

# Fonction pour convertir une couleur en valeur numérique
def color_to_value(color):
    return color[0] * 65536 + color[1] * 256 + color[2]

# Fonction pour convertir une valeur numérique en couleur
def value_to_color(value):
    blue = value % 256
    green = (value // 256) % 256
    red = value // (256 * 256)
    return (red, green, blue)

# Fonction de tri par tas pour trier les couleurs
def heapify(number_list, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and number_list[i] < number_list[l]:
        largest = l

    if r < n and number_list[largest] < number_list[r]:
        largest = r

    if largest != i:
        number_list[i], number_list[largest] = number_list[largest], number_list[i]
        heapify(number_list, n, largest)

def heap_sort(number_list):
    n = len(number_list)

    for i in range(n // 2 - 1, -1, -1):
        heapify(number_list, n, i)

    for i in range(n-1, 0, -1):
        number_list[i], number_list[0] = number_list[0], number_list[i]
        heapify(number_list, i, 0)

# Paramètres du cercle
circle_center = (width // 2, height // 2)
circle_radius = min(width, height) // 3

# Nombre de camemberts
num_slices = 100

# Génération aléatoire des couleurs
colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(num_slices)]

# Conversion des couleurs en valeurs numériques
color_values = [color_to_value(color) for color in colors]

# Tri des valeurs numériques
heap_sort(color_values)

# Conversion des valeurs triées en couleurs
sorted_colors = [value_to_color(value) for value in color_values]

# Calcul des positions des points de départ et d'arrivée de chaque camembert sur le cercle
slice_angles = [math.radians(i * (360 / num_slices)) for i in range(num_slices)]
slice_points = [(circle_center[0] + circle_radius * math.cos(angle), circle_center[1] + circle_radius * math.sin(angle)) for angle in slice_angles]

# Boucle principale
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((255, 255, 255))  # Fond blanc

    # Dessiner le cercle
    pygame.draw.circle(screen, (0, 0, 0), circle_center, circle_radius, 2)

    # Dessiner les camemberts avec les couleurs triées
    for i in range(num_slices):
        start_angle = slice_angles[i]
        end_angle = slice_angles[(i + 1) % num_slices]
        color = sorted_colors[i]
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
