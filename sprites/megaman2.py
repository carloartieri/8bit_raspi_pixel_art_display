import sys
sys.path.append("../")
from settings import (NES_PALETTE_HEX, animation_settings)
from core import sprite

MegaMan02StandRight = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[2, 0],
        "d":NES_PALETTE_HEX[1, 2],
        "l":NES_PALETTE_HEX[3, 1],
        "s":NES_PALETTE_HEX[3, 7],
    },
    matrix = [
        "x11b2x8",
        "x8b3l2b1x7",
        "x7b1d3b1l2b1x6",
        "x6b1d5b4x5",
        "x6b1d5b1l2d1b1x4",
        "x5b1l1d6b2d1b1x4",
        "x5b1l1d2s1w3d2w1b1x4",
        "x5b1l1d1s1w2b2s1b1w1b1x4",
        "x6b1d1s1w2b2s1b1w1b1x4",
        "x5b2d1s1w4s1w1s1b1x4",
        "x3b2l2b1d1s1b4s1b3x3",
        "x2b1d1l4b1s5b1l2d1b1x2",
        "x2b1d2l4b5l2d2b1x2",
        "x1b1d3l1b1l7b1l1d3b1x1",
        "x1b1d2b3l7b3d2b1x1",
        "x1b1d3b2l7b2d3b1x1",
        "x1b1d3b2d7b2d3b1x1",
        "x2b3x1b1d7b1x1b3x2",
        "x5b1l2d4l3b1x5",
        "x4b1d2l3b1l4d1b1x4",
        "x3b2d3l1b1x1b1l1d3b2x3",
        "x1b2d5b1x3b1d5b2x1",
        "b1d7b1x3b1d7b1",
        "b9x3b9",
    ]    
)


MegaMan02RunLeft01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[2, 0],
        "d":NES_PALETTE_HEX[1, 2],
        "l":NES_PALETTE_HEX[3, 1],
        "s":NES_PALETTE_HEX[3, 7],
    },
    matrix = [
        "x9b3x12",
        "x8b1l2b3x10",
        "x7b1l2b1d3b1x9",
        "x6b4d5b1x8",
        "x5b1d1l2b1d5b1x8",
        "x5b1d1b2d6l1b3x5",
        "x5b1w1d2w3s1d2l1b1l2b2x3",
        "x5b1w1b1s1b2w2s1d1l1b1l2b1d1b1x2",
        "x1b3x1b1w1b1s1b2w2s1d1b1l2b1d3b1x1",
        "b1d3b2s1w1s1w3s2d1b1l2b1d4b1",
        "b1d3b1x1b1s1b4s1d1b1l2b1x1b1d3b1",
        "b1d3b2l1b1s5b1l3b1x1b1d3b1",
        "x1b1d3l3b5l3d1b1x2b3x1",
        "x2b1d3l2b1l5d3b1x1b2x3",
        "x3b1d2l1b1x1b1l1d6b2d2b1x2",
        "x4b3x3b1l3d2b2d4b1x1",
        "x9b1l4d1b2l1d5b1",
        "x8b1d1l3b2l3d2b1d2b1",
        "x8b1d4b1x1b1l2d1b4x1",
        "x7b3d3b1x2b3x5",
        "x6b1d7b1x9",
        "x6b9x9"
    ]    
)

MegaMan02RunLeft02 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[2, 0],
        "d":NES_PALETTE_HEX[1, 2],
        "l":NES_PALETTE_HEX[3, 1],
        "s":NES_PALETTE_HEX[3, 7],
    },
    matrix = [
        "x4b3x9",
        "x3b1l2b3x7",
        "x2b1l2b1d3b1x6",
        "x1b4d5b1x5",
        "b1d1l2b1d5b1x5",
        "b1d1b2d6l1b1x4",
        "b1w1d2w3s1d2l1b1x4",
        "b1w1b1s1b2w2s1d1l1b2x3",
        "b1w1b1s1b2w2s1d1b1l2b1x2",
        "b1s1w1s1w3s2d1b1l3b1x1",
        "x1b1s1b4s1d1b1l5b1",
        "x2b1s5b1l2b1l3b1",
        "x2b6l2b1d3b1x1",
        "x1b1d1b1l4b2d4b1x1",
        "x1b1d2b1l2b1d2b1d2b1x2",
        "x2b4d1b1d4b1x3",
        "x4b1l1b1d1b1d2b1x4",
        "x4b1l1b1l2b2x5",
        "x5b2l3b2x4",
        "x6b1d5b1x3",
        "x7b1d5b1x2",
        "x7b3d3b1x2",
        "x6b1d5b1x3",
        "x6b6x4"
    ]    
)


MegaMan02RunLeft03 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[2, 0],
        "d":NES_PALETTE_HEX[1, 2],
        "l":NES_PALETTE_HEX[3, 1],
        "s":NES_PALETTE_HEX[3, 7],
    },
    matrix = [
        "x5b3x13",
        "x4b1l2b3x11",
        "x3b1l2b1d3b1x10",
        "x2b4d5b1x9",
        "x1b1d1l2b1d5b1x9",
        "x1b1d1b2d6l1b1x8",
        "x1b1w1d2w3s1d2l1b1x8",
        "x1b1w1b1s1b2w2s1d1l1b3x6",
        "x1b1w1b1s1b2w2s1d1b1l3b2x4",
        "x1b1s1w1s1w3s2b1l3d3b1x3",
        "x2b1s1b4s1l2b1l2d4b1x2",
        "x1b3s3d1l4b3d3b1x2",
        "b1d3b3l5b1x1b1d3b1x2",
        "b1d6l2d1b1l1d1b1x1b3x3",
        "b1d6l1d1b1l1d2b3d2b1x2",
        "x1b8d4l1b1d4b1x1",
        "x4b1l3d4l3d5b1",
        "x3b1d2l3b3l3d2b1d2b1",
        "x3b1d4b1x3b1l1d2b4x1",
        "x2b3d3b1x4b3x5",
        "x1b1d7b1x11",
        "x1b9x11"
    ]    
)

megaman2bg_1 = sprite(
    palette = { 
        "r":NES_PALETTE_HEX[1, 7],
        "b":NES_PALETTE_HEX[0, 14],
        "l":NES_PALETTE_HEX[2, 7],
        "d":NES_PALETTE_HEX[0, 7],
        "e":NES_PALETTE_HEX[0, 8],
    },
    matrix = [
        "b16" + "b16",
        "e3b10e2b1" + "e3b10e2b1",
        "e7b4e3b1e1" + "e7b4e3b1e1",
        "e9b1e4b1e1" + "e9b1e4b1e1",
        "e7b2e4b1e2" + "e7b2e4b1e2",
        "e4b3e4b2e3" + "e4b3e4b2e3",
        "e1b3e4b3e5" + "e1b3e4b3e5",
        "b1e4b3e7b1" + "b1e4b3e7b1",
        "e2b3e9b1e1" + "e2b3e9b1e1",
        "e1b1e11b1e2" + "e1b1e11b1e2",
        "b1e11b1e3" + "b1e11b1e3",
        
        "b1e9b2e4" + "b1e9b2e4",
        "e8b2e5b1" + "e8b2e5b1",
        "e6b2e7b1" + "e6b2e7b1",
        "e5b1e8b1e1" + "e5b1e8b1e1",
        "e4b1e8b1e2" + "e4b1e8b1e2",
        "e3b1e9b1e2" + "e3b1e9b1e2",
        "b3e8b2e3" + "b3e8b2e3",
        "e10b1e4b1" + "e10b1e4b1",
        "e9b1e4b1e1" + "e9b1e4b1e1",
        "e7b2e4b1e2" + "e7b2e4b1e2",
        "e4b3e4b2e3" + "e4b3e4b2e3",
        "e1b3e4b3e5" + "e1b3e4b3e5",
        "b1e4b3e7b1" + "b1e4b3e7b1",
        "e2b3e9b1e1" + "e2b3e9b1e1",
        "e1b1e11b1e2" + "e1b1e11b1e2",
        "b1e11b1e3" + "b1e11b1e3",
        "r5b1r3b1l3b1r2" + "r5b1r3b1l3b1r2",
        "r5d1r3b1l3b1l2" + "r5d1r3b1l3b1l2",
        "r5d1r3b1l3b1r1l1" + "r5d1r3b1l3b1r1l1",
        "r5b1r3b1l3b1r2" + "r5b1r3b1l3b1r2",
        "d5b1d3b1l3b1d2" + "d5b1d3b1l3b1d2",
    ]    
)

megaman2_animation = animation_settings(
    sprite_list=[MegaMan02RunLeft01.hflip(),
                 MegaMan02RunLeft02.hflip(),
                 MegaMan02RunLeft03.hflip(),
                 MegaMan02RunLeft02.hflip()],
    bg_sprite=megaman2bg_1,
    xoff=(0, 1, 3, 1),
    yoff=0,
    frame_time=0.035,
    spbg_ratio=3,
    center=True,
    bg_scroll_speed=(1, 0)
    )
