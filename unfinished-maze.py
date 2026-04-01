import random
import time

WIDTH = 732
HEIGHT = 732

alien = Actor('coin')
alien.x = 30
alien.y = 30

box = Rect((0, -500), (732, 10))

box_background = Rect((0,0), (732, 732))

background = Actor('maze-background-template')

def draw():
    screen.clear()
    screen.draw.filled_rect(box_background, "white")
    alien.draw()
    screen.draw.filled_rect(box, "red")
    background.draw()
    

def update():
    if keyboard.right:
        alien.x = alien.x + 5
    elif keyboard.left:
        alien.x = alien.x - 5
    elif keyboard.up:
        alien.y = alien.y - 5
    elif keyboard.down:
        alien.y = alien.y + 5

    box.y = box.y + 1.3
    if box.y > HEIGHT:
        box.x = 0
        box.y = 0
    
    # if alien.colliderect(box) or alien.colliderect(background):
    #     exit()