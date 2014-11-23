from turtle import *

color('black', 'purple')
speed(11)

step = 20
angle = 10
quadrant = 1

begin_fill()
while True:
    forward(step)
    left(angle)
    if abs(pos()) < 1:
        quadrant = quadrant + 1
        if quadrant > 4:
            break
        else:
            left(90)
end_fill()
done()
