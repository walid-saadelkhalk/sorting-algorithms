from colors import *
from bubble import *
from selection import *
from combes import *
from insertion import *
from heapify import *
from merge import *
from quick import *
import pygame
import threading
import time

# Initialisation de pygame
pygame.init()
window = pygame.display.set_mode((1200, 300))
pygame.display.set_caption("Sorting Algorithms")

NUM_SECTIONS = 20
WHITE = (255, 255, 255)
font = pygame.font.Font(None, 36)

liste_rgb = list_rgb(NUM_SECTIONS)
liste_hsv_selection, liste_hsv_bubble, liste_hsv_insertion, liste_hsv_merge, liste_hsv_quick, liste_hsv_heap, liste_hsv_combes = RGB_to_HSV(liste_rgb)


running = True

# Créer et démarrer un thread pour chaque algorithme de tri
# selection_thread = threading.Thread(target=selection_sort(liste_hsv_selection, font, 'Selection', window, liste_rgb, 100, 100, 75, WHITE, NUM_SECTIONS))
# bubble_thread = threading.Thread(target=bubble_sort_step(liste_hsv_bubble, font, 'Bubble', window, liste_rgb, 270, 100, 75, WHITE, NUM_SECTIONS))
# combes_thread = threading.Thread(target=combes_sort(liste_hsv_combes, font, 'Combes', window, liste_rgb, 1120, 100, 75, WHITE, NUM_SECTIONS))
# insertion_thread = threading.Thread(target=insertion_sort(liste_hsv_insertion, font, 'Insertion', window, liste_rgb, 440, 100, 75, WHITE, NUM_SECTIONS))
# merge_thread = threading.Thread(target=merge_sort(liste_hsv_merge, font, 'Merge', window, liste_rgb, 610, 100, 75, WHITE, NUM_SECTIONS))
# quick_thread = threading.Thread(target=quick_sort(liste_hsv_quick, font, 'Quick', window, liste_rgb, 780, 100, 75, WHITE, NUM_SECTIONS))
# heap_thread = threading.Thread(target=heap_sort(liste_hsv_heap, font, 'Heap', window, liste_rgb, 950, 100, 75, WHITE, NUM_SECTIONS))

# selection_thread = threading.Thread(target=selection_sort, args=(liste_hsv_selection, font, 'Selection', window, liste_rgb, 100, 100, 75, WHITE, NUM_SECTIONS))
# bubble_thread = threading.Thread(target=bubble_sort_step, args=(liste_hsv_bubble, font, 'Bubble', window, liste_rgb, 270, 100, 75, WHITE, NUM_SECTIONS))
# combes_thread = threading.Thread(target=combes_sort, args=(liste_hsv_combes, font, 'Combes', window, liste_rgb, 1120, 100, 75, WHITE, NUM_SECTIONS))
# insertion_thread = threading.Thread(target=insertion_sort, args=(liste_hsv_insertion, font, 'Insertion', window, liste_rgb, 440, 100, 75, WHITE, NUM_SECTIONS))
# merge_thread = threading.Thread(target=merge_sort, args=(liste_hsv_merge, font, 'Merge', window, liste_rgb, 610, 100, 75, WHITE, NUM_SECTIONS))
# quick_thread = threading.Thread(target=quick_sort, args=(liste_hsv_quick, font, 'Quick', window, liste_rgb, 780, 100, 75, WHITE, NUM_SECTIONS))
# heap_thread = threading.Thread(target=heap_sort, args=(liste_hsv_heap, font, 'Heap', window, liste_rgb, 950, 100, 75, WHITE, NUM_SECTIONS))

# from functools import partial

selection_thread = threading.Thread(target=lambda: selection_sort(liste_hsv_selection, font, 'Selection', window, liste_rgb, 100, 100, 75, WHITE, NUM_SECTIONS))
bubble_thread = threading.Thread(target=lambda: bubble_sort_step(liste_hsv_bubble, font, 'Bubble', window, liste_rgb, 270, 100, 75, WHITE, NUM_SECTIONS))
combes_thread = threading.Thread(target=lambda: combes_sort(liste_hsv_combes, font, 'Combes', window, liste_rgb, 1120, 100, 75, WHITE, NUM_SECTIONS))
insertion_thread = threading.Thread(target=lambda: insertion_sort(liste_hsv_insertion, font, 'Insertion', window, liste_rgb, 440, 100, 75, WHITE, NUM_SECTIONS))
merge_thread = threading.Thread(target=lambda: merge_sort(liste_hsv_merge, font, 'Merge', window, liste_rgb, 610, 100, 75, WHITE, NUM_SECTIONS))
quick_thread = threading.Thread(target=lambda: quick_sort(liste_hsv_quick, font, 'Quick', window, liste_rgb, 780, 100, 75, WHITE, NUM_SECTIONS))
heap_thread = threading.Thread(target=lambda: heap_sort(liste_hsv_heap, font, 'Heap', window, liste_rgb, 950, 100, 75, WHITE, NUM_SECTIONS))

# selection_thread = threading.Thread(target=partial(selection_sort, liste_hsv_selection, font, 'Selection', window, liste_rgb, 100, 100, 75, WHITE, NUM_SECTIONS))
# bubble_thread = threading.Thread(target=partial(bubble_sort_step, liste_hsv_bubble, font, 'Bubble', window, liste_rgb, 270, 100, 75, WHITE, NUM_SECTIONS))
# combes_thread = threading.Thread(target=partial(combes_sort, liste_hsv_combes, font, 'Combes', window, liste_rgb, 1120, 100, 75, WHITE, NUM_SECTIONS))
# insertion_thread = threading.Thread(target=partial(insertion_sort, liste_hsv_insertion, font, 'Insertion', window, liste_rgb, 440, 100, 75, WHITE, NUM_SECTIONS))
# merge_thread = threading.Thread(target=partial(merge_sort, liste_hsv_merge, font, 'Merge', window, liste_rgb, 610, 100, 75, WHITE, NUM_SECTIONS))
# quick_thread = threading.Thread(target=partial(quick_sort, liste_hsv_quick, font, 'Quick', window, liste_rgb, 780, 100, 75, WHITE, NUM_SECTIONS))
# heap_thread = threading.Thread(target=partial(heap_sort, liste_hsv_heap, font, 'Heap', window, liste_rgb, 950, 100, 75, WHITE, NUM_SECTIONS))
selection_thread.start()
bubble_thread.start()
combes_thread.start()
insertion_thread.start()
merge_thread.start()
quick_thread.start()
heap_thread.start()



while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(10)
    pygame.display.flip()


# Attendre que tous les threads se terminent
selection_thread.join()
bubble_thread.join()
combes_thread.join()
insertion_thread.join()
merge_thread.join()
quick_thread.join()
heap_thread.join()


