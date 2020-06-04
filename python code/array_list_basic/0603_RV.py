# merge sort:

def mergeSort(s):
    if len (s) < 2:
        return s
    
    mid = len(s) // 2
    l = s[0:mid]
    r = s[mid:len(s)]
    
    merge(s, mergeSort(l), mergeSort(r))
    return s


def merge(s, l, r):
    i = j =0
    while i+j < len(s):
        if j == len(r) or ( i < len(l) and l[i] < r[j]):
            s[i+j] = l[i]
            i+=1
        else: 
            s[i+j] = r[j]
            j+=1

def bubbleSort(s):
    
    end = len(s)-1
    while 1 < end:
        for i in range(0,end):
            if s[i] > s[i+1]:
                temp = s[i]
                s[i] = s[i+1]
                s[i+1] = temp
        end -= 1
    




s = [1,3,557,7,5,43,2,66,5,4]
#sorted = mergeSort(s)

print (s)
bubbleSort(s)
print(s)
