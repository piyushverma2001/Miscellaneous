import turtle
t=turtle.Turtle()
list=["red","yellow","blue","green","purple"]
for i in range(200):
    t.color(list[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)