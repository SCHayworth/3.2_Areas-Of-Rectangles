# 3-2 Area of Rectangles Program
# Shaun Hayworth
# CIS 2
# 10-01-2019

# Prompts the user for the lengths and widths of two rectangles, calculates and compares their area, and
# displays a message saying which one has the greater area, or if both areas are the same.

# Get length and width of rectangle A from user, and calculate its area.
rect_a_length = float(input('What is the length of Rectangle A in feet? '))
rect_a_width = float(input('What is the width of Rectangle A in feet? '))
rect_a_area = rect_a_length * rect_a_width

# Get length and width of rectangle B from user, and calculate its area.
rect_b_length = float(input('What is the length of Rectangle B in feet? '))
rect_b_width = float(input('What is the width of Rectangle B in feet? '))
rect_b_area = rect_b_length * rect_b_width

# Compare the areas of both rectangles and display which one has the greater area, or if they are equal.
if rect_a_area > rect_b_area:
  print(f'Rectangle A has the greatest area: {rect_a_area:.2f} sq. feet.')
elif rect_a_area < rect_b_area: 
  print(f'Rectangle B has the greatest area: {rect_b_area:.2f} sq. feet.')
else:
  print(f'Rectangle A has an area of {rect_a_area:.2f} sq. feet and Rectangle B has an area of {rect_b_area:.2f} sq. feet.')
