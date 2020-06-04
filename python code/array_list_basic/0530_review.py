





#merge sort
def merge_sort(s):
    if len(s) < 2:
        return s
    
    mid = len(s)//2
    l = s[0:mid]
    r = s[mid:len(s)]
    
    merge(s, merge_sort(l), merge_sort(r))
    return s
    
def merge(s,l,r):
    i = j = 0
    while i+j < len(l+r):
        if j == len(r) or (i < len(l) and l[i] < r[j]):
            s[i+j] = l[i]
            i += 1
        else: 
            s[i+j] = r[j]
            j += 1
    

#bubble sort
def bubbleSort(s):
    n = len(s)
    start = 0
    end = n
    while start < end:
        for n in range(start,end-1):
            if s[n] > s[n+1]:
                temp = s[n]
                s[n] = s[n+1]
                s[n+1] = temp
        end -= 1
    return s



s = [1,4,3,5,1,3,4,2,66]
sorted_s = bubbleSort(s)
print(sorted_s)

