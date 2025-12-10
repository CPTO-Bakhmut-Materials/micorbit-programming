is_rolled = False

roll_animation = [
    images.create_image("""
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        """),
    images.create_image("""
        . . . . .
        . . # . .
        . # # # .
        . . # . .
        . . . . .
        """),
    images.create_image("""
        . . . . .
        . # # # .
        . # . # .
        . # # # .
        . . . . .
        """),
]

def play_animation():
    for cycle in range(int(Math.random() * 2) + 1):
        for index in range(len(roll_animation)):
            roll_animation[index].show_image(0)
            pause(100)

def reset():
    global is_rolled
    is_rolled = False
    basic.clear_screen()
input.on_button_pressed(Button.A, reset)

def do_roll():
    global is_rolled
    is_rolled = True
input.on_gesture(Gesture.SHAKE, do_roll)

dice_images = [
    images.create_image("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """),
    images.create_image("""
        . . . . .
        . # . . .
        . . . . .
        . . . # .
        . . . . .
        """),
    images.create_image( """
        . . . . .
        . . . # .
        . . # . .
        . # . . .
        . . . . .
        """),
    images.create_image( """
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . . . . .
        """),
    images.create_image( """
        . . . . .
        . # . # .
        . . # . .
        . # . # .
        . . . . .
        """),
    images.create_image( """
        . . . . .
        . # # # .
        . . . . .
        . # # # .
        . . . . .
        """),
    ]

def on_forever():
    global is_rolled
    if is_rolled:
        play_animation()

        roll = Math.round(Math.random() * 5)
        image_to_show = dice_images[int(roll) % len(dice_images)]
        image_to_show.show_image(0)
        pause(100)

        is_rolled = False
basic.forever(on_forever)