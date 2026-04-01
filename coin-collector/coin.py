from random import randint

WIDTH = 800
HEIGHT = 600
coins = 0
game_over = False
fox = Actor("fox")
fox.pos = 400, 300

coin = Actor("coin")
coin.pos = 0, 0

def draw():
    screen.fill("blue")
    fox.draw()
    coin.draw()
    screen.draw.text("Current Score: " + str(coins), color = "black", topleft = (10, 10))

    if game_over:
        screen.fill("black")
        screen.draw.text("Final Score: " + str(coins), color = "white", topleft = (400,10), fontsize = 60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global coins

    if keyboard.left:
        fox.x = fox.x - 4
    elif keyboard.right:
        fox.x = fox.x + 4
    elif keyboard.up:
        fox.y = fox.y - 4
    elif keyboard.down:
        fox.y = fox.y + 4

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        coins = coins + 1
        place_coin()

clock.schedule(time_up, 20.0)
place_coin()