import random
import sys
import os


print("helloworld")

name = "snow"
print (name)


# Numbers Strings Lists Tuples Dictionaries


# Arithmetic operations: + - * / % **(exp) //(floor division)
print("5 + 2 =", 5+2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
print("5 % 2 =", 5%2)
print("5 ** 2 =", 5**2)
print("5 // 2 =", 5//2)


#quote and multi_line_string
quote = "\"Always remenber back slash"
multi_line_quote = ''' just like
 everyone else '''
new_string = quote + multi_line_quote
print(new_string)
#quote with format
print("%s %s" % ('formating', new_string))


# Lists
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('First Item', grocery_list[0])
print(grocery_list[1:3])
#another list & add them together
other_events = ['Wash Car', 'Pick Up Kids', 'Cash Check']
to_do_list = [other_events, grocery_list]
print(to_do_list)
print(to_do_list[1][1])
grocery_list.append('Onions')
print(to_do_list)
grocery_list.insert(1, "Pickle")
print(to_do_list)
grocery_list.sort()
print(to_do_list)