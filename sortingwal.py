number_list = [2, 3, 1, 4, 6, 5, 7, 8, 9, 10, 20, 15, 19, 13, 14, 18, 11, 17, 12, 16]
# number_list = [2, 3, 1, 4, 6, 5, 7, 8, 9, 10]

def insertion_sort(number_list):
    for i in range(1, len(number_list)):
        key = number_list[i]
        j = i-1
        while j >= 0 and key < number_list[j]:
            number_list[j + 1] = number_list[j]
            j -= 1
        number_list[j + 1] = key

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


insertion_sort(number_list)
print(number_list)
heap_sort(number_list)
print(number_list)
