from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.avr_promicro import translate as avr
from kmk.quickpin.pro_micro.helios import pinout as pins
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        pins[avr['C6']],
        pins[avr['D7']],
        pins[avr['E6']],
        pins[avr['B4']],
        pins[avr['B5']],
    )
    row_pins = (
        pins[avr['F7']],
        pins[avr['B1']],
        pins[avr['B3']],
        pins[avr['B2']],
        pins[avr['B6']],
    )
    data_pin = pins[avr['D0']]
    # data_pin2 =
    # rgb_pixel_pin = pins[avr['D3']]
    # num_pixels = 12
    diode_orientation = DiodeOrientation.COLUMNS
    # fmt: off
    coord_mapping = [
        0,  1,  2,  3,  4,             25, 26, 27, 28, 29,
        5,  6,  7,  8,  9,             30, 31, 32, 33, 34,
        10, 11, 12, 13, 14,            35, 36, 37, 38, 39,
            16, 17,         24,    45,         42, 43,
                    18, 19, 23,    46, 40, 41,
                        22,            47
    ]
    # fmt:on
