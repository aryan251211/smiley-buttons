input.onButtonPressed(Button.A, function () {
    led.stopAnimation()
    basic.showLeds(`
        # # . # #
        # # . # #
        . . . . .
        # . . . #
        . # # # .
        `)
})
input.onButtonPressed(Button.AB, function () {
    led.stopAnimation()
    basic.showLeds(`
        . . # . .
        . # # # .
        # # . # #
        # # # # #
        # . # . #
        `)
    basic.showLeds(`
        # # . # #
        # # # # #
        # . # . #
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        # . # . #
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
input.onButtonPressed(Button.B, function () {
    led.stopAnimation()
    basic.showLeds(`
        # # . # #
        # # . # #
        . . . . .
        . # # # .
        # . . . #
        `)
})
basic.forever(function () {
    basic.showString("ARYAN")
    basic.pause(100)
})
