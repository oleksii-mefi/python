def is_point_in_shaded_region(x, y):

  x_condition = x >= 1
  y_condition = 2 <= y <= 4
  return x_condition and y_condition

#ліміт по x не встановлений оскільки там нескінченність
point1_x = 7
point1_y = 3

result1 = is_point_in_shaded_region(point1_x, point1_y)
print(f"Point ({point1_x}, {point1_y}) is in the shaded region: {result1}")