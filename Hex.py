#d raw an equilateral triangle
# 1. draw AB
# 2. draw BC
# 3. draw CD
# 4. draw DE
# 5. draw EF
# 6. draw FA

import turtle

#input and data
side_length = int(input("Enter the side length: "))
for zebras in range(6):
    turtle.forward(side_length)
    turtle.left(60)

turtle.exitonclick()