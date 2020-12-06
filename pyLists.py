
courses = ['Arts', 'Physics', 'Chemistry', 'Maths']
courses_supplementary = ['French', 'Hindi']
num_range = list(i for i in range(31))

# read course by index
# 0,1 (2 not included)
print(courses[0:2])

# num_list[-9:], read the part in the brackets as "9th from the end, to the end." or  "-9, onwards"
print(courses[-2:])

# to slice using step jumps sequence[start:stop:step]
print(num_range[-10::2])

# we can also put slice in a variable. However the assignment needs to happen through the slice object. slice (stop)
# first argument is stop: slice(stop); e.g.
slice_object = slice(2)  # prints stopping BEFORE 2 i.e. 0,1,2  e.g.
print(courses[slice_object])


# if you want first argument to be start use slice(start, None) e.g.
slice_object = slice(2, None)  # prints 2 to end of list
print(courses[slice_object])

# modifying a list
courses.append("Comp Sci")
# sort a list. Note that reverse attribute does the reverse sort. ** Note : case matters  True (vs TRUE, true)
courses.sort(reverse=True)
# sorted does not mutate coureses while courses.sort will mutate courses. Acting on the object vs. passing data
az_courses = sorted(courses)
courses.pop()

# adding a new list in a flat way to the new list. Note that append will add the new list as an element and not as a flat item list
courses.extend(courses_supplementary)
print(courses)
print(az_courses)

# get index of an item in a list
print(courses.index('Chemistry'))
print('Chemistry' in courses)     # exists
print('Philosophy' in courses)   # does not exist

# if we need to get both the index and the value from a list we can use enumerate. To have index start at 1 (instead of 0) use parameter start=1
for index, course in enumerate(courses, start=1):
    print(index, course)

# to convert a list to a string use join with separator
str_courses = ','.join(courses)
print(str_courses)
# to get back the list use split
list_courses = str_courses.split(',')
print(list_courses)

# Lists (and dict) are mutable. list2 = list1 is assigns both pointers to be the same memory address so change in one changes the other.
copy_courses = courses
# To create a new list from contents but not share addresses create a new list by list() or slicing [:]
new_courses = list(courses)      # we can also use new_courses = courses[:]
# verifying that one was a shared pointer and the other was a new copy

courses[0] = "Engineering fundamentals"
print("courses -- original                                ", courses, id(courses))
print("copy_courses -- shared pointer                     ",
      copy_courses, id(copy_courses))
print("new courses  -- new list with content of original  ",
      new_courses, id(new_courses))
