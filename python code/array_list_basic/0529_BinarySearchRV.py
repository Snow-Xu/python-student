

def binary_search(S, value):

    l = 0
    r = len(S)-1

    while l <= r:
        mid = (l + r)//2
        if S[mid] == value:
            return mid
        elif S[mid] < value:
            l = mid + 1
        else:
            r = mid - 1

    return -1


S = [1, 3, 9, 11, 19, 29]
test_val1 = 30
test_val2 = 1
print(binary_search(S, test_val1))
print(binary_search(S, test_val2))

# boader test!
# each iteration has different start and end
# floor division
