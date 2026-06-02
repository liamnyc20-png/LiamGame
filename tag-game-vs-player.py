import pgzrun
import time
import random
import math
import pygame

WIDTH = 1920
HEIGHT = 1080

superman_alive = False
batman_alive = False
flash_alive = False
joker_alive = False
guy_alive = False
luthor_alive = False
two_face_alive = False

batman = Actor("batmangood")
batman.x = 960
batman.y = 540
bac = 0

superman = Actor("supermangood")
# while (True):
#     superman.x = random.randint(0, WIDTH)
#     superman.y = random.randint(0, HEIGHT)
#     if (abs(superman.x - batman.x) > 200 and abs(superman.y - batman.y) > 200):
#         break
superman.x = 1060
superman.y = 440

flash = Actor("flashgood")
# while (True):
#     flash.x = random.randint(0, WIDTH)
#     flash.y = random.randint(0, HEIGHT)
#     if (abs(flash.x - batman.x) > 200 and abs(flash.y - batman.y) > 200):
#         break
flash.x = 1060
flash.y = 540
flash_phase = False
fpf = 0

# cooldowns
fpc = 0
fpt = 0

flash_bad = False

guy = Actor("guygood")
# while (True):
#     guy.x = random.randint(0, WIDTH)
#     guy.y = random.randint(0, HEIGHT)
#     if (abs(guy.x - batman.x) > 200 and abs(guy.y - batman.y) > 200):
#         break
guy.x = 960 
guy.y = 440
guy_faces = 0

joker = Actor("jokergood")
# while (True):
#     joker.x = random.randint(0, WIDTH)
#     joker.y = random.randint(0, HEIGHT)
#     if (abs(joker.x - batman.x) > 200 and abs(joker.y - batman.y) > 200):
#         break
joker.x = 1060
joker.y = 640
joker_faces = 0
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
upmiddle_cardmove = False
upleft_cardmove = False
upright_cardmove = False

joker_upmiddle.x = -100
joker_upmiddle.y = -100
joker_upleft.x = -100
joker_upleft.y = -100
joker_upright.x = -100
joker_upright.y = -100

joker_downmiddle = Actor("downmiddlecard")
joker_downleft = Actor("downleft")
joker_downright = Actor("downright")
downmiddle_cardmove = False
downleft_cardmove = False
downright_cardmove = False

joker_downmiddle.x = -100
joker_downmiddle.y = -100
joker_downleft.x = -100
joker_downleft.y = -100
joker_downright.x = -100
joker_downright.y = -100

joker_leftmiddle = Actor("leftmiddlecard")
joker_leftbottom = Actor("leftbottom")
joker_lefttop = Actor("lefttop")
leftmiddle_cardmove = False
leftbottom_cardmove = False
lefttop_cardmove = False

joker_leftmiddle.x = -100
joker_leftmiddle.y = -100
joker_leftbottom.x = -100
joker_leftbottom.y = -100
joker_lefttop.x = -100
joker_lefttop.y = -100

joker_rightmiddle = Actor("rightmiddlecard")
joker_righttop = Actor("righttop")
joker_rightbottom = Actor("rightbottom")
rightmiddle_cardmove = False
righttop_cardmove = False
rightbottom_cardmove = False

joker_rightmiddle.x = -100
joker_rightmiddle.y = -100
joker_righttop.x = -100
joker_righttop.y = -100
joker_rightbottom.x = -100
joker_rightbottom.y = -100

upcards = False
downcards = False
leftcards = False
rightcards = False

luthor = Actor("luthorgood")
# while (True):
#     luthor.x = random.randint(0, WIDTH)
#     luthor.y = random.randint(0, HEIGHT)
#     if (abs(luthor.x - batman.x) > 200 and abs(luthor.y - batman.y) > 200):
#         break
luthor.x = 860
luthor.y = 440
luthor_faces = 0

doomsday = Actor("doomsdaynear")
doomsday.x = -500
doomsday.y = -500
doomsday_alive = False
luthorsday = False
doomsday_faces = 0
luthorsday_kill = False
luthorsday_bleed_count = 0
luthorneardeath = False
doomsday_catch = False

two_face = Actor("twofacebetter")
two_face.x = 960
two_face.y = 640
two_face_faces = 0
two_face_frozen = False
bullet_end = Actor("bullet0")
bullet_end.x = two_face.x
bullet_end.y = two_face.y

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

superman_hearts = Actor("bigsupheart")
# if superman_alive == True:
superman_hearts.x = 1305
superman_hearts.y = 45
# else:
#     superman_hearts.x = -100
#     superman_hearts.y = -100

batman_hearts = Actor("bigbatheart")
# if batman_alive == True:
batman_hearts.x = 1450
batman_hearts.y = 45
# else:
#     batman_hearts.x = -100
#     batman_hearts.y = -100

flash_hearts = Actor("bigflaheart")
# if flash_alive == True:
flash_hearts.x = 1595
flash_hearts.y = 45
# else:
#     flash_hearts.x = -100
#     flash_hearts.y = -100

joker_hearts = Actor("bigjokheart")
# if joker_alive == True:
joker_hearts.x = 1740
joker_hearts.y = 45
# else:
#     joker_hearts.x = -100
#     joker_hearts.y = -100

guy_hearts = Actor("bigguyheart")
# if guy_alive == True:
guy_hearts.x = 1885
guy_hearts.y = 45
# else:
#     guy_hearts.x = -100
#     guy_hearts.y = -100

luthor_hearts = Actor("biglutheart")
luthor_hearts.x = 1160
luthor_hearts.y = 45

two_face_hearts = Actor("bigtwoheart")
two_face_hearts.x = 1015
two_face_hearts.y = 45

superman_lives = 100
batman_lives = 100
flash_lives = 100
joker_lives = 100
guy_lives = 100
luthor_lives = 100
two_face_lives = 100

start_time = time.time()
end_time = 0

superman_slowed = False
batman_slowed = False
flash_slowed = False
guy_slowed = False
joker_slowed = False
luthor_slowed = False
two_face_slowed = False

batman_stunned = 0
flash_stunned = 0
guy_stunned = 0
joker_stunned = 0
luthor_stunned = 0
two_face_stunned = 0

superman_confused = False
batman_confused = False
flash_confused = False 
guy_confused = False
joker_confused = False
luthor_confused = False
two_face_confused = False

superman_bleed = False
batman_bleed = False
flash_bleed = False
guy_bleed = False
joker_bleed = False
luthor_bleed = False
two_face_bleed = False

superman_bleed_count = False
batman_bleed_count = False
flash_bleed_count = False
guy_bleed_count = False
joker_bleed_count = False
luthor_bleed_count = False
two_face_bleed_count = False

superman_caught = False
batman_caught = False
flash_caught = False
joker_caught = False
guy_caught = False
luthor_caught = False
joker_helper_caught = False
two_face_caught = False

superman_shot = False
batman_shot = False
flash_shot = False
joker_shot = False
guy_shot = False
joker_helper_shot = False
luthor_shot = False

game_over = False

players_alive = 0
player1 = 0
player2 = 0
player3 = 0
player4 = 0
supermanplayer = 0
batmanplayer = 0
flashplayer = 0
jokerplayer = 0
guyplayer = 0
luthorplayer = 0
two_faceplayer = 0

music.play("tag-game-music1")
music.set_volume(0.2)

NUM_LIGHTNING = 5

lightning = []

for _ in range(NUM_LIGHTNING):
    lightning.append(Actor("lightning"))


playbox = Rect(810, 880, 300, 150)
playcolor = "lightgrey"
playtextcolor = "dimgrey"
playtextmsg = "PLAY"
p1box = Rect(50, 50, 885, 365)
p1color = "turquoise"
p2box = Rect(985, 50, 885, 365)
p2color = "turquoise"
p3box = Rect(50, 465, 885, 365)
p3color = "turquoise"
p4box = Rect(985, 465, 885, 365)
p4color = "turquoise"

canplay = False
playing = False

def on_mouse_down(pos):
    global superman, batman, flash, joker, guy, superman_alive, batman_alive, flash_alive, joker_alive, guy_alive, players_alive, superman_lives, batman_lives, flash_lives, joker_lives, guy_lives \
        , luthor_alive, luthor, luthor_lives, player1, player2, player3, player4, supermanplayer, batmanplayer, flashplayer, jokerplayer, guyplayer, luthorplayer, canplay, playing, playtextmsg \
        , two_face, two_face_alive, two_faceplayer

    if superman.collidepoint(pos) and players_alive <= 3 and superman_alive == False:
        superman_alive = True
        players_alive += 1
        supermanplayer = players_alive
    if batman.collidepoint(pos) and players_alive <= 3 and batman_alive == False:
        batman_alive = True
        players_alive += 1
        batmanplayer = players_alive
    if flash.collidepoint(pos) and players_alive <= 3 and flash_alive == False:
        flash_alive = True
        players_alive += 1
        flashplayer = players_alive
    if joker.collidepoint(pos) and players_alive <= 3 and joker_alive == False:
        joker_alive = True
        players_alive += 1
        jokerplayer = players_alive
    if guy.collidepoint(pos) and players_alive <= 3 and guy_alive == False:
        guy_alive = True
        players_alive += 1
        guyplayer = players_alive
    if luthor.collidepoint(pos) and players_alive <= 3 and luthor_alive == False:
        luthor_alive = True
        players_alive += 1
        luthorplayer = players_alive
    if two_face.collidepoint(pos) and players_alive <= 3 and two_face_alive == False:
        two_face_alive = True
        players_alive += 1
        two_faceplayer = players_alive
        
    if playbox.collidepoint(pos) and players_alive >= 2:
        p1box.x -= 1000
        p2box.x -= 2000
        p3box.x -= 1000
        p4box.x -= 2000
        playbox.x -= 2000
        playtextmsg = ""

        playing = True

        superman_hearts.draw()
        batman_hearts.draw()
        flash_hearts.draw()
        joker_hearts.draw()
        guy_hearts.draw()
        luthor_hearts.draw()

        screen.draw.text(str(superman_lives), (1290, 38), color="yellow")
        screen.draw.text(str(batman_lives), (1435, 38), color="yellow")
        screen.draw.text(str(flash_lives), (1580, 38), color="yellow")
        screen.draw.text(str(joker_lives), (1725, 38), color="green")
        screen.draw.text(str(guy_lives), (1870, 38), color="green")
        screen.draw.text(str(luthor_lives), (1145, 38), color="purple")
        screen.draw.text(str(two_face_lives), (1000, 38), color="black")


    
    
    

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

        screen.draw.filled_rect(playbox, playcolor)
        screen.draw.text(str(playtextmsg), (827, 910), color=playtextcolor, fontsize=150)
        screen.draw.filled_rect(p1box, p1color)
        screen.draw.filled_rect(p2box, p2color)
        screen.draw.filled_rect(p3box, p3color)
        screen.draw.filled_rect(p4box, p4color)

        superman_hearts.draw()
        batman_hearts.draw()
        flash_hearts.draw()
        joker_hearts.draw()
        guy_hearts.draw()
        luthor_hearts.draw()
        two_face_hearts.draw()

        screen.draw.text(str(superman_lives), (1290, 38), color="yellow")
        screen.draw.text(str(batman_lives), (1435, 38), color="yellow")
        screen.draw.text(str(flash_lives), (1580, 38), color="yellow")
        screen.draw.text(str(joker_lives), (1725, 38), color="green")
        screen.draw.text(str(guy_lives), (1870, 38), color="green")
        screen.draw.text(str(luthor_lives), (1145, 38), color="purple")
        screen.draw.text(str(two_face_lives), (1000, 38), color="black")

        # Temporary input debug (remove once confirmed working).
        # Shows whether the game sees top-row 4/5/6/8 and numpad 4/5/6/8.
        try:
            screen.draw.text(
                f"TopRow 4/5/6/8: {keyboard[keys.K_4]} {keyboard[keys.K_5]} {keyboard[keys.K_6]} {keyboard[keys.K_8]}    "
                f"Numpad 4/5/6/8: {keyboard[keys.KP4]} {keyboard[keys.KP5]} {keyboard[keys.KP6]} {keyboard[keys.KP8]}",
                (20, 930),
                color="white",
                fontsize=28,
            )
            screen.draw.text(
                f"TwoFace alive={two_face_alive} frozen={two_face_frozen} stunned={round(time.time()-two_face_stunned,2)} "
                f"pos=({int(two_face.x)},{int(two_face.y)})",
                (20, 960),
                color="white",
                fontsize=28,
            )
        except Exception:
            pass

        superman.draw()
        batman.draw()
        flash.draw()
        guy.draw()
        joker.draw()
        luthor.draw()
        bullet_end.draw()
        two_face.draw()

        batarang.draw()
        joker_helper.draw()
        doomsday.draw()
        boom.draw()
        joker_upmiddle.draw()
        joker_upleft.draw()
        joker_upright.draw()
        joker_downmiddle.draw()
        joker_downleft.draw()
        joker_downright.draw()
        joker_leftmiddle.draw()
        joker_leftbottom.draw()
        joker_lefttop.draw()
        joker_rightmiddle.draw()
        joker_righttop.draw()
        joker_rightbottom.draw()


        screen.draw.filled_rect(lasersuperman, "red")
        for i in range(0, NUM_LIGHTNING):
            lightning[i].draw()



def update():
    global HEIGHT, WIDTH, superman, batman, flash, guy, joker, superman_stun, batman_stun, ice_cooldown, superman_lives, superman_hearts, game_over, superman_slowed, batman_stunned \
    , batarang, batarang_dir, batarang_throw, batman_faces, superman_faces, flash_faces, batarang_frame, batarang_frame_skip, breturn, superman_confused \
    , bpull, flash_stunned, flash_confused, flash_phase, fpf, guy_stunned, guy_confused, joker_confused, joker_stunned, batman_lives, batman_hearts, flash_lives, flash_hearts, joker_lives \
    , joker_hearts, guy_lives, guy_hearts, superman_alive, batman_alive, flash_alive, joker_alive, guy_alive, bac, fpc, fpt, joker_helper, joker_helper_alive, flash_bad, boom, boom_wait \
    , joker_upmiddle, joker_upleft, joker_upright, joker_downmiddle, joker_downleft, joker_downright, joker_leftmiddle, joker_leftbottom, joker_lefttop, joker_rightmiddle, joker_righttop \
    , joker_rightbottom, upmiddle_cardmove, upleft_cardmove, upright_cardmove, downmiddle_cardmove, downleft_cardmove, downright_cardmove, leftmiddle_cardmove, leftbottom_cardmove \
    , lefttop_cardmove, rightmiddle_cardmove, righttop_cardmove, rightbottom_cardmove, upcards, downcards, leftcards, rightcards, guy_faces, joker_faces, batman_slowed, flash_slowed \
    , guy_slowed, joker_slowed, superman_bleed, batman_bleed, flash_bleed, joker_bleed, guy_bleed, superman_bleed_count, batman_bleed_count, flash_bleed_count, joker_bleed_count \
    , guy_bleed_count, luthor, luthor_confused, luthor_bleed, luthor_bleed_count, luthor_stunned, luthor_slowed, luthor_lives, luthor_alive, luthor_faces, doomsday, doomsday_alive, luthorsday \
    , doomsday_faces, lasersuperman_dir, luthorsday_kill, luthorsday_bleed_count, luthorneardeath, doomsday_catch, superman_caught, batman_caught, flash_caught, joker_caught, guy_caught \
    , joker_helper_caught, luthor_caught, player1, player2, player3, player4, supermanplayer, batmanplayer, flashplayer, jokerplayer, guyplayer, luthorplayer, p1color, p2color \
    , p3color, p4color, canplay, playing, playcolor, playtextcolor, two_face, two_face_stunned, two_face_slowed, two_face_alive, two_face_bleed, two_face_bleed_count \
    , two_face_caught, two_face_confused, two_face_faces, two_face_hearts, luthor_hearts, two_face_lives, superman_shot, batman_shot, flash_shot, joker_shot, guy_shot, joker_helper_shot \
    , luthor_shot, two_face_frozen, bullet_end

    #do run cycles
    if game_over:
        return
    


    # superman_batman_distance = (abs(superman.x - batman.x)) + (abs(superman.y - batman.y))
    # superman_flash_distance = (abs(superman.x - flash.x)) + (abs(superman.y - flash.y))
    # batman_flash_distance = (abs(batman.x - flash.x)) + (abs(batman.y - flash.y))
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
    joker_upmiddle_position = (joker_upmiddle.x, joker_upmiddle.y)
    joker_upleft_position = (joker_upleft.x, joker_upleft.y)
    joker_upright_position = (joker_upright.x, joker_upright.y)
    joker_downmiddle_position = (joker_downmiddle.x, joker_downmiddle.y)
    joker_downleft_position = (joker_downleft.x, joker_downleft.y)
    joker_downright_position = (joker_downright.x, joker_downright.y)
    joker_leftmiddle_position = (joker_leftmiddle.x, joker_leftmiddle.y)
    joker_leftbottom_position = (joker_leftbottom.x, joker_leftbottom.y)
    joker_lefttop_position = (joker_lefttop.x, joker_lefttop.y)
    joker_rightmiddle_position = (joker_rightmiddle.x, joker_rightmiddle.y)
    joker_righttop_position = (joker_righttop.x, joker_righttop.y)
    joker_rightbottom_position = (joker_rightbottom.x, joker_rightbottom.y)
    luthor_position = (luthor.x, luthor.y)
    doomsday_position = (doomsday.x, doomsday.y)
    two_face_position = (two_face.x, two_face.y)

    superman_batman_distance = (abs(superman.x - batman.x)) + (abs(superman.y - batman.y))
    superman_flash_distance = (abs(superman.x - flash.x)) + (abs(superman.y - flash.y))
    superman_joker_distance = (abs(superman.x - joker.x)) + (abs(superman.y - joker.y))
    superman_guy_distance = (abs(superman.x - guy.x)) + (abs(superman.y - guy.y))
    superman_joker_helper_distance = (abs(superman.x - joker_helper.x)) + (abs(superman.y - joker_helper.y))
    superman_luthor_distance = (abs(superman.x - luthor.x)) + (abs(superman.y - luthor.y))
    superman_doomsday_distance = (abs(superman.x - doomsday.x)) + (abs(superman.y - doomsday.y))
    superman_two_face_distance = (abs(superman.x - two_face.x)) + (abs(superman.y - two_face.y))

    batman_flash_distance = (abs(batman.x - flash.x)) + (abs(batman.y - flash.y))
    batman_joker_distance = (abs(batman.x - joker.x)) + (abs(batman.y - joker.y))
    batman_guy_distance = (abs(batman.x - guy.x)) + (abs(batman.y - guy.y))
    batman_joker_helper_distance = (abs(batman.x - joker_helper.x)) + (abs(batman.y - joker_helper.y))
    batman_luthor_distance = (abs(batman.x - luthor.x)) + (abs(batman.y - luthor.y))
    batman_doomsday_distance = (abs(batman.x - doomsday.x)) + (abs(batman.y - doomsday.y))
    batman_two_face_distance = (abs(batman.x - two_face.x)) + (abs(batman.y - two_face.y))

    flash_joker_distance = (abs(flash.x - joker.x)) + (abs(flash.y - joker.y))
    flash_guy_distance = (abs(flash.x - guy.x)) + (abs(flash.y - guy.y))
    flash_joker_helper_distance = (abs(flash.x - joker_helper.x)) + (abs(flash.y - joker_helper.y))
    flash_luthor_distance = (abs(flash.x - luthor.x)) + (abs(flash.y - luthor.y))
    flash_doomsday_distance = (abs(flash.x - doomsday.x)) + (abs(flash.y - doomsday.y))
    flash_two_face_distance = (abs(flash.x - two_face.x)) + (abs(flash.y - two_face.y))

    joker_guy_distance = (abs(joker.x - guy.x)) + (abs(joker.y - guy.y))
    joker_joker_helper_distance = (abs(joker.x - joker_helper.x)) + (abs(joker.y - joker_helper.y))
    joker_luthor_distance = (abs(joker.x - luthor.x)) + (abs(joker.y - luthor.y))
    joker_doomsday_distance = (abs(joker.x - doomsday.x)) + (abs(joker.y - doomsday.y))
    joker_two_face_distance = (abs(joker.x - two_face.x)) + (abs(joker.y - two_face.y))

    guy_joker_helper_distance = (abs(guy.x - joker_helper.x)) + (abs(guy.y - joker_helper.y))
    guy_luthor_distance = (abs(guy.x - luthor.x)) + (abs(guy.y - luthor.y))
    guy_doomsday_distance = (abs(guy.x - doomsday.x)) + (abs(guy.y - doomsday.y))
    guy_two_face_distance = (abs(guy.x - two_face.x)) + (abs(guy.y - two_face.y))

    joker_helper_luthor_distance = (abs(joker_helper.x - luthor.x)) + (abs(joker_helper.y - luthor.y))
    joker_helper_doomsday_distance = (abs(joker_helper.x - doomsday.x)) + (abs(joker_helper.y - doomsday.y))
    joker_helper_two_face_distance = (abs(joker_helper.x - two_face.x)) + (abs(joker_helper.y - two_face.y))

    luthor_doomsday_distance = (abs(luthor.x - doomsday.x)) + (abs(luthor.y - doomsday.y))
    luthor_two_face_distance = (abs(luthor.x - two_face.x)) + (abs(luthor.y - two_face.y))

    doomsday_two_face_distance = (abs(doomsday.x - two_face.x)) + (abs(doomsday.y - two_face.y))

    if player1 == 1:
        p1color = "#4d6df3"
    elif player1 == 2:
        p1color = "#000000"
    elif player1 == 3:
        p1color = "#ec1d25"
    elif player1 == 4:
        p1color = "#22b04d"
    elif player1 == 5:
        p1color = "#e5aa7b"
    elif player1 == 6 and luthorsday == False:
        p1color = "#0dff00"
    elif player1 == 6 and luthorsday == True:
        p1color = "#607d8b"
    elif player1 == 7:
        p1color = "#d4d4d4"
    
    if player2 == 1:
        p2color = "#4d6df3"
    elif player2 == 2:
        p2color = "#000000"
    elif player2 == 3:
        p2color = "#ec1d25"
    elif player2 == 4:
        p2color = "#22b04d"
    elif player2 == 5:
        p2color = "#e5aa7b"
    elif player2 == 6 and luthorsday == False:
        p2color = "#0dff00"
    elif player2 == 6 and luthorsday == True:
        p2color = "#607d8b"
    elif player2 == 7:
        p2color = "#d4d4d4"

    if player3 == 1:
        p3color = "#4d6df3"
    elif player3 == 2:
        p3color = "#000000"
    elif player3 == 3:
        p3color = "#ec1d25"
    elif player3 == 4:
        p3color = "#22b04d"
    elif player3 == 5:
        p3color = "#e5aa7b"
    elif player3 == 6 and luthorsday == False:
        p3color = "#0dff00"
    elif player3 == 6 and luthorsday == True:
        p3color = "#607d8b"
    elif player3 == 7:
        p3color = "#d4d4d4"
    
    if player4 == 1:
        p4color = "#4d6df3"
    elif player4 == 2:
        p4color = "#000000"
    elif player4 == 3:
        p4color = "#ec1d25"
    elif player4 == 4:
        p4color = "#22b04d"
    elif player4 == 5:
        p4color = "#e5aa7b"
    elif player4 == 6 and luthorsday == False:
        p4color = "#0dff00"
    elif player4 == 6 and luthorsday == True:
        p4color = "#607d8b"
    elif player4 == 7:
        p4color = "#d4d4d4"

    if players_alive >= 2:
        canplay = True
    elif players_alive <= 2:
        canplay = False

    if canplay == True:
        playcolor = "turquoise"
        playtextcolor = "SpringGreen4"
    elif canplay == False:
        playcolor = "lightgrey"
        playtextcolor = "dimgrey"
        

    if superman_lives <= 0:
        superman_lives = 0
        superman_alive = False

    if superman_alive == False:
        superman = Actor("supermandead")
        superman.pos = superman_position
    elif superman_alive == True and lasersuperman == False and superman_slowed == False and (superman_batman_distance >= 400 or superman_flash_distance >= 400):
        superman = Actor("supermangood")
        superman.pos = superman_position

    if batman_lives <= 0:
        batman_lives = 0
        batman_alive = False

    if batman_alive == False:
        batman = Actor("batmandead")
        batman.pos = batman_position
    elif batman_alive == True and superman_batman_distance >= 300 and batman_stunned == False and batman_slowed == False:
        batman = Actor("batmangood")
        batman.pos = batman_position

    if flash_lives <= 0:
        flash_lives = 0
        flash_alive = False

    if flash_alive == False:    
        flash = Actor("flashdead")
        flash.pos = flash_position
    elif flash_alive == True and flash_phase == False:
        flash = Actor("flashgood")
        flash.pos = flash_position

    if guy_lives <= 0:
        guy_lives = 0
        guy_alive = False

    if guy_alive == False:
        guy = Actor("guydead")
        guy.pos = guy_position
    else:
        guy = Actor("guygood")
        guy.pos = guy_position

    if joker_lives <= 0:
        joker_lives = 0
        joker_alive = False

    if joker_alive == False:
        joker = Actor("jokerdead")
        joker.pos = joker_position
    else:
        joker = Actor("jokergood")
        joker.pos = joker_position

    if luthor_lives <= 0:
        luthor_lives = 0
        luthor_alive = False

    if luthor_alive == False:
        luthor = Actor("luthordead")
        luthor.pos = luthor_position
    else:
        luthor = Actor("luthorgood")
        luthor.pos = luthor_position

    if two_face_lives <= 0:
        two_face_lives = 0
        two_face_alive = False

    if two_face_alive == False:
        two_face = Actor("twofacedead")
        two_face.pos = two_face_position
    else:
        two_face = Actor("twofacebetter")
        two_face.pos = two_face_position


    if supermanplayer == 1:
        player1 = 1
    elif batmanplayer == 1:
        player1 = 2
    elif flashplayer == 1:
        player1 = 3
    elif jokerplayer == 1:
        player1 = 4
    elif guyplayer == 1:
        player1 = 5
    elif luthorplayer == 1:
        player1 = 6
    elif two_faceplayer == 1:
        player1 = 7

    if supermanplayer == 2:
        player2 = 1
    elif batmanplayer == 2:
        player2 = 2
    elif flashplayer == 2:
        player2 = 3
    elif jokerplayer == 2:
        player2 = 4
    elif guyplayer == 2:
        player2 = 5
    elif luthorplayer == 2:
        player2 = 6
    elif two_faceplayer == 2:
        player2 = 7

    if supermanplayer == 3:
        player3 = 1
    elif batmanplayer == 3:
        player3 = 2
    elif flashplayer == 3:
        player3 = 3
    elif jokerplayer == 3:
        player3 = 4
    elif guyplayer == 3:
        player3 = 5
    elif luthorplayer == 3:
        player3 = 6
    elif two_faceplayer == 3:
        player3 = 7

    if supermanplayer == 4:
        player4 = 1
    elif batmanplayer == 4:
        player4 = 2
    elif flashplayer == 4:
        player4 = 3
    elif jokerplayer == 4:
        player4 = 4
    elif guyplayer == 4:
        player4 = 5
    elif luthorplayer == 4:
        player4 = 6
    elif two_faceplayer == 4:
        player4 = 7

    if supermanplayer == 0 and playing == True:
        superman_alive = False
        superman.x = -500
        superman.y = -500
        superman_position = superman.pos
    if batmanplayer == 0 and playing == True:
        batman_alive = False
        batman.x = -500
        batman.y = -500
        batman_position = batman.pos
    if flashplayer == 0 and playing == True:
        flash_alive == False
        flash.x = -500
        flash.y = -500
        flash_position = flash.pos
    if jokerplayer == 0 and playing == True:
        joker_alive = False
        joker.x = -500
        joker.y = -500
        joker_position = joker.pos
    if guyplayer == 0 and playing == True:
        guy_alive = False
        guy.x = -500
        guy.y = -500
        guy_position = guy.pos
    if luthorplayer == 0 and playing == True:
        luthor_alive = False
        luthor.x = -500
        luthor.y = -500
        luthor_position = luthor.pos
    if two_faceplayer == 0 and playing == True:
        two_face_alive = False
        two_face.x = -500
        two_face.y = -500
        two_face_position = two_face.pos

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
                        superman = Actor("kryptonicegood")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x += 2
                            superman.y += 2
                        else:
                            superman.x -= 2
                            superman.y -= 2
                    else:
                        superman = Actor("supermangood")
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
                        superman = Actor("kryptonicegood")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x += 2
                            superman.y -= 2
                        else:
                            superman.x -= 2
                            superman.y += 2
                    else:
                        superman = Actor("supermangood")
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
                        superman = Actor("kryptonicegood")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x -= 2
                            superman.y += 2
                        else:
                            superman.x += 2
                            superman.y -= 2
                    else:
                        superman = Actor("supermangood")
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
                        superman = Actor("kryptonicegood")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x -= 2
                            superman.y -= 2
                        else:
                            superman.x += 2
                            superman.y += 2
                    else:
                        superman = Actor("supermangood")
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
                        superman = Actor("kryptonicegood")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x += 3
                        else:
                            superman.x -= 3
                    else:
                        superman = Actor("supermangood")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x += 5
                        else:
                            superman.x -= 5
                    superman_faces = 8

                elif keyboard.d:
                    if superman_slowed == True:
                        superman = Actor("kryptonicegood")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x -= 5
                        else:
                            superman.x += 3
                    else:
                        superman = Actor("supermangood")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.x -= 5
                        else:
                            superman.x += 5
                    superman_faces = 4

                elif keyboard.w:
                    if superman_slowed:
                        superman = Actor("kryptonicegood")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.y += 3
                        else:
                            superman.y -= 3
                    else:
                        superman = Actor("supermangood")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.y += 5
                        else:
                            superman.y -= 5
                    superman_faces = 2

                elif keyboard.s:
                    if superman_slowed:
                        superman = Actor("kryptonicegood")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.y -= 3
                        else:
                            superman.y += 3
                    else:
                        superman = Actor("supermangood")
                        superman.pos = superman_position
                        if superman_confused == True:
                            superman.y -= 5
                        else:
                            superman.y += 5
                    superman_faces = 6

                else:
                    superman_faces = 0
                    if superman_slowed:
                        superman = Actor("kryptonicegood")
                    else:
                        superman = Actor("supermangood")
                    superman.pos = superman_position
                superman_stun = 0
        superman_position = (superman.x, superman.y)
    # if keyboard.space:
    #     if time.time() - ice_cooldown > 10:
    #         superman.x = random.randint(int(superman.x - 500), int(superman.x + 500))
    #         superman.y = random.randint(int(superman.y - 500), int(superman.y + 500))
    #         ice_cooldown = time.time()
    if superman_alive == True:
        if superman_confused == False:
            if time.time() - ice_cooldown > 8:
                if superman_batman_distance <= 400 or superman_flash_distance <= 400:
                    superman = Actor("supermanicegood")
                    superman.pos = superman_position
                    if keyboard.q:
                        superman = Actor("supermanicegoodbreath")
                        superman.pos = superman_position
                        if superman_batman_distance <= 400:
                            batman_stunned = time.time()
                            batman = Actor("batmanicegreat")
                            batman.pos = batman_position
                        elif superman_flash_distance <= 400 and flash_phase == False:
                            flash_stunned = time.time()
                        elif superman_batman_distance <= 400 and superman_flash_distance <= 400 and flash_phase == False:
                            batman_stunned = time.time()
                            batman = Actor("batmanicegreat")
                            batman.pos = batman_position
                            flash_stunned = time.time()
                        elif superman_batman_distance <= 400 and superman_flash_distance <= 400 and flash_phase == True:
                            batman_stunned = time.time
                            batman = Actor("batmanicegreat")
                            batman.pos = batman_position
                        batman.pos = batman_position
                        ice_cooldown = time.time()
                        sounds.superman_ice_sfx.play(1)

    if time.time() - batman_stunned <= 3.0:
        superman = Actor("supermanicegoodbreath")
        superman.pos = superman_position

    if superman_alive == True:
        if superman_slowed == True and superman_batman_distance <= 400:
            superman = Actor("kryptonicegood")
            superman.pos = superman_position
        elif superman_slowed == False and superman_batman_distance <= 400:
            superman = Actor("supermanicegood")
            superman.pos = superman_position
        elif superman_slowed == False and superman_batman_distance > 400:
            superman = Actor("supermangood")
            superman.pos = superman_position

    if superman_alive == True:
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

    if joker.colliderect(lasersuperman):
        if lasersuperman_dir == 2 or lasersuperman_dir == 6:
            if joker.y > superman.y:
                joker.y += 10
            elif joker.y < superman.y:
                joker.y -= 10
        elif lasersuperman_dir == 4 or lasersuperman_dir == 8:
            if joker.x > superman.x:
                joker.x += 10
            elif joker.x < superman.x:
                joker.x -= 10

    if guy.colliderect(lasersuperman):
        if lasersuperman_dir == 2 or lasersuperman_dir == 6:
            if guy.y > superman.y:
                guy.y += 10
            elif guy.y < superman.y:
                guy.y -= 10
        elif lasersuperman_dir == 4 or lasersuperman_dir == 8:
            if guy.x > superman.x:
                guy.x += 10
            elif guy.x < superman.x:
                guy.x -= 10

    if luthor.colliderect(lasersuperman):
        if lasersuperman_dir == 2 or lasersuperman_dir == 6:
            if luthor.y > superman.y:
                luthor.y += 10
            elif luthor.y < superman.y:
                luthor.y -= 10
        elif lasersuperman_dir == 4 or lasersuperman_dir == 8:
            if luthor.x > superman.x:
                luthor.x += 10
            elif luthor.x < superman.x:
                luthor.x -= 10

    if two_face.colliderect(lasersuperman):
        if lasersuperman_dir == 2 or lasersuperman_dir == 6:
            if two_face.y > superman.y:
                two_face.y += 10
            elif two_face.y < superman.y:
                two_face.y -= 10
        elif lasersuperman_dir == 4 or lasersuperman_dir == 8:
            if two_face.x > superman.x:
                two_face.x += 10
            elif two_face.x < superman.x:
                two_face.x -= 10
    
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
                    batman = Actor("batmankryptonitegood")
                else:
                    batman = Actor("batmangood")
                batman.pos = batman_position
                if batman_slowed == True:
                    batman.x -= 2
                    batman.y -= 2
                else:
                    batman.x -= 3.5
                    batman.y -= 3.5
                batman_faces = 1
            elif keyboard.left and keyboard.down:
                if superman_batman_distance <= 300:
                    batman = Actor("batmankryptonitegood")
                else:
                    batman = Actor("batmangood")
                batman.pos = batman_position
                if batman_slowed == True:
                    batman.x -= 2
                    batman.y += 2
                else:
                    batman.x -= 3.5
                    batman.y += 3.5
                batman_faces = 7
            elif keyboard.right and keyboard.up:
                if superman_batman_distance <= 300:
                    batman = Actor("batmankryptonitegood")
                else:
                    batman = Actor("batmangood")
                batman.pos = batman_position
                if batman_slowed == True:
                    batman.x += 2
                    batman.y -= 2
                else:
                    batman.x += 3.5
                    batman.y -= 3.5
                batman_faces = 3
            elif keyboard.right and keyboard.down:
                if superman_batman_distance <= 300:
                    batman = Actor("batmankryptonitegood")
                else:
                    batman = Actor("batmangood")
                batman.pos = batman_position
                if batman_slowed == True:
                    batman.x += 2
                    batman.y += 2
                else:
                    batman.x += 3.5
                    batman.y += 3.5
                batman_faces = 5
            elif keyboard.left:
                if superman_batman_distance <= 300:
                    batman = Actor("batmankryptonitegood")
                else:
                    batman = Actor("batmangood")
                batman.pos = batman_position
                if batman_slowed == True:
                    batman.x -= 3
                else:
                    batman.x -= 5
                batman_faces = 8
            elif keyboard.right:
                if superman_batman_distance <= 300:
                    batman = Actor("batmankryptonitegood")
                else:
                    batman = Actor("batmangood")
                batman.pos = batman_position
                if batman_slowed == True:
                    batman.x += 3
                else:
                    batman.x += 5
                batman_faces = 4
            elif keyboard.up:
                if superman_batman_distance <= 300:
                    batman = Actor("batmankryptonitegood")
                else:
                    batman = Actor("batmangood")
                batman.pos = batman_position
                if batman_slowed == True:
                    batman.y -= 3
                else:
                    batman.y -= 5
                batman_faces = 2
            elif keyboard.down:
                if superman_batman_distance <= 300:
                    batman = Actor("batmankryptonitegood")
                else:
                    batman = Actor("batmangood")
                batman.pos = batman_position
                if batman_slowed == True:
                    batman.y += 3
                else:
                    batman.y += 5
                batman_faces = 6
            else:
                if superman_batman_distance <= 300:
                    batman = Actor("batmankryptonitegood")
                else:
                    batman = Actor("batmangood")
                batman.pos = batman_position
                batman_faces = 0
            batman_stun = 0
            batman_stunned = 0
        batman_position = (batman.x, batman.y)



    # superman_batman_distance_left = (abs(superman.x - (batman.x - 6))) + (abs(superman.y - batman.y))
    # superman_batman_distance_right = (abs(superman.x - (batman.x + 6))) + (abs(superman.y - batman.y))
    # superman_batman_distance_up = (abs(superman.x - batman.x)) + (abs(superman.y - (batman.y - 6)))
    # superman_batman_distance_down = (abs(superman.x - batman.x)) + (abs(superman.y - (batman.y + 6)))
    if batman_alive == True:
        if keyboard.K_2:
            if superman_batman_distance <= 300:
                if time.time() - batman_stunned > 3.0:
                    superman_slowed = True

    if superman_batman_distance > 300:
        superman_slowed = False

    if flash_alive == True:
        if time.time() - flash_stunned > 4.0:
            if keyboard.j and keyboard.i:
                flash = Actor("flashgood")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.x += 4
                    flash.y += 4
                else:
                    flash.x -= 4
                    flash.y -= 4
                flash_faces = 1
            elif keyboard.j and keyboard.k:
                flash = Actor("flashgood")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.x += 4
                    flash.y -= 4
                else:
                    flash.x -= 4
                    flash.y += 4
                flash_faces = 7
            elif keyboard.l and keyboard.i:
                flash = Actor("flashgood")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.x -= 4
                    flash.y += 4
                else:
                    flash.x += 4
                    flash.y -= 4
                flash_faces = 3
            elif keyboard.l and keyboard.k:
                flash = Actor("flashgood")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.x -= 4
                    flash.y -= 4
                else:
                    flash.x += 4
                    flash.y += 4
                flash_faces = 5
            elif keyboard.j:
                flash = Actor("flashgood")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.x += 5.5
                else:
                    flash.x -= 5.5
                flash_faces = 8
            elif keyboard.l:
                flash = Actor("flashgood")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.x -= 5.5
                else:
                    flash.x += 5.5
                flash_faces = 4
            elif keyboard.i:
                flash = Actor("flashgood")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.y += 5.5
                else:
                    flash.y -= 5.5
                flash_faces = 2
            elif keyboard.k:
                flash = Actor("flashgood")
                flash.pos = flash_position
                if flash_confused == True:
                    flash.y -= 5.5
                else:
                    flash.y += 5.5
                flash_faces = 6
            else:
                flash = Actor("flashgood")
                flash.pos = flash_position
                flash_faces = 0
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

    # if guy_alive == True:
    #     if time.time() - guy_stunned > 4.0:
    #         if keyboard.f and keyboard.t:
    #             guy = Actor("guygood")
    #             guy.pos = guy_position
    #             if guy_confused == True:
    #                 guy.x += 3.5
    #                 guy.y += 3.5
    #             else:
    #                 guy.x -= 3.5
    #                 guy.y -= 3.5
    #             guy_faces = 1
    #         elif keyboard.f and keyboard.g:
    #             guy = Actor("guygood")
    #             guy.pos = guy_position
    #             if guy_confused == True:
    #                 guy.x += 3.5
    #                 guy.y -= 3.5
    #             else:
    #                 guy.x -= 3.5
    #                 guy.y += 3.5
    #             guy_faces = 7
    #         elif keyboard.h and keyboard.t:
    #             guy = Actor("guygood")
    #             guy.pos = guy_position
    #             if guy_confused == True:
    #                 guy.x -= 3.5
    #                 guy.y += 3.5
    #             else:
    #                 guy.x += 3.5
    #                 guy.y -= 3.5
    #             guy_faces = 3
    #         elif keyboard.h and keyboard.g:
    #             guy = Actor("guygood")
    #             guy.pos = guy_position
    #             if guy_confused == True:
    #                 guy.x -= 3.5
    #                 guy.y -= 3.5
    #             else:
    #                 guy.x += 3.5
    #                 guy.y += 3.5
    #             guy_faces = 5
    #         elif keyboard.f:
    #             guy = Actor("guygood")
    #             guy.pos = guy_position
    #             if guy_confused == True:
    #                 guy.x += 5
    #             else:
    #                 guy.x -= 5
    #             guy_faces = 8
    #         elif keyboard.h:
    #             guy = Actor("guygood")
    #             guy.pos = guy_position
    #             if guy_confused == True:
    #                 guy.x -= 5
    #             else:
    #                 guy.x += 5
    #             guy_faces = 4
    #         elif keyboard.t:
    #             guy = Actor("guygood")
    #             guy.pos = guy_position
    #             if guy_confused == True:
    #                 guy.y += 5
    #             else:
    #                 guy.y -= 5
    #             guy_faces = 2
    #         elif keyboard.g:
    #             guy = Actor("guygood")
    #             guy.pos = guy_position
    #             if guy_confused == True:
    #                 guy.y -= 5
    #             else:
    #                 guy.y += 5
    #             guy_faces = 6
    #         else:
    #             guy = Actor("guygood")
    #             guy.pos = guy_position
    #             guy_faces = 0
    #         guy_position = (guy.x, guy.y)

    if joker_alive == True:
        if time.time() - joker_stunned > 4.0:
            if keyboard.KP_4 and keyboard.KP_8:
                joker = Actor("jokergood")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.x += 3.5
                    joker.y += 3.5
                else:
                    joker.x -= 3.5
                    joker.y -= 3.5
                joker_faces = 1
            elif keyboard.KP_4 and keyboard.KP_5:
                joker = Actor("jokergood")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.x += 3.5
                    joker.y -= 3.5
                else:
                    joker.x -= 3.5
                    joker.y += 3.5
                joker_faces = 7
            elif keyboard.KP_6 and keyboard.KP_8:
                joker = Actor("jokergood")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.x -= 3.5
                    joker.y += 3.5
                else:
                    joker.x += 3.5
                    joker.y -= 3.5
                joker_faces = 3
            elif keyboard.KP_6 and keyboard.KP_5:
                joker = Actor("jokergood")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.x -= 3.5
                    joker.y -= 3.5
                else:
                    joker.x += 3.5
                    joker.y += 3.5
                joker_faces = 5
            elif keyboard.KP_4:
                joker = Actor("jokergood")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.x += 5
                else:
                    joker.x -= 5
                joker_faces = 8
            elif keyboard.KP_6:
                joker = Actor("jokergood")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.x -= 5
                else:
                    joker.x += 5
                joker_faces = 4
            elif keyboard.KP_8:
                joker = Actor("jokergood")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.y += 5
                else:
                    joker.y -= 5
                joker_faces = 2
            elif keyboard.KP_5:
                joker = Actor("jokergood")
                joker.pos = joker_position
                if joker_confused == True:
                    joker.y -= 5
                else:
                    joker.y += 5
                joker_faces = 6
            else:
                joker = Actor("jokergood")
                joker.pos = joker_position
                joker_faces = 0

            joker_position = (joker.x, joker.y)

    

    if two_face_alive == True and two_face_frozen == False:
        if True:
        # if time.time() - two_face_stunned > 4.0:
            two_face_position = (two_face.x, two_face.y)
            if keyboard[keys.K_4] and keyboard[keys.K_8]:
                two_face = Actor("twofacebetter")
                two_face.pos = two_face_position
                if two_face_confused == False:
                    print("here1")
                    two_face.x -= 3.5
                    two_face.y -= 3.5
                else:
                    print("here")
                    two_face.x += 3.5
                    two_face.y += 3.5
                two_face_faces = 1
            elif keyboard[keys.K_4] and keyboard[keys.K_5]:
                two_face = Actor("twofacebetter")
                two_face.pos = two_face_position
                if two_face_confused == True:
                    two_face.x += 3.5
                    two_face.y -= 3.5
                else:
                    two_face.x -= 3.5
                    two_face.y += 3.5
                two_face_faces = 7
            elif keyboard[keys.K_6] and keyboard[keys.K_8]:
                two_face = Actor("twofacebetter")
                two_face.pos = two_face_position
                if two_face_confused == True:
                    two_face.x -= 3.5
                    two_face.y += 3.5
                else:
                    two_face.x += 3.5
                    two_face.y -= 3.5
                two_face_faces = 3
            elif keyboard[keys.K_6] and keyboard[keys.K_5]:
                two_face = Actor("twofacebetter")
                two_face.pos = two_face_position
                if two_face_confused == True:
                    two_face.x -= 3.5
                    two_face.y -= 3.5
                else:
                    two_face.x += 3.5
                    two_face.y += 3.5
                two_face_faces = 5
            elif keyboard[keys.K_4]:
                two_face = Actor("twofacebetter")
                two_face.pos = two_face_position
                if two_face_confused == True:
                    two_face.x += 5
                else:
                    two_face.x -= 5
                two_face_faces = 8
            elif keyboard[keys.K_6]:
                two_face = Actor("twofacebetter")
                two_face.pos = two_face_position
                if two_face_confused == True:
                    two_face.x -= 5
                else:
                    two_face.x += 5
                two_face_faces = 4
            elif keyboard[keys.K_8]:
                two_face = Actor("twofacebetter")
                two_face.pos = two_face_position
                if two_face_confused == True:
                    two_face.y += 5
                else:
                    two_face.y -= 5
                two_face_faces = 2
            elif keyboard[keys.K_5]:
                two_face = Actor("twofacebetter")
                two_face.pos = two_face_position
                if two_face_confused == True:
                    two_face.y -= 5
                else:
                    two_face.y += 5
                two_face_faces = 6
            else:
                two_face = Actor("twofacebetter")
                two_face.pos = two_face_position
                two_face_faces = 0

            two_face_position = (two_face.x, two_face.y)

    if keyboard.k_7:
        if two_face_faces == 2:
            bullet_end.x = two_face.x
            bullet_end.y = 0
            two_face_frozen = True
            bullet_end = Actor("shotend2")
            if abs(superman.x - two_face.x) <= 5 and superman.y < two_face.y:
                superman_shot = True
                superman.y -= 10
                superman_lives -= 15
            elif abs(batman.x - two_face.x) <= 5 and batman.y < two_face.y:
                batman_shot = True
                batman.y -= 10
                batman_lives -= 15
            elif abs(flash.x - two_face.x) <= 5 and flash.y < two_face.y:
                flash_shot = True
                flash.y -= 10
                flash_lives -= 15
            elif abs(joker.x - two_face.x) <= 5 and joker.y < two_face.y:
                joker_shot = True
                joker.y -= 10
                joker_lives -= 15
            elif abs(guy.x - two_face.x) <= 5 and guy.y < two_face.y:
                guy_shot = True
                guy.y -= 10
                guy_lives -= 15
            elif abs(joker_helper.x - two_face.x) <= 5 and joker_helper.y < two_face.y:
                joker_helper_shot = True
                joker_helper_alive = False
                joker_helper.x = -100
                joker_helper.y = -100
            elif abs(luthor.x - two_face.x) <= 5 and luthor.y < two_face.y:
                luthor_shot = True
                luthor.y -= 10
                luthor_lives -= 15
        elif two_face_faces == 4:
            bullet_end.x = WIDTH
            bullet_end.y = two_face.y
            two_face_frozen = True
            bullet_end = Actor("shotend4")
            if abs(superman.y - two_face.y) <= 5 and superman.x > two_face.x:
                superman_shot = True
                superman.x += 10
                superman_lives -= 15
            elif abs(batman.y - two_face.y) <= 5 and batman.x > two_face.x:
                batman_shot = True
                batman.x += 10
                batman_lives -= 15
            elif abs(flash.y - two_face.y) <= 5 and flash.x > two_face.x:
                flash_shot = True
                flash.x += 10
                flash_lives -= 15
            elif abs(joker.y - two_face.y) <= 5 and joker.x > two_face.x:
                joker_shot = True
                joker.x += 10
                joker_lives -= 15
            elif abs(guy.y - two_face.y) <= 5 and guy.x > two_face.x:
                guy_shot = True
                guy.x += 10
                guy_lives -= 15
            elif abs(joker_helper.y - two_face.y) <= 5 and joker_helper.x > two_face.x:
                joker_helper_shot = True
                joker_helper_alive = False
                joker_helper.x = -100
                joker_helper.y = -100
            elif abs(luthor.x - two_face.x) <= 5 and luthor.x > two_face.x:
                luthor_shot = True
                luthor.x += 10
                luthor_lives -= 15
        elif two_face_faces == 6:
            bullet_end.x = HEIGHT
            bullet_end.y = two_face.y
            two_face_frozen = True
            bullet_end = Actor("shotend6")
            if abs(superman.x - two_face.x) <= 5 and superman.y > two_face.y:
                superman_shot = True
                superman.y += 10
                superman_lives -= 15
            elif abs(batman.x - two_face.x) <= 5 and batman.y > two_face.y:
                batman_shot = True
                batman.y += 10
                batman_lives -= 15
            elif abs(flash.x - two_face.x) <= 5 and flash.y > two_face.y:
                flash_shot = True
                flash.y += 10
                flash_lives -= 15
            elif abs(joker.x - two_face.x) <= 5 and joker.y > two_face.y:
                joker_shot = True
                joker.y += 10
                joker_lives -= 15
            elif abs(guy.x - two_face.x) <= 5 and guy.y > two_face.y:
                guy_shot = True
                guy.y += 10
                guy_lives -= 15
            elif abs(joker_helper.x - two_face.x) <= 5 and joker_helper.y > two_face.y:
                joker_helper_shot = True
                joker_helper_alive = False
                joker_helper.x = -100
                joker_helper.y = -100
            elif abs(luthor.x - two_face.x) <= 5 and luthor.y > two_face.y:
                luthor_shot = True
                luthor.y += 10
                luthor_lives -= 15
        elif two_face_faces == 8:
            bullet_end.x = 0
            bullet_end.y = two_face.y
            two_face_frozen = True
            bullet_end = Actor("shotend8")
            if abs(superman.y - two_face.y) <= 5 and superman.x < two_face.x:
                superman_shot = True
                superman.x -= 10
                superman_lives -= 15
            elif abs(batman.y - two_face.y) <= 5 and batman.x < two_face.x:
                batman_shot = True
                batman.x -= 10
                batman_lives -= 15
            elif abs(flash.y - two_face.y) <= 5 and flash.x < two_face.x:
                flash_shot = True
                flash.x -= 10
                flash_lives -= 15
            elif abs(joker.y - two_face.y) <= 5 and joker.x < two_face.x:
                joker_shot = True
                joker.x -= 10
                joker_lives -= 15
            elif abs(guy.y - two_face.y) <= 5 and guy.x < two_face.x:
                guy_shot = True
                guy.x -= 10
                guy_lives -= 15
            elif abs(joker_helper.y - two_face.y) <= 5 and joker_helper.x < two_face.x:
                joker_helper_shot = True
                joker_helper_alive = False
                joker_helper.x = -100
                joker_helper.y = -100
            elif abs(luthor.x - two_face.x) <= 5 and luthor.x < two_face.x:
                luthor_shot = True
                luthor.x -= 10
                luthor_lives -= 15

        elif two_face_faces == 1:
            pass
        elif two_face_faces == 3:
            pass
        elif two_face_faces == 5:
            pass
        elif two_face_faces == 7:
            pass


    # if superman_shot == True or batman_shot == True or flash_shot == True or joker_shot == True or joker_helper_shot == True or luthor_shot == True or guy_shot == True or time thingy is over
        # _shot = False
        # frozen = False

    if joker_helper_alive == False:
        if keyboard.KP_7:
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

# and (superman_joker_helper_distance < 200 or batman_joker_helper_distance < 200 or flash_joker_helper_distance < 200 or guy_joker_helper_distance < 200)

    if keyboard.KP_9 and joker_helper_alive == True:
        joker_helper_caught = False
        doomsday_catch = False
        if superman_joker_helper_distance < 200:
            superman_lives -= 5
            if superman.x > joker_helper.x:
                superman.x += 50
            elif superman.x < joker_helper.x:
                superman.x -= 50
            if superman.y > joker_helper.y:
                superman.y += 50
            elif superman.y < joker_helper.y:
                superman.y -= 50

        if batman_joker_helper_distance < 200:
            batman_lives -= 8
            if batman.x > joker_helper.x:
                batman.x += 100
            elif batman.x < joker_helper.x:
                batman.x -= 100
            if batman.y > joker_helper.y:
                batman.y += 100
            elif batman.y < joker_helper.y:
                batman.y -= 100

        if flash_joker_helper_distance < 200:
            flash_lives -= 8
            if flash.x > joker_helper.x:
                flash.x += 100
            elif flash.x < joker_helper.x:
                flash.x -= 100
            if flash.y > joker_helper.y:
                flash.y += 100
            elif flash.y < joker_helper.y:
                flash.y -= 100

        if guy_joker_helper_distance < 200:
            guy_lives -= 10
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

    if upcards == False and downcards == False and leftcards == False and rightcards == False:
        batman_slowed = False

    if keyboard.KP_0 and upcards == False and downcards == False and leftcards == False and rightcards == False:
        joker_upmiddle_position = joker_position
        joker_upmiddle.pos = joker_upmiddle_position
        joker_upleft_position = joker_position
        joker_upleft.pos = joker_upleft_position
        joker_upright_position = joker_position
        joker_upright.pos = joker_upright_position

        upmiddle_cardmove = True
        upleft_cardmove = True
        upright_cardmove = True

        joker_downmiddle_position = joker_position
        joker_downmiddle.pos = joker_downmiddle_position
        joker_downleft_position = joker_position
        joker_downleft.pos = joker_downleft_position
        joker_downright_position = joker_position
        joker_downright.pos = joker_downright_position

        downmiddle_cardmove = True
        downleft_cardmove = True
        downright_cardmove = True

        joker_leftmiddle_position = joker_position
        joker_leftmiddle.pos = joker_leftmiddle_position
        joker_leftbottom_position = joker_position
        joker_leftbottom.pos = joker_leftbottom_position
        joker_lefttop_position = joker_position
        joker_lefttop.pos = joker_lefttop_position

        leftmiddle_cardmove = True
        leftbottom_cardmove = True
        lefttop_cardmove = True

        joker_rightmiddle_position = joker_position
        joker_rightmiddle.pos = joker_rightmiddle_position
        joker_righttop_position = joker_position
        joker_righttop.pos = joker_righttop_position
        joker_rightbottom_position = joker_position
        joker_rightbottom.pos = joker_rightbottom_position

        rightmiddle_cardmove = True
        righttop_cardmove = True
        rightbottom_cardmove = True

    if upmiddle_cardmove == True:
        joker_upmiddle.y -= 5
        if joker_upmiddle.colliderect(superman):
            superman_confused = True
            superman_bleed = True
        elif joker_upmiddle.colliderect(batman):
            batman_slowed = True
            batman_bleed = True
        elif joker_upmiddle.colliderect(flash):
            flash_stunned = time.time()
            flash_bleed = True
        elif joker_upmiddle.colliderect(luthor):
            luthor_confused = True
            luthor_bleed = True
        elif joker_upmiddle.colliderect(two_face):
            coincard = rand(randint(1, 2))
            # 1 = head = good
            # 2 = tails = bad

            if coincard == 2:
                two_face_bleed = True
                two_face_confused = True
        elif joker_upmiddle.colliderect(guy):
            guy_bleed = True
            if guy_faces == 2:
                guy.y -= 20
            elif guy_faces == 4:
                guy.x += 20
            elif guy_faces == 6:
                guy.y += 20
            elif guy_faces == 8:
                guy.x -= 20
            elif guy_faces == 1:
                guy.x -= 14
                guy.y -= 14
            elif guy_faces == 3:
                guy.x += 14
                guy.y -= 14
            elif guy_faces == 5:
                guy.x += 14
                guy.y += 14
            elif guy_faces == 7:
                guy.x -= 14
                guy.y += 14

    if upleft_cardmove == True:
        joker_upleft.x -= 2.5
        joker_upleft.y -= 4.3
        if joker_upleft.colliderect(superman):
            superman_confused = True
            superman_bleed = True
        elif joker_upleft.colliderect(batman):
            batman_slowed = True
            batman_bleed = True
        elif joker_upleft.colliderect(flash):
            flash_stunned = time.time()
            flash_bleed = True
        elif joker_upleft.colliderect(luthor):
            luthor_confused = True
            luthor_bleed = True
        elif joker_upleft.colliderect(two_face):
            coincard = rand(randint(1, 2))
            # 1 = head = good
            # 2 = tails = bad

            if coincard == 2:
                two_face_bleed = True
                two_face_confused = True
        elif joker_upleft.colliderect(guy):
            guy_bleed = True
            if guy_faces == 2:
                guy.y -= 20
            elif guy_faces == 4:
                guy.x += 20
            elif guy_faces == 6:
                guy.y += 20
            elif guy_faces == 8:
                guy.x -= 20
            elif guy_faces == 1:
                guy.x -= 14
                guy.y -= 14
            elif guy_faces == 3:
                guy.x += 14
                guy.y -= 14
            elif guy_faces == 5:
                guy.x += 14
                guy.y += 14
            elif guy_faces == 7:
                guy.x -= 14
                guy.y += 14

    if upright_cardmove == True:
        joker_upright.x += 2.5
        joker_upright.y -= 4.3
        if joker_upright.colliderect(superman):
            superman_confused = True
            superman_bleed = True
        elif joker_upright.colliderect(batman):
            batman_slowed = True
            batman_bleed = True
        elif joker_upright.colliderect(flash):
            flash_stunned = time.time()
            flash_bleed = True
        elif joker_upright.colliderect(luthor):
            luthor_confused = True
            luthor_bleed = True
        elif joker_upright.colliderect(two_face):
            coincard = rand(randint(1, 2))
            # 1 = head = good
            # 2 = tails = bad

            if coincard == 2:
                two_face_bleed = True
                two_face_confused = True
        elif joker_upright.colliderect(guy):
            guy_bleed = True
            if guy_faces == 2:
                guy.y -= 20
            elif guy_faces == 4:
                guy.x += 20
            elif guy_faces == 6:
                guy.y += 20
            elif guy_faces == 8:
                guy.x -= 20
            elif guy_faces == 1:
                guy.x -= 14
                guy.y -= 14
            elif guy_faces == 3:
                guy.x += 14
                guy.y -= 14
            elif guy_faces == 5:
                guy.x += 14
                guy.y += 14
            elif guy_faces == 7:
                guy.x -= 14
                guy.y += 14
    
    if downmiddle_cardmove == True:
        joker_downmiddle.y += 5
        if joker_downmiddle.colliderect(superman):
            superman_confused = True
            superman_bleed = True
        elif joker_downmiddle.colliderect(batman):
            batman_slowed = True
            batman_bleed = True
        elif joker_downmiddle.colliderect(flash):
            flash_stunned = time.time()
            flash_bleed = True
        elif joker_downmiddle.colliderect(luthor):
            luthor_confused = True
            luthor_bleed = True
        elif joker_downmiddle.colliderect(two_face):
            coincard = rand(randint(1, 2))
            # 1 = head = good
            # 2 = tails = bad

            if coincard == 2:
                two_face_bleed = True
                two_face_confused = True
        elif joker_downmiddle.colliderect(guy):
            guy_bleed = True
            if guy_faces == 2:
                guy.y -= 20
            elif guy_faces == 4:
                guy.x += 20
            elif guy_faces == 6:
                guy.y += 20
            elif guy_faces == 8:
                guy.x -= 20
            elif guy_faces == 1:
                guy.x -= 14
                guy.y -= 14
            elif guy_faces == 3:
                guy.x += 14
                guy.y -= 14
            elif guy_faces == 5:
                guy.x += 14
                guy.y += 14
            elif guy_faces == 7:
                guy.x -= 14
                guy.y += 14

    if downleft_cardmove == True:
        joker_downleft.x -= 2.5
        joker_downleft.y += 4.3
        if joker_downleft.colliderect(superman):
            superman_confused = True
            superman_bleed = True
        elif joker_downleft.colliderect(batman):
            batman_slowed = True
            batman_bleed = True
        elif joker_downleft.colliderect(flash):
            flash_stunned = time.time()
            flash_bleed = True
        elif joker_downleft.colliderect(luthor):
            luthor_confused = True
            luthor_bleed = True
        elif joker_downleft.colliderect(two_face):
            coincard = rand(randint(1, 2))
            # 1 = head = good
            # 2 = tails = bad

            if coincard == 2:
                two_face_bleed = True
                two_face_confused = True
        elif joker_downleft.colliderect(guy):
            guy_bleed = True
            if guy_faces == 2:
                guy.y -= 20
            elif guy_faces == 4:
                guy.x += 20
            elif guy_faces == 6:
                guy.y += 20
            elif guy_faces == 8:
                guy.x -= 20
            elif guy_faces == 1:
                guy.x -= 14
                guy.y -= 14
            elif guy_faces == 3:
                guy.x += 14
                guy.y -= 14
            elif guy_faces == 5:
                guy.x += 14
                guy.y += 14
            elif guy_faces == 7:
                guy.x -= 14
                guy.y += 14

    if downright_cardmove == True:
        joker_downright.x += 2.5
        joker_downright.y += 4.3
        if joker_downright.colliderect(superman):
            superman_confused = True
            superman_bleed = True
        elif joker_downright.colliderect(batman):
            batman_slowed = True
            batman_bleed = True
        elif joker_downright.colliderect(flash):
            flash_stunned = time.time()
            flash_bleed = True
        elif joker_downright.colliderect(luthor):
            luthor_confused = True
            luthor_bleed = True
        elif joker_downleft.colliderect(two_face):
            coincard = rand(randint(1, 2))
            # 1 = head = good
            # 2 = tails = bad

            if coincard == 2:
                two_face_bleed = True
                two_face_confused = True
        elif joker_downright.colliderect(guy):
            guy_bleed = True
            if guy_faces == 2:
                guy.y -= 20
            elif guy_faces == 4:
                guy.x += 20
            elif guy_faces == 6:
                guy.y += 20
            elif guy_faces == 8:
                guy.x -= 20
            elif guy_faces == 1:
                guy.x -= 14
                guy.y -= 14
            elif guy_faces == 3:
                guy.x += 14
                guy.y -= 14
            elif guy_faces == 5:
                guy.x += 14
                guy.y += 14
            elif guy_faces == 7:
                guy.x -= 14
                guy.y += 14

    if leftmiddle_cardmove == True:
        joker_leftmiddle.x -= 5
        if joker_leftmiddle.colliderect(superman):
            superman_confused = True
            superman_bleed = True
        elif joker_leftmiddle.colliderect(batman):
            batman_slowed = True
            batman_bleed = True
        elif joker_leftmiddle.colliderect(flash):
            flash_stunned = time.time()
            flash_bleed = True
        elif joker_leftmiddle.colliderect(luthor):
            luthor_confused = True
            luthor_bleed = True
        elif joker_leftmiddle.colliderect(two_face):
            coincard = rand(randint(1, 2))
            # 1 = head = good
            # 2 = tails = bad

            if coincard == 2:
                two_face_bleed = True
                two_face_confused = True
        elif joker_leftmiddle.colliderect(guy):
            guy_bleed = True
            if guy_faces == 2:
                guy.y -= 20
            elif guy_faces == 4:
                guy.x += 20
            elif guy_faces == 6:
                guy.y += 20
            elif guy_faces == 8:
                guy.x -= 20
            elif guy_faces == 1:
                guy.x -= 14
                guy.y -= 14
            elif guy_faces == 3:
                guy.x += 14
                guy.y -= 14
            elif guy_faces == 5:
                guy.x += 14
                guy.y += 14
            elif guy_faces == 7:
                guy.x -= 14
                guy.y += 14


    if leftbottom_cardmove == True:
        joker_leftbottom.x -= 4.3
        joker_leftbottom.y += 2.5
        if joker_leftbottom.colliderect(superman):
            superman_confused = True
            superman_bleed = True
        elif joker_leftbottom.colliderect(batman):
            batman_slowed = True
            batman_bleed = True
        elif joker_leftbottom.colliderect(flash):
            flash_stunned = time.time()
            flash_bleed = True
        elif joker_leftbottom.colliderect(luthor):
            luthor_confused = True
            luthor_bleed = True
        elif joker_leftbottom.colliderect(two_face):
            coincard = rand(randint(1, 2))
            # 1 = head = good
            # 2 = tails = bad

            if coincard == 2:
                two_face_bleed = True
                two_face_confused = True
        elif joker_leftbottom.colliderect(guy):
            if guy_faces == 2:
                guy.y -= 20
            elif guy_faces == 4:
                guy.x += 20
            elif guy_faces == 6:
                guy.y += 20
            elif guy_faces == 8:
                guy.x -= 20
            elif guy_faces == 1:
                guy.x -= 14
                guy.y -= 14
            elif guy_faces == 3:
                guy.x += 14
                guy.y -= 14
            elif guy_faces == 5:
                guy.x += 14
                guy.y += 14
            elif guy_faces == 7:
                guy.x -= 14
                guy.y += 14

    if lefttop_cardmove == True:
        joker_lefttop.x -= 4.3
        joker_lefttop.y -= 2.5
        if joker_lefttop.colliderect(superman):
            superman_confused = True
            superman_bleed = True
        elif joker_lefttop.colliderect(batman):
            batman_slowed = True
            batman_bleed = True
        elif joker_lefttop.colliderect(flash):
            flash_stunned = time.time()
            flash_bleed = True
        elif joker_lefttop.colliderect(luthor):
            luthor_confused = True
            luthor_bleed = True
        elif joker_lefttop.colliderect(two_face):
            coincard = rand(randint(1, 2))
            # 1 = head = good
            # 2 = tails = bad

            if coincard == 2:
                two_face_bleed = True
                two_face_confused = True
        elif joker_lefttop.colliderect(guy):
            guy_bleed = True
            if guy_faces == 2:
                guy.y -= 20
            elif guy_faces == 4:
                guy.x += 20
            elif guy_faces == 6:
                guy.y += 20
            elif guy_faces == 8:
                guy.x -= 20
            elif guy_faces == 1:
                guy.x -= 14
                guy.y -= 14
            elif guy_faces == 3:
                guy.x += 14
                guy.y -= 14
            elif guy_faces == 5:
                guy.x += 14
                guy.y += 14
            elif guy_faces == 7:
                guy.x -= 14
                guy.y += 14

    if rightmiddle_cardmove == True:
        joker_rightmiddle.x += 5
        if joker_rightmiddle.colliderect(superman):
            superman_confused = True
            superman_bleed = True
        elif joker_rightmiddle.colliderect(batman):
            batman_slowed = True
            batman_bleed = True
        elif joker_rightmiddle.colliderect(flash):
            flash_stunned = time.time()
            flash_bleed = True
        elif joker_rightmiddle.colliderect(luthor):
            luthor_confused = True
            luthor_bleed = True
        elif joker_rightmiddle.colliderect(two_face):
            coincard = rand(randint(1, 2))
            # 1 = head = good
            # 2 = tails = bad

            if coincard == 2:
                two_face_bleed = True
                two_face_confused = True
        elif joker_rightmiddle.colliderect(guy):
            guy_bleed = True
            if guy_faces == 2:
                guy.y -= 20
            elif guy_faces == 4:
                guy.x += 20
            elif guy_faces == 6:
                guy.y += 20
            elif guy_faces == 8:
                guy.x -= 20
            elif guy_faces == 1:
                guy.x -= 14
                guy.y -= 14
            elif guy_faces == 3:
                guy.x += 14
                guy.y -= 14
            elif guy_faces == 5:
                guy.x += 14
                guy.y += 14
            elif guy_faces == 7:
                guy.x -= 14
                guy.y += 14

    if righttop_cardmove == True:
        joker_righttop.x += 4.3
        joker_righttop.y -= 2.5
        if joker_righttop.colliderect(superman):
            superman_confused = True
            superman_bleed = True
        elif joker_righttop.colliderect(batman):
            batman_slowed = True
            batman_bleed = True
        elif joker_righttop.colliderect(flash):
            flash_stunned = time.time()
            flash_bleed = True
        elif joker_righttop.colliderect(luthor):
            luthor_confused = True
            luthor_bleed = True
        elif joker_righttop.colliderect(two_face):
            coincard = rand(randint(1, 2))
            # 1 = head = good
            # 2 = tails = bad

            if coincard == 2:
                two_face_bleed = True
                two_face_confused = True
        elif joker_righttop.colliderect(guy):
            guy_bleed = True
            if guy_faces == 2:
                guy.y -= 20
            elif guy_faces == 4:
                guy.x += 20
            elif guy_faces == 6:
                guy.y += 20
            elif guy_faces == 8:
                guy.x -= 20
            elif guy_faces == 1:
                guy.x -= 14
                guy.y -= 14
            elif guy_faces == 3:
                guy.x += 14
                guy.y -= 14
            elif guy_faces == 5:
                guy.x += 14
                guy.y += 14
            elif guy_faces == 7:
                guy.x -= 14
                guy.y += 14

    if rightbottom_cardmove == True:
        joker_rightbottom.x += 4.3
        joker_rightbottom.y += 2.5
        if joker_rightbottom.colliderect(superman):
            superman_confused = True
            superman_bleed = True
        elif joker_rightbottom.colliderect(batman):
            batman_slowed = True
            batman_bleed = True
        elif joker_rightbottom.colliderect(flash):
            flash_stunned = time.time()
            flash_bleed = True
        elif joker_rightbottom.colliderect(luthor):
            luthor_confused = True
            luthor_bleed = True
        elif joker_rightbottom.colliderect(two_face):
            coincard = rand(randint(1, 2))
            # 1 = head = good
            # 2 = tails = bad

            if coincard == 2:
                two_face_bleed = True
                two_face_confused = True
        elif joker_rightbottom.colliderect(guy):
            guy_bleed = True
            if guy_faces == 2:
                guy.y -= 20
            elif guy_faces == 4:
                guy.x += 20
            elif guy_faces == 6:
                guy.y += 20
            elif guy_faces == 8:
                guy.x -= 20
            elif guy_faces == 1:
                guy.x -= 14
                guy.y -= 14
            elif guy_faces == 3:
                guy.x += 14
                guy.y -= 14
            elif guy_faces == 5:
                guy.x += 14
                guy.y += 14
            elif guy_faces == 7:
                guy.x -= 14
                guy.y += 14

    if upmiddle_cardmove == False and upleft_cardmove == False and upright_cardmove == False:
        upcards = False
    else:
        upcards = True

    if downmiddle_cardmove == False and downleft_cardmove == False and downright_cardmove == False:
        downcards = False
    else:
        downcards = True

    if leftmiddle_cardmove == False and leftbottom_cardmove == False and lefttop_cardmove == False:
        leftcards = False
    else:
        leftcards = True

    if rightmiddle_cardmove == False and righttop_cardmove == False and rightbottom_cardmove == False:
        rightcards = False
    else:
        rightcards = True

    
    if upmiddle_cardmove == True and joker_upmiddle.y < 0:
        upmiddle_cardmove = False
        joker_upmiddle.x = -100
        joker_upmiddle.y = -100

    if upleft_cardmove == True and (joker_upleft.y < 0 or joker_upleft.x < 0):
        upleft_cardmove = False
        joker_upleft.x = -100
        joker_upleft.y = -100

    if upright_cardmove == True and (joker_upright.y < 0 or joker_upright.x > WIDTH):
        upright_cardmove = False
        joker_upright.x = -100
        joker_upright.y = -100


    if downmiddle_cardmove == True and joker_downmiddle.y > HEIGHT:
        downmiddle_cardmove = False
        joker_downmiddle.x = -100
        joker_downmiddle.y = -100

    if downleft_cardmove == True and (joker_downleft.y > HEIGHT or joker_downleft.x < 0):
        downleft_cardmove = False
        joker_downleft.x = -100
        joker_downleft.y = -100

    if downright_cardmove == True and (joker_downright.y > HEIGHT or joker_downright.x > WIDTH):
        downright_cardmove = False
        joker_downright.x = -100
        joker_downright.y = -100


    if leftmiddle_cardmove == True and joker_leftmiddle.x < 0:
        leftmiddle_cardmove = False
        joker_leftmiddle.x = -100
        joker_leftmiddle.y = -100

    if leftbottom_cardmove == True and (joker_leftbottom.y > HEIGHT or joker_leftbottom.x < 0):
        leftbottom_cardmove = False
        joker_leftbottom.x = -100
        joker_leftbottom.y = -100

    if lefttop_cardmove == True and (joker_lefttop.y < 0 or joker_lefttop.x < 0):
        lefttop_cardmove = False
        joker_lefttop.x = -100
        joker_lefttop.y = -100


    if rightmiddle_cardmove == True and joker_rightmiddle.x > WIDTH:
        rightmiddle_cardmove = False
        joker_rightmiddle.x = -100
        joker_rightmiddle.y = -100

    if righttop_cardmove == True and (joker_righttop.y < 0 or joker_righttop.x > WIDTH):
        righttop_cardmove = False
        joker_righttop.x = -100
        joker_righttop.y = -100

    if rightbottom_cardmove == True and (joker_rightbottom.y > HEIGHT or joker_rightbottom.x > WIDTH):
        rightbottom_cardmove = False
        joker_rightbottom.x = -100
        joker_rightbottom.y = -100
    





# if doomsday.colliderect(syhsfgs) or:
    # if doomsday_strength ==
        # if doomsday_faces = :
            # sfgdgs.x += 3456w36
        # if doomsday_strength < 5:
        #   doomsday_strength += 1
    




    if luthor_alive == True or luthorsday == True:
        if time.time() - luthor_stunned > 4.0:
            if keyboard.f and keyboard.t:
                if luthorsday == False:
                    luthor = Actor("luthorgood")
                    luthor.pos = luthor_position
                    if luthor_confused == True:
                        luthor.x += 3.5
                        luthor.y += 3.5
                    else:
                        luthor.x -= 3.5
                        luthor.y -= 3.5
                    luthor_faces = 1
                else:
                    doomsday = Actor("doomsdaynear")
                    doomsday.pos = doomsday_position
                    doomsday.x -= 3.5
                    doomsday.y -= 3.5
                    doomsday_faces = 1
            elif keyboard.f and keyboard.g:
                if luthorsday == False:
                    luthor = Actor("luthorgood")
                    luthor.pos = luthor_position
                    if luthor_confused == True:
                        luthor.x += 3.5
                        luthor.y -= 3.5
                    else:
                        luthor.x -= 3.5
                        luthor.y += 3.5
                    luthor_faces = 7
                else:
                    doomsday = Actor("doomsdaynear")
                    doomsday.pos = doomsday_position
                    doomsday.x -= 3.5
                    doomsday.y += 3.5
                    doomsday_faces = 7
            elif keyboard.h and keyboard.t:
                if luthorsday == False:
                    luthor = Actor("luthorgood")
                    luthor.pos = luthor_position
                    if luthor_confused == True:
                        luthor.x -= 3.5
                        luthor.y += 3.5
                    else:
                        luthor.x += 3.5
                        luthor.y -= 3.5
                    luthor_faces = 3
                else:
                    doomsday = Actor("doomsdaynear")
                    doomsday.pos = doomsday_position
                    doomsday.x += 3.5
                    doomsday.y -= 3.5
                    doomsday_faces = 3
            elif keyboard.h and keyboard.g:
                if luthorsday == False:
                    luthor = Actor("luthorgood")
                    luthor.pos = luthor_position
                    if luthor_confused == True:
                        luthor.x -= 3.5
                        luthor.y -= 3.5
                    else:
                        luthor.x += 3.5
                        luthor.y += 3.5
                    luthor_faces = 5
                else:
                    doomsday = Actor("doomsdaynear")
                    doomsday.pos = doomsday_position
                    doomsday.x += 3.5
                    doomsday.y += 3.5
                    doomsday_faces = 5
            elif keyboard.f:
                if luthorsday == False:
                    luthor = Actor("luthorgood")
                    luthor.pos = luthor_position
                    if luthor_confused == True:
                        luthor.x += 5
                    else:
                        luthor.x -= 5
                    luthor_faces = 8
                else:
                    doomsday = Actor("doomsdaynear")
                    doomsday.pos = doomsday_position
                    doomsday.x -= 5
                    doomsday_faces = 8
            elif keyboard.h:
                if luthorsday == False:
                    luthor = Actor("luthorgood")
                    luthor.pos = luthor_position
                    if luthor_confused == True:
                        luthor.x -= 5
                    else:
                        luthor.x += 5
                    luthor_faces = 4
                else:
                    doomsday = Actor("doomsdaynear")
                    doomsday.pos = doomsday_position
                    doomsday.x += 5
                    doomsday_faces = 4
            elif keyboard.t:
                if luthorsday == False:
                    luthor = Actor("luthorgood")
                    luthor.pos = luthor_position
                    if luthor_confused == True:
                        luthor.y += 5
                    else:
                        luthor.y -= 5
                    luthor_faces = 2
                else:
                    doomsday = Actor("doomsdaynear")
                    doomsday.pos = doomsday_position
                    doomsday.y -= 5
                    doomsday_faces = 2
            elif keyboard.g:
                if luthorsday == False:
                    luthor = Actor("luthorgood")
                    luthor.pos = luthor_position
                    if luthor_confused == True:
                        luthor.y -= 5
                    else:
                        luthor.y += 5
                    luthor_faces = 6
                else:
                    doomsday = Actor("doomsdaynear")
                    doomsday.pos = doomsday_position
                    doomsday.y += 5
                    doomsday_faces = 6
            else:
                luthor = Actor("luthorgood")
                luthor.pos = luthor_position
                luthor_faces = 0
                doomsday_faces = 0

    luthorsday_bleed_count += 1

    if keyboard.r:
        doomsday_alive = True
        doomsday.x = luthor.x
        doomsday.y = luthor.y
        doomsday_position = luthor_position
        luthorsday = True
        luthorsday_kill = True
        luthorneardeath = True


    if luthorneardeath == True:
        luthor_lives -= 60
        luthorneardeath = False


    if luthorsday_bleed_count % 60 == 0:
        if luthorsday_kill == True:
            luthor_lives -= 4

    if luthor_alive == False:
        luthorsday_kill = False
        luthorsday_bleed_count = 0

    if superman_caught == True:
        superman.x = doomsday.x
        superman.y = doomsday.y - 50
    if batman_caught == True:
        batman.x = doomsday.x
        batman.y = doomsday.y - 50
    if flash_caught == True:
        flash.x = doomsday.x
        flash.y = doomsday.y - 50
    if joker_caught == True:
        joker.x = doomsday.x
        joker.y = doomsday.y - 50
    if guy_caught == True:
        guy.x = doomsday.x
        guy.y = doomsday.y - 50
    if joker_helper_caught == True:
        joker_helper.x = doomsday.x
        joker_helper.y = doomsday.y - 50
    if luthor_caught == True:
        luthor.x = doomsday.x
        luthor.y = doomsday.y - 50
    if two_face_caught == True:
        two_face.x = doomsday.x
        two_face.y = doomsday.y - 50

    if keyboard.y:
        if doomsday_catch == False:
            if doomsday.colliderect(superman):
                superman_caught = True
                doomsday_catch = True
            elif doomsday.colliderect(batman):
                batman_caught = True
                doomsday_catch = True
            elif doomsday.colliderect(flash):
                flash_caught = True
                doomsday_catch = True
            elif doomsday.colliderect(joker):
                joker_caught = True
                doomsday_catch = True
            elif doomsday.colliderect(guy):
                guy_caught = True
                doomsday_catch = True
            elif doomsday.colliderect(joker_helper):
                joker_helper_caught = True
                doomsday_catch = True
            elif doomsday.colliderect(luthor):
                luthor_caught = True
                doomsday_catch = True
            elif doomsday.colliderect(two_face):
                two_face_caught = True
                doomsday_catch = True

        elif doomsday_catch == True and doomsday_faces != 0:
            if superman_caught == True:
                if doomsday_faces == 2:
                    superman.y = 0
                    superman_caught = False
                    doomsday_catch = False
                    superman_lives -= 15
                if doomsday_faces == 4:
                    superman.x = WIDTH
                    superman_caught = False
                    doomsday_catch = False
                    superman_lives -= 15
                if doomsday_faces == 6:
                    superman.y = HEIGHT
                    superman_caught = False
                    doomsday_catch = False
                    superman_lives -= 15
                if doomsday_faces == 8:
                    superman.x = 0
                    superman_caught = False
                    doomsday_catch = False
                    superman_lives -= 15

            elif batman_caught == True:
                if doomsday_faces == 2:
                    batman.y = 0
                    batman_caught = False
                    doomsday_catch = False
                    batman_lives -= 15
                if doomsday_faces == 4:
                    batman.x = WIDTH
                    batman_caught = False
                    doomsday_catch = False
                    batman_lives -= 15
                if doomsday_faces == 6:
                    batman.y = HEIGHT
                    batman_caught = False
                    doomsday_catch = False
                    batman_lives -= 15
                if doomsday_faces == 8:
                    batman.x = 0
                    batman_caught = False
                    doomsday_catch = False
                    batman_lives -= 15

            elif flash_caught == True:
                if doomsday_faces == 2:
                    flash.y = 0
                    flash_caught = False
                    doomsday_catch = False
                    flash_lives -= 15
                if doomsday_faces == 4:
                    flash.x = WIDTH
                    flash_caught = False
                    doomsday_catch = False
                    flash_lives -= 15
                if doomsday_faces == 6:
                    flash.y = HEIGHT
                    flash_caught = False
                    doomsday_catch = False
                    flash_lives -= 15
                if doomsday_faces == 8:
                    flash.x = 0
                    flash_caught = False
                    doomsday_catch = False
                    flash_lives -= 15

            elif joker_caught == True:
                if doomsday_faces == 2:
                    joker.y = 0
                    joker_caught = False
                    doomsday_catch = False
                    joker_lives -= 15
                if doomsday_faces == 4:
                    joker.x = WIDTH
                    joker_caught = False
                    doomsday_catch = False
                    joker_lives -= 15
                if doomsday_faces == 6:
                    joker.y = HEIGHT
                    joker_caught = False
                    doomsday_catch = False
                    joker_lives -= 15
                if doomsday_faces == 8:
                    joker.y = 0
                    joker_caught = False
                    doomsday_catch = False
                    joker_lives -= 15

            elif joker_helper_caught == True:
                if doomsday_faces == 2:
                    joker_helper.y = 0
                    joker_helper_caught = False
                    doomsday_catch = False
                if doomsday_faces == 4:
                    joker_helper.x = WIDTH
                    joker_helper_caught = False
                    doomsday_catch = False
                if doomsday_faces == 6:
                    joker_helper.y = HEIGHT
                    joker_helper_caught = False
                    doomsday_catch = False
                if doomsday_faces == 8:
                    joker_helper.x = 0
                    joker_helper_caught = False
                    doomsday_catch = False

            elif guy_caught == True:
                if doomsday_faces == 2:
                    guy.y = 0
                    guy_caught = False
                    doomsday_catch = False
                    guy_lives -= 15
                if doomsday_faces == 4:
                    guy.x = WIDTH
                    guy_caught = False
                    doomsday_catch = False
                    guy_lives -= 15
                if doomsday_faces == 6:
                    guy.y = HEIGHT
                    guy_caught = False
                    doomsday_catch = False
                    guy_lives -= 15
                if doomsday_faces == 8:
                    guy.x = 0
                    guy_caught = False
                    doomsday_catch = False
                    guy_lives -= 15

            elif luthor_caught == True:
                if doomsday_faces == 2:
                    luthor.y = 0
                    luthor_caught = False
                    doomsday_catch = False
                    luthor_lives -= 15
                if doomsday_faces == 4:
                    luthor.x = WIDTH
                    luthor_caught = False
                    doomsday_catch = False
                    luthor_lives -= 15
                if doomsday_faces == 6:
                    luthor.y = HEIGHT
                    luthor_caught = False
                    doomsday_catch = False
                    luthor_lives -= 15
                if doomsday_faces == 8:
                    luthor.x = 0
                    luthor_caught = False
                    doomsday_catch = False
                    luthor_lives -= 15

            elif two_face_caught == True:
                if doomsday_faces == 2:
                    two_face.y = 0
                    two_face_caught = False
                    doomsday_catch = False
                    two_face_lives -= 15
                if doomsday_faces == 4:
                    two_face.x = WIDTH
                    two_face_caught = False
                    doomsday_catch = False
                    two_face_lives -= 15
                if doomsday_faces == 6:
                    two_face.y = HEIGHT
                    two_face_caught = False
                    doomsday_catch = False
                    two_face_lives -= 15
                if doomsday_faces == 8:
                    two_face.x = 0
                    two_face_caught = False
                    doomsday_catch = False
                    two_face_lives -= 15



    if batman_alive == True:
        if keyboard.K_1 and batarang_throw == False and batman_alive == True:
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

    if guy.y > HEIGHT:
        guy.y = HEIGHT
    elif guy.y < 0:
        guy.y = 0

    if joker.x > WIDTH:
        joker.x = WIDTH
    elif joker.x < 0:
        joker.x = 0

    if joker.y > HEIGHT:
        joker.y = HEIGHT
    elif joker.y < 0:
        joker.y = 0

    if luthor.x > WIDTH:
        luthor.x = WIDTH
    elif luthor.x < 0:
        luthor.x = 0

    if luthor.y > HEIGHT:
        luthor.y = HEIGHT
    elif luthor.y < 0:
        luthor.y = 0

    if doomsday.x > WIDTH:
        doomsday.x = WIDTH
    elif doomsday.x < 0:
        doomsday.x = 0

    if doomsday.y > HEIGHT:
        doomsday.y = HEIGHT
    elif doomsday.y < 0:
        doomsday.y = 0

    if two_face.x > WIDTH:
        two_face.x = WIDTH
    elif two_face.x < 0:
        two_face.x = 0

    if two_face.y > HEIGHT:
        two_face.y = HEIGHT
    elif two_face.y < 0:
        two_face.y = 0

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
    elif batarang.colliderect(luthor) and breturn == False:
        luthor_confused = True
        dx = batman.x - luthor.x
        dy = batman.y - luthor.y
        total_batman_luthor_distance = math.sqrt(dx ** 2 + dy ** 2)
        if total_batman_luthor_distance > 0 and luthor_alive == True:
            bpull = 150
            luthor.x += (dx / total_batman_luthor_distance) * bpull
            luthor.y += (dy / total_batman_luthor_distance) * bpull
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
    elif batarang.colliderect(two_face) and breturn == False:
        two_face_confused = True
        dx = batman.x - two_face.x
        dy = batman.y - two_face.y
        total_batman_two_face_distance = math.sqrt(dx ** 2 + dy ** 2)
        if total_batman_two_face_distance > 0 and two_face_alive == True:
            bpull = 150
            two_face.x += (dx / total_batman_two_face_distance) * bpull
            two_face.y += (dy / total_batman_two_face_distance) * bpull
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
        if batman.colliderect(superman) and superman_lives > 10 and batman_alive == True:
            superman_lives -= 10
            bac = time.time()
        elif batman.colliderect(superman) and superman_lives <= 10 and superman_alive == True and batman_alive == True:
            superman_lives = 0
            superman_alive = False
            bac = time.time()

    if flash_phase == False:
        if time.time() - bac > 3.0:
            if batman.colliderect(flash) and flash_lives > 10 and batman_alive == True:
                flash_lives -= 10
                bac = time.time()
            elif batman.colliderect(flash) and flash_lives <= 10 and flash_alive == True and batman_alive == True:
                flash_lives = 0
                flash_alive = False
                bac = time.time()

    if time.time() - bac > 3.0:
        if (superman_joker_distance > 150 and superman_alive == True) or (flash_joker_distance > 150 and flash_alive == True) or (joker_guy_distance > 150 and guy_alive == True) or (joker_luthor_distance > 150 and luthor_alive == True):
            if batman.colliderect(joker) and joker_lives > 10 and batman_alive == True:
                joker_lives -= 10
                bac = time.time()
            elif batman.colliderect(joker) and joker_lives <= 10 and joker_alive == True and batman_alive == True:
                joker_lives = 0
                joker_alive = False
                bac = time.time()

    if time.time() - bac > 3.0:
        if batman.colliderect(guy) and guy_lives > 10 and batman_alive == True:
            guy_lives -= 10
            bac = time.time()
        elif batman.colliderect(guy) and guy_lives <= 10 and guy_alive == True and batman_alive == True:
            guy_lives = 0
            guy_alive = False
            bac = time.time() 

    if time.time() - bac > 3.0:
        if batman.colliderect(luthor) and luthor_lives > 10 and batman_alive == True:
            luthor_lives -= 10
            bac = time.time()
        elif batman.colliderect(luthor) and luthor_lives <= 10 and luthor_alive == True and batman_alive == True:
            luthor_lives = 0
            luthor_alive = False
            bac = time.time()

    if time.time() - bac > 3.0:
        if batman.colliderect(two_face) and two_face_lives > 10 and batman_alive == True:
            two_face_lives -= 10
            bac = time.time()
        elif batman.colliderect(two_face) and two_face_lives <= 10 and two_face_lives == True and batman_alive == True:
            two_face_lives = 0
            two_face_alive = False
            bac = time.time()

# superman
        
#     if superman_lives == 0:
#         superman_hearts.x = -100
#         superman_hearts.y = -100
        
# # batman
#     if batman_lives == 0:
#         batman_hearts.x = -100
#         batman_hearts.y = -100

# # flash
#     if flash_lives == 0:
#         flash_hearts.x = -100
#         flash_hearts.y = -100

# # joker
#     if joker_lives == 0:
#         joker_hearts.x = -100
#         joker_hearts.y = -100

# # guy
#     if guy_lives == 0:
#         guy_hearts.x = -100
#         guy_hearts.y = -100

    if superman_lives <= 0 and flash_lives <= 0 and joker_lives <= 0 and guy_lives <= 0 and luthor_lives <= 0 and two_face_lives <= 0:
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

    if batman.colliderect(luthor) and luthor_alive == False:
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

    if batman.colliderect(two_face) and two_face_alive == False:
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

    if superman.colliderect(luthor) and luthor_alive == False:
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

    if superman.colliderect(two_face) and two_face_alive == False:
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
            flash.y += 5.5
        if flash_faces == 4:
            flash.x -= 5.5
        if flash_faces == 6:
            flash.y -= 5.5
        if flash_faces == 8:
            flash.x += 5.5

        if flash_faces == 1:
            flash.x += 4
            flash.y += 4
        if flash_faces == 3:
            flash.x -= 4
            flash.y += 4
        if flash_faces == 5:
            flash.x -= 4
            flash.y -= 4
        if flash_faces == 7:
            flash.x += 4
            flash.y -= 4

    if flash.colliderect(batman) and batman_alive == False:
        if flash_faces == 2:
            flash.y += 5.5
        if flash_faces == 4:
            flash.x -= 5.5
        if flash_faces == 6:
            flash.y -= 5.5
        if flash_faces == 8:
            flash.x += 5.5

        if flash_faces == 1:
            flash.x += 4
            flash.y += 4
        if flash_faces == 3:
            flash.x -= 4
            flash.y += 4
        if flash_faces == 5:
            flash.x -= 4
            flash.y -= 4
        if flash_faces == 7:
            flash.x += 4
            flash.y -= 4

    if flash.colliderect(guy) and guy_alive == False:
        if flash_faces == 2:
            flash.y += 5.5
        if flash_faces == 4:
            flash.x -= 5.5
        if flash_faces == 6:
            flash.y -= 5.5
        if flash_faces == 8:
            flash.x += 5.5

        if flash_faces == 1:
            flash.x += 4
            flash.y += 4
        if flash_faces == 3:
            flash.x -= 4
            flash.y += 4
        if flash_faces == 5:
            flash.x -= 4
            flash.y -= 4
        if flash_faces == 7:
            flash.x += 4
            flash.y -= 4

    if flash.colliderect(joker) and joker_alive == False:
        if flash_faces == 2:
            flash.y += 5.5
        if flash_faces == 4:
            flash.x -= 5.5
        if flash_faces == 6:
            flash.y -= 5.5
        if flash_faces == 8:
            flash.x += 5.5

        if flash_faces == 1:
            flash.x += 4
            flash.y += 4
        if flash_faces == 3:
            flash.x -= 4
            flash.y += 4
        if flash_faces == 5:
            flash.x -= 4
            flash.y -= 4
        if flash_faces == 7:
            flash.x += 4
            flash.y -= 4

    if flash.colliderect(luthor) and luthor_alive == False:
        if flash_faces == 2:
            flash.y += 5.5
        if flash_faces == 4:
            flash.x -= 5.5
        if flash_faces == 6:
            flash.y -= 5.5
        if flash_faces == 8:
            flash.x += 5.5

        if flash_faces == 1:
            flash.x += 4
            flash.y += 4
        if flash_faces == 3:
            flash.x -= 4
            flash.y += 4
        if flash_faces == 5:
            flash.x -= 4
            flash.y -= 4
        if flash_faces == 7:
            flash.x += 4
            flash.y -= 4

    if flash.colliderect(two_face) and two_face_alive == False:
        if flash_faces == 2:
            flash.y += 5.5
        if flash_faces == 4:
            flash.x -= 5.5
        if flash_faces == 6:
            flash.y -= 5.5
        if flash_faces == 8:
            flash.x += 5.5

        if flash_faces == 1:
            flash.x += 4
            flash.y += 4
        if flash_faces == 3:
            flash.x -= 4
            flash.y += 4
        if flash_faces == 5:
            flash.x -= 4
            flash.y -= 4
        if flash_faces == 7:
            flash.x += 4
            flash.y -= 4


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

    if guy.colliderect(luthor) and luthor_alive == False:
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
        
    if guy.colliderect(two_face) and two_face_alive == False:
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

    if joker.colliderect(luthor) and luthor_alive == False:
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

    if joker.colliderect(two_face) and two_face_alive == False:
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


    if luthor.colliderect(superman) and superman_alive == False:
        if luthor_faces == 2:
            luthor.y += 5
        if luthor_faces == 4:
            luthor.x -= 5
        if luthor_faces == 6:
            luthor.y -=5
        if luthor_faces == 8:
            luthor.x += 5

        if luthor_faces == 1:
            luthor.x += 3.5
            luthor.y += 3.5
        if luthor_faces == 3:
            luthor.x -= 3.5
            luthor.y += 3.5
        if luthor_faces == 5:
            luthor.x -= 3.5
            luthor.y -= 3.5
        if luthor_faces == 7:
            luthor.x += 3.5
            luthor.y -= 3.5

    if luthor.colliderect(batman) and batman_alive == False:
        if luthor_faces == 2:
            luthor.y += 5
        if luthor_faces == 4:
            luthor.x -= 5
        if luthor_faces == 6:
            luthor.y -=5
        if luthor_faces == 8:
            luthor.x += 5

        if luthor_faces == 1:
            luthor.x += 3.5
            luthor.y += 3.5
        if luthor_faces == 3:
            luthor.x -= 3.5
            luthor.y += 3.5
        if luthor_faces == 5:
            luthor.x -= 3.5
            luthor.y -= 3.5
        if luthor_faces == 7:
            luthor.x += 3.5
            luthor.y -= 3.5
    
    if luthor.colliderect(flash) and flash_alive == False:
        if luthor_faces == 2:
            luthor.y += 5
        if luthor_faces == 4:
            luthor.x -= 5
        if luthor_faces == 6:
            luthor.y -=5
        if luthor_faces == 8:
            luthor.x += 5

        if luthor_faces == 1:
            luthor.x += 3.5
            luthor.y += 3.5
        if luthor_faces == 3:
            luthor.x -= 3.5
            luthor.y += 3.5
        if luthor_faces == 5:
            luthor.x -= 3.5
            luthor.y -= 3.5
        if luthor_faces == 7:
            luthor.x += 3.5
            luthor.y -= 3.5

    if luthor.colliderect(joker) and joker_alive == False:
        if luthor_faces == 2:
            luthor.y += 5
        if luthor_faces == 4:
            luthor.x -= 5
        if luthor_faces == 6:
            luthor.y -=5
        if luthor_faces == 8:
            luthor.x += 5

        if luthor_faces == 1:
            luthor.x += 3.5
            luthor.y += 3.5
        if luthor_faces == 3:
            luthor.x -= 3.5
            luthor.y += 3.5
        if luthor_faces == 5:
            luthor.x -= 3.5
            luthor.y -= 3.5
        if luthor_faces == 7:
            luthor.x += 3.5
            luthor.y -= 3.5

    if luthor.colliderect(guy) and guy_alive == False:
        if luthor_faces == 2:
            luthor.y += 5
        if luthor_faces == 4:
            luthor.x -= 5
        if luthor_faces == 6:
            luthor.y -=5
        if luthor_faces == 8:
            luthor.x += 5

        if luthor_faces == 1:
            luthor.x += 3.5
            luthor.y += 3.5
        if luthor_faces == 3:
            luthor.x -= 3.5
            luthor.y += 3.5
        if luthor_faces == 5:
            luthor.x -= 3.5
            luthor.y -= 3.5
        if luthor_faces == 7:
            luthor.x += 3.5
            luthor.y -= 3.5 

    if luthor.colliderect(two_face) and two_face_alive == False:
        if luthor_faces == 2:
            luthor.y += 5
        if luthor_faces == 4:
            luthor.x -= 5
        if luthor_faces == 6:
            luthor.y -=5
        if luthor_faces == 8:
            luthor.x += 5

        if luthor_faces == 1:
            luthor.x += 3.5
            luthor.y += 3.5
        if luthor_faces == 3:
            luthor.x -= 3.5
            luthor.y += 3.5
        if luthor_faces == 5:
            luthor.x -= 3.5
            luthor.y -= 3.5
        if luthor_faces == 7:
            luthor.x += 3.5
            luthor.y -= 3.5   


    if doomsday.colliderect(superman) and doomsday_faces != 0:
        if doomsday_faces == 2:
            superman.y -= 5
        if doomsday_faces == 4:
            superman.x += 5
        if doomsday_faces == 6:
            superman.y += 5
        if doomsday_faces == 8:
            superman.x -= 5

        if doomsday_faces == 1:
            superman.x -= 3.5
            superman.y -= 3.5
        if doomsday_faces == 3:
            superman.x += 3.5
            superman.y -= 3.5
        if doomsday_faces == 5:
            superman.x += 3.5
            superman.y += 3.5
        if doomsday_faces == 7:
            superman.x -= 3.5
            superman.y += 3.5
    elif doomsday.colliderect(superman) and doomsday_faces == 0:
        if superman_faces == 2:
            superman.y += 5
        if superman_faces == 4:
            superman.x -= 5
        if superman_faces == 6:
            superman.y -= 5
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

    if doomsday.colliderect(batman) and doomsday_faces != 0:
        if doomsday_faces == 2:
            batman.y -= 5
        if doomsday_faces == 4:
            batman.x += 5
        if doomsday_faces == 6:
            batman.y += 5
        if doomsday_faces == 8:
            batman.x -= 5

        if doomsday_faces == 1:
            batman.x -= 3.5
            batman.y -= 3.5
        if doomsday_faces == 3:
            batman.x += 3.5
            batman.y -= 3.5
        if doomsday_faces == 5:
            batman.x += 3.5
            batman.y += 3.5
        if doomsday_faces == 7:
            batman.x -= 3.5
            batman.y += 3.5
    elif doomsday.colliderect(batman) and doomsday_faces == 0:
        if batman_faces == 2:
            batman.y += 5
        if batman_faces == 4:
            batman.x -= 5
        if batman_faces == 6:
            batman.y -= 5
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
    
    if doomsday.colliderect(flash) and doomsday_faces != 0:
        if doomsday_faces == 2:
            flash.y -= 5
        if doomsday_faces == 4:
            flash.x += 5
        if doomsday_faces == 6:
            flash.y += 5
        if doomsday_faces == 8:
            flash.x -= 5

        if doomsday_faces == 1:
            flash.x -= 3.5
            flash.y -= 3.5
        if doomsday_faces == 3:
            flash.x += 3.5
            flash.y -= 3.5
        if doomsday_faces == 5:
            flash.x += 3.5
            flash.y += 3.5
        if doomsday_faces == 7:
            flash.x -= 3.5
            flash.y += 3.5
    elif doomsday.colliderect(flash) and doomsday_faces == 0:
        if flash_faces == 2:
            flash.y += 5.5
        if flash_faces == 4:
            flash.x -= 5.5
        if flash_faces == 6:
            flash.y -= 5.5
        if flash_faces == 8:
            flash.x += 5.5

        if flash_faces == 1:
            flash.x += 4
            flash.y += 4
        if flash_faces == 3:
            flash.x -= 4
            flash.y += 4
        if flash_faces == 5:
            flash.x -= 4
            flash.y -= 4
        if flash_faces == 7:
            flash.x += 4
            flash.y -= 4

    if doomsday.colliderect(joker) and doomsday_faces != 0:
        if doomsday_faces == 2:
            joker.y -= 5
        if doomsday_faces == 4:
            joker.x += 5
        if doomsday_faces == 6:
            joker.y += 5
        if doomsday_faces == 8:
            joker.x -= 5

        if doomsday_faces == 1:
            joker.x -= 3.5
            joker.y -= 3.5
        if doomsday_faces == 3:
            joker.x += 3.5
            joker.y -= 3.5
        if doomsday_faces == 5:
            joker.x += 3.5
            joker.y += 3.5
        if doomsday_faces == 7:
            joker.x -= 3.5
            joker.y += 3.5
    elif doomsday.colliderect(joker) and doomsday_faces == 0:
        if joker_faces == 2:
            joker.y += 5
        if joker_faces == 4:
            joker.x -= 5
        if joker_faces == 6:
            joker.y -= 5
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

    if doomsday.colliderect(guy) and doomsday_faces != 0:
        if doomsday_faces == 2:
            guy.y -= 5
        if doomsday_faces == 4:
            guy.x += 5
        if doomsday_faces == 6:
            guy.y += 5
        if doomsday_faces == 8:
            guy.x -= 5

        if doomsday_faces == 1:
            guy.x -= 3.5
            guy.y -= 3.5
        if doomsday_faces == 3:
            guy.x += 3.5
            guy.y -= 3.5
        if doomsday_faces == 5:
            guy.x += 3.5
            guy.y += 3.5
        if doomsday_faces == 7:
            guy.x -= 3.5
            guy.y += 3.5
    elif doomsday.colliderect(guy) and doomsday_faces == 0:
        if guy_faces == 2:
            guy.y += 5
        if guy_faces == 4:
            guy.x -= 5
        if guy_faces == 6:
            guy.y -= 5
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

    if doomsday.colliderect(two_face) and doomsday_faces != 0:
        if doomsday_faces == 2:
            two_face.y -= 5
        if doomsday_faces == 4:
            two_face.x += 5
        if doomsday_faces == 6:
            two_face.y += 5
        if doomsday_faces == 8:
            two_face.x -= 5

        if doomsday_faces == 1:
            two_face.x -= 3.5
            two_face.y -= 3.5
        if doomsday_faces == 3:
            two_face.x += 3.5
            two_face.y -= 3.5
        if doomsday_faces == 5:
            two_face.x += 3.5
            two_face.y += 3.5
        if doomsday_faces == 7:
            guy.x -= 3.5
            guy.y += 3.5
    elif doomsday.colliderect(guy) and doomsday_faces == 0:
        if two_face_faces == 2:
            two_face.y += 5
        if two_face_faces == 4:
            two_face.x -= 5
        if two_face_faces == 6:
            two_face.y -= 5
        if two_face_faces == 8:
            two_face.x += 5

        if two_face_faces == 1:
            two_face.x += 3.5
            two_face.y += 3.5
        if two_face_faces == 3:
            two_face.x -= 3.5
            two_face.y += 3.5
        if two_face_faces == 5:
            two_face.x -= 3.5
            two_face.y -= 3.5
        if two_face_faces == 7:
            two_face.x += 3.5
            two_face.y -= 3.5


    if two_face.colliderect(superman) and superman_alive == False:
        if two_face_faces == 2:
            two_face.y += 5
        if two_face_faces == 4:
            two_face.x -= 5
        if two_face_faces == 6:
            two_face.y -=5
        if two_face_faces == 8:
            two_face.x += 5

        if two_face_faces == 1:
            two_face.x += 3.5
            two_face.y += 3.5
        if two_face_faces == 3:
            two_face.x -= 3.5
            two_face.y += 3.5
        if two_face_faces == 5:
            two_face.x -= 3.5
            two_face.y -= 3.5
        if two_face_faces == 7:
            two_face.x += 3.5
            two_face.y -= 3.5

    if two_face.colliderect(batman) and batman_alive == False:
        if two_face_faces == 2:
            two_face.y += 5
        if two_face_faces == 4:
            two_face.x -= 5
        if two_face_faces == 6:
            two_face.y -=5
        if two_face_faces == 8:
            two_face.x += 5

        if two_face_faces == 1:
            two_face.x += 3.5
            two_face.y += 3.5
        if two_face_faces == 3:
            two_face.x -= 3.5
            two_face.y += 3.5
        if two_face_faces == 5:
            two_face.x -= 3.5
            two_face.y -= 3.5
        if two_face_faces == 7:
            two_face.x += 3.5
            two_face.y -= 3.5
    
    if two_face.colliderect(flash) and flash_alive == False:
        if two_face_faces == 2:
            two_face.y += 5
        if two_face_faces == 4:
            two_face.x -= 5
        if two_face_faces == 6:
            two_face.y -=5
        if two_face_faces == 8:
            two_face.x += 5

        if two_face_faces == 1:
            two_face.x += 3.5
            two_face.y += 3.5
        if two_face_faces == 3:
            two_face.x -= 3.5
            two_face.y += 3.5
        if two_face_faces == 5:
            two_face.x -= 3.5
            two_face.y -= 3.5
        if two_face_faces == 7:
            two_face.x += 3.5
            two_face.y -= 3.5

    if two_face.colliderect(joker) and joker_alive == False:
        if two_face_faces == 2:
            two_face.y += 5
        if two_face_faces == 4:
            two_face.x -= 5
        if two_face_faces == 6:
            two_face.y -=5
        if two_face_faces == 8:
            two_face.x += 5

        if two_face_faces == 1:
            two_face.x += 3.5
            two_face.y += 3.5
        if two_face_faces == 3:
            two_face.x -= 3.5
            two_face.y += 3.5
        if two_face_faces == 5:
            two_face.x -= 3.5
            two_face.y -= 3.5
        if two_face_faces == 7:
            two_face.x += 3.5
            two_face.y -= 3.5

    if two_face.colliderect(guy) and guy_alive == False:
        if two_face_faces == 2:
            two_face.y += 5
        if two_face_faces == 4:
            two_face.x -= 5
        if two_face_faces == 6:
            two_face.y -=5
        if two_face_faces == 8:
            two_face.x += 5

        if two_face_faces == 1:
            two_face.x += 3.5
            two_face.y += 3.5
        if two_face_faces == 3:
            two_face.x -= 3.5
            two_face.y += 3.5
        if two_face_faces == 5:
            two_face.x -= 3.5
            two_face.y -= 3.5
        if two_face_faces == 7:
            two_face.x += 3.5
            two_face.y -= 3.5 

    if two_face.colliderect(luthor) and luthor_alive == False:
        if two_face_faces == 2:
            two_face.y += 5
        if two_face_faces == 4:
            two_face.x -= 5
        if two_face_faces == 6:
            two_face.y -=5
        if two_face_faces == 8:
            two_face.x += 5

        if two_face_faces == 1:
            two_face.x += 3.5
            two_face.y += 3.5
        if two_face_faces == 3:
            two_face.x -= 3.5
            two_face.y += 3.5
        if two_face_faces == 5:
            two_face.x -= 3.5
            two_face.y -= 3.5
        if two_face_faces == 7:
            two_face.x += 3.5
            two_face.y -= 3.5   


    superman_bleed_count += 1
    batman_bleed_count += 1
    flash_bleed_count += 1
    joker_bleed_count += 1
    guy_bleed_count += 1
    luthor_bleed_count += 1

    if superman_bleed_count % 60 == 0:
        if superman_bleed == True:
            superman_lives -= 3

    if superman_bleed_count == 240:
        superman_bleed = False
        superman_bleed_count = 0


    if batman_bleed_count % 60 == 0:
        if batman_bleed == True:
            batman_lives -= 5

    if batman_bleed_count == 300:
        batman_bleed = False
        batman_bleed_count = 0


    if flash_bleed_count % 60 == 0:
        if flash_bleed == True:
            flash_lives -= 5

    if flash_bleed_count == 240:
        flash_bleed = False
        flash_bleed_count = 0


    if joker_bleed_count % 60 == 0:
        if joker_bleed == True:
            joker_lives -= 5

    if joker_bleed_count == 300:
        joker_bleed = False
        joker_bleed_count = 0


    if guy_bleed_count % 60 == 0:
        if guy_bleed == True:
            guy_lives -= 7

    if guy_bleed_count == 480:
        guy_bleed = False
        guy_bleed_count = 0


    if luthor_bleed_count % 60 == 0:
        if luthor_bleed == True:
            luthor_lives -= 4

    if luthor_bleed_count == 240:
        luthor_bleed = False
        luthor_bleed_count = 0


    if two_face_bleed_count % 60 == 0:
        if two_face_bleed == True:
            two_face_lives -= 5

    if two_face_bleed_count == 300:
        two_face_bleed = False
        two_face_bleed_count = 0

pgzrun.go()