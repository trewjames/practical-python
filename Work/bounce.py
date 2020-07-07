# bounce.py
#
# Exercise 1.5

height = 100
bounce_factor = 3 / 5
bounces = 10

for i in range(1, bounces + 1):
    height *= bounce_factor
    print(i, round(height, 4))
