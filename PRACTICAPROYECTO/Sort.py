listaN = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

import random

def random_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)   # pivote aleatorio

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return random_quick_sort(left) + middle + random_quick_sort(right)

def counting_sort(arr):
    max_val = max(arr)

    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []

    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

ListaB = listaN.copy()
bubble_sort(ListaB)
print("Bubble:", ListaB)

ListaS = listaN.copy()
selection_sort(ListaS)
print("Selection:", ListaS)

ListaI = listaN.copy()
insertion_sort(ListaI)
print("Insertion:", ListaI)

ListaM = listaN.copy()
merge_sort(ListaM)
print("Merge:", ListaM)

ListaQ = listaN.copy()
ListaQ = quick_sort(ListaQ)
print("Quick:", ListaQ)

ListaRQ = listaN.copy()
ListaRQ = random_quick_sort(ListaRQ)
print("Random Quick:", ListaRQ)

ListaC = listaN.copy()
ListaC = counting_sort(ListaC)
print("Counting:", ListaC)