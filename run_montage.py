import sys
import re
import time
import argparse

from collections import namedtuple, deque
from itertools import cycle, chain, repeat

import numpy as np

from PIL import Image
import rgbmatrix as rgb

sys.path.append("/home/pi/pixel_art/")
from settings import (NES_PALETTE_HEX, dispmatrix)
from core import *

from sprites.zelda2 import zelda2_animation
from sprites.finalfantasy import finalfantasy_animation
from sprites.megaman2 import megaman2_animation
from sprites.ninjagaiden import ninjagaiden_animation
from sprites.blastermaster import blastermaster_animation
from sprites.dragonwarrior import dragonwarrior_animation

def parse_arguments():

    class CustomFormatter(argparse.RawDescriptionHelpFormatter):
        pass

    desc = ("Run 8-bit pixel art animation montage on 32 x 32 RGB LED display")

    epilog = """
    """

    parser = argparse.ArgumentParser(description=desc,
                                     add_help=False,
                                     epilog=epilog,
                                     formatter_class=CustomFormatter)
    
    opt = parser.add_argument_group("Optional arguments")
    opt.add_argument("-c", "--cycles",
                     action="store",
                     dest="cycles",
                     help=("Number of animation frames (roughly) to run per animation sequence "
                           "(default: 500)"),
                     default=500,
                     type=int,
                     metavar="INT")
    opt.add_argument("-s", "--shuffle",
                     action="store_true",
                     dest="shuffle",
                     help="Shuffle sequence of of animations prior to launch")
    opt.add_argument("-h", "--help",
                     action="help",
                     help="show this help message and exit")
    return parser.parse_args()


def main():

    args = parse_arguments()

    cycles = args.cycles
    shuffle = args.shuffle

    scenes = [zelda2_animation, 
              finalfantasy_animation,
              megaman2_animation,
              ninjagaiden_animation,
              blastermaster_animation,
              dragonwarrior_animation]

    if shuffle:
        np.random.shuffle(scenes)

    scenes = deque(scenes)  
    
    #Clear the display in case anything's still on it.
    dispmatrix.Clear()

    while True:
        
        arr1 = animate_sprites(dispmatrix=dispmatrix, 
                               sprite_list=scenes[0].sprite_list, 
                               bg_sprite=scenes[0].bg_sprite,
                               xoff=scenes[0].xoff,
                               yoff=scenes[0].yoff,
                               frame_time=scenes[0].frame_time,
                               spbg_ratio=scenes[0].spbg_ratio,
                               center=scenes[0].center,
                               bg_scroll_speed=scenes[0].bg_scroll_speed,
                               cycles=max(1, int(cycles/(len(scenes[0].sprite_list) * scenes[0].spbg_ratio))),
                               clear=False)
        
        arr2 = display_sprite(dispmatrix=dispmatrix, 
                              sprite=scenes[1].sprite_list[0], 
                              bg_sprite=scenes[1].bg_sprite, 
                              center=scenes[1].center,
                              display=False)
        
        transition(dispmatrix=dispmatrix,
                   arr_one=arr1,
                   arr_two=arr2)

        scenes.rotate(-1)


if __name__ == "__main__":
    try:
      main()
    # If the script is killed by ctrl-c, clear the display.
    except KeyboardInterrupt:
      dispmatrix.Clear()
