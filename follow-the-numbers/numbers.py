from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

dots = []
lines = []
next_dot = 0
start_time = time()
end_time = time()

def update():
    pass

for dot in range(0, 10):
    actor = Actor("dot")
    actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
    dots.append(actor)

def draw():
    global start_time
    global next_dot
    if next_dot < 11:
        screen.fill("black")
        number = 1
        for dot in dots:
            screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))

            dot.draw()
            number = number + 1
        for line in lines:
            screen.draw.line(line[0], line[1], (100, 0, 0))

    if next_dot == 10:
        global end_time
        end_time = time()
        total_time = round(end_time - start_time)
        screen.fill("black")
        screen.draw.text(str(total_time), (400, 300), fontsize = 60)
        next_dot = 11


def on_mouse_down(pos):
    global next_dot
    global lines
    print(next_dot)
    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot = next_dot + 1
    else:
        lines = []
        next_dot = 0