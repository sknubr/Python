
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
