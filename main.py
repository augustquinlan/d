def on_pin_pressed_p0():
    basic.show_string("May I play switch?")
    basic.clear_screen()
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    basic.show_string("I am scared.")
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    basic.show_string("I'm hungry.")
    basic.clear_screen()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    basic.show_string("I am sad")
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    basic.show_string("May I go around the block?")
    basic.clear_screen()
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
