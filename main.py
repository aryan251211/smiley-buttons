def on_button_pressed_a():
    led.stop_animation()
    basic.show_leds("""
        # # . # #
        # # . # #
        . . . . .
        # . . . #
        . # # # .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    led.stop_animation()
    basic.show_leds("""
        . . # . .
        . # # # .
        # # . # #
        # # # # #
        # . # . #
        """)
    basic.show_leds("""
        # # . # #
        # # # # #
        # . # . #
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        # . # . #
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    led.stop_animation()
    basic.show_leds("""
        # # . # #
        # # . # #
        . . . . .
        . # # # .
        # . . . #
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_string("ARYAN")
    basic.pause(2000)
basic.forever(on_forever)
