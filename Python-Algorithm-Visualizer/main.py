import pygame
import random
import time
import os
from operator import attrgetter
from noncomparison2 import *

pygame.init()

op = 5000
WIDTH, HEIGHT = 800, 700

filenum = 0

FONT_BIG = pygame.font.SysFont('comicsans', 40)
FONT_MEDIUM = pygame.font.SysFont('comicsans', 30)
FONT_SMALL = pygame.font.SysFont('comicsans', 20)


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sorting')

LIGHT_BLUE = (64, 224, 208)
BLUE = (41, 41, 64)
DARK_BLUE = (15, 15, 38)
BLACK_BLUE = (5, 5, 28)
RED = (255, 10, 10)
GREEN = (10, 255, 10)
WHITE = (255, 255, 255)
L_BLUE = (20, 20, 255)
ORANGE = (255, 100, 0)

NUM_BAR = 170

BORDER = 25

SORTED = False

SPACE = (WIDTH - 25 - BORDER) / NUM_BAR

BAR_WIDTH, BAR_HEIGHT = SPACE - 1.2, 2.87


FPS = 80

RUN = True

DOWN = 25

COUNT = 0

whichAlgo = 0

AlgoIndex = 0

project = FONT_MEDIUM.render('Armaghan Ejaz', 1, WHITE)
complexity = FONT_SMALL.render('Complexity', 1, WHITE)
current = FONT_SMALL.render('Current Algo: ', 1, WHITE)
on = FONT_MEDIUM.render('O(n^2)', 1, WHITE)

sorting = [FONT_SMALL.render('1. Bubble Sort', 1, WHITE),
           FONT_SMALL.render('2. Merge Sort', 1, WHITE),
           FONT_SMALL.render('3. Quick Sort', 1, WHITE),
           FONT_SMALL.render('4. Heap Sort', 1, WHITE),
           FONT_SMALL.render('5. Insertion Sort', 1, WHITE)]
sorting2 = [FONT_SMALL.render('6. 7.4.5 Sort', 1, WHITE),
            FONT_SMALL.render('7. Plots of rest of the algorithms', 1, WHITE),
            FONT_SMALL.render('a. Small b. Medium c. High', 1, WHITE),
            FONT_SMALL.render('0. Reset', 1, WHITE)]

currentSorting = [FONT_SMALL.render(' ', 1, WHITE),
                  FONT_SMALL.render('', 1, WHITE),
                  FONT_SMALL.render('Bubble', 1, WHITE),
                  FONT_SMALL.render('Merge', 1, WHITE),
                  FONT_SMALL.render('Quick', 1, WHITE),
                  FONT_SMALL.render('Heap', 1, WHITE),
                  FONT_SMALL.render('Insertion', 1, WHITE),
                  FONT_SMALL.render('Book 7.4.5', 1, WHITE)]


complexities = [FONT_SMALL.render('O(N)', 1, WHITE),
                FONT_SMALL.render('O(N^2)', 1, WHITE),
                FONT_SMALL.render('O(nLOGn)', 1, WHITE),
                FONT_SMALL.render('7.4.5 Sort', 1, WHITE),
                FONT_SMALL.render('8.2.4 Sort', 1, WHITE),
                FONT_SMALL.render('Reset', 1, WHITE)]


class Bar:

    def __init__(self, x, y, width, height, value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = LIGHT_BLUE
        self.value = value

    def reset(self, num):
        self.x = BORDER + num * SPACE
        return self

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))

    def check(self):
        self.color = RED

    def done(self):
        self.color = GREEN

    def match(self):
        self.color = L_BLUE

    def back(self):
        self.color = LIGHT_BLUE


def genBars2():
    global sort
    global bar
    global whichAlgo
    global AlgoIndex
    AlgoIndex = 0
    whichAlgo = 0
    # code that works for QUICKSORT

    sort = [x for x in range(1, NUM_BAR + 2)]
    random.shuffle(sort)

    bar = [Bar((BORDER + i * SPACE), (HEIGHT - DOWN - (BAR_HEIGHT * sort[i])),
               BAR_WIDTH, BAR_HEIGHT * sort[i], sort[i]) for i in range(NUM_BAR)]


def genBars(filenum):
    global sort
    global bar
    global whichAlgo
    global AlgoIndex
    AlgoIndex = 0
    whichAlgo = 0

    filepaths = ['medium.txt', 'medium.txt', 'high.txt']
    fullpath = os.path.join(
        os.path.dirname(__file__),
        filepaths[filenum])

    # read = open(fullpath, "r")
    # int_list = read.read().split(',')
    # sort = []
    # for i in range(NUM_BAR):
    #     sort.append(int(int_list[i][0:]) % 170)
    # for i in range(len(sort)):
    #     print(sort[i])

    read = open(fullpath, "r")
    rand_list = read.read().split(',')
    sort = []

    for i in range(1, NUM_BAR+1):
        sort.append(int(rand_list[i][0:]) % NUM_BAR)
    # for i in sort:
    #     print(i)

    # code that works for QUICKSORT

    # sort = [x for x in range(1, NUM_BAR + 2)]
    # random.shuffle(sort)

    bar = [Bar((BORDER + i * SPACE), (HEIGHT - DOWN - (BAR_HEIGHT * sort[i])),
               BAR_WIDTH, BAR_HEIGHT * sort[i], sort[i]) for i in range(NUM_BAR)]


def main(win):
    clock = pygame.time.Clock()

    global RUN
    global AlgoIndex
    global bar
    global SORTED
    global whichAlgo
    global filenum
    global NUM_BAR
    
    

    genBars(filenum)
    while RUN:
        clock.tick(FPS)
        draw(win, bar)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            genBars(filenum)
            SORTED = False

        if keys[pygame.K_1]:
            check()
            AlgoIndex = 2
            whichAlgo = 1
            bubble(bar, win)
        if keys[pygame.K_2]:
            check()
            AlgoIndex = 3
            whichAlgo = 2
            merge_sort(bar, 0, len(bar) - 1, win)
        if keys[pygame.K_3]:
            genBars2()
            AlgoIndex = 4
            whichAlgo = 2
            quick_sort(bar, 0, len(bar) - 1, win)
        if keys[pygame.K_4]:
            check()
            AlgoIndex = 5
            whichAlgo = 2
            heap_sort(bar, win)
        if keys[pygame.K_5]:
            check()
            AlgoIndex = 6
            whichAlgo = 1
            insertion(bar, win)
        if keys[pygame.K_6]:
            check()
            AlgoIndex = 7
            book_725(bar, win)

        if keys[pygame.K_7]:
            main2(filenum)

        if keys[pygame.K_a]:
            filenum = 0
            genBars(filenum)
        if keys[pygame.K_b]:
            filenum = 1
            genBars(filenum)

        if keys[pygame.K_c]:
            filenum = 2
            genBars(filenum)
    pygame.quit()


def check():
    global SORTED
    global bar
    global AlgoIndex
    AlgoIndex = 0

    if SORTED:
        SORTED = False
        genBars(filenum)

# draw function for the screen


def draw(win, bar):
    # set global variables for all elements before drawing
    global reset
    global name
    global sorting
    global project
    global whichAlgo
    win.fill(WHITE)

    pygame.draw.rect(win, BLACK_BLUE, (0, 0, 800, 180))

    win.blit(project, (30, 20))

    win.blit(name, (40, 90))

    for i in range(len(sorting)):
        win.blit(sorting[i], (270, 13 + (25 * i)))

    for i in range(len(sorting2)):
        win.blit(sorting2[i], (460, 13 + (25 * i)))

    if whichAlgo != 0:
        win.blit(complexity, (680, 28 + (30 * 3)))
        win.blit(complexities[whichAlgo], (680, 28 + (30 * 4)))

    win.blit(current, (460, 13 + (25 * 5)))
    win.blit(currentSorting[AlgoIndex], (600, 13 + (25 * 5)))

    for i in bar:
        i.draw(win)

    pygame.display.update()


def draw2(win, bar):
    # set global variables for all elements before drawing
    global reset
    global name
    global sorting
    global project
    global whichAlgo
    win.fill(BLACK_BLUE)

    pygame.draw.rect(win, ORANGE, (0, 0, 800, 180))

    win.blit(project, (30, 20))

    win.blit(name, (40, 90))

    pygame.draw.rect(win, BLUE, (250, 15, 5, 150))

    pygame.display.update()


def quick_sort(bar, low, high, win):
    # Set global variables to control
    # the quitting function and shuffle function for the list
    # before running
    global RUN
    global SORTED
    SORTED = True

    if len(bar) == 1:
        return bar
    if low < high:

        pi = partition(bar, low, high, win)
        draw(win, bar)
        quick_sort(bar, low, pi - 1, win)

        if not RUN:
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break

        for i in range(pi + 1):
            bar[i].done()
        quick_sort(bar, pi, high, win)


def partition(bar, low, high, win):
    i = low
    pivot = bar[high]
    pivot.color = ORANGE
    for j in range(low, high):

        bar[j].check()
        bar[i].check()
        draw(win, bar)
        bar[j].back()
        bar[i].back()
        if bar[j].value < pivot.value:

            bar[i], bar[j] = bar[j], bar[i]
            bar[i].reset(i)
            bar[j].reset(j)
            i += 1

    bar[i], bar[high] = bar[high], bar[i]
    bar[i].reset(i)
    pivot.back()
    draw(win, bar)
    bar[high].reset(high)
    return i


def merge(bar, left, mid, right, win):
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        bar[i].check()
        bar[j].check()
        draw(win, bar)
        bar[i].back()
        bar[j].back()
        if bar[i].value < bar[j].value:
            temp.append(bar[i])
            i += 1
        else:
            temp.append(bar[j])
            j += 1
    while i <= mid:
        bar[i].check()
        draw(win, bar)
        bar[i].back()
        temp.append(bar[i])
        i += 1
    while j <= right:
        bar[j].check()
        draw(win, bar)
        bar[j].back()
        temp.append(bar[j])
        j += 1
    k = 0
    for i in range(left, right + 1):
        bar[i] = temp[k]
        bar[i].reset(i)
        bar[i].check()
        draw(win, bar)
        if right - left == len(bar) - 1:
            bar[i].done()
        else:
            bar[i].back()
        k += 1


def merge_sort(bar, left, right, win):
    # Set global variables to control
    # the quitting function and shuffle function for the list
    # before running
    global SORTED
    SORTED = True
    global RUN

    mid = left + (right - left) // 2
    if left < right:
        merge_sort(bar, left, mid, win)
        merge_sort(bar, mid + 1, right, win)
        if not RUN:
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break
        merge(bar, left, mid, right, win)


def insertion(bar, win):
    # Set global variables to control
    # the quitting function and shuffle function for the list
    # before running
    global RUN
    global SORTED
    SORTED = True

    for i in range(1, len(bar)):
        bar[i].check()
        draw(win, bar)
        bar[i].back()
        j = i
        while j > 0 and bar[j].value < bar[j - 1].value:
            if not RUN:
                return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
                    break
            bar[i].check()
            draw(win, bar)
            bar[i].back()
            bar[j], bar[j - 1] = bar[j - 1], bar[j]
            bar[j].reset(j)
            bar[j - 1].reset(j - 1)
            j -= 1
    for i in range(len(bar)):
        bar[i].done()
        pygame.time.delay(1)
        draw(win, bar)


def heap_sort(bar, win):
    # Set global variables to control
    # the quitting function and shuffle function for the list
    # before running
    global RUN
    global SORTED
    SORTED = True
    n = len(bar)
    for i in range(n // 2 - 1, -1, -1):
        heapify(bar, n, i, win)

    for i in range(n - 1, 0, -1):
        bar[i], bar[0] = bar[0], bar[i]
        bar[i].reset(i)
        bar[0].reset(0)
        bar[i].done()
        draw(win, bar)
        heapify(bar, i, 0, win)


def heapify(bar, n, i, win):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and bar[left].value > bar[largest].value:
        largest = left
    if right < n and bar[right].value > bar[largest].value:
        largest = right
    if largest != i:
        bar[i].check()
        bar[largest].check()
        draw(win, bar)

        bar[i], bar[largest] = bar[largest], bar[i]

        bar[i].reset(i)
        bar[largest].reset(largest)

        bar[i].back()
        bar[largest].back()
        draw(win, bar)

        heapify(bar, n, largest, win)


def count_sort(bar):
    start = time.time()
    max_attr = max(bar, key=attrgetter('value'))
    min_attr = min(bar, key=attrgetter('value'))
    max_element = max(max_attr)
    min_element = min(min_attr)
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0

    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(bar))]

    # Store count of each character
    for i in range(0, len(bar)):
        count_arr[bar[i].value-min_element] += 1

    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    # Build the output character array
    for i in range(len(bar)-1, -1, -1):
        output_arr[count_arr[bar[i].value - min_element] - 1] = bar[i].value
        count_arr[bar[i].value - min_element] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(bar)):
        bar[i].value = output_arr[i]
    end = time.time()
    return end - start


def bubble(bar, win):
    # Set global variables to control
    # the quitting function and shuffle function for the list
    # before running
    global RUN
    global SORTED
    SORTED = True

    for i in range(len(bar)):
        if not RUN:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
                break

        for j in range(len(bar) - 1 - i):

            bar[j].check()
            draw(win, bar)
            bar[j].back()

            if bar[j].value > bar[j + 1].value:
                temp = bar[j]
                bar[j] = bar[j + 1]
                bar[j + 1] = temp
                bar[j].reset(j)
                bar[j + 1].reset(j + 1)
        bar[len(bar) - 1 - i].done()


def book_725(bar, win):
    quicksort_inplace(bar, 0, len(bar)-1, win)
    for i in range(len(bar)):
        bar[i].done()
        pygame.time.delay(2)


def insertion_sort(bar, low, n, win):  # 725
    for i in range(low + 1, n + 1):
        bar[i].check()
        draw(win, bar)
        bar[i].back()
        val = bar[i].value
        j = i
        # while j > low and bar[j-1].value > val:
        while j > low and bar[j].value < bar[j - 1].value:
            bar[i].check()
            draw(win, bar)
            bar[i].back()
            bar[j], bar[j - 1] = bar[j - 1], bar[j]
            j -= 1
            bar[j].reset(j)
            bar[j - 1].reset(j - 1)
        bar[i].value = val


def quicksort_inplace(bar, low, high, win):  # 725

    if low < high:
        if high - low + 1 < 1:

            insertion_sort(bar, low, high, win)
            return
        # Size of the subarray is greater than the threshold, quicksort
        pivot_index = partition(bar, low, high, win)
        quicksort_inplace(bar, low, pivot_index - 1, win)
        quicksort_inplace(bar, pivot_index + 1, high, win)


if __name__ == "__main__":
    main(win)
