"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.

"""

from random import *
from turtle import *
from freegames import path

opt=int(input("Choose a gamemode:\nSize 1 is 8x8\nSize 2 is 4x4\n"))
if opt==1:
    print("     You chose gamemode 8x8\n")

    car = path('car.gif')
    tiles = list(range(32)) * 2
    state = {'mark': None}
    hide = [True] * 64
    def square(x, y):
        "Draw white square with black outline at (x, y)."
        "Note: Later changed to orange with cyan outlines"
        up()
        goto(x, y)
        down()
        color('cyan', 'orange')
        begin_fill()
        for count in range(4):
            forward(50)
            left(90)
        end_fill()

    def index(x, y):
        "Convert (x, y) coordinates to tiles index."
        return int((x + 200) // 50 + ((y + 200) // 50) * 8)

    def xy(count):
        "Convert tiles count to (x, y) coordinates."
        return (count % 8) * 50 - 200, (count // 8) * 50 - 200

    def tap(x, y):
        "Update mark and hidden tiles based on tap."
        spot = index(x, y)
        mark = state['mark']

        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
        else:
            hide[spot] = False
            hide[mark] = False
            state['mark'] = None

    def draw():
        "Draw image and tiles."
        clear()
        goto(0, 0)
        shape(car)
        stamp()

        for count in range(64):
            if hide[count]:
                x, y = xy(count)
                square(x, y)

        mark = state['mark']

        if mark is not None and hide[mark]:
            x, y = xy(mark)
            up()
            goto(x + 2, y)
            color('black')
            write(tiles[mark],font=('Arial', 30, 'normal'))
        update()
        ontimer(draw, 100)

    shuffle(tiles)
    setup(420, 420, 370, 0)
    addshape(car)
    hideturtle()
    tracer(False)
    onscreenclick(tap)
    draw()
    done()


elif opt==2:
    print("     You chose gamemode 4x4\n")

    car = path('car.gif')
    tiles= list(range(8))*2
    state= {'mark':None}
    hide= [True] * 16
    def square(x, y):
        "Draw white square with black outline at (x, y)."
        "Note: Later changed to orange"
        up()
        goto(x, y)
        down()
        color('cyan', 'magenta')
        begin_fill()
        for count in range(4):
            forward(100)
            left(90)
        end_fill()

    def index(x, y):
        "Convert (x, y) coordinates to tiles index."
        return int((x + 200) // 100 + ((y + 200) // 100) * 4)

    def xy(count):
        "Convert tiles count to (x, y) coordinates."
        return (count % 4) * 100 - 200, (count // 4) * 100 - 200

    def tap(x, y):
        "Update mark and hidden tiles based on tap."
        spot = index(x, y)
        mark = state['mark']

        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
        else:
            hide[spot] = False
            hide[mark] = False
            state['mark'] = None

    def draw():
        "Draw image and tiles."
        clear()
        goto(0, 0)
        shape(car)
        stamp()

        for count in range(16):
            if hide[count]:
                x, y = xy(count)
                square(x, y)

        mark = state['mark']

        if mark is not None and hide[mark]:
            x, y = xy(mark)
            up()
            goto(x + 2, y)
            color('black')
            write(tiles[mark],font=('Arial', 30, 'normal'))
        update()
        ontimer(draw, 100)


    shuffle(tiles)
    setup(420, 420, 370, 0)
    addshape(car)
    hideturtle()
    tracer(False)
    onscreenclick(tap)
    draw()
    done()