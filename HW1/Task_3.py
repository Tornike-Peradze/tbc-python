# What this program does:
# In this program, user type sides of triangle, and we calculate perimeter of that triangle and area also.

# How this program works:
# At first I create three variables with float() at the beginning of input to have a float data type outcome.
# Then, I calculate perimeter of triangle by simply add them together. After that at first I calculate
# semi_perimeter of triangle that I use afterward to figure out what's the area. Then I write Heron's area formula
# which involves the semi-perimeter and the lengths of the sides. Finally, I print those calculated variables.

import math

triangle_side_a = float(input('Please type triangles first sides size: '))
triangle_side_b = float(input('Please type triangles second sides size: '))
triangle_side_c = float(input('Please type triangles thirds sides size: '))

# Perimeter of a triangle - (a + b + c):
perimeter_of_triangle = triangle_side_a + triangle_side_b + triangle_side_c

# Area of triangle - at first find the semi-perimeter = s = (a + b + c) / 2 and then find the area using that info
# Area = Root(s(s-a)(s-b)(s-c))
semi_perimeter = ((triangle_side_a + triangle_side_b + triangle_side_c) / 2)
area = math.sqrt(semi_perimeter*(semi_perimeter - triangle_side_a) * (semi_perimeter - triangle_side_b) * (semi_perimeter - triangle_side_c))

print(f"Perimeter of a triangle: {perimeter_of_triangle}, Area of a triangle: {area}")