import random

# implement bubble sort with basic concept:


# bubble sort
def bubbleSort(array):
    length = len(array)
    while length > 0:
        for n in range(0, length - 1):
            if array[n] > array[n+1]:
                temp = array[n]
                array[n] = array[n+1]
                array[n+1] = temp
        length -= 1

# array base, recursion
# merge sort:
def merge_sort(a):
    # basic
    n = len(a)
    if n < 2:
        return

    mid = n // 2
    a1 = a[0:mid]
    a2 = a[mid:n]

    merge_sort(a1)
    merge_sort(a2)

    merge(a1, a2, a)

# merge:
def merge(a1, a2, a):

    i = j = 0
    while i+j < len(a1+a2):
        if j == len(a2) or (i < len(a1) and a1[i] < a2[j]):
            # seperate test
            a[i+j] = a1[i]
            i += 1
        else:
            a[i+j] = a2[j]
            j += 1


# a random array:
a1 = []
a2 = []
for n in range(0, 10):
    a1.append(random.randint(1, 50))
    a2.append(a1[n])
print("Original: ", a1)
bubbleSort(a1)
print("Bubble Sorted: ", a1)

print("Original: ", a2)
bubbleSort(a2)
print("Merge Sorted: ", a2)


