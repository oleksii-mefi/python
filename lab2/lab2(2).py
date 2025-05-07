import math

def is_inside_region(x, y):

  condition1 = y >= -0.5
  condition2 = y <= 1
  condition3 = x <= 2
  condition4 = y <= x + 1
  condition5 = x**2 + y**2 <= 4
  return condition1 and condition2 and condition3 and condition4 and condition5

try:
  x_coordinate = float(input("напишіть х: "))
  y_coordinate = float(input("напишіть y: "))

  result = is_inside_region(x_coordinate, y_coordinate)

  if result:
    print(f"точка ({x_coordinate}, {y_coordinate}) всередині")
  else:
    print(f"точка ({x_coordinate}, {y_coordinate}) ззовні")

except ValueError:
  print("впишіть коректні значення")