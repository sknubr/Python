
import random
from functools import reduce

# basic list comprehension
kilometer = [39.2, 36.5, 37.3, 37.8]
feet = [float(3280.9)*x for x in kilometer]
feet = [int(x) for x in feet]
print(feet)
total = 0
reduced_feet = [total := (total + x) for x in feet][-1]
print(reduced_feet)

# example to replicate more efficient for loop
mylist = []
for i in range(5):
    mylist.append(i**2)

complist = [x**2 for x in range(5)]
print "for-loop to create list", mylist, "\n"
print "comprehension list", complist, "\n"

# listcomp to create a nested list
nums = [x for x in range(10)]
letters = ["a", "b", "c", "d", "e"]
num_letter = [[n, l] for n in nums for l in letters]

print num_letter, "\n"

iter_string = "Say something"
char_extract = [x for x in iter_string if x != " "]
print char_extract

# map function
#squared_list = list(map(lambda x: x**2, [1,2,3,4]))
squared_list = map(lambda x: x**2, [1, 2, 3, 4])

print "sq ", squared_list, "\n"

# extract char from string
name = "sat"
print(list(name))


people = ['sam', 'abe', 'liam', 'joe']
print random.choice(people)


kilometer = [39.2, 36.5, 37.3, 37.8]
feet = [float(3280.8399)*x for x in kilometer]
print feet

# feet to integers
int_feet = [int(x) for x in feet]
print int_feet

# feet to only keep non-even values
uneven_feet = [x for x in int_feet if x % 2 != 0]
print uneven_feet

# reducing with lambda function
reduced_feet = reduce(lambda x, y: x+y, feet)
print reduced_feet

# reducing with list comprehension
total = 0
reduced_feet2 = [total := total+x for x in feet]
