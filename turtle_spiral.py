import turtle as t

t.color("blue")
t.bgcolor("pink")

t.down()
t.speed(0)
t.hideturtle()

for distance in range(1000):
    t.forward(distance)
    t.left(44)

t.exitonclick()