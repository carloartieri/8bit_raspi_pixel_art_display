import sys
sys.path.append("../")
from settings import (NES_PALETTE_HEX, animation_settings)
from core import sprite

LinkLeft01 = sprite(
    palette = { 
        "g":NES_PALETTE_HEX[1, 9],
        "b":NES_PALETTE_HEX[1, 8],
        "s":NES_PALETTE_HEX[3, 8],
    },
    matrix = [
        "x7b6x3",
        "x4b3g3b1g2b1x2",
        "x3b5g1b1s1b1g2b1x1",
        "x3b7s1b1g1b1g1b1",
        "b3x1b1s2b2s2b1g1b3",
        "b1g1b3s1b1s1b1s2b3x2",
        "b1g1b1s3b1s1b1s2b2x3",
        "b1g1b2s6b4x2",
        "b1g1b1x1b2s4b2x4",
        "b1g1b1x1b1s4b4x3",
        "b1g1b1x2b3s1b4x3",
        "b1g1b1x2b1g1b2g3b2x2",
        "b4x1b1g1b1g3b3x2",
        "b1s3b2g4b5x1",
        "b1s4b1g5b4x1",
        "b2s4b1g2b2g1b4",
        "b1g1b1s4b8x1",
        "x1b1x1b2s3b1s3b2x2",
        "x5b2s1b1s4b1x2",
        "x5b1g1b2s4b1x2",
        "x4b1g3b2s2b1x3",
        "x4b10x2",
        "x4b1s2b2s3b1x3",
        "x3b1s4b1s3b1x3",
        "x2b1s4b2s3b1x3",
        "x2b3s1b1x2b1s1b2x3",
        "x2b4x3b3g1b1x2",
        "x1b3g1b1x3b5x2",
        "x1b5x4b3g1b1x1",
        "x1b3g1b1x5b4x1",
        "b6x4b5x1",
        "b6x3b4x3"
        
    ]    
)

LinkLeft02 = sprite(
    palette = { 
        "g":NES_PALETTE_HEX[1, 9],
        "b":NES_PALETTE_HEX[1, 8],
        "s":NES_PALETTE_HEX[3, 8],
    },
    matrix = [
        "x7b6x3",
        "x4b3g3b1g2b1x2",
        "x3b5g1b1s1b1g2b1x1",
        "x3b7s1b1g1b1g1b1",
        "b3x1b1s2b2s2b1g1b3",
        "b1g1b3s1b1s1b1s2b3x2",
        "b1g1b1s3b1s1b1s2b2x3",
        "b1g1b2s6b4x2",
        "b1g1b1x1b2s4b2x4",
        "b1g1b1x1b1s4b4x3",
        "b1g1b1x2b3s1b4x3",
        "b1g1b1x2b1g1b2g3b2x2",
        "b4x1b1g1b1g3b3x2",
        "b1s3b2g4b5x1",
        "b1s4b1g5b4x1",
        "b2s4b1g2b2g1b4",
        "b1g1b1s4b8x1",
        "x1b1x1b2s3b1s3b2x2",
        "x5b2s1b1s4b1x2",
        "x4b2g1b2s4b1x2",
        "x5b5s2b1x3",
        "x4b1s1b1s2b4x3",
        "x4b1s1b1s3b1x5",
        "x4b1s1b1s3b1x5",
        "x4b1s1b1s2b1x6",
        "x5b5x6",
        "x6b3g1b1x5",
        "x5b6x5",
        "x5b5g1b1x4",
        "x7b5x4",
        "x6b6x4",
        "x6b5x5",
    ]    
)

LinkLeft03 = sprite(
    palette = { 
        "g":NES_PALETTE_HEX[1, 9],
        "b":NES_PALETTE_HEX[1, 8],
        "s":NES_PALETTE_HEX[3, 8],
    },
    matrix = [
        "x7b6x3",
        "x4b3g3b1g2b1x2",
        "x3b5g1b1s1b1g2b1x1",
        "x3b7s1b1g1b1g1b1",
        "b3x1b1s2b2s2b1g1b3",
        "b1g1b3s1b1s1b1s2b3x2",
        "b1g1b1s3b1s1b1s2b2x3",
        "b1g1b2s6b4x2",
        "b1g1b1x1b2s4b2x4",
        "b1g1b1x1b1s4b4x3",
        "b1g1b1x2b3s1b4x3",
        "b1g1b1x2b1g1b2g3b2x2",
        "b4x1b1g1b1g3b3x2",
        "b1s3b2g4b5x1",
        "b1s4b1g5b4x1",
        "b2s4b1g2b2g1b4",
        "b1g1b1s4b8x1",
        "x1b1x1b2s3b1s3b2x2",
        "x5b2s1b1s4b1x2",
        "x4b2g1b2s4b1x2",
        "x4b1s1b4s2b1x3",
        "x3b1s4b6x2",
        "x2b1s4b2s3b1x3",
        "x2b3s1b1x1b1s3b1x3",
        "x2b4x2b1s3b1x3",
        "x2b2g1b1x3b1s1b2x3",
        "x2b4x3b3g1b1x2",
        "b4g1b1x3b5x2",
        "b6x4b3g1b1x1",
        "x3b3x5b4x1",
        "x10b5x1",
        "x9b4x3",
    ]    
)

LinkLeft04 = sprite(
    palette = { 
        "g":NES_PALETTE_HEX[1, 9],
        "b":NES_PALETTE_HEX[1, 8],
        "s":NES_PALETTE_HEX[3, 8],
    },
    matrix = [
        "x6b6x4",
        "x3b3g3b1g2b1x3",
        "x2b5g1b1s1b1g2b1x2",
        "x2b7s1b1g1b1g1b1x1",
        "b4s2b2s2b1g1b3x1",
        "b1g1b2s1b1s1b1s2b3x3",
        "b2s3b1s1b1s2b2x4",
        "b1g1b1s6b4x3",
        "b1g1b3s4b2x5",
        "b1g1b2s4b4x4",
        "b1g1b1x1b3s1b1g3b1x3",
        "b1g1b1x1b1g1b2g3b2x3",
        "b5g1b1g3b3x3",
        "b1s3b1g4b5x2",
        "b1s4b1g4b4x2",
        "b2s4b1g1b1g2b4x1",
        "b1g1b1s4b8x1",
        "x1b1x2b1s2b1s3b3x2",
        "x5b3s4b1x3",
        "x4b1g1b2s4b2x2",
        "x4b3g1b1s2b1g1b1x2",
        "x4b1s1b7x3",
        "x3b1s3b2s3b1x3",
        "x3b1s3b1x1b1s3b1x2",
        "x3b1s2b1x2b1s2b3x1",
        "x3b4x3b3g1b2",
        "x3b2g1b1x4b3g1b1",
        "x3b4x5b4",
        "x3b2g1b1x6b3",
        "x2b5x5b3x1",
        "x1b6x5b2x2",
    ]    
)

zelda2bg_1 = sprite(
    palette = { 
        "r":NES_PALETTE_HEX[0, 6],
        "b":NES_PALETTE_HEX[0, 13],
        "l":NES_PALETTE_HEX[2, 6],
    },
    matrix = [
        "r15b1" + "b1l14b1",
        "r14b2" + "l2r12b2",
        "r2b14" + "l1r2b2r6b2r2b1",
        "r2b14" + "l1r1b1l1r1b1r4b1l1r1b1r1b1", 
        "r2b14" + "b1r4b2r2b2r4b1",
        "r2b14" + "b2r2b1r1b1r2b1r1b1r2b2",
        "r1b15" + "b4r1b6r1b4",
        "b16" + "b3l1r1b2r2b2r1b4",
        "r7b1r8" + "b16",
        "r6b2r8" + "b1l2r1l1r1l1r2b1r2b4",
        "b8r2b6" + "b1l1r1l1r2l1r2b2r1b4",
        "b8r2b6" + "b1l1r1l1r2l1r2b2r2b3",
        "b8r2b6" + "l2r1l1r2l1r2b2r2b3",
        "b8r2b6" + "l2r1l1r2l1r2b2r2b3",
        "b8r1b7" + "l2r1l1r2l1r2b2r2b3",
        "b16" + "b16",
        "r15b1" + "l1r1l1r2l1b1r1l1b2r2b3",
        "r14b2" + "l1r1l1r2l1b1r1l1b2r2b3",
        "r2b14" + "l1r1l1r2l1b1r1l1b2r2b3",
        "r2b14" + "l1r1l1r2l1b1r1l1b2r2b3", 
        "r2b14" + "l1r1l1r2l1b1r1l1b2r2b3",
        "r2b14" + "l1r1l1r2l1b1r1l1b2r2b3",
        "r1b15" + "l1r1l1r2l1b1r1l1b2r2b3",
        "b16" +  "b16",
        "r7b1r8" + "l1r1l1r2l1b1r1l1b2r2b3",
        "r6b2r8" + "l1r1l1r2l1b1r1l1b2r2b3",
        "b8r2b6" + "l1r1l1r2l1b1r1l1b2r2b3",
        "b8r2b6" + "l1r1l1r2l1b1r1l1b2r2b3",
        "b8r2b6" + "l1r1l1r2l1b1r1l1b2r2b3",
        "b8r2b6" + "l1r1l1r2l1b1r1l1b2r2b3",
        "b8r1b7" + "l1r1l1r2l1b1r1l1b2r2b3",
        "b16" + "b16",
    ]    
)

zelda2_animation = animation_settings(
    sprite_list=[LinkLeft03, LinkLeft04, LinkLeft02],
    bg_sprite=zelda2bg_1,
    xoff=0,
    yoff=(0, 1, 0),
    frame_time=0.04,
    spbg_ratio=2,
    center=True,
    bg_scroll_speed=(-1, 0)
    )
