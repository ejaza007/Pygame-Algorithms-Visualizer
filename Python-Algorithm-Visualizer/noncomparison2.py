import pygame
import random
import time
import os
import math
from random import randint
from operator import attrgetter
from matplotlib import pyplot as plt

pygame.init()

op = 5000
WIDTH, HEIGHT = 800, 700

FONT_BIG = pygame.font.SysFont('comicsans', 40)
FONT_MEDIUM = pygame.font.SysFont('comicsans', 30)
FONT_SMALL = pygame.font.SysFont('comicsans', 20)


win2 = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sorting')


def draw3(win2, ct):
    # set global variables for all elements before drawing
    LIGHT_BLUE = (64, 224, 208)
    BLUE = (41, 41, 64)
    DARK_BLUE = (15, 15, 38)
    BLACK_BLUE = (5, 5, 28)
    RED = (255, 10, 10)
    GREEN = (10, 255, 10)
    WHITE = (255, 255, 255)
    L_BLUE = (20, 20, 255)
    ORANGE = (255, 100, 0)
    sorti = [FONT_MEDIUM.render('1. Count Sort', 1, WHITE),
             FONT_MEDIUM.render('2. Radix Sort', 1, WHITE),
             FONT_MEDIUM.render('3. Quick Sort', 1, WHITE),
             FONT_MEDIUM.render('4. Heap Sort', 1, WHITE),
             FONT_MEDIUM.render('5. merge Sort', 1, WHITE),
             FONT_MEDIUM.render('6. insertion Sort', 1, WHITE),
             FONT_MEDIUM.render(
                 '7. Bubble sort', 1, WHITE),
             FONT_MEDIUM.render('8. Book 7.4.5', 1, WHITE),
             FONT_MEDIUM.render('9. Bucket sort', 1, WHITE),
             FONT_MEDIUM.render('10. Book 8.2.4', 1, WHITE)]
    win2.fill(LIGHT_BLUE)

    head1 = FONT_MEDIUM.render(
        'Calculating time for algorithms one by one.', 1, WHITE)
    head2 = FONT_MEDIUM.render('Done the following;  ', 1, WHITE)
    win2.blit(head1, (30, 20))
    win2.blit(head2, (40, 90))

    for i in range(ct):
        win2.blit(sorti[i], (350, 90 + (30 * i)))

    pygame.display.update()


def main2(filenum):
    count = 0
    global win3
    filepaths = ['small.txt', 'medium.txt', 'high.txt']
    fullpath = os.path.join(
        os.path.dirname(__file__),
        filepaths[filenum])
    print(fullpath)

    read = open(fullpath, "r")

    raw_list = read.read().split(',')
    sort = []
    for x in range(len(raw_list)):
        sort.append(int(raw_list[x][0:]))
    sort_float = []
    for i in range(len(raw_list)):
        sort_float.append(float(raw_list[i][0:]))
    times = []
    times.append(count_Sort(sort))
    draw3(win2, count)
    count = count + 1

    times.append(radix_Sort(sort))
    draw3(win2, count)
    count = count + 1

    times.append(quick_Sort(sort))
    draw3(win2, count)
    count = count + 1

    times.append(heap_Sort(sort))
    draw3(win2, count)
    count = count + 1

    times.append(merge_Sort(sort))
    draw3(win2, count)
    count = count + 1

    # times.append(insertion_Sort(sort))
    # draw3(win2, count)
    # count = count + 1

    # times.append(bubble_Sort(sort))
    # draw3(win2, count)
    # count = count + 1

    times.append(alg_745(sort))
    draw3(win2, count)
    count = count + 1

    times.append(bucket_sort(sort_float))
    draw3(win2, count)
    count = count + 1

    times.append(alg_824(sort, 80, 100))
    draw3(win2, count)
    count = count + 1

    # algos = ['Count sort', 'Radix sort', 'Quick Sort',
    #          'Heap sort', 'Merge sort', 'Insertion sort', 'Bubble sort', 'Book 7.4.5 sort', 'Bucket sort', 'Book 8.2.4']
    algos = ['Count sort', 'Radix sort', 'Quick Sort',
             'Heap sort', 'Merge sort', 'Book 7.4.5 sort', 'Bucket sort', 'Book 8.2.4']

    plt.plot(algos, times, label='algorithms')
    plt.ylabel('Time in seconds')
    plt.xlabel('Algorithms')
    plt.title("Time comparison of algorithms")
    plt.show()


def alg_824(temp, x, y):
    array = temp[:]
    s = time.time()
    maxE = int(max(array))
    minE = int(min(array))
    range_ = maxE - minE + 1

    count = [0 for _ in range(range_)]
    output = [0 for _ in range(len(array))]

    for j in range(0, len(array)):
        count[array[j]-minE] += 1

    for j in range(1, len(count)):
        count[j] += count[j-1]

    for j in range(len(array)-1, -1, -1):
        output[count[array[j] - minE] - 1] = array[j]
        count[array[j] - minE] -= 1

    for j in range(0, len(array)):
        array[j] = output[j]
    print('number of elements between range n and m: ', (count[y]-count[x]))
    e = time.time()
    return e-s


def alg_745(temp):
    array = temp[:]
    s = time.time()
    quicksort_inplace(array, 0, len(array)-1)
    e = time.time()
    return (e - s)


def insertion_sort(array, low, n):  # 725

    for i in range(low + 1, n + 1):
        pygame.event.pump()
        val = array[i]
        j = i
        while j > low and array[j] < array[j - 1]:
            pygame.event.pump()
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
        array[i] = val


def partition2(array, low, high):  # 725
    i = low
    pivot = array[high]
    for j in range(low, high):
        pygame.event.pump()
        if array[j] < pivot:
            pygame.event.pump()
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i


def quicksort_inplace(array, low, high):  # 725

    if low < high:
        if high - low + 1 < 1:
            insertion_sort(array, low, high)
            return
        pivot_index = partition2(array, low, high)
        quicksort_inplace(array, low, pivot_index - 1)
        quicksort_inplace(array, pivot_index + 1, high)


def insertionSort(b):
    for i in range(1, len(b)):
        pygame.event.pump()
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            pygame.event.pump()
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def bucket_sort(temp):
    s = time.time()
    arr = temp[:]
    # find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)

    # create n empty buckets
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]

    # put elements into their corresponding buckets
    for el in arr:
        bucket_index = int((el - min_val) / (max_val -
                           min_val) * (num_buckets - 1))
        buckets[bucket_index].append(el)

    # sort each non-empty bucket
    for bucket in buckets:
        bucket.sort()

    # concatenate the sorted buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    for i in sorted_arr:
        print(i)

    e = time.time()
    return (e - s)


def count_Sort(temp):
    array = temp[:]
    s = time.time()

    max_ = int(max(array))
    min_ = int(min(array))
    rangeElements = max_ - min_ + 1

    countArr = [0 for _ in range(rangeElements)]
    outputArr = [0 for _ in range(len(array))]

    for x in range(0, len(array)):
        pygame.event.pump()
        countArr[array[x]-min_] += 1

    for x in range(1, len(countArr)):
        pygame.event.pump()
        countArr[x] += countArr[x-1]

    for x in range(len(array)-1, -1, -1):
        pygame.event.pump()
        outputArr[countArr[array[x] - min_] - 1] = array[x]
        countArr[array[x] - min_] -= 1

    for x in range(0, len(array)):
        pygame.event.pump()
        array[x] = outputArr[x]
    e = time.time()

    return (e - s)


def countSort_forRadix(array, place):
    length = len(array)
    output = [0] * length
    count = [0] * 10

    for x in range(0, length):
        pygame.event.pump()
        index = array[x] // place
        count[index % 10] += 1

    for x in range(1, 10):
        pygame.event.pump()
        count[x] += count[x - 1]
    x = length - 1

    while x >= 0:
        pygame.event.pump()
        index = array[x] // place
        output[count[index % 10] - 1] = array[x]
        count[index % 10] -= 1
        x -= 1

    for x in range(0, length):
        array[x] = output[x]


def radix_Sort(temp):
    array = temp[:]
    startTime = time.time()
    max_element = max(array)

    place = 1
    while max_element // place > 0:
        pygame.event.pump()
        countSort_forRadix(array, place)
        place *= 10
    endTime = time.time()
    return (endTime-startTime)


def quick_Sort(temp):
    array = temp[:]
    startTime = time.time()
    if len(array) <= 1:
        return array
    smaller, equal, larger = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    for x in array:
        pygame.event.pump()
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    endTime = time.time()
    return endTime-startTime


def heapify(array, N, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and array[largest] < array[l]:
        largest = l

    if r < N and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        heapify(array, N, largest)


def heap_Sort(temp):
    array = temp[:]
    startTime = time.time()
    N = len(array)
    for x in range(N//2 - 1, -1, -1):
        pygame.event.pump()
        heapify(array, N, x)

    for x in range(N-1, 0, -1):
        array[x], array[0] = array[0], array[x]
        pygame.event.pump()
        heapify(array, x, 0)
    endTime = time.time()
    return endTime-startTime


def bubble_Sort(temp):
    array = temp[:]
    startTime = time.time()
    n = len(array)

    for x in range(n):
        for j in range(0, n-x-1):
            pygame.event.pump()
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    endTime = time.time()
    return endTime-startTime


def merge_Sort(temp):
    array = temp[:]
    startTime = time.time()
    if len(array) > 1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        merge_Sort(L)
        merge_Sort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            pygame.event.pump()
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            pygame.event.pump()
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            pygame.event.pump()
            array[k] = R[j]
            j += 1
            k += 1

    endTime = time.time()
    return endTime - startTime


def insertion_Sort(temp):
    array = temp[:]
    startTime = time.time()
    for x in range(1, len(array)):
        pygame.event.pump()
        key = array[x]
        k = x-1
        while k >= 0 and key < array[k]:
            pygame.event.pump()
            array[k + 1] = array[k]
            k -= 1
        array[k + 1] = key
    endTime = time.time()
    return endTime-startTime
