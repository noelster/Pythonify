# Drawing a flower
# 1. Draw the stem
# 2. Draw the petals
# 3. Draw the center of the flower
# 4. Profit

# Import turtle module
import turtle as t

# 1. Draw the stem
t.left(90)
t.forward(100)

# 2. Draw the petals
for angles in range(0, 360, 45):
    t.left(angles)
    t.circle(25)

# 3. Draw the center of the flower

t.exitonclick()