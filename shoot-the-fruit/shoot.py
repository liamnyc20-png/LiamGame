from random import randint
cnt = 0
game_over = False
apple = Actor("apple")
def draw():
    screen.clear()
    apple.draw()

    if game_over:
        screen.fill("black")
        screen.draw.text("Score: " + str(cnt), color = "white", topleft = (10, 10))

def place_apple():
    apple.x = randint(100, 800)
    apple.y = randint(100, 600)

def time_up():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global cnt
    if apple.collidepoint(pos):
        print("Good Shot!")
        cnt += 1
        place_apple()
    else:
        print("You Missed!")
        print(cnt)
        time_up

clock.schedule(time_up, 10.0)
place_apple()