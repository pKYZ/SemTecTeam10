"""Snake, classic arcade game.

xercises

. How do you make the snake faster or slower?
. How can you make the snake go around the edges?
. How would you move the food?
. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
   "Change snake direction."
   aim.x = x
   aim.y = y

def inside(head):
   "Return True if head inside boundaries."
   return -200 < head.x < 190 and -200 < head.y < 190

def move():
   "Move snake forward one segment."
   head = snake[-1].copy()
   head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        print('You are dead :(')
        update()
        return

   snake.append(head)

   if head == food:
       print('Snake:', len(snake))
       food.x = randrange(-15, 15) * 10
       food.y = randrange(-15, 15) * 10
   else:
       snake.pop(0)

   clear()

   for body in snake:
       square(body.x, body.y,10, 'green')

   square(food.x,food.y,10, 'purple')
   update()
   ontimer(move, 100)

setup(500, 500, 370, 0)

color("black")
width(3)
speed(10)

# print hello to the player
# letter H
goto(0,0)
left(90)
forward(70)
penup()
goto(0, 35)
pendown()
right(90)
forward(30)
penup()
goto(30, 70)
pendown()
right(90)
forward(70)
 
# letter E
penup()
goto(40, 0)
pendown()
right(180)
forward(70)
right(90)
forward(35)
penup()
goto(40, 35)
pendown()
forward(35)
penup()
goto(40, 0)
pendown()
forward(35)
  
# letter L
penup()
goto(90, 70)
pendown()
right(90)
forward(70)
left(90)
forward(35)
   
# letter L
penup()
goto(135, 70)
pendown()
right(90)
forward(70)
left(90)
forward(35)
    
# letter O
penup()
goto(210, 70)
pendown()
for i in range(25):
    right(15)
    forward(10)

right(-60)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
