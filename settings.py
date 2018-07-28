#!/usr/bin/env python

from collections import namedtuple

import numpy as np
import rgbmatrix as rgb

# Define the NES palette in hex RGB values.
NES_PALETTE_HEX = np.array([["7c7c7c", "0000fc", "0000bc", "4428bc", "940084", "a80020",
                             "a81000", "881400", "503000", "007800", "006800", "005800",
                             "004058", "000000", "000000", "000000"],
                            ["bcbcbc", "0078f8", "0058f8", "6844fc", "d800cc", "e40058",
                             "f83800", "e45c10", "ac7c00", "00b800", "00a800", "00a844",
                             "008888", "000000", "000000", "000000"],
                            ["f8f8f8", "3cbcfc", "6888fc", "9878f8", "f878f8", "f85898",
                             "f87858", "fca044", "f8b800", "b8f818", "58d854", "58f898",
                             "00e8d8", "787878", "000000", "000000"],
                            ["fcfcfc", "a4e4fc", "b8b8f8", "d8b8f8", "f8b8f8", "f8a4c0",
                             "f0d0b0", "fce0a8", "f8d878", "d8f878", "b8f8b8", "b8f8d8",
                             "00fcfc", "f8d8f8", "000000", "000000"]], dtype='<U6')


# Configure the rgbmatrix library for the 32 x 32 LED display
options = rgb.RGBMatrixOptions()
options.rows = 32
options.cols = 32
options.brightness = 50
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = "adafruit-hat"
options.disable_hardware_pulsing = False

dispmatrix = rgb.RGBMatrix(options=options)

# Define animation settings tuple
animation_settings = namedtuple("animation_settings", ("sprite_list "  
                                                       "bg_sprites "
                                                       "xoffs "
                                                       "yoffs "
                                                       "frame_time "
                                                       "spbg_ratio "
                                                       "center "
                                                       "bg_scroll_speed "
                                                       "cycles_per_char "
                                                       "reversible"))
