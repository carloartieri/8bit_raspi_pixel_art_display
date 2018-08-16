import sys
sys.path.append("../")
from settings import (NES_PALETTE_HEX, animation_settings)
from core import sprite

VicViper01 = sprite(
    palette = { 
        "w":NES_PALETTE_HEX[3, 0],
        "b":NES_PALETTE_HEX[0, 2],
        "l":NES_PALETTE_HEX[3, 1],
        "r":NES_PALETTE_HEX[1, 6],
        "o":NES_PALETTE_HEX[2, 8],
    },
    matrix = [
        "x2l2x19",
        "x3l3x17",
        "x4l3x8r2w1r1x4",
        "x5l6b3l1w1r3o1x3",
        "x1r2x2w16l2",
        "r2w1r1x3b7l4b4x1",
        "x1r2x1w3l2w4b1l1x8",
        "r2w1r1x1w5b1x12",
        "x1r2x3w1b3x1l1w1x10",
    ]    
)

VicViper02 = sprite(
    palette = { 
        "w":NES_PALETTE_HEX[3, 0],
        "b":NES_PALETTE_HEX[0, 2],
        "l":NES_PALETTE_HEX[3, 1],
        "r":NES_PALETTE_HEX[1, 6],
        "o":NES_PALETTE_HEX[2, 8],
    },
    matrix = [
        "x3l2x19",
        "x4l3x17",
        "x5l3x8r2w1r1x4",
        "x6l6b3l1w1r3o1x3",
        "x2r2x2w16l2",
        "r2o1w1r1x3b7l4b4x1",
        "x2r2x1w3l2w4b1l1x8",
        "r2o1w1r1x1w5b1x12",
        "x2r2x3w1b3x1l1w1x10",
    ]    
)

LordBritish01 = sprite(
    palette = { 
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 2],
        "o":NES_PALETTE_HEX[3, 1],
        "b":NES_PALETTE_HEX[1, 6],
        "l":NES_PALETTE_HEX[2, 8],
    },
    matrix = [
        "x2l2x19",
        "x3l3x17",
        "x4l3x8r2w1r1x4",
        "x5l6b3l1w1r3o1x3",
        "x1r2x2w16l2",
        "r2w1r1x3b7l4b4x1",
        "x1r2x1w3l2w4b1l1x8",
        "r2w1r1x1w5b1x12",
        "x1r2x3w1b3x1l1w1x10",
    ]    
)

LordBritish02 = sprite(
    palette = { 
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 2],
        "o":NES_PALETTE_HEX[3, 1],
        "b":NES_PALETTE_HEX[1, 6],
        "l":NES_PALETTE_HEX[2, 8],
    },
    matrix = [
        "x3l2x19",
        "x4l3x17",
        "x5l3x8r2w1r1x4",
        "x6l6b3l1w1r3o1x3",
        "x2r2x2w16l2",
        "r2o1w1r1x3b7l4b4x1",
        "x2r2x1w3l2w4b1l1x8",
        "r2o1w1r1x1w5b1x12",
        "x2r2x3w1b3x1l1w1x10",
    ]    
)

LifeForceBG01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "l":NES_PALETTE_HEX[0, 1],
        "d":NES_PALETTE_HEX[0, 12],
        "r":NES_PALETTE_HEX[0, 7],
        "p":NES_PALETTE_HEX[1, 5],
        "i":NES_PALETTE_HEX[3, 13],
    },
    matrix = [
        "b1l1d2b4d2l1b4l1" + "d2b6l1d1b6",
        "l1d2b6d2l1b2l1d1" + "d1b7l1d1b6",
        "d2b8d6" + "b8d2b4l1d1",
        "d1b10d4b1" + "b8l1d1b3l1d2",
        "b12l1d3" + "l1b7l1d1b2l1d3",
        "d1b11d2b1d1" + "d1l1b6l1d1b1l1d1b2d1",
        "d1b10l1d1b3" + "b1d2l1b4l1d1l1d1b4",
        
        "d2b8l1d1b4" + "b3d2l1b2d3b5",
        "b1d1b8d1b5" + "b5d5b6",
        "b1d2b6l1d1b5" + "b7l1d2b6",
        "b2d2b4l1d1b6" + "b7l1d1b7",
        "b2d3b2l1d2b6" + "b6l1d1b8",
        "b3d7b6" + "b5l1d2b8",
        "b3l1d2b2d2b6" + "b4l1d3b8",
        "b2l1d2b3l1d1b6" + "b3l1d4l1b7",
        
        "b1l1d1b5l1d1b6" + "b2l1d2b2d2l1b6",
        "d2b6l1d1b6" + "b1l1d2b4d2l1b4l1",
        "d1b7l1d1b6" + "l1d2b6d2l1b2l1d1",
        "b8d2b4l1d1" + "d2b8d6",
        "b8l1d1b3l1d2" + "d1b10d4b1",
        "l1b7l1d1b2l1d3" + "b12l1d3",
        "d1l1b6l1d1b1l1d1b2d1" + "d1b11d2b1d1",
        "b1d2l1b4l1d1l1d1b4" + "d1b10l1d1b3",
        "b3d2l1b2d3b5" + "d2b8l1d1b4",
        "b5d5b6" + "b1d1b8d1b5",
        
        "b2r6b2r1b2r3" + "b2r6b2r1b2r3",
        "b1r7b1r4b3" + "b1r7b1r4b3",
        "r1p4r2b1r1p4r2b1" + "r1p4r2b1r1p4r2b1",
        "p1i2p3r1b1p1i2p3r1b1" + "p1i2p3r1b1p1i2p3r1b1",
        "i1p5r1b1i1p5r1b1" + "i1p5r1b1i1p5r1b1",
        "p5r2b1p5r2b1" + "p5r2b1p5r2b1",
        "p4r1p1r2p4r1p1r2" + "p4r1p1r2p4r1p1r2",
    ]    
)

LifeForceBG02 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "l":NES_PALETTE_HEX[0, 1],
        "d":NES_PALETTE_HEX[0, 12],
        "p":NES_PALETTE_HEX[1, 3],
        "i":NES_PALETTE_HEX[3, 1],
    },
    matrix = [
        "b3p1b3p1b3p1b3p1" + "b3p1b3p1b3p1b3p1",
        "p2b1p2b1p1b1p2b1p2b1p1b1" + "p2b1p2b1p1b1p2b1p2b1p1b1",
        "b4p1b7p1b3" + "b4p1b7p1b3",
        "b3p1b1p1b1p1b3p1b1p1b1p1" + "b3p1b1p1b1p1b3p1b1p1b1p1",
        "p1b1p1b3p1b1p1b1p1b3p1b1" + "p1b1p1b3p1b1p1b1p1b3p1b1",
        "b32",
        "b2p1b2p1b4p1b2p1b2" + "b2p1b2p1b4p1b2p1b2",
        "b4p1b7p1b3" + "b4p1b7p1b3",
        "b32",
        "b3p1b7p1b4" + "b3p1b7p1b4",
        "b5p1b7p1b2" + "b5p1b7p1b2",

        "b32",
        "b32",
        "b32",
        "b32",
        "b32",
        "b32",
        "b32",
        "b32",
        "b5l1b7l1b2" + "b5l1b7l1b2",
        
        "b3l1b7l1b4" + "b1l1b1l1b5l1b1l1b4",
        "b16" + "b2l1b1l1b1l1b3l1b1l1b1l1b1",
        "b4l1b7l1b3" + "b1l1d4l2b1l1d4l2",
        "b2l1b2l1b4l1b2l1b2" + "l1d1l4d1l2d1l4d1l1",
        "b16" + "d1l1i4l1d2l1i4l1d1",
        "l1b1l1b3l1b1l1b1l1b3l1b1" + "l1i6l2i6l1",
        "b3l1b1l1b1l1b3l1b1l1b1l1" + "l1i2l2i2l2i2l2i2l1",
        "b2l4b4l4b2" + "l1i1l1i2l1i1l2i1l1i2l1i1l1",
        "b1l1i4l1b2l1i4l1b1" + "l1i6l2i6l1",
        "l1i6l2i6l1" + "b1l1i4l1d1b1l1i4l1d1",
        "l1i1l1i2l1i1l2i1l1i2l1i1l1" + "b2l4d2b2l4d2",
        "l1i2l2i2l2i2l2i2l1" + "b4l1d3b4l1d3",
    ]    
)

lifeforce_animation = animation_settings(
    sprite_list=[[VicViper01,
                  VicViper02],
                 [LordBritish01,
                  LordBritish02],
                ],
    bg_sprites=[LifeForceBG01,
                LifeForceBG02],
    xoffs=[[0, 0],
           [0, 0],
          ],
    yoffs=[[-1, -1],
           [-1, -1],
          ],
    frame_time=0.03,
    spbg_ratio=3,
    center=True,
    bg_scroll_speed=(1, 0),
    cycles_per_char=5,
    reversible=False,
    )
