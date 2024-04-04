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

# Initialisation de pygame
pygame.init()
window = pygame.display.set_mode((1200, 300))
pygame.display.set_caption("Sorting Algorithms")

NUM_SECTIONS = 10
WHITE = (255, 255, 255)
font = pygame.font.Font(None, 30)

liste_rgb = list_rgb(NUM_SECTIONS)
liste_hsv_selection, liste_hsv_bubble, liste_hsv_insertion, liste_hsv_merge, liste_hsv_quick, liste_hsv_heap, liste_hsv_combes = RGB_to_HSV(liste_rgb)


running = True


# Créer et démarrer un thread pour chaque algorithme de tri
selection_thread = threading.Thread(target=selection_sort, args=(liste_hsv_selection.copy(), font, 'Selection', window, liste_rgb.copy(), 100, 100, 75, WHITE, NUM_SECTIONS))
bubble_thread = threading.Thread(target=bubble_sort_step, args=(liste_hsv_bubble.copy(), font, 'Bubble', window, liste_rgb.copy(), 270, 100, 75, WHITE, NUM_SECTIONS))
combes_thread = threading.Thread(target=combes_sort, args=(liste_hsv_combes.copy(), font, 'Combes', window, liste_rgb.copy(), 1120, 100, 75, WHITE, NUM_SECTIONS))
insertion_thread = threading.Thread(target=insertion_sort, args=(liste_hsv_insertion.copy(), font, 'Insertion', window, liste_rgb.copy(), 440, 100, 75, WHITE, NUM_SECTIONS))
merge_thread = threading.Thread(target=merge_sort, args=(liste_hsv_merge.copy(), font, 'Merge', window, liste_rgb.copy(), 610, 100, 75, WHITE, NUM_SECTIONS))
quick_thread = threading.Thread(target=quick_sort, args=(liste_hsv_quick.copy(), font, 'Quick', window, liste_rgb.copy(), 780, 100, 75, WHITE, NUM_SECTIONS))
heap_thread = threading.Thread(target=heap_sort, args=(liste_hsv_heap.copy(), font, 'Heap', window, liste_rgb.copy(), 950, 100, 75, WHITE, NUM_SECTIONS))



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
    
    # Mise à jour de l'interface graphique
    pygame.display.flip()

    # Vérification de l'état des threads
    # if not any(thread.is_alive() for thread in (selection_thread, bubble_thread, combes_thread, insertion_thread, merge_thread, quick_thread, heap_thread)):
    #     break


# Attendre que tous les threads se terminent
selection_thread.join()
bubble_thread.join()
combes_thread.join()
insertion_thread.join()
merge_thread.join()
quick_thread.join()
heap_thread.join()



pygame.quit()
