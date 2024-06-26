from colors import HSV_to_RGB
from threading import Lock

'''
Heap sort algorithm :
The heap sort algorithm is a comparison-based sorting algorithm.
1. Build a max heap from the input data.
2. The largest element is stored at the root of the heap.
3. Swap the root element with the last element of the heap.
4. Remove the last element from the heap.
5. Heapify the root element.
6. Repeat the process until the heap is empty.
'''

pygame_lock = Lock()

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

def heap_sort(time_start, liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):
    n = len(liste_hsv)

    for i in range(n // 2 - 1, -1, -1):
        heapify(liste_hsv, n, i)
        HSV_to_RGB(time_start, liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)

    for i in range(n-1, 0, -1):
        liste_hsv[i], liste_hsv[0] = liste_hsv[0], liste_hsv[i]
        heapify(liste_hsv, i, 0)
        with pygame_lock:
            HSV_to_RGB(time_start,liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)