# Basic KMK Keyboard with Rotary Encoder and Macros yet to personalize. This code is a starting point and can be further customized to fit specific needs.

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Macros
from kmk.extensions.media_keys import MediaKeys

# Initialize the keyboard, macros and encoder modules
keyboard = KMKKeyboard()
macros = Macros()
encoder_handler = EncoderHandler()

keyboard.modules.append(macros)
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())

# Define the key matrix
keyboard.row_pins = (board.D8, board.D9, board.D10) 
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3, board.D4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define the rotary encoder
encoder_handler.pins = (
    (board.D5, board.D6, board.D7, True),
)

# Keymap
keyboard.keymap = [
    [
        # First row D8
        KC.LWIN(KC.L), KC.LALT(KC.F4), KC.LWIN(KC.TAB), KC.LWIN(KC.LCTL(KC.LEFT)), KC.LWIN(KC.LCTL(KC.RIGHT)),
        
        # Second row D9
        KC.LCTL(KC.LSHIFT(KC.ESC)), KC.LWIN(KC.I), KC.LWIN(KC.D), KC.LALT(KC.LSHIFT(KC.ESC)), KC.LALT(KC.ESC),
        
        # Third row D10
        KC.LWIN(KC.R), KC.LWIN(KC.E), KC.LCTL(KC.LSHIFT(KC.S)), KC.LCTL(KC.LSHIFT(KC.TAB)), KC.LCTL(KC.TAB),
    ]
]

# Encoder Actions
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),), 
]

if __name__ == '__main__':
    keyboard.go()
