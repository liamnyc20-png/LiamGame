import time
import random
import math
import pygame

WIDTH = 1920
HEIGHT = 1080

superman_alive = True
batman_alive = True
flash_alive = True
joker_alive = True
guy_alive = True

batman = Actor("actual-batman-maybe")
batman.x = 960
batman.y = 540
bac = 0

superman = Actor("supermanmaybe")
while (True):
    superman.x = random.randint(0, WIDTH)
    superman.y = random.randint(0, HEIGHT)
    if (abs(superman.x - batman.x) > 200 and abs(superman.y - batman.y) > 200):
        break

flash = Actor("flashmaybe")
while (True):
    flash.x = random.randint(0, WIDTH)
    flash.y = random.randint(0, HEIGHT)
    if (abs(flash.x - batman.x) > 200 and abs(flash.y - batman.y) > 200):
        break
flash_phase = False
fpf = 0

# cooldowns
fpc = 0
fpt = 0

flash_bad = False

guy = Actor("papamaybe")
while (True):
    guy.x = random.randint(0, WIDTH)
    guy.y = random.randint(0, HEIGHT)
    if (abs(guy.x - batman.x) > 200 and abs(guy.y - batman.y) > 200):
        break

joker = Actor("jokerbettermaybe")
while (True):
    joker.x = random.randint(0, WIDTH)
    joker.y = random.randint(0, HEIGHT)
    if (abs(joker.x - batman.x) > 200 and abs(joker.y - batman.y) > 200):
        break
joker_helper = Actor("jokersmen")
joker_helper.x = -100
joker_helper.y = -100
joker_helper_alive = False
boom = Actor("boomfx")
boom.x = -100
boom.y = -100
boom_wait = 0

joker_upmiddle = Actor("upmiddlecard")
joker_upleft = Actor("upleft")
joker_upright = Actor("upright")

Joker_downmiddle = Actor("downmiddlecard")
joker_downleft = Actor("downleft")
joker_upright = Actor("downright")

joker_leftmiddle = Actor("leftmiddlecard")
joker_leftbottom = Actor("leftbottom")
joker_lefttop = Actor("lefttop")

joker_rightmiddle = Actor("rightmiddlecard")
joker_rightbottom = Actor("rightbottomn")
joker_righttop = Actor("righttop")

superman_stun = 0
batman_stun = 0
guy_stun = 0
ice_cooldown = 0

batarang = Actor("batarang-downleft")
batarang.x = -100
batarang.y = -100
batarang_throw = False
batarang_dir = 0
batarang_frame = 0
batarang_frame_skip = 0
breturn = False
bpull = 0
batman_faces = 0
superman_faces = 0
flash_faces = 0

lasersuperman = Rect((0, 0), (1500, 8))
lasersuperman.x = -100
lasersuperman.y = -100
lasersuperman_dir = 0

superman_hearts = Actor("supermanheart3")
if superman_alive == True:
    superman_hearts.x = 1450
    superman_hearts.y = 50
else:
    superman_hearts.x = -100
    superman_hearts.y = -100

batman_hearts = Actor("batmanheart3")
batman_hearts.x = 1500
batman_hearts.y = 50

flash_hearts = Actor("flashheart3")
flash_hearts.x = 1550
flash_hearts.y = 50

joker_hearts = Actor("jokerheart3")
joker_hearts.x = 1600
joker_hearts.y = 50

guy_hearts = Actor("guyheart3")
guy_hearts.x = 1650
guy_hearts.y = 50

superman_lives = 3
batman_lives = 3
flash_lives = 3
joker_lives = 3
guy_lives = 3

start_time = time.time()
end_time = 0

superman_slowed = False
batman_stunned = 0
superman_confused = False
batman_confused = False
flash_stunned = 0
flash_confused = False 
guy_stunned = 0
guy_confused = False
joker_confused = False
joker_stunned = 0

game_over = False

music.play("tag-game-music1")
music.set_volume(0.2)

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
        superman.draw()
        batman.draw()
        flash.draw()
        guy.draw()
        joker.draw()
        superman_hearts.draw()
        batman_hearts.draw()
        flash_hearts.draw()
        joker_hearts.draw()
        guy_hearts.draw()
        batarang.draw()
        joker_helper.draw()
        boom.draw()
        screen.draw.filled_rect(lasersuperman, "red")
        for i in range(0, NUM_LIGHTNING):
            lightning[i].draw()

def update():
    global HEIGHT, WIDTH, superman, batman, flash, guy, joker, superman_stun, batman_stun, ice_cooldown, superman_lives, superman_hearts, game_over, superman_slowed, batman_stunned \
    , batarang, batarang_dir, batarang_throw, batman_faces, superman_faces, flash_faces, batarang_frame, batarang_frame_skip, breturn, superman_confused \
    , bpull, flash_stunned, flash_confused, flash_phase, fpf, guy_stunned, guy_confused, joker_confused, joker_stunned, batman_lives, batman_hearts, flash_lives, flash_hearts, joker_lives \
    , joker_hearts, guy_lives, guy_hearts, superman_alive, batman_alive, flash_alive, joker_alive, guy_alive, bac, fpc, fpt, joker_helper, joker_helper_alive, flash_bad, boom, boom_wait
    #do run cycles
    if game_over:
        return
    
    superman_batman_distance = (abs(superman.x - batman.x)) + (abs(superman.y - batman.y))
    superman_flash_distance = (abs(superman.x - flash.x)) + (abs(superman.y - flash.y))
    batman_flash_distance = (abs(batman.x - flash.x)) + (abs(batman.y - flash.y))
    sounds.lightning_collide.set_volume(0.1)

    for i in range(0, NUM_LIGHTNING):
        lightning[i].y += 5
        if lightning[i].y > HEIGHT:
            lightning[i].y = 0
            if (random.randint(0,1) == 0):
                lightning[i].x = random.randint(int(max(superman.x - 500, 0)), int(min(superman.x + 500, WIDTH)))
            else:
                lightning[i].x = random.randint(int(max(batman.x - 500, 0)), int(min(batman.x + 500, WIDTH)))

    superman_position = (superman.x, superman.y)
    superman_hearts_pos = (superman_hearts.x, superman_hearts.y)
    batman_position = (batman.x, batman.y)
    batman_hearts_pos = (batman_hearts.x, batman_hearts.y)
    flash_position = (flash.x, flash.y)
    flash_hearts_pos = (flash_hearts.x, flash_hearts.y)
    guy_position = (guy.x, guy.y)
    guy_hearts_pos = (guy_hearts.x, guy_hearts.y)
    joker_position = (joker.x, joker.y)
    joker_hearts_pos = (joker_hearts.x, joker_hearts.y)
    joker_helper_position = (joker_helper.x, joker_helper.y)

    for i in range(0, NUM_LIGHTNING):
        if superman.colliderect(lightning[i]):
            if (random.randint(0,1) == 0):
                lightning[i].x = random.randint(int(max(superman.x - 500, 0)), int(min(superman.x + 500, WIDTH)))
            else:
                lightning[i].x = random.randint(int(max(batman.x - 500, 0)), int(min(batman.x + 500, WIDTH)))
            lightning[i].y = 0
            sounds.lightning_collide.set_volume(0.1)
            sounds.lightning_collide.play(1)
            superman_stun = time.time()

    if superman_alive == True:
        if time.time() - superman_stun > 0.5:
                if keyboard.a and keyboard.w:
                    if superman_slowed:
                        superman = Actor("superman-kryptonice")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x += 2
                            superman.y += 2
                        else:
                            superman.x -= 2
                            superman.y -= 2
                    else:
                        superman = Actor("supermanmaybe")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x += 3.5
                            superman.y += 3.5
                        else:
                            superman.x -= 3.5
                            superman.y -= 3.5
                    superman_faces = 1

                elif keyboard.a and keyboard.s:
                    if superman_slowed:
                        superman = Actor("superman-kryptonice")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x += 2
                            superman.y -= 2
                        else:
                            superman.x -= 2
                            superman.y += 2
                    else:
                        superman = Actor("supermanmaybe")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x += 3.5
                            superman.y -= 3.5
                        else:
                            superman.x -= 3.5
                            superman.y += 3.5
                    superman_faces = 7

                elif keyboard.d and keyboard.w:
                    if superman_slowed:
                        superman = Actor("superman-kryptonice")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x -= 2
                            superman.y += 2
                        else:
                            superman.x += 2
                            superman.y -= 2
                    else:
                        superman = Actor("supermanmaybe")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x -= 3.5
                            superman.y += 3.5
                        else:
                            superman.x += 3.5
                            superman.y -= 3.5
                    superman_faces = 3

                elif keyboard.d and keyboard.s:
                    if superman_slowed:
                        superman = Actor("superman-kryptonice")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x -= 2
                            superman.y -= 2
                        else:
                            superman.x += 2
                            superman.y += 2
                    else:
                        superman = Actor("supermanmaybe")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x -= 3.5
                            superman.y -= 3.5
                        else:
                            superman.x += 3.5
                            superman.y += 3.5
                    superman_faces = 5

                elif keyboard.a:
                    if superman_slowed:
                        superman = Actor("superman-kryptonice")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x += 3
                        else:
                            superman.x -= 3
                    else:
                        superman = Actor("supermanmaybe")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x += 5
                        else:
                            superman.x -= 5
                    superman_faces = 8

                elif keyboard.d:
                    if superman_slowed == True:
                        superman = Actor("superman-kryptonice")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x -= 5
                        else:
                            superman.x += 3
                    else:
                        superman = Actor("supermanmaybe")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x -= 5
                        else:
                            superman.x += 5
                    superman_faces = 4

                elif keyboard.w:
                    if superman_slowed:
                        superman = Actor("superman-kryptonice")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.y += 3
                        else:
                            superman.y -= 3
                    else:
                        superman = Actor("supermanmaybe")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.y += 5
                        else:
                            superman.y -= 5
                    superman_faces = 2

                elif keyboard.s:
                    if superman_slowed:
                        superman = Actor("superman-kryptonice")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.y -= 3
                        else:
                            superman.y += 3
                    else:
                        superman = Actor("supermanmaybe")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.y -= 5
                        else:
                            superman.y += 5
                    superman_faces = 6

                else:
                    if superman_slowed:
                        superman = Actor("superman-kryptonice")
                    else:
                        superman = Actor("supermanmaybe")
                    superman.pos = superman_position
                superman_stun = 0

        superman_position = (superman.x, superman.y)
    # if keyboard.space:
    #     if time.time() - ice_cooldown > 10:
    #         superman.x = random.randint(int(superman.x - 500), int(superman.x + 500))
    #         superman.y = random.randint(int(superman.y - 500), int(superman.y + 500))
    #         ice_cooldown = time.time()
    if superman_confused == False:
        if time.time() - ice_cooldown > 8:
            if superman_batman_distance <= 400 or superman_flash_distance <= 400:
                superman = Actor("superman-ice")
                superman.pos = superman_position
                if keyboard.q:
                    superman = Actor("superman-icebreath")
                    superman.pos = superman_position
                    if superman_batman_distance <= 400:
                        batman_stunned = time.time()
                    elif superman_flash_distance <= 400 and flash_phase == False:
                        flash_stunned = time.time()
                    elif superman_batman_distance <= 400 and superman_flash_distance <= 400 and flash_phase == False:
                        batman_stunned = time.time()
                        flash_stunned = time.time()
                    elif superman_batman_distance <= 400 and superman_flash_distance <= 400 and flash_phase == True:
                        batman_stunned = time.time
                    batman = Actor("batman-frozen")
                    batman.pos = batman_position
                    ice_cooldown = time.time()
                    sounds.superman_ice_sfx.play(1)

    if time.time() - batman_stunned <= 3.0:
        superman = Actor("superman-icebreath")
        superman.pos = superman_position

    if superman_slowed == True and superman_batman_distance <= 400:
        superman = Actor("superman-kryptonice")
        superman.pos = superman_position
    elif superman_slowed == False and superman_batman_distance <= 400:
        superman = Actor("superman-ice")
        superman.pos = superman_position
    elif superman_slowed == False and superman_batman_distance > 400:
        superman = Actor("supermanmaybe")
        superman.pos = superman_position

    if keyboard.e:
        lasersuperman_dir = superman_faces

        if lasersuperman_dir == 2:
            lasersuperman.width = 8
            lasersuperman.height = superman.y - 15
            lasersuperman.x = superman.x - 5
            lasersuperman.y = 0

        elif lasersuperman_dir == 6:
            lasersuperman.width = 8
            lasersuperman.height = HEIGHT - superman.y
            lasersuperman.x = superman.x - 5
            lasersuperman.y = superman.y - 15

        elif lasersuperman_dir == 4:
            lasersuperman.width = WIDTH - superman.x
            lasersuperman.height = 8
            lasersuperman.x = superman.x
            lasersuperman.y = superman.y - 23

        elif lasersuperman_dir == 8:
            lasersuperman.width = superman.x
            lasersuperman.height = 8
            lasersuperman.x = 0
            lasersuperman.y = superman.y - 23

    else:
        lasersuperman.x = -100
        lasersuperman.y = -100

    if batman.colliderect(lasersuperman):
        if lasersuperman_dir == 2 or lasersuperman_dir == 6:
            if batman.y > superman.y:
                batman.y += 10
            elif batman.y < superman.y:
                batman.y -= 10
        elif lasersuperman_dir == 4 or lasersuperman_dir == 8:
            if batman.x > superman.x:
                batman.x += 10
            elif batman.x < superman.x:
                batman.x -= 10

    if flash_phase == False:
        if flash.colliderect(lasersuperman):
            if lasersuperman_dir == 2 or lasersuperman_dir == 6:
                if flash.y > superman.y:
                    flash.y += 10
                elif flash.y < superman.y:
                    flash.y -= 10
            elif lasersuperman_dir == 4 or lasersuperman_dir == 8:
                if flash.x > superman.x:
                    flash.x += 10
                elif flash.x < superman.x:
                    flash.x -= 10
    
    # if keyboard.f:
    #     WIDTH = 1920
    #     HEIGHT = 1080
    #     pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    # if keyboard.escape:
    #     exit()

    flash_position = (flash.x, flash.y)
    batman_position = (batman.x, batman.y)
    joker_position = (joker.x, joker.y)

    for i in range(0, NUM_LIGHTNING):
        if batman.colliderect(lightning[i]):
            if (random.randint(0,1) == 0):
                lightning[i].x = random.randint(int(max(superman.x - 500, 0)), int(min(superman.x + 500, WIDTH)))
            else:
                lightning[i].x = random.randint(int(max(batman.x - 500, 0)), int(min(batman.x + 500, WIDTH)))
            lightning[i].y = 0
            sounds.lightning_collide.set_volume(0.1)
            sounds.lightning_collide.play(1)
            batman_stun = time.time()

    if batman_alive == True:
        if time.time() - batman_stun > 0.5 and time.time() - batman_stunned > 3.0:
            if keyboard.left and keyboard.up:
                if superman_batman_distance <= 300:
                    batman = Actor("batman-kryptonite")
                else:
                    batman = Actor("actual-batman-maybe")
                batman.pos = batman_position
                batman.x -= 3.5
                batman.y -= 3.5
                batman_faces = 1
            elif keyboard.left and keyboard.down:
                if superman_batman_distance <= 300:
                    batman = Actor("batman-kryptonite")
                else:
                    batman = Actor("actual-batman-maybe")
                batman.pos = batman_position
                batman.x -= 3.5
                batman.y += 3.5
                batman_faces = 7
            elif keyboard.right and keyboard.up:
                if superman_batman_distance <= 300:
                    batman = Actor("batman-kryptonite")
                else:
                    batman = Actor("actual-batman-maybe")
                batman.pos = batman_position
                batman.x += 3.5
                batman.y -= 3.5
                batman_faces = 3
            elif keyboard.right and keyboard.down:
                if superman_batman_distance <= 300:
                    batman = Actor("batman-kryptonite")
                else:
                    batman = Actor("actual-batman-maybe")
                batman.pos = batman_position
                batman.x += 3.5
                batman.y += 3.5
                batman_faces = 5
            elif keyboard.left:
                if superman_batman_distance <= 300:
                    batman = Actor("batman-kryptonite")
                else:
                    batman = Actor("actual-batman-maybe")
                batman.pos = batman_position
                batman.x -= 5
                batman_faces = 8
            elif keyboard.right:
                if superman_batman_distance <= 300:
                    batman = Actor("batman-kryptonite")
                else:
                    batman = Actor("actual-batman-maybe")
                batman.pos = batman_position
                batman.x += 5
                batman_faces = 4
            elif keyboard.up:
                if superman_batman_distance <= 300:
                    batman = Actor("batman-kryptonite")
                else:
                    batman = Actor("actual-batman-maybe")
                batman.pos = batman_position
                batman.y -= 5
                batman_faces = 2
            elif keyboard.down:
                if superman_batman_distance <= 300:
                    batman = Actor("batman-kryptonite")
                else:
                    batman = Actor("actual-batman-maybe")
                batman.pos = batman_position
                batman.y += 5
                batman_faces = 6
            else:
                if superman_batman_distance <= 300:
                    batman = Actor("batman-kryptonite")
                else:
                    batman = Actor("actual-batman-maybe")
                batman.pos = batman_position
            batman_stun = 0
            batman_stunned = 0

        batman_position = (batman.x, batman.y)

    superman_batman_distance = (abs(superman.x - batman.x)) + (abs(superman.y - batman.y))
    superman_flash_distance = (abs(superman.x - flash.x)) + (abs(superman.y - flash.y))
    superman_joker_distance = (abs(superman.x - joker.x)) + (abs(superman.y - joker.y))
    superman_guy_distance = (abs(superman.x - guy.x)) + (abs(superman.y - guy.y))
    superman_joker_helper_distance = (abs(superman.x - joker_helper.x)) + (abs(superman.y - joker_helper.y))

    batman_flash_distance = (abs(batman.x - flash.x)) + (abs(batman.y - flash.y))
    batman_joker_distance = (abs(batman.x - joker.x)) + (abs(batman.y - joker.y))
    batman_guy_distance = (abs(batman.x - guy.x)) + (abs(batman.y - guy.y))
    batman_joker_helper_distance = (abs(batman.x - joker_helper.x)) + (abs(batman.y - joker_helper.y))

    flash_joker_distance = (abs(flash.x - joker.x)) + (abs(flash.y - joker.y))
    flash_guy_distance = (abs(flash.x - guy.x)) + (abs(flash.y - guy.y))
    flash_joker_helper_distance = (abs(flash.x - joker_helper.x)) + (abs(flash.y - joker_helper.y))

    joker_guy_distance = (abs(joker.x - guy.x)) + (abs(joker.y - guy.y))
    joker_joker_helper_distance = (abs(joker.x - joker_helper.x)) + (abs(joker.y - joker_helper.y))

    guy_joker_helper_distance = (abs(guy.x - joker_helper.x)) + (abs(guy.y - joker_helper.y))

    # superman_batman_distance_left = (abs(superman.x - (batman.x - 6))) + (abs(superman.y - batman.y))
    # superman_batman_distance_right = (abs(superman.x - (batman.x + 6))) + (abs(superman.y - batman.y))
    # superman_batman_distance_up = (abs(superman.x - batman.x)) + (abs(superman.y - (batman.y - 6)))
    # superman_batman_distance_down = (abs(superman.x - batman.x)) + (abs(superman.y - (batman.y + 6)))
    
    if keyboard.K_2:
        if superman_batman_distance <= 300:
            if time.time() - batman_stunned > 3.0:
                superman_slowed = True

    if superman_batman_distance > 300:
        superman_slowed = False

    if flash_alive == True:
        if time.time() - flash_stunned > 4.0:
            if keyboard.j and keyboard.i:
                flash = Actor("flashmaybe")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.x += 4
                    flash.y += 4
                else:
                    flash.x -= 4
                    flash.y -= 4
                flash_faces = 1
            elif keyboard.j and keyboard.k:
                flash = Actor("flashmaybe")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.x += 4
                    flash.y -= 4
                else:
                    flash.x -= 4
                    flash.y += 4
                flash_faces = 7
            elif keyboard.l and keyboard.i:
                flash = Actor("flashmaybe")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.x -= 4
                    flash.y += 4
                else:
                    flash.x += 4
                    flash.y -= 4
                flash_faces = 3
            elif keyboard.l and keyboard.k:
                flash = Actor("flashmaybe")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.x -= 4
                    flash.y -= 4
                else:
                    flash.x += 4
                    flash.y += 4
                flash_faces = 5
            elif keyboard.j:
                flash = Actor("flashmaybe")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.x += 5.5
                else:
                    flash.x -= 5.5
                flash_faces = 8
            elif keyboard.l:
                flash = Actor("flashmaybe")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.x -= 5.5
                else:
                    flash.x += 5.5
                flash_faces = 4
            elif keyboard.i:
                flash = Actor("flashmaybe")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.y += 5.5
                else:
                    flash.y -= 5.5
                flash_faces = 2
            elif keyboard.k:
                flash = Actor("flashmaybe")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.y -= 5.5
                else:
                    flash.y += 5.5
                flash_faces = 6
            else:
                flash = Actor("flashmaybe")
                flash.pos = flash_position

            flash_position = (flash.x, flash.y)

    if flash_bad == False:
        if keyboard.u:
            if flash_faces == 1:
                if flash_confused == True:
                    flash.x += 8
                    flash.y += 8
                else:
                    flash.x -= 8
                    flash.y -= 8
            elif flash_faces == 2:
                if flash_confused == True:
                    flash.y += 11
                else:
                    flash.y -= 11
            elif flash_faces == 3:
                if flash_confused == True:
                    flash.x -= 8
                    flash.y += 8
                else:
                    flash.x += 8
                    flash.y -= 8 
            elif flash_faces == 4:
                if flash_confused == True:
                    flash.x -= 11
                else:
                    flash.x += 11
            elif flash_faces == 5:
                if flash_confused == True:
                    flash.x -= 8
                    flash.y -= 8
                else:
                    flash.x += 8
                    flash.y += 8
            elif flash_faces == 6:
                if flash_confused == True:
                    flash.y -= 11
                else:
                    flash.y += 11
            elif flash_faces == 7:
                if flash_confused == True:
                    flash.x += 8
                    flash.y -= 8
                else:
                    flash.x -= 8
                    flash.y += 8
            elif flash_faces == 8:
                if flash_confused == True:
                    flash.x += 11
                else:
                    flash.x -= 11

    if flash_bad == False:
        if flash_phase == False:
            if time.time() - fpc > 8.0:
                if keyboard.o:
                    flash_phase = True
                    fpc = time.time()
                    fpt = time.time()

    if flash_phase == True:
        if time.time() - fpt <= 3.0:
            if fpf == 0:
                flash = Actor("flashphase")
                flash.pos = flash_position
                fpf = 1
            elif fpf == 1:
                flash = Actor("flashphaseleft")
                flash.pos = flash_position
                fpf = 0
        else:   
            fpt = time.time()
            fpc = time.time()
            flash_phase = False

    if guy_alive == True:
        if time.time() - guy_stunned > 4.0:
            if keyboard.f and keyboard.t:
                guy = Actor("papamaybe")
                guy.pos = guy_position
                if guy_confused == True:
                    guy.x += 3.5
                    guy.y += 3.5
                else:
                    guy.x -= 3.5
                    guy.y -= 3.5
                guy_faces = 1
            elif keyboard.f and keyboard.g:
                guy = Actor("papamaybe")
                guy.pos = guy_position
                if guy_confused == True:
                    guy.x += 3.5
                    guy.y -= 3.5
                else:
                    guy.x -= 3.5
                    guy.y += 3.5
                guy_faces = 7
            elif keyboard.h and keyboard.t:
                guy = Actor("papamaybe")
                guy.pos = guy_position
                if guy_confused == True:
                    guy.x -= 3.5
                    guy.y += 3.5
                else:
                    guy.x += 3.5
                    guy.y -= 3.5
                guy_faces = 3
            elif keyboard.h and keyboard.g:
                guy = Actor("papamaybe")
                guy.pos = guy_position
                if guy_confused == True:
                    guy.x -= 3.5
                    guy.y -= 3.5
                else:
                    guy.x += 3.5
                    guy.y += 3.5
                guy_faces = 5
            elif keyboard.f:
                guy = Actor("papamaybe")
                guy.pos = guy_position
                if guy_confused == True:
                    guy.x += 5
                else:
                    guy.x -= 5
                guy_faces = 8
            elif keyboard.h:
                guy = Actor("papamaybe")
                guy.pos = guy_position
                if guy_confused == True:
                    guy.x -= 5
                else:
                    guy.x += 5
                guy_faces = 4
            elif keyboard.t:
                guy = Actor("papamaybe")
                guy.pos = guy_position
                if guy_confused == True:
                    guy.y += 5
                else:
                    guy.y -= 5
                guy_faces = 2
            elif keyboard.g:
                guy = Actor("papamaybe")
                guy.pos = guy_position
                if guy_confused == True:
                    guy.y -= 5
                else:
                    guy.y += 5
                guy_faces = 6
            else:
                guy = Actor("papamaybe")
                guy.pos = guy_position

            guy_position = (guy.x, guy.y)

    if joker_alive == True:
        if time.time() - joker_stunned > 4.0:
            if keyboard.K_4 and keyboard.K_8:
                joker = Actor("jokerbettermaybe")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.x += 3.5
                    joker.y += 3.5
                else:
                    joker.x -= 3.5
                    joker.y -= 3.5
                joker_faces = 1
            elif keyboard.K_4 and keyboard.K_5:
                joker = Actor("jokerbettermaybe")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.x += 3.5
                    joker.y -= 3.5
                else:
                    joker.x -= 3.5
                    joker.y += 3.5
                joker_faces = 7
            elif keyboard.K_6 and keyboard.K_8:
                joker = Actor("jokerbettermaybe")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.x -= 3.5
                    joker.y += 3.5
                else:
                    joker.x += 3.5
                    joker.y -= 3.5
                joker_faces = 3
            elif keyboard.K_6 and keyboard.K_5:
                joker = Actor("jokerbettermaybe")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.x -= 3.5
                    joker.y -= 3.5
                else:
                    joker.x += 3.5
                    joker.y += 3.5
                joker_faces = 5
            elif keyboard.K_4:
                joker = Actor("jokerbettermaybe")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.x += 5
                else:
                    joker.x -= 5
                joker_faces = 8
            elif keyboard.K_6:
                joker = Actor("jokerbettermaybe")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.x -= 5
                else:
                    joker.x += 5
                joker_faces = 4
            elif keyboard.K_8:
                joker = Actor("jokerbettermaybe")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.y += 5
                else:
                    joker.y -= 5
                joker_faces = 2
            elif keyboard.K_5:
                joker = Actor("jokerbettermaybe")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.y -= 5
                else:
                    joker.y += 5
                joker_faces = 6
            else:
                joker = Actor("jokerbettermaybe")
                joker.pos = joker_position

            joker_position = (joker.x, joker.y)

    if joker_helper_alive == False:
        if keyboard.K_7:
            joker_helper_alive = True
            joker_helper_position = joker.pos
            joker_helper.x = joker.x
            joker_helper.y = joker.y

    if joker_helper_alive == True:
        if superman_alive == True:
            if (superman_joker_helper_distance < batman_joker_helper_distance or batman_alive == False) and (superman_joker_helper_distance < flash_joker_helper_distance or flash_alive == False) and (superman_joker_helper_distance < guy_joker_helper_distance or guy_alive == False):
                distance = (abs(superman.x - joker_helper.x)) + (abs(superman.y - joker_helper.y))

                distance_left = (abs(superman.x - (joker_helper.x - 6))) + (abs(superman.y - joker_helper.y))
                distance_right = (abs(superman.x - (joker_helper.x + 6))) + (abs(superman.y - joker_helper.y))
                distance_up = (abs(superman.x - joker_helper.x)) + (abs(superman.y - (joker_helper.y - 6)))
                distance_down = (abs(superman.x - joker_helper.x)) + (abs(superman.y - (joker_helper.y + 6)))

                best_moves = []
                best_moves_count = 0
                #print(best_moves)

                if distance_left <= distance_right and distance_left <= distance_up and distance_left <= distance_down:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0] - 5, joker_helper_position[1])])
                    best_moves_count += 1
                if distance_right <= distance_left and distance_right <= distance_up and distance_right <= distance_down:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0] + 5, joker_helper_position[1])])
                    best_moves_count += 1
                if distance_up <= distance_left and distance_up <= distance_right and distance_up <= distance_down:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0], joker_helper_position[1] - 5)])
                    best_moves_count += 1
                if distance_down <= distance_left and distance_down <= distance_right and distance_down <= distance_up:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0], joker_helper_position[1] + 5)])
                    best_moves_count += 1

                random_best_move = random.randint(0, best_moves_count - 1)
                #print(best_moves)
                #print(random_best_move)
                joker_helper_position = best_moves[random_best_move][0]
                joker_helper.pos = best_moves[random_best_move][1]



        if batman_alive == True:
            if (batman_joker_helper_distance < superman_joker_helper_distance or superman_alive == False) and (batman_joker_helper_distance < flash_joker_helper_distance or flash_alive == False) and (batman_joker_helper_distance + 100 < guy_joker_helper_distance or guy_alive == False):
                distance = (abs(batman.x - joker_helper.x)) + (abs(batman.y - joker_helper.y))

                distance_left = (abs(batman.x - (joker_helper.x - 6))) + (abs(batman.y - joker_helper.y))
                distance_right = (abs(batman.x - (joker_helper.x + 6))) + (abs(batman.y - joker_helper.y))
                distance_up = (abs(batman.x - joker_helper.x)) + (abs(batman.y - (joker_helper.y - 6)))
                distance_down = (abs(batman.x - joker_helper.x)) + (abs(batman.y - (joker_helper.y + 6)))

                best_moves = []
                best_moves_count = 0
                #print(best_moves)

                if distance_left <= distance_right and distance_left <= distance_up and distance_left <= distance_down:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0] - 5, joker_helper_position[1])])
                    best_moves_count += 1
                if distance_right <= distance_left and distance_right <= distance_up and distance_right <= distance_down:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0] + 5, joker_helper_position[1])])
                    best_moves_count += 1
                if distance_up <= distance_left and distance_up <= distance_right and distance_up <= distance_down:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0], joker_helper_position[1] - 5)])
                    best_moves_count += 1
                if distance_down <= distance_left and distance_down <= distance_right and distance_down <= distance_up:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0], joker_helper_position[1] + 5)])
                    best_moves_count += 1

                random_best_move = random.randint(0, best_moves_count - 1)
                #print(best_moves)
                #print(random_best_move)
                joker_helper_position = best_moves[random_best_move][0]
                joker_helper.pos = best_moves[random_best_move][1]



        if flash_alive == True:
            if (flash_joker_helper_distance < superman_joker_helper_distance or superman_alive == False) and (flash_joker_helper_distance < batman_joker_helper_distance or batman_alive == False) and (flash_joker_helper_distance < guy_joker_helper_distance or guy_alive == False):
                distance = (abs(flash.x - joker_helper.x)) + (abs(flash.y - joker_helper.y))

                distance_left = (abs(flash.x - (joker_helper.x - 6))) + (abs(flash.y - joker_helper.y))
                distance_right = (abs(flash.x - (joker_helper.x + 6))) + (abs(flash.y - joker_helper.y))
                distance_up = (abs(flash.x - joker_helper.x)) + (abs(flash.y - (joker_helper.y - 6)))
                distance_down = (abs(flash.x - joker_helper.x)) + (abs(flash.y - (joker_helper.y + 6)))

                best_moves = []
                best_moves_count = 0
                #print(best_moves)

                if distance_left <= distance_right and distance_left <= distance_up and distance_left <= distance_down:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0] - 5, joker_helper_position[1])])
                    best_moves_count += 1
                if distance_right <= distance_left and distance_right <= distance_up and distance_right <= distance_down:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0] + 5, joker_helper_position[1])])
                    best_moves_count += 1
                if distance_up <= distance_left and distance_up <= distance_right and distance_up <= distance_down:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0], joker_helper_position[1] - 5)])
                    best_moves_count += 1
                if distance_down <= distance_left and distance_down <= distance_right and distance_down <= distance_up:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0], joker_helper_position[1] + 5)])
                    best_moves_count += 1

                random_best_move = random.randint(0, best_moves_count - 1)
                #print(best_moves)
                #print(random_best_move)
                joker_helper_position = best_moves[random_best_move][0]
                joker_helper.pos = best_moves[random_best_move][1]



        if guy_alive == True:
            if (guy_joker_helper_distance < superman_joker_helper_distance or superman_alive == False) and (guy_joker_helper_distance < batman_joker_helper_distance or batman_alive == False) and (guy_joker_helper_distance < flash_joker_helper_distance or flash_alive == False):
                distance = (abs(guy.x - joker_helper.x)) + (abs(guy.y - joker_helper.y))

                distance_left = (abs(guy.x - (joker_helper.x - 6))) + (abs(guy.y - joker_helper.y))
                distance_right = (abs(guy.x - (joker_helper.x + 6))) + (abs(guy.y - joker_helper.y))
                distance_up = (abs(guy.x - joker_helper.x)) + (abs(guy.y - (joker_helper.y - 6)))
                distance_down = (abs(guy.x - joker_helper.x)) + (abs(guy.y - (joker_helper.y + 6)))

                best_moves = []
                best_moves_count = 0
                #print(best_moves)

                if distance_left <= distance_right and distance_left <= distance_up and distance_left <= distance_down:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0] - 5, joker_helper_position[1])])
                    best_moves_count += 1
                if distance_right <= distance_left and distance_right <= distance_up and distance_right <= distance_down:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0] + 5, joker_helper_position[1])])
                    best_moves_count += 1
                if distance_up <= distance_left and distance_up <= distance_right and distance_up <= distance_down:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0], joker_helper_position[1] - 5)])
                    best_moves_count += 1
                if distance_down <= distance_left and distance_down <= distance_right and distance_down <= distance_up:
                    best_moves.append([Actor("jokersmen"), (joker_helper_position[0], joker_helper_position[1] + 5)])
                    best_moves_count += 1

                random_best_move = random.randint(0, best_moves_count - 1)
                #print(best_moves)
                #print(random_best_move)
                joker_helper_position = best_moves[random_best_move][0]
                joker_helper.pos = best_moves[random_best_move][1]



    if keyboard.K_9 and joker_helper_alive == True and (superman_joker_helper_distance < 200 or batman_joker_helper_distance < 200 or flash_joker_helper_distance < 200 or guy_joker_helper_distance < 200):
        if superman_joker_helper_distance < 200:
            if superman.x > joker_helper.x:
                superman.x += 50
            elif superman.x < joker_helper.x:
                superman.x -= 50
            if superman.y > joker_helper.y:
                superman.y += 50
            elif superman.y < joker_helper.y:
                superman.y -= 50

        if batman_joker_helper_distance < 200:
            if batman.x > joker_helper.x:
                batman.x += 100
            elif batman.x < joker_helper.x:
                batman.x -= 100
            if batman.y > joker_helper.y:
                batman.y += 100
            elif batman.y < joker_helper.y:
                batman.y -= 100

        if flash_joker_helper_distance < 200:
            if flash.x > joker_helper.x:
                flash.x += 100
            elif flash.x < joker_helper.x:
                flash.x -= 100
            if flash.y > joker_helper.y:
                flash.y += 100
            elif flash.y < joker_helper.y:
                flash.y -= 100

        if guy_joker_helper_distance < 200:
            if guy.x > joker_helper.x:
                guy.x += 50
            elif guy.x < joker_helper.x:
                guy.x -= 50
            if guy.y > joker_helper.y:
                guy.y += 50
            elif guy.y < joker_helper.y:
                guy.y -= 50
        

        boom.x = joker_helper.x
        boom.y = joker_helper.y
        joker_helper_alive = False
        joker_helper.x = -100
        joker_helper.y = -100
        boom_wait = time.time()

    if time.time() - boom_wait > 0.5:
        boom.x = -100
        boom.y = -100



    if keyboard.K_0:


    # if joker_helper.colliderect(superman):
    #     joker_helper.x = -100
    #     joker_helper.y = -100
    #     joker_helper_alive = False
    #     if superman.x > joker

    # if joker_helper.colliderect(batman):
    #     pass

    # if joker_helper.colliderect(flash):
    #     flash_bad = True
    #     joker_helper.x = -100
    #     joker_helper.y = -100
    #     joker_helper_alive = False

    # if joker_helper.colliderect(guy):
    #     pass

    if keyboard.K_1 and batarang_throw == False:
        if batman_faces == 0:
            batarang.pos = batman.pos
            batarang_throw = True
            batarang_dir = random.randint(1, 8)
        else:
            batarang.pos = batman.pos
            batarang_throw = True
            batarang_dir = batman_faces

    if batarang_throw == True:
        batarang_frame_skip = (batarang_frame_skip + 1) % 3
        if batarang_dir == 1:
            batarang.x -= 7
            batarang.y -= 7
            if batarang_frame_skip == 0:
                batarang_frame = (batarang_frame + 1) % 4
        elif batarang_dir == 2:
            batarang.y -= 10
            if batarang_frame_skip == 0:
                batarang_frame = (batarang_frame + 1) % 4
        elif batarang_dir == 3:
            batarang.x += 7
            batarang.y -= 7
            if batarang_frame_skip == 0:
                batarang_frame = (batarang_frame + 1) % 4
        elif batarang_dir == 4:
            batarang.x += 10
            if batarang_frame_skip == 0:
                batarang_frame = (batarang_frame + 1) % 4
        elif batarang_dir == 5:
            batarang.x += 7
            batarang.y += 7
            if batarang_frame_skip == 0:
                batarang_frame = (batarang_frame + 1) % 4
        elif batarang_dir == 6:
            batarang.y += 10
            if batarang_frame_skip == 0:
                batarang_frame = (batarang_frame + 1) % 4
        elif batarang_dir == 7:
            batarang.x -= 7
            batarang.y += 7
            if batarang_frame_skip == 0:
                batarang_frame = (batarang_frame + 1) % 4
        elif batarang_dir == 8:
            batarang.x -= 10
            if batarang_frame_skip == 0:
                batarang_frame = (batarang_frame + 1) % 4

    batarang_position = (batarang.x, batarang.y)

    if batarang_throw == True:
        if batarang_frame == 0:
            batarang = Actor("batarang-upleft")
            batarang.pos = batarang_position
        elif batarang_frame == 1:
            batarang = Actor("batarang-upright")
            batarang.pos = batarang_position
        elif batarang_frame == 2:
            batarang = Actor("batarang-downright")
            batarang.pos = batarang_position
        elif batarang_frame == 3:
            batarang = Actor("batarang-downleft")
            batarang.pos = batarang_position

        batarang.pos = batarang_position

    if superman.x > WIDTH:
        superman.x = WIDTH
    elif superman.x < 0:
        superman.x = 0
    
    if superman.y > HEIGHT:
        superman.y = HEIGHT
    elif superman.y < 0:
        superman.y = 0

    if batman.x > WIDTH:
        batman.x = WIDTH
    elif batman.x < 0:
        batman.x = 0
    
    if batman.y > HEIGHT:
        batman.y = HEIGHT
    elif batman.y < 0:
        batman.y = 0

    if flash.x > WIDTH:
        flash.x = WIDTH
    elif flash.x < 0:
        flash.x = 0
    
    if flash.y > HEIGHT:
        flash.y = HEIGHT
    elif flash.y < 0:
        flash.y = 0

    if guy.x > WIDTH:
        guy.x = WIDTH
    elif guy.x < 0:
        guy.x = 0

    if guy.y > WIDTH:
        guy.y = WIDTH
    elif guy.y < 0:
        guy.y = 0

    if joker.x > WIDTH:
        joker.x = WIDTH
    elif joker.x < 0:
        joker.x = 0

    if joker.y > WIDTH:
        joker.y = WIDTH
    elif joker.y < 0:
        joker.y = 0

    # if batarang.x > WIDTH:
    #     batarang.x = WIDTH
    # elif batarang.x < 0:
    #     batarang.x = 0
    
    # if batarang.y > HEIGHT:
    #     batarang.y = HEIGHT
    # elif batarang.y < 0:
    #     batarang.y = 0

    if batarang.x >= WIDTH or batarang.x <= 0 or batarang.y >= HEIGHT or batarang.y <= 0:
            breturn = True
            if batarang_dir == 1:
                batarang_dir = 5
            elif batarang_dir == 2:
                batarang_dir = 6
            elif batarang_dir == 3:
                batarang_dir = 7
            elif batarang_dir == 4:
                batarang_dir = 8
            elif batarang_dir == 5:
                batarang_dir = 1
            elif batarang_dir == 6:
                batarang_dir = 2
            elif batarang_dir == 7:
                batarang_dir = 3
            elif batarang_dir == 8:
                batarang_dir = 4

    if batarang.colliderect(superman) and breturn == False:
        superman_confused = True
        dx = batman.x - superman.x
        dy = batman.y - superman.y
        total_superman_batman_distance = math.sqrt(dx ** 2 + dy ** 2)
        if total_superman_batman_distance > 0 and superman_alive == True:
            bpull = 150
            superman.x += (dx / total_superman_batman_distance) * bpull
            superman.y += (dy / total_superman_batman_distance) * bpull
        breturn = True
        if batarang_dir == 1:
            batarang_dir = 5
        elif batarang_dir == 2:
            batarang_dir = 6
        elif batarang_dir == 3:
            batarang_dir = 7
        elif batarang_dir == 4:
            batarang_dir = 8
        elif batarang_dir == 5:
            batarang_dir = 1
        elif batarang_dir == 6:
            batarang_dir = 2
        elif batarang_dir == 7:
            batarang_dir = 3
        elif batarang_dir == 8:
            batarang_dir = 4
    elif batarang.colliderect(flash) and flash_phase == False and breturn == False:
        flash_confused = True
        dx = batman.x - flash.x
        dy = batman.y - flash.y
        total_batman_flash_distance = math.sqrt(dx ** 2 + dy ** 2)
        if total_batman_flash_distance > 0 and flash_alive == True:
            bpull = 150
            flash.x += (dx / total_batman_flash_distance) * bpull
            flash.y += (dy / total_batman_flash_distance) * bpull
        breturn = True
        if batarang_dir == 1:
            batarang_dir = 5
        elif batarang_dir == 2:
            batarang_dir = 6
        elif batarang_dir == 3:
            batarang_dir = 7
        elif batarang_dir == 4:
            batarang_dir = 8
        elif batarang_dir == 5:
            batarang_dir = 1
        elif batarang_dir == 6:
            batarang_dir = 2
        elif batarang_dir == 7:
            batarang_dir = 3
        elif batarang_dir == 8:
            batarang_dir = 4
    elif batarang.colliderect(joker) and breturn == False:
        joker_confused = True
        dx = batman.x - joker.x
        dy = batman.y - joker.y
        total_batman_joker_distance = math.sqrt(dx ** 2 + dy ** 2)
        if total_batman_joker_distance > 0 and joker_alive == True:
            bpull = 150
            joker.x += (dx / total_batman_joker_distance) * bpull
            joker.y += (dy / total_batman_joker_distance) * bpull
        breturn = True
        if batarang_dir == 1:
            batarang_dir = 5
        elif batarang_dir == 2:
            batarang_dir = 6
        elif batarang_dir == 3:
            batarang_dir = 7
        elif batarang_dir == 4:
            batarang_dir = 8
        elif batarang_dir == 5:
            batarang_dir = 1
        elif batarang_dir == 6:
            batarang_dir = 2
        elif batarang_dir == 7:
            batarang_dir = 3
        elif batarang_dir == 8:
            batarang_dir = 4
    elif batarang.colliderect(guy) and breturn == False:
        guy_confused = True
        dx = batman.x - guy.x
        dy = batman.y - guy.y
        total_batman_guy_distance = math.sqrt(dx ** 2 + dy ** 2)
        if total_batman_guy_distance > 0 and guy_alive == True:
            bpull = 150
            guy.x += (dx / total_batman_guy_distance) * bpull
            guy.y += (dy / total_batman_guy_distance) * bpull
        breturn = True
        if batarang_dir == 1:
            batarang_dir = 5
        elif batarang_dir == 2:
            batarang_dir = 6
        elif batarang_dir == 3:
            batarang_dir = 7
        elif batarang_dir == 4:
            batarang_dir = 8
        elif batarang_dir == 5:
            batarang_dir = 1
        elif batarang_dir == 6:
            batarang_dir = 2
        elif batarang_dir == 7:
            batarang_dir = 3
        elif batarang_dir == 8:
            batarang_dir = 4

    if batarang.colliderect(joker_helper):
        joker_helper.x = -100
        joker_helper.y = -100
        joker_helper_alive = False

    # if breturn == True:
    #     if batarang_dir == 1:
    #         batarang_dir = 5
    #     elif batarang_dir == 2:
    #         batarang_dir = 6
    #     elif batarang_dir == 3:
    #         batarang_dir = 7
    #     elif batarang_dir == 4:
    #         batarang_dir = 8
    #     elif batarang_dir == 5:
    #         batarang_dir = 1
    #     elif batarang_dir == 6:
    #         batarang_dir = 2
    #     elif batarang_dir == 7:
    #         batarang_dir = 3
    #     elif batarang_dir == 8:
    #         batarang_dir = 4

    if breturn == True and batarang.colliderect(batman):
        batarang_throw = False
        breturn = False
        batarang_frame = 0
        batarang.pos = (-100, -100)

    if time.time() - bac > 3.0:
        if batman.colliderect(superman) and (superman_lives) > 1:
            superman_lives -= 1
            bac = time.time()
        elif batman.colliderect(superman) and superman_lives == 1:
            superman_lives -= 1
            superman_alive = False
            bac = time.time()

    if flash_phase == False:
        if time.time() - bac > 3.0:
            if batman.colliderect(flash) and (flash_lives) > 1:
                flash_lives -= 1
                bac = time.time()
            elif batman.colliderect(flash) and flash_lives == 1:
                flash_lives -= 1
                flash_alive = False
                bac = time.time()

    if time.time() - bac > 3.0:
        if superman_joker_distance > 150 and flash_joker_distance > 150 and joker_guy_distance > 150:
            if batman.colliderect(joker) and (joker_lives) > 1:
                joker_lives -= 1
                bac = time.time()
            elif batman.colliderect(joker) and joker_lives == 1:
                joker_lives -= 1
                joker_alive = False
                bac = time.time()

    if time.time() - bac > 3.0:
        if batman.colliderect(guy) and (guy_lives) > 1:
            guy_lives -= 1
            bac = time.time()
        elif batman.colliderect(guy) and guy_lives == 1:
            guy_lives -= 1
            guy_alive = False
            bac = time.time() 

# superman
    if superman_lives == 3:
        superman_hearts = Actor("supermanheart3")
        superman_hearts.pos = superman_hearts_pos
    elif superman_lives == 2:
        superman_hearts = Actor("supermanheart2")
        superman_hearts.pos = superman_hearts_pos
    elif superman_lives == 1:
        superman_hearts = Actor("supermanheart1")
        superman_hearts.pos = superman_hearts_pos
    elif superman_lives == 0:
        superman_hearts.x = -100
        superman_hearts.y = -100
    else:
        superman_hearts = Actor("hearts")
        
# batman
    if batman_lives == 3:
        batman_hearts = Actor("batmanheart3")
        batman_hearts.pos = batman_hearts_pos
    elif batman_lives == 2:
        batman_hearts = Actor("batmanheart2")
        batman_hearts.pos = batman_hearts_pos
    elif batman_lives == 1:
        batman_hearts = Actor("batmanheart1")
        batman_hearts.pos = batman_hearts_pos
    elif batman_lives == 0:
        batman_hearts.x = -100
        batman_hearts.y = -100
    else:
        batman_hearts = Actor("hearts")

# flash
    if flash_lives == 3:
        flash_hearts = Actor("flashheart3")
        flash_hearts.pos = flash_hearts_pos
    elif flash_lives == 2:
        flash_hearts = Actor("flashheart2")
        flash_hearts.pos = flash_hearts_pos
    elif flash_lives == 1:
        flash_hearts = Actor("flashheart1")
        flash_hearts.pos = flash_hearts_pos
    elif flash_lives == 0:
        flash_hearts.x = -100
        flash_hearts.y = -100
    else:
        flash_hearts = Actor("hearts")

# joker
    if joker_lives == 3:
        joker_hearts = Actor("jokerheart3")
        joker_hearts.pos = joker_hearts_pos
    elif joker_lives == 2:
        joker_hearts = Actor("jokerheart2")
        joker_hearts.pos = joker_hearts_pos
    elif joker_lives == 1:
        joker_hearts = Actor("jokerheart1")
        joker_hearts.pos = joker_hearts_pos
    elif joker_lives == 0:
        joker_hearts.x = -100
        joker_hearts.y = -100
    else:
        joker_hearts = Actor("hearts")

# guy
    if guy_lives == 3:
        guy_hearts = Actor("guyheart3")
        guy_hearts.pos = guy_hearts_pos
    elif guy_lives == 2:
        guy_hearts = Actor("guyheart2")
        guy_hearts.pos = guy_hearts_pos
    elif guy_lives == 1:
        guy_hearts = Actor("guyheart1")
        guy_hearts.pos = guy_hearts_pos
    elif guy_lives == 0:
        guy_hearts.x = -100
        guy_hearts.y = -100
    else:
        guy_hearts = Actor("hearts")

    if superman_lives == 0 and batman_lives == 0 and flash_lives == 0 and joker_lives == 0 and guy_lives == 0:
        game_over = True
        end_time = time.time()
        

    if batman.colliderect(superman) and superman_alive == False:
        if batman_faces == 2:
            batman.y += 5
        if batman_faces == 4:
            batman.x -= 5
        if batman_faces == 6:
            batman.y -=5
        if batman_faces == 8:
            batman.x += 5

        if batman_faces == 1:
            batman.x += 3.5
            batman.y += 3.5
        if batman_faces == 3:
            batman.x -= 3.5
            batman.y += 3.5
        if batman_faces == 5:
            batman.x -= 3.5
            batman.y -= 3.5
        if batman_faces == 7:
            batman.x += 3.5
            batman.y -= 3.5

    if batman.colliderect(flash) and flash_alive == False:
        if batman_faces == 2:
            batman.y += 5
        if batman_faces == 4:
            batman.x -= 5
        if batman_faces == 6:
            batman.y -=5
        if batman_faces == 8:
            batman.x += 5

        if batman_faces == 1:
            batman.x += 3.5
            batman.y += 3.5
        if batman_faces == 3:
            batman.x -= 3.5
            batman.y += 3.5
        if batman_faces == 5:
            batman.x -= 3.5
            batman.y -= 3.5
        if batman_faces == 7:
            batman.x += 3.5
            batman.y -= 3.5

    if batman.colliderect(guy) and guy_alive == False:
        if batman_faces == 2:
            batman.y += 5
        if batman_faces == 4:
            batman.x -= 5
        if batman_faces == 6:
            batman.y -=5
        if batman_faces == 8:
            batman.x += 5

        if batman_faces == 1:
            batman.x += 3.5
            batman.y += 3.5
        if batman_faces == 3:
            batman.x -= 3.5
            batman.y += 3.5
        if batman_faces == 5:
            batman.x -= 3.5
            batman.y -= 3.5
        if batman_faces == 7:
            batman.x += 3.5
            batman.y -= 3.5

    if batman.colliderect(joker) and joker_alive == False:
        if batman_faces == 2:
            batman.y += 5
        if batman_faces == 4:
            batman.x -= 5
        if batman_faces == 6:
            batman.y -=5
        if batman_faces == 8:
            batman.x += 5
        
        if batman_faces == 1:
            batman.x += 3.5
            batman.y += 3.5
        if batman_faces == 3:
            batman.x -= 3.5
            batman.y += 3.5
        if batman_faces == 5:
            batman.x -= 3.5
            batman.y -= 3.5
        if batman_faces == 7:
            batman.x += 3.5
            batman.y -= 3.5


    if superman.colliderect(batman) and batman_alive == False:
        if superman_faces == 2:
            superman.y += 5
        if superman_faces == 4:
            superman.x -= 5
        if batman_faces == 6:
            superman.y -=5
        if superman_faces == 8:
            superman.x += 5

        if superman_faces == 1:
            superman.x += 3.5
            superman.y += 3.5
        if superman_faces == 3:
            superman.x -= 3.5
            superman.y += 3.5
        if superman_faces == 5:
            superman.x -= 3.5
            superman.y -= 3.5
        if superman_faces == 7:
            superman.x += 3.5
            superman.y -= 3.5

    if superman.colliderect(flash) and flash_alive == False:
        if superman_faces == 2:
            superman.y += 5
        if superman_faces == 4:
            superman.x -= 5
        if batman_faces == 6:
            superman.y -=5
        if superman_faces == 8:
            superman.x += 5

        if superman_faces == 1:
            superman.x += 3.5
            superman.y += 3.5
        if superman_faces == 3:
            superman.x -= 3.5
            superman.y += 3.5
        if superman_faces == 5:
            superman.x -= 3.5
            superman.y -= 3.5
        if superman_faces == 7:
            superman.x += 3.5
            superman.y -= 3.5

    if superman.colliderect(guy) and guy_alive == False:
        if superman_faces == 2:
            superman.y += 5
        if superman_faces == 4:
            superman.x -= 5
        if batman_faces == 6:
            superman.y -=5
        if superman_faces == 8:
            superman.x += 5

        if superman_faces == 1:
            superman.x += 3.5
            superman.y += 3.5
        if superman_faces == 3:
            superman.x -= 3.5
            superman.y += 3.5
        if superman_faces == 5:
            superman.x -= 3.5
            superman.y -= 3.5
        if superman_faces == 7:
            superman.x += 3.5
            superman.y -= 3.5

    if superman.colliderect(joker) and joker_alive == False:
        if superman_faces == 2:
            superman.y += 5
        if superman_faces == 4:
            superman.x -= 5
        if batman_faces == 6:
            superman.y -=5
        if superman_faces == 8:
            superman.x += 5

        if superman_faces == 1:
            superman.x += 3.5
            superman.y += 3.5
        if superman_faces == 3:
            superman.x -= 3.5
            superman.y += 3.5
        if superman_faces == 5:
            superman.x -= 3.5
            superman.y -= 3.5
        if superman_faces == 7:
            superman.x += 3.5
            superman.y -= 3.5

    if flash.colliderect(superman) and superman_alive == False:
        if flash_faces == 2:
            flash.y += 5
        if flash_faces == 4:
            flash.x -= 5
        if flash_faces == 6:
            flash.y -=5
        if flash_faces == 8:
            flash.x += 5

        if flash_faces == 1:
            flash.x += 3.5
            flash.y += 3.5
        if flash_faces == 3:
            flash.x -= 3.5
            flash.y += 3.5
        if flash_faces == 5:
            flash.x -= 3.5
            flash.y -= 3.5
        if flash_faces == 7:
            flash.x += 3.5
            flash.y -= 3.5

    if flash.colliderect(batman) and batman_alive == False:
        if flash_faces == 2:
            flash.y += 5
        if flash_faces == 4:
            flash.x -= 5
        if flash_faces == 6:
            flash.y -=5
        if flash_faces == 8:
            flash.x += 5

        if flash_faces == 1:
            flash.x += 3.5
            flash.y += 3.5
        if flash_faces == 3:
            flash.x -= 3.5
            flash.y += 3.5
        if flash_faces == 5:
            flash.x -= 3.5
            flash.y -= 3.5
        if flash_faces == 7:
            flash.x += 3.5
            flash.y -= 3.5

    if flash.colliderect(guy) and guy_alive == False:
        if flash_faces == 2:
            flash.y += 5
        if flash_faces == 4:
            flash.x -= 5
        if flash_faces == 6:
            flash.y -=5
        if flash_faces == 8:
            flash.x += 5

        if flash_faces == 1:
            flash.x += 3.5
            flash.y += 3.5
        if flash_faces == 3:
            flash.x -= 3.5
            flash.y += 3.5
        if flash_faces == 5:
            flash.x -= 3.5
            flash.y -= 3.5
        if flash_faces == 7:
            flash.x += 3.5
            flash.y -= 3.5

    if flash.colliderect(joker) and joker_alive == False:
        if flash_faces == 2:
            flash.y += 5
        if flash_faces == 4:
            flash.x -= 5
        if flash_faces == 6:
            flash.y -=5
        if flash_faces == 8:
            flash.x += 5

        if flash_faces == 1:
            flash.x += 3.5
            flash.y += 3.5
        if flash_faces == 3:
            flash.x -= 3.5
            flash.y += 3.5
        if flash_faces == 5:
            flash.x -= 3.5
            flash.y -= 3.5
        if flash_faces == 7:
            flash.x += 3.5
            flash.y -= 3.5

    if guy.colliderect(superman) and superman_alive == False:
        if guy_faces == 2:
            guy.y += 5
        if guy_faces == 4:
            guy.x -= 5
        if guy_faces == 6:
            guy.y -=5
        if guy_faces == 8:
            guy.x += 5

        if guy_faces == 1:
            guy.x += 3.5
            guy.y += 3.5
        if guy_faces == 3:
            guy.x -= 3.5
            guy.y += 3.5
        if guy_faces == 5:
            guy.x -= 3.5
            guy.y -= 3.5
        if guy_faces == 7:
            guy.x += 3.5
            guy.y -= 3.5

    if guy.colliderect(batman) and batman_alive == False:
        if guy_faces == 2:
            guy.y += 5
        if guy_faces == 4:
            guy.x -= 5
        if guy_faces == 6:
            guy.y -=5
        if guy_faces == 8:
            guy.x += 5

        if guy_faces == 1:
            guy.x += 3.5
            guy.y += 3.5
        if guy_faces == 3:
            guy.x -= 3.5
            guy.y += 3.5
        if guy_faces == 5:
            guy.x -= 3.5
            guy.y -= 3.5
        if guy_faces == 7:
            guy.x += 3.5
            guy.y -= 3.5
    
    if guy.colliderect(flash) and flash_alive == False:
        if guy_faces == 2:
            guy.y += 5
        if guy_faces == 4:
            guy.x -= 5
        if guy_faces == 6:
            guy.y -=5
        if guy_faces == 8:
            guy.x += 5

        if guy_faces == 1:
            guy.x += 3.5
            guy.y += 3.5
        if guy_faces == 3:
            guy.x -= 3.5
            guy.y += 3.5
        if guy_faces == 5:
            guy.x -= 3.5
            guy.y -= 3.5
        if guy_faces == 7:
            guy.x += 3.5
            guy.y -= 3.5

    if guy.colliderect(joker) and joker_alive == False:
        if guy_faces == 2:
            guy.y += 5
        if guy_faces == 4:
            guy.x -= 5
        if guy_faces == 6:
            guy.y -=5
        if guy_faces == 8:
            guy.x += 5

        if guy_faces == 1:
            guy.x += 3.5
            guy.y += 3.5
        if guy_faces == 3:
            guy.x -= 3.5
            guy.y += 3.5
        if guy_faces == 5:
            guy.x -= 3.5
            guy.y -= 3.5
        if guy_faces == 7:
            guy.x += 3.5
            guy.y -= 3.5

    if joker.colliderect(superman) and superman_alive == False:
        if joker_faces == 2:
            joker.y += 5
        if joker_faces == 4:
            joker.x -= 5
        if joker_faces == 6:
            joker.y -=5
        if joker_faces == 8:
            joker.x += 5

        if joker_faces == 1:
            joker.x += 3.5
            joker.y += 3.5
        if joker_faces == 3:
            joker.x -= 3.5
            joker.y += 3.5
        if joker_faces == 5:
            joker.x -= 3.5
            joker.y -= 3.5
        if joker_faces == 7:
            joker.x += 3.5
            joker.y -= 3.5

    if joker.colliderect(batman) and batman_alive == False:
        if joker_faces == 2:
            joker.y += 5
        if joker_faces == 4:
            joker.x -= 5
        if joker_faces == 6:
            joker.y -=5
        if joker_faces == 8:
            joker.x += 5

        if joker_faces == 1:
            joker.x += 3.5
            joker.y += 3.5
        if joker_faces == 3:
            joker.x -= 3.5
            joker.y += 3.5
        if joker_faces == 5:
            joker.x -= 3.5
            joker.y -= 3.5
        if joker_faces == 7:
            joker.x += 3.5
            joker.y -= 3.5

    if joker.colliderect(flash) and flash_alive == False:
        if joker_faces == 2:
            joker.y += 5
        if joker_faces == 4:
            joker.x -= 5
        if joker_faces == 6:
            joker.y -=5
        if joker_faces == 8:
            joker.x += 5

        if joker_faces == 1:
            joker.x += 3.5
            joker.y += 3.5
        if joker_faces == 3:
            joker.x -= 3.5
            joker.y += 3.5
        if joker_faces == 5:
            joker.x -= 3.5
            joker.y -= 3.5
        if joker_faces == 7:
            joker.x += 3.5
            joker.y -= 3.5

    if joker.colliderect(guy) and guy_alive == False:
        if joker_faces == 2:
            joker.y += 5
        if joker_faces == 4:
            joker.x -= 5
        if joker_faces == 6:
            joker.y -=5
        if joker_faces == 8:
            joker.x += 5

        if joker_faces == 1:
            joker.x += 3.5
            joker.y += 3.5
        if joker_faces == 3:
            joker.x -= 3.5
            joker.y += 3.5
        if joker_faces == 5:
            joker.x -= 3.5
            joker.y -= 3.5
        if joker_faces == 7:
            joker.x += 3.5
            joker.y -= 3.5