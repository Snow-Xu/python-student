# Dictionary 

# Question from https://classroom.udacity.com/courses/ud513/lessons/7118294395/concepts/78812863000923
'''
locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

print(1)
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print (city)

print(2)
asia_cities = []
for countires, cities in locations['Asia'].items():
    city_country = cities[0] + " - " + countires
    asia_cities.append(city_country)

asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print (city)

'''

# Practise problem from Python Crash Course 2 P102

# 6-1. Person: Use a dictionary to store information about a person you know . 
# Store their first name, last name, age, and the city in which they live . 
# You should have keys such as first_name, last_name, age, and city . 
# Print each piece of information stored in your dictionary .
Sam = {'first_name': 'Sam',
        'last_name': 'Jobs',
        'age': 36}
Sam['city'] = 'San Jose'

print(Sam['first_name'])
print(Sam['last_name'])
print(Sam['age'])
print(Sam['city'])

Sam['cars'] = {'daily':['mustang','Explorer','Raptors'], 'favorate':'911'}
Sam['cars']['don\'t like'] = ['puris']
Sam['cars']['don\'t like'].append('vw')
print (Sam['cars']['daily'])