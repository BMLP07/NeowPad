# Basic KMK Keyboard with Rotary Encoder and Macros yet to personalize. This code is a starting point and can be further customized to fit specific needs.

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Macros

# Initialize the keyboard and macros module
keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

# Define the key matrix
keyboard.row_pins = (board.GP4, board.GP3, board.GP2) 
keyboard.col_pins = (board.GP26, board.GP27, board.GP28, board.GP29, board.GP6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define rotary encoder
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (board.GP7, board.GP1, board.GP0, False),
)

# Macros 
MAIL_MACRO = KC.MACRO("hello@earth.com")

LOCK_PC = KC.MACRO(KC.LCMD(KC.L))

UNDO = KC.MACRO(KC.LCTL(KC.Z))

# Keymap
keyboard.keymap = [
    [
        MAIL_MACRO, UNDO, LOCK_PC, KC.N9, KC.N0,
        
        KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,
        
        KC.A,  KC.B,  KC.C,  KC.D,  KC.E,
    ]
]

# Encoder Actions
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),), # Vol Down / Vol Up / Mute
]

if __name__ == '__main__':
    keyboard.go()