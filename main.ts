input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    basic.showString("May I play switch?")
    basic.clearScreen()
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("I am scared.")
    basic.clearScreen()
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    basic.showString("I'm hungry.")
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showString("I am sad")
    basic.clearScreen()
})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    basic.showString("May I go around the block?")
    basic.clearScreen()
})
