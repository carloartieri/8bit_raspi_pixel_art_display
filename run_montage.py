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
from sprites.supermariobros3 import smb3_animation
from sprites.castlevania3 import castlevania3_animation

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
    opt.add_argument("-a", "--cycleall",
                     action="store_true",
                     dest="cycleall",
                     help="Cycle through all sprites in a scene rather than choosing one at random "
                     )
    opt.add_argument("-h", "--help",
                     action="help",
                     help="show this help message and exit")
    return parser.parse_args()


def main():

    args = parse_arguments()

    shuffle = args.shuffle
    
    scenes = [
              zelda2_animation, 
              finalfantasy_animation,
              megaman2_animation,
              ninjagaiden_animation,
              blastermaster_animation,
              dragonwarrior_animation,
              smb3_animation,
              castlevania3_animation
              dragonstrike_animation
              excitebike_animation
             ]

    #Adjust cycles for cycleall
    cycles = max(1, int(args.cycles/(len(scenes[0].sprite_list) * scenes[0].spbg_ratio)))
    if args.cycleall:
        cycles = int(cycles/np.mean([x.cycles_per_char for x in scenes]))
 
    if shuffle:
        np.random.shuffle(scenes)

    scenes = deque(scenes)  
    
    #Clear the display in case anything's still on it.
    dispmatrix.Clear()
    
    #Seed the display with black for the first transition
    arr = display_sprite(dispmatrix=dispmatrix, 
                           sprite=scenes[0].bg_sprites[0], 
                           bg_sprite=None, 
                           center=True,
                           xoff=0,
                           yoff=0,
                           display=False)
    arr1 = np.full((arr.shape[0], arr.shape[1], 3), convert_hex_to_rgb_tuple("000000"), dtype=np.uint8)

    while True:
        
        arr1 = animate_sprites(dispmatrix=dispmatrix, 
                               sprite_list=scenes[0].sprite_list, 
                               bg_sprites=scenes[0].bg_sprites,
                               xoffs=scenes[0].xoffs,
                               yoffs=scenes[0].yoffs,
                               frame_time=scenes[0].frame_time,
                               spbg_ratio=scenes[0].spbg_ratio,
                               center=scenes[0].center,
                               bg_scroll_speed=scenes[0].bg_scroll_speed,
                               cycles=cycles,
                               clear=False,
                               transition=True,
                               transition_arr=arr1,
                               cycles_per_char=scenes[0].cycles_per_char,
                               cycle_all=args.cycleall
                              )

        scenes.rotate(-1)


if __name__ == "__main__":
    try:
      main()
    # If the script is killed by ctrl-c, clear the display.
    except KeyboardInterrupt:
      dispmatrix.Clear()
