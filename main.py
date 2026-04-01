WIDTH = 640
HEIGHT = 360

TITLE = "LiamGame"

def draw():
    screen.clear()
    screen.fill((30, 30, 40))
    screen.draw.text(
        "Hello, Pygame Zero!",
        midtop=(WIDTH // 2, 40),
        fontsize=48,
        color=(240, 240, 255),
        owidth=1,
        ocolor=(20, 20, 30),
    )

