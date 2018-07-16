import sys
sys.path.append("../")
from settings import (NES_PALETTE_HEX, animation_settings)
from core import sprite

from settings import (NES_PALETTE_HEX, animation_settings)
from core import sprite

Sophia01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 5],
    },
    matrix = [
        "x10b15x1",
        "x9b1w2b2w2b1w1b3w4b1",
        "x1b8w1b2w4b6w3b1",
        "b1w2b1w4b3w5b4w1b2w1b1x1",
        "b1w2b1w4b3w4b4w1r2b2x2",
        "b1r2b1r4b3w3b1w1r2w1r4b1x2",
        "x1b13w1b2r6b1x2",
        "x8b1w1r8b5x3",
        "x9b1w1r6b1x8",
        "x10b7x9",
        "x3b4x3b1w4b1x4b3x3",
        "x2b1w4b1x1b1w6b1x2b1w3b1x2",
        "x1b1w6b2w6b1x1b3w3b1x1",
        "x1b8x1b6x1b1w1b3w2b1x1",
        "x1b8x1b1w1r3b1x1b1w2b3w1b1x1",
        "x1b1r1w4r1b1x2b4x2b1r1w2b3x2",
        "x2b1r4b1x10b1r3b1x3",
        "x3b4x12b3x4"
        
    ]    
)

Sophia02 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 5],
    },
    matrix = [
        "x10b15x1",
        "x9b1w2b2w2b1w1b3w4b1",
        "x1b8w1b2w4b6w3b1",
        "b1w2b1w4b3w5b4w1b2w1b1x1",
        "b1w2b1w4b3w4b4w1r2b2x2",
        "b1r2b1r4b3w3b1w1r2w1r4b1x2",
        "x1b13w1b2r6b1x2",
        "x8b1w1r8b5x3",
        "x9b1w1r6b1x8",
        "x10b7x9",
        "x4b3x3b1w4b1x3b4x3",
        "x3b1w3b1x1b1w6b1x1b1w1b2w1b1x2",
        "x2b3w3b2w6b2w2b2w2b1x1",
        "x1b1w1b3w2b1x1b6x1b1w2b2w2b1x1",
        "x1b1w2b3w1b1x1b1w1r3b1x1b1w2b2w2b1x1",
        "x1b1r1w2b3x3b4x2b1r1w1b2w1r1b1x1",
        "x2b1r3b1x11b1r1b2r1b1x2",
         "x3b3x13b4x3"
        
    ]    
)

Sophia03 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 5],
    },
    matrix = [
        "x10b15x1",
        "x9b1w2b2w2b1w1b3w4b1",
        "x1b8w1b2w4b6w3b1",
        "b1w2b1w4b3w5b4w1b2w1b1x1",
        "b1w2b1w4b3w4b4w1r2b2x2",
        "b1r2b1r4b3w3b1w1r2w1r4b1x2",
        "x1b13w1b2r6b1x2",
        "x8b1w1r8b5x3",
        "x9b1w1r6b1x8",
        "x10b7x9",
        "x3b4x3b1w4b1x3b3x4",
        "x2b1w1b2w1b1x1b1w6b1x1b1w3b1x3",
        "x1b1w2b2w2b2w6b2w3b3x2",
        "x1b1w2b2w2b1x1b6x1b1w2b3w1b1x1",
        "x1b1w2b2w2b1x1b1w1r3b1x1b1w1b3w2b1x1",
        "x1b1r1w1b2w1r1b1x2b4x3b3w2r1b1x1",
        "x2b1r1b2r1b1x11b1r3b1x2",
        "x3b4x13b3x3"
        
    ]    
)

Sophia04 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 5],
    },
    matrix = [
        "x10b15x1",
        "x9b1w2b2w2b1w1b3w4b1",
        "x1b8w1b2w4b6w3b1",
        "b1w2b1w4b3w5b4w1b2w1b1x1",
        "b1w2b1w4b3w4b4w1r2b2x2",
        "b1r2b1r4b3w3b1w1r2w1r4b1x2",
        "x1b13w1b2r6b1x2",
        "x8b1w1r8b5x3",
        "x9b1w1r6b1x8",
        "x10b7x9",
        "x3b3x4b1w4b1x3b4x3",
        "x2b1w3b1x2b1w6b1x1b1w4b1x2",
        "x1b1w3b3x1b1w6b2w6b1x1",
        "x1b1w2b3w1b1x1b6x1b8x1",
        "x1b1w1b3w2b1x1b1w1r3b1x1b8x1",
        "x2b3w2r1b1x2b4x2b1r1w4r1b1x1",
        "x3b1r3b1x10b1r4b1x2",
        "x4b3x12b4x3"
    ]    
)

bmbg_1 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "r":NES_PALETTE_HEX[1, 8],
        "g":NES_PALETTE_HEX[1, 0],
        "e":NES_PALETTE_HEX[1, 9],
        "f":NES_PALETTE_HEX[0, 8],
    },
    matrix = [
        "b3f1b12" + "b3f1b12",
        "f1b2f1b7f1b4" + "f1b2f1b7f1b4",
        "f1b5f1b2f1b4f1b1" + "f1b5f1b2f1b4f1b1",
        "b8f3b5" + "b8f3b5",
        "b4f2b2f1g1f2b4" + "b4f2b2f1g1f2b4",
        "f2b3f1b2f2g1f1b4" + "f2b3f1b2f2g1f1b4",
        "f1g1f1b6f2b3f2" + "f1g1f1b6f2b3f2",
        "g1f2b2f2b7f1b1" + "g1f2b2f2b7f1b1",
        "g1f2b1f1g1f1b2f1b6" + "g1f2b1f1g1f1b2f1b6",
        "f1g1f1b1f1g1b2f3b1f2b2" + "f1g1f1b1f1g1b2f3b1f2b2",
        "g1f1b3f1b1f1g2f1b1f1b3" + "g1f1b3f1b1f1g2f1b1f1b3",
        "f1b6f1g1f2b5" + "f1b6f1g1f2b5",
        "b7f2g1f1b5" + "b7f2g1f1b5",
        "b4f1b3g1f1b5f1" + "b4f1b3g1f1b5f1",
        "b3f3b2f2b2f1b3" + "b3f3b2f2b2f1b3",
        "f1b2f1g1f2b4f1g1f1b2" + "f1b2f1g1f2b4f1g1f1b2",
        "f1b1f1g3f1b2f1b2f1b3" + "f1b1f1g3f1b2f1b2f1b3",
        "b3f1g1f2g1f1g1f1b3f2" + "b3f1g1f2g1f1g1f1b3f2",
        "b3f4b1f4b2f1b1" + "b3f4b1f4b2f1b1",
        "b4f1b3f1g2f1b4" + "b4f1b3f1g2f1b4",
        "f1b4f1b2f1g2f1b4" + "f1b4f1b2f1g2f1b4",
        "g1f1b6f2g1f1b4" + "g1f1b6f2g1f1b4",
        "f3b6f2b3f2" + "f3b6f2b3f2",
        "g1f2b2f2b7f1b1" + "g1f2b2f2b7f1b1",
        "b1e2g4e1b2e1g3e1b1" + "b1e2g4e1b2e1g3e1b1",
        "e1g3e2g1e1g2e1g1e1g1e1g1" + "e1g3e2g1e1g2e1g1e1g1e1g1",
        "g1e4g1e4g1e1g1e3" + "g1e4g1e4g1e1g1e3",
        "e2g1e5g1e7" + "e2g1e5g1e7",
        "e1b1e1b1e2b1e2b1e3b1g1e1" + "e1b1e1b1e2b1e2b1e3b1g1e1",
        "e2b1e1b2e1b1e2b2e3b1" + "e2b1e1b2e1b1e2b2e3b1",
        "b1e1b3r1b1e2b1r1b3e2" + "b1e1b3r1b1e2b1r1b3e2",
        "e1b2r1b2r1b1r1b3r2b2" + "e1b2r1b2r1b1r1b3r2b2",
    ]    
)

blastermaster_animation = animation_settings(
    sprite_list=[Sophia04, Sophia03, Sophia02, Sophia01],
    bg_sprite=bmbg_1,
    xoff=0,
    yoff=0,
    frame_time=0.03,
    spbg_ratio=2,
    center=True,
    bg_scroll_speed=(-1, 0),
    )
