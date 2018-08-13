import sys
sys.path.append("../")
from settings import (NES_PALETTE_HEX, animation_settings)
from core import sprite

SophiaLeft01 = sprite(
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

SophiaLeft02 = sprite(
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

SophiaLeft03 = sprite(
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

SophiaLeft04 = sprite(
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

JasonWalkLeft01 = sprite(
    palette = { 
        "w":NES_PALETTE_HEX[3, 0],
        "b":NES_PALETTE_HEX[0, 13],
        "r":NES_PALETTE_HEX[1, 5],
    },
    matrix = [
        "x3b4x3",
        "x2b1r4b1x2",
        "x1b1r3w3b1x1",
        "b1r3w5b1",
        "b1r1b2w1b1w3b1",
        "x1b3w1b1w3b1",
        "x1b3w1b1w3b1",
        "x1b3w4b1x1",
        "x1b1w5b1x2",
        "x2b5x3",
        "x2b1r1w2r1b1x2",
        "x1b1r5b1x2",
        "x1b1r2w2r1b1x2",
        "x1b1r2w2r1b1x2",
        "x2b1r3b1x3",
        "x2b1w1b2x4",
        "x3b1x6",
        
    ]    
)

JasonWalkLeft02 = sprite(
    palette = { 
        "w":NES_PALETTE_HEX[3, 0],
        "b":NES_PALETTE_HEX[0, 13],
        "r":NES_PALETTE_HEX[1, 5],
    },
    matrix = [
        "x3b4x3",
        "x2b1r4b1x2",
        "x1b1r3w3b1x1",
        "b1r3w5b1",
        "b1r1b2w1b1w3b1",
        "x1b3w1b1w3b1",
        "x1b3w1b1w3b1",
        "x1b3w4b1x1",
        "x1b1w3b3x2",
        "x1b3w2b3x1",
        "b1w2r5w1b1",
        "b1w2r5w1b1",
        "x1b2r4b2x1",
        "x1b1w1r4b1x2",
        "x2b4w1b1x2",
        "x6b1x3",
    ]    
)

JasonWalkLeft03 = sprite(
    palette = { 
        "w":NES_PALETTE_HEX[3, 0],
        "b":NES_PALETTE_HEX[0, 13],
        "r":NES_PALETTE_HEX[1, 5],
    },
    matrix = [
        "x3b4x3",
        "x2b1r4b1x2",
        "x1b1r3w3b1x1",
        "b1r3w5b1",
        "b1r1b2w1b1w3b1",
        "x1b3w1b1w3b1",
        "x1b3w1b1w3b1",
        "x1b3w4b1x1",
        "x1b1w3b3x2",
        "x1b4w2b2x1",
        "b1w1r5w2b1",
        "b1w1r3w1r1w2b1",
        "x1b2r4b2x1",
        "x1b1w1r4b1x2",
        "x2b4w1b1x2",
        "x6b1x3",
    ]    
)

BlasterMasterBG01 = sprite(
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

BlasterMasterBG02 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "g":NES_PALETTE_HEX[1, 0],
        "y":NES_PALETTE_HEX[2, 8],
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 8],
    },
    matrix = [
        "r1b1g1b1g2b2g1b1r1b2r1g1b1" + "r1b1g1b1g2b1g1b1g1b1g1r1b1g1b1",
        "b6r1b2r1b2g1b3" + "b2g1b1w1g5b1g1r1b3",
        "b1r2b1g1b1r1b5g1b1g2" + "b4g2b1g1b2g2r1b3",
        "b4g1b3g2b2r1b3" + "b1r2b1g8r1b1g2",
        "b1g1b13r1" + "b4r8b4",
        "b1g1b2r2b3r1g2b4" + "b1g1b2r2b3r1g2b4",
        "b6g2b1r1b4g1b1" + "b6g2b1r1b4g1b1",
        "r1b2r2b7r1b1g1b1" + "r1b2r2b7r1b1g1b1",
        
        "b2g2b1r1b4g2b1r1b2" + "b2g2b1r1b4g2b1r1b2",
        "r2b3r1b2r2b3r1b2" + "r2b3r1b2r2b3r1b2",
        "b16" + "b16",
        "g1r1b1g1r1b1r1g2r1b1g1r1b1r1g1" + "g1r1b1g1r1b1r1g2r1b1g1r1b1r1g1",
        "b1r1b1g1r1b1r1b2r1b1g1r1b1r1b1" + "b1r1b1g1r1b1r1b2r1b1g1r1b1r1b1",  
        "b16" + "b16",
        "w16" + "w16",
        "r16" + "r16",
        "b3r1b7r1b4" + "b3r1b7r1b4",
        "r2b1g1r1b3r2b1g1r1b3" + "r2b1g1r1b3r2b1g1r1b3",
        "b3w1r1b1g1r1b3w1r1b1g1r1" + "b3w1r1b1g1r1b3w1r1b1g1r1",
        "r1b2w1r1b3r1b2w1r1b3" + "r1b2w1r1b3r1b2w1r1b3",
        "g1b2w1r1b3g1b2w1r1b3" + "g1b2w1r1b3g1b2w1r1b3",
        "r1b2w1r1b3r1b2w1r1b3" + "r1b2w1r1b3r1b2w1r1b3",
        "b3w1r1b1r1b4w1r1b1r1b1" + "b3w1r1b1r1b4w1r1b1r1b1",
        "b3r2b1r1b4r2b1r1b1" + "b3r2b1r1b4r2b1r1b1",

        "g16" + "g16",
        "y3b4y4b4y1" + "y3b4y4b4y1",
        "y2b4y4b4y2" + "y2b4y4b4y2",
        "y1b4y4b4y3" + "y1b4y4b4y3",
        "b4y4b4y4" + "b4y4b4y4",
        "b3y4b4y4b1" + "b3y4b4y4b1",
        "b2y4b4y4b2" + "b2y4b4y4b2",
        "b1y4b4y4b3" + "b1y4b4y4b3",
    ]    
)

blastermaster_animation = animation_settings(
    sprite_list=[[SophiaLeft04, SophiaLeft03, 
                  SophiaLeft02, SophiaLeft01],
                 [JasonWalkLeft01, JasonWalkLeft01,
                  JasonWalkLeft02, JasonWalkLeft02,
                  JasonWalkLeft01, JasonWalkLeft01,
                  JasonWalkLeft03, JasonWalkLeft03,],
                ],
    bg_sprites=[BlasterMasterBG01,
                BlasterMasterBG02,],
    xoffs=[[0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0,],
          ],
    yoffs=[[0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0,],
          ],
    frame_time=0.03,
    spbg_ratio=2,
    center=True,
    bg_scroll_speed=(-1, 0),
    cycles_per_char=5,
    reversible="horizontal",
    )
