import random
import time
fileName = 'data.txt'
dataLength = 20000

# Bubble Sort 
def bubbleSort(s):
    start = 0
    end = len(s)

    while end >= 2: 
        length = end - start

        for n in range(0,length-1):
            if s[n] > s[n+1]:
                tem = s[n]
                s[n] = s[n+1]
                s[n+1] = tem
        end -= 1
    
    return s


# Merge Sort
def mergeSort(s):
    if len(s) < 2:
        return s

    length = len(s)
    
    mid = length//2

    l = s[0:mid]
    r = s[mid:length]
    
    merge(s,mergeSort(l),mergeSort(r))     
    return s

def merge(s,l,r):
    i=j=0
    while i+j < len(l+r):
        if j == len(r) or (i < len(l) and l[i] < r[j]):
            s[i+j] = l[i]
            i+=1
        else:
            s[i+j] = r[j]
            j+=1
    

# Quick Sort: pivot locates the left most of the array
def quickSort(s):
    if len(s) < 2:
        return s
   
    pivot = s[len(s)-1]

    l = []
    e = []
    g = []

    for n in s:
        if n < pivot:
            l.append(n)
        elif n == pivot:
            e.append(n)
        else:
            g.append(n)
    
    s = quickSort(l) + e + quickSort(g)
    return s

# Create data file:
def dataGenerator(dataLength, fileName):
    
    with open(fileName, 'w') as file_object:
        
        for n in range(0,dataLength):
            s = str(random.randrange(0,dataLength))+'\n'
            file_object.write(s)

    file_object.close()

# read data from file to an array
def readFrom(fileName):
    s = []
    with open(fileName, 'r') as read_object:
        for line in read_object:
            s.append(int(line))
    read_object.close()
    return s


dataGenerator(dataLength,fileName)
s = readFrom(fileName)
print('for data size of: ', dataLength)
'''
# bubble sort:
t0 = time.time()
bubbleSorted_s = bubbleSort(s)
t1 = time.time()
t_bubbleSort = t1-t0
print ('Bubble sort takes: ', t_bubbleSort)

# merge sort:
t0 = time.time()
mergeSorted_s = mergeSort(s)
t1 = time.time()
t_mergeSort = t1-t0
print ('Merge sort takes: ', t_mergeSort)

'''
#quick sort
t0 = time.time()
sorted_s = quickSort(s)
t1 = time.time()
t_quickSort = t1-t0
print('Quick sort takes: ',t_quickSort)


