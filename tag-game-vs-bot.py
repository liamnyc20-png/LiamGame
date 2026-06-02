import time
import random
import pygame

WIDTH = 1920
HEIGHT = 1080

player = Actor("supermanmaybe")
player.x = 50
player.y = 50
faces = 0

run = False
direction = 0
first_direction = 0
start_position = Actor("supermanmaybe")
end_position = Actor("supermanmaybe")
start_position.x = player.x
start_position.y = player.y
end_position.x = player.x
end_position.y = player.y

start_position_position = (start_position.x, start_position.y)
end_position_position = (end_position.x, end_position.y)

starttosuperman = True

player_stun = 0
bot_stun = 0
cooldown = 0

bot = Actor("down-or-idle")
bot.x = 1450
bot.y = 900

hearts = Actor("supermanheart3")
hearts.x = 1450
hearts.y = 50

lives = 3

start_time = time.time()
end_time = 0

game_over = False

music.play("tag-game-music1")

NUM_LIGHTNING = 5

lightning = []

for _ in range(NUM_LIGHTNING):
    lightning.append(Actor("lightning"))

def draw():
    screen.clear()

    if game_over:
        global start_time, end_time
        screen.clear()
        screen.fill("black")
        screen.draw.text("Game Over!", (750, 475), color=("white"), fontsize=60)
        screen.draw.text(str(round(end_time - start_time,3)) + "s", (750, 525), color=("white"), fontsize=45)
    else:
        screen.fill("sandybrown")
        player.draw()
        bot.draw()
        hearts.draw()
        start_position.draw()
        end_position.draw()
        for i in range(0, NUM_LIGHTNING):
            lightning[i].draw()



def update():
    global player, bot, player_stun, bot_stun, cooldown, lives, hearts, game_over, run, faces, direction, first_direction, start_posititon, end_position, starttosuperman
    #do run cycles
    if game_over:
        return
    
    start_position_position = (start_position.x, start_position.y)
    end_position_position = (end_position.x, end_position.y)

    sp_distance = abs(start_position.x - player.x) + abs(start_position.y - player.y)
    ep_distance = abs(end_position.x - player.x) + abs(end_position.y - player.y)

    if starttosuperman == True:
        start_position.x = player.x
        start_position.y = player.y

    for i in range(0, NUM_LIGHTNING):
        lightning[i].y += 5
        if lightning[i].y > HEIGHT:
            lightning[i].y = 0
            lightning[i].x = random.randint(int(max(player.x - 500, 0)), int(min(player.x + 500, WIDTH)))

    player_position = (player.x, player.y)

    for i in range(0, NUM_LIGHTNING):
        if player.colliderect(lightning[i]):
            lightning[i].x = random.randint(int(max(player.x - 500, 0)), int(min(player.x + 500, WIDTH)))
            lightning[i].y = 0
            sounds.lightning_collide.play(1)
            player_stun = time.time()
            run = False

    if time.time() - player_stun > 1.0:
        if keyboard.a:
            player = Actor("supermanmaybe")
            player.pos = player_position
            player.x -= 5
            faces = 8
            direction = 8
        elif keyboard.d:
            player = Actor("supermanmaybe")
            player.pos = player_position
            player.x += 5
            faces = 4
            direction = 4
        elif keyboard.w:
            player = Actor("supermanmaybe")
            player.pos = player_position
            player.y -= 5
            faces = 2
            direction = 2
        elif keyboard.s:
            player = Actor("supermanmaybe")
            player.pos = player_position
            player.y += 5
            faces = 6
            direction = 6
        else:
            player = Actor("supermanmaybe")
            player.pos = player_position
            faces = 0
            direction = 0
        player_stun = 0

    if keyboard.q:
        if time.time() - cooldown > 10:
            player.x = random.randint(int(player.x - 500), int(player.x + 500))
            player.y = random.randint(int(player.y - 500), int(player.y + 500))
            cooldown = time.time()

    if keyboard.e:
        run = True
        first_direction = direction
        direction = 0
        start_position_position = start_position.pos

    if run == True:
        if faces == 2:
            direction = 2
            player.y -= 10
        elif faces == 4:
            direction = 4
            player.x += 10
        elif faces == 6:
            direction = 6
            player.y += 10
        elif faces == 8:
            direction = 8
            player.x -= 10
        elif faces == 0:
            direction = 0
            run = False

    if run == True and first_direction == 2:
        if faces == 4 or faces == 6 or faces == 8:
            direction = 0
            first_direction = 0
            run = False
            starttosuperman = True
    elif run == True and first_direction == 4:
        if faces == 2 or faces == 6 or faces == 8:
            direction = 0
            first_direction = 0
            run = False
            starttosuperman = True
    elif run == True and first_direction == 6:
        if faces == 2 or faces == 4 or faces == 8:
            direction = 0
            first_direction = 0
            run = False
            starttosuperman = True
    elif run == True and first_direction == 8:
        if faces == 2 or faces == 4 or faces == 6:
            direction = 0
            first_direction = 0
            run = False
            starttosuperman = True

    if sp_distance >= 300:
        direction = 0
        first_direction = 0
        run = False
        starttosuperman = True
    

    if keyboard.f:
        pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    if keyboard.escape:
        exit()

    bot_position = (bot.x, bot.y)

    for i in range(0, NUM_LIGHTNING):
        if bot.colliderect(lightning[i]):
            lightning[i].x = random.randint(int(max(player.x - 500, 0)), int(min(player.x + 500, WIDTH)))
            lightning[i].y = 0
            sounds.lightning_collide.play(1)
            bot_stun = time.time()


    if time.time() - bot_stun > 0.5:

        distance = (abs(player.x - bot.x)) + (abs(player.y - bot.y))

        distance_left = (abs(player.x - (bot.x - 6))) + (abs(player.y - bot.y))
        distance_right = (abs(player.x - (bot.x + 6))) + (abs(player.y - bot.y))
        distance_up = (abs(player.x - bot.x)) + (abs(player.y - (bot.y - 6)))
        distance_down = (abs(player.x - bot.x)) + (abs(player.y - (bot.y + 6)))

        best_moves = []
        best_moves_count = 0

        if distance_left <= distance_right and distance_left <= distance_up and distance_left <= distance_down:
            best_moves.append([Actor("left"), (bot_position[0] - 5, bot_position[1])])
            best_moves_count += 1
        if distance_right <= distance_left and distance_right <= distance_up and distance_right <= distance_down:
            best_moves.append([Actor("right"), (bot_position[0] + 5, bot_position[1])])
            best_moves_count += 1
        if distance_up <= distance_left and distance_up <= distance_right and distance_up <= distance_down:
            best_moves.append([Actor("up"), (bot_position[0], bot_position[1] - 5)])
            best_moves_count += 1
        if distance_down <= distance_left and distance_down <= distance_right and distance_down <= distance_up:
            best_moves.append([Actor("down-or-idle"), (bot_position[0], bot_position[1] + 5)])
            best_moves_count += 1

        random_best_move = random.randint(0, best_moves_count - 1)

        bot = best_moves[random_best_move][0]
        bot.pos = best_moves[random_best_move][1]

        bot_stun = 0

    if player.x > WIDTH:
        player.x = WIDTH
    elif player.x < 0:
        player.x = 0
    
    if player.y > HEIGHT:
        player.y = HEIGHT
    elif player.y < 0:
        player.y = 0

    if bot.colliderect(player) and (lives) > 1:
        lives -= 1
        player.pos = (50, 50)
        bot.pos = (1450, 900)
        for i in range(0, NUM_LIGHTNING):
            lightning[i].x = random.randint(int(max(player.x - 500, 0)), int(min(player.x + 500, WIDTH)))
            lightning[i].y = 0
        run = False
    elif bot.colliderect(player) and lives == 1:
        game_over = True
        global end_time
        end_time = time.time()

    if lives == 3:
        hearts = Actor("supermanheart3")
        hearts.x = 1450
        hearts.y = 50
    elif lives == 2:
        hearts = Actor("supermanheart2")
        hearts.x = 1450
        hearts.y = 50
    elif lives == 1:
        hearts = Actor("supermanheart1")
        hearts.x = 1450
        hearts.y = 50
    else:
        hearts = Actor("hearts")