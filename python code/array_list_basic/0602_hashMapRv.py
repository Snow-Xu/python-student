# quick sort

def quickSort(s):
    if len(s) < 2:
        return s
    
    pivot = s[0]
    l=[]
    e=[]
    g=[]
    for n in s:
        if n < pivot:
            l.append(n)
        elif n == pivot:
            e.append(n)
        else: 
            g.append(n)
    
    s = quickSort(l) + e + quickSort(g)
    return s

s = [1,5,3,677,4,3,2]

sorted = quickSort(s)
print (sorted)

locations = {'North America': {'USA': ['Mountain View']}}
'''
Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""
'''
locations['Asia'] = {'India': ['Bangalore']}
locations['North America']['USA'].append('Atlanta')
locations['Africa'] = {'Egypt': ['Cario']}
locations['Asia']['China'] = ['Shangahi']

usa_sorted = sorted([locations['North America']['USA']])
for city in usa_sorted:
    print (city)