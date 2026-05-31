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
keyboard.row_pins = (board.D8, board.D10, board.D9) 
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3, board.D4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define the rotary encoder
encoder_handler.pins = (
    (board.D5, board.D6, board.D7, True),
)

# Macros 
MAIL_MACRO = KC.MACRO("esto funciona")

LOCK_PC  = KC.LWIN(KC.L)

# Keymap
keyboard.keymap = [
    [
        # First row D8
        LOCK_PC, KC.NO, MAIL_MACRO, KC.NO, KC.N0,
        
        # Second row D10
        KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, 
        
        # Third row D9
        KC.A,  KC.B,  KC.C,  KC.D,  KC.E,
    ]
]

# Encoder Actions
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),), 
]

if __name__ == '__main__':
    keyboard.go()
