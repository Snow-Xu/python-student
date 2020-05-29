
# quick sort basic
# implement the method in LinkedQueue, provided by Text basic quick sort(recursivly)
def quicksort(S):
    #base case:
    length = len(S)
    if length < 2:
        return S
    else:
    
        # changeble condition:
        p = S[length-1]    #set the pivot as the leftmost element
        L = []
        E = []
        G = []
        
        for n in S:
            if n < p:
                L.append(n)
            elif n == p:
                E.append(n)
            else:
                G.append(n)
    
        S = quicksort(L) + E + quicksort(G)
        return S


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print(quicksort(test)) 
