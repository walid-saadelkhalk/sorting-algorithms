import pygame
import random
import math

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cercle avec camemberts")

circle_center = (width // 2, height // 2)
circle_radius = min(width, height) // 3
num_slices = 100
colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(num_slices)]

red_group = sorted([color for color in colors], key=lambda x: x[0])
green_group = sorted([color for color in colors], key=lambda x: x[1])
blue_group = sorted([color for color in colors], key=lambda x: x[2])
sorted_colors = red_group + green_group + blue_group

def draw_slices(color_list):
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), circle_center, circle_radius, 2)
    for i, color in enumerate(color_list):
        start_angle = math.radians(i * (360 / num_slices))
        end_angle = math.radians((i + 1) * (360 / num_slices))
        pygame.draw.arc(screen, color, (circle_center[0] - circle_radius, circle_center[1] - circle_radius, circle_radius * 2, circle_radius * 2), start_angle, end_angle, circle_radius)
    pygame.display.flip()

def insertion_sort_color(color_list):
    for i in range(1, len(color_list)):
        key = color_list[i]
        j = i - 1
        while j >= 0 and sum(key) < sum(color_list[j]):
            color_list[j + 1] = color_list[j]
            j -= 1
        color_list[j + 1] = key

insertion_sort_color(sorted_colors)
draw_slices(sorted_colors)

def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(60)

    pygame.quit()

main()
