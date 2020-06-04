

def mergeSort(s):
    if len(s) < 2:
        return s
    mid = len(s)//2
    l = s[0:mid]
    r = s[mid:len(s)]
    merge(s, mergeSort(l), mergeSort(r))
    return s

def merge(s, l, r):
    i=j=0
    while i+j < len(s):
        if j == len(r) or (i < len(l) and l[i] < r[j]):
            s[i+j] = l[i]
            i+=1
        else:
            s[i+j] = r[j]
            j+=1

def bubbleSort(s):
    n = len(s)
    l = 0
    r = n-1
    while l<=r:
        for n in range(l,r):
            if s[n] > s[n+1]:
                temp = s[n]
                s[n] = s[n+1]
                s[n+1] = temp
        r-=1

def quickSort(s):
    if len(s) < 2:
        return s
    pivot = s[0]
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



s = [1,5,3,2,5,13,15]
qSorted_s = quickSort(s)
print(qSorted_s)
sorted_s = mergeSort(s)
print(sorted_s)
bubbleSort(s)
print(s)