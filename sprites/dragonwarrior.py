import sys
sys.path.append("../")
from settings import (NES_PALETTE_HEX, animation_settings)
from core import sprite

DWHeroPrincessSouth01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 1],
        "r":NES_PALETTE_HEX[0, 7],
        "w":NES_PALETTE_HEX[3, 0],
        "s":NES_PALETTE_HEX[3, 13],
        
    },
    matrix = [
        "x2r2w1r1w1x1b4x3w1",
        "x1r1w1r2w2r1b5w3",
        "r3w2r3w4b1w2x1",
        "r2w1r5b6x2",
        "r6s1r1b1s2b1s1b1x2",
        "r4s1r1s1r1b1s2b1s2b2",
        "r3s2r1s1r1s5b3",
        "r4s3r1b1s2b4s1",
        "r3w3r1w2r2w3r1s1",
        "x1r2w2s4r1w1r2w2r1",
        "x2s1r1w5r1w3r2w1",
        "x3s1r1w3r1s2r1w3r1",
        "x4w3r4w1r1w3",
        "x5s4w3r1w2x1",
        "x5s4w2r1w2x2",
        "x5r4x7",
        
    ]    
)

DWHeroPrincessSouth02 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 1],
        "r":NES_PALETTE_HEX[0, 7],
        "w":NES_PALETTE_HEX[3, 0],
        "s":NES_PALETTE_HEX[3, 13],
        
    },
    matrix = [
        "x2r2w1r1w1x1b4x3w1",
        "x1r1w1r2w2r1b5w3",
        "r3w2r3w4b1w2x1",
        "r2w1r5b6x2",
        "r6s1r1b1s2b1s1b1x2",
        "r4s1r1s1r1b1s2b1s2b2",
        "r3s2r1s1r1s5b3",
        "r4s3r1b1s2b4s1",
        "r3w3r1w2r2w3r1s1",
        "x1r2w2s4r1w1r1w3r1",
        "x2s1r1w5r1w2r2w2",
        "x3s1r1w3r1s2w3r1w1",
        "x4w3r5w2r1w1",
        "x5s3x1w2r1w3x1",
        "x5r3x1w1r1w3x2",
        "x10r4x2",
        
    ]    
)

DWKingSouth01 = sprite(
    palette = { 
        "r":NES_PALETTE_HEX[0, 7],
        "w":NES_PALETTE_HEX[3, 0],
        "s":NES_PALETTE_HEX[3, 13],
        
    },
    matrix = [
        "x1w1x1w1x1w2x2w2x1w1x3",
        "w1r1w1r1w1r2w2r2w1r1x3",
        "x1w1x1w10x3",
        "x1s1x1w2r6w2x3",
        "x1w1x1r2s1r1s2r1s1r2x3",
        "x1w1x1w1s2r1s2r1s2w1x3",
        "x1w1x1w2s1w4s1w2x3",
        "x1w1r1w4r2w4r2x1",
        "s2r2w8r4",
        "s2r3w2r2w2r5",
        "r1w1r5w2r5w2",
        "x1s1r4w1r2w1r4s2",
        "x1w1r5w2r5s2",
        "w1r1w1r4w2r5x2",
        "x1w1r5w6r2x1",
        "x1w7x1r4w2x1",        
    ]    
)

DWKingSouth02 = sprite(
    palette = { 
        "r":NES_PALETTE_HEX[0, 7],
        "w":NES_PALETTE_HEX[3, 0],
        "s":NES_PALETTE_HEX[3, 13],
        
    },
    matrix = [
        "x3w1x1w2x2w2x1w1x3",
        "x1w1x1r1w1r2w2r2w1r1x3",
        "w1r1w11x3",
        "x1w1x1w2r6w2x3",
        "x1s1x1r2s1r1s2r1s1r2x3",
        "x1w1x1w1s2r1s2r1s2w1x3",
        "x1w1x1w2s1w4s1w2x3",
        "x1w1r1w4r2w4r2x1",
        "r1w1r2w8r2s2",
        "s2r3w2r2w2r3s2",
        "s2r5w2r7",
        "x1w1r4w1r2w1r5x1",
        "x1s1r5w2r5x2",
        "x1w1r5w2r5x2",
        "w1r2w6r6x1",
        "x1w2r4x1w7x1",
    ]    
)

DWDragonLordSouth01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 1],
        "w":NES_PALETTE_HEX[3, 0],
        "s":NES_PALETTE_HEX[3, 13],
        
    },
    matrix = [
        "x1w2b3x5b3x2",
        "w1s1x1b4x3b4x2",
        "w3x1b9x3",
        "w1x3b2s1b3s1b2x3",
        "w1x2w2b1s2b1s2b1w2x2",
        "w1x1w1b2s1b1w1s1w1b1s1b2w1x1",
        "w4b1s1b2s1b2s1b1w2x1",
        "x1w4b1s5b1w3x1",
        "s2b1w2b1s1b3s1b1w2b1x1",
        "s2b3w1b1s3b1w1b4",
        "x1w1x1b3w1b3w1b5",
        "x1w1x1b4w1s1w1b4s2",
        "x1w1x1b4w1s1w1b4s2",
        "x1w1x1b11x2",
        "x1w1b13x1",
        "x1b8s4b3",        
    ]    
)

DWDragonLordSouth02 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 1],
        "w":NES_PALETTE_HEX[3, 0],
        "s":NES_PALETTE_HEX[3, 13],
        
    },
    matrix = [
        "x3b3x5b3x2",
        "x1w2b4x3b4x2",
        "w1s1x2b9x3",
        "w3x1b2s1b3s1b2x3",
        "w1x2w2b1s2b1s2b1w2x2",
        "w1x1w1b2s1b1w1s1w1b1s1b2w1x1",
        "w1x1w2b1s1b2s1b2s1b1w2x1",
        "w5b1s5b1w3x1",
        "x1w1b1w2b1s5b1w2b1x1",
        "s2b3w1b1s3b1w1s2b2",
        "s2b4w1b3w1b1s2b2",
        "x1w1x1b4w1s1w1b5x1",
        "x1w1x1b4w1s1w1b4x2",
        "x1w1x1b11x2",
        "x1w1b13x1",
        "x1w1b1s4b9",
    ]    
)

DragonWarriorBG01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "e":NES_PALETTE_HEX[2, 9],
        "r":NES_PALETTE_HEX[3, 6],
        "d":NES_PALETTE_HEX[2, 7],
        "f":NES_PALETTE_HEX[1, 10],
        "w":NES_PALETTE_HEX[3, 0],
        "g":NES_PALETTE_HEX[1, 0],
        "u":NES_PALETTE_HEX[1, 1],
        "a":NES_PALETTE_HEX[0, 0],
    },
    matrix = [
        "e3b1f1e3" + "e5f1e7f1e2"  + "e5b1a1e1",
        "b2b1f3e2" + "e2f1e7f1e5" + "e2a1e1b2g1b1",
        "e1b1f2e1f2e1" + "e16"  + "e4b1a1g1b1",
        "e1b1f5e1" + "e6f1e7f1e1"  + "e4b1a1g1b1",
        "b1f2b1f4" + "e1f1e7f1e6" + "e1a1e1b2a1g1a1",
        "f1b1f3e1f2" + "e16" + "e3b2a1g2",
        "b1f7" + "e3f1e7f1e4" + "e3b1a2g1a1", 
        "f1b1f4e1f1" + "e16" + "e2b2a1g1a1g1",
        "b1f1b1f5" + "e5f1e7f1e2" + "e2b2a1g3",
        "f1b1f4d1f1" + "e2f1e7f1e5" + "e2b2a1g2a1",
        "b1f1b1f4b1" + "e16" + "e1b2a2g1b1a1",
        "e1b1d2f1d1b1e1" + "e6f1e7f1e1" + "e1b2a2g1b1a1",
        "e2b1d2e3" + "e6f1e7f1e1" + "b3a2b2g1",
        "b3d2b1e2" + "e16" + "b2a3b1g2",
        "b2d1b1d2b1e1" + "e3f1e7f1e4" + "e1b2a1b2a1g1",
        "e1b5e2" + "e16" + "e2b5a1",      
        "e5b1e2" + "e5f1e7f1e2"  + "e5b1a1e1", 
        "e2b1e5" + "e2f1e7f1e5" + "e2a1e1b2g1b1",
        "e8" + "e16"  + "e4b1a1g1b1",
        "b2e4b1e1" + "e6f1e7f1e1"  + "e4b1a1g1b1",
        "e2b1e5" + "e1f1e7f1e6" + "e1a1e1b2a1g1a1",
        "e1r1e1b1e4" + "e16" + "e3b2a1g2",
        "e2r1e1b1e3" + "e3f1e7f1e4" + "e3b1a2g1a1",
        "e2r2e1b1e2" + "e16" + "e2b2a1g1a1g1",
        "e4r1e1b1e1" + "e5f1e7f1e2" + "e2b2a1g3",
        "r1b1e1r3e1b1" + "e2f1e7f1e5" + "e2b2a1g2a1",
        "r2b1e1r3e1" + "e16" + "e1b2a2g1b1a1",
        "b1r1b2e1b1r2" + "e6f1e7f1e1"  + "e1b2a2g1b1a1",
        "r3b2r2b1" + "e1f1e7f1e6" + "b3a2b2g1",
        "b1r1b1r1b3e1" + "e16" + "b2a3b1g2",
        "b4e4" + "e3f1e7f1e4" + "e1b2a1b2a1g1",
        "e8" + "e16" + "e2b5a1",       
    ]    
)

DragonWarriorBG02 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "g":NES_PALETTE_HEX[1, 0],
        "d":NES_PALETTE_HEX[0, 0],

        "l":NES_PALETTE_HEX[1, 1],
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 6],
        
    },
    matrix = [
        "b4l4" + "r4b1d1r6b1d1r2" + "b6g2",
        "b1l1b1l1b2l2" + "r4b1d1r6b1d1r2" + "b3g3b2",
        "b1l1b1l1b1l1b1l1" + "d4b1d7b1d3" + "b2g1b3d2",
        "b5l1b2" + "b16" + "b1g1b1d5",
        "g4b4" + "b1d1r6b1d1r6" + "b1g1b1d4r1",
        "g6b2" + "b1d1r6b1d1r6" + "b1g1b1d3r2",
        "g7b1" + "b1d7b1d7" + "b1g1b1d1r4",
        "g8" + "b16" + "b1g1b1r4g1",

        "b4g4" + "r4b1d1r6b1d1r2" + "b1g1b1r3g2",
        "w4b2g2" + "r4b1d1r6b1d1r2" + "b3r2g3",
        "b1w1b1w3b1g1" + "d4b1d7b1d3" + "b1g2b1g3b1",
        "b1w1b1w1b1w2b1" + "b16" + "b2g1d1g2b1d1",
        "w4b1w1b1w1" + "b1d1r6b1d1r6" + "b2r1g1d1b1d2",
        "b4w2b1w1" + "b1d1r6b1d1r6" + "b1r3g2d2",
        "l4b2w2" + "b1d7b1d7" + "r3b2g1b2",
        "l6b1w1" + "b16" + "r2b4g2",
        
        "l8" + "r4b1d1r6b1d1r2" + "b2d1g2d1g2",        
        "l2w2l4" + "r4b1d1r6b1d1r2" + "b1d2g3d1g1",
        "l1w1l1w2l3" + "d4b1d7b1d3" + "d1b1g6",
        "l6w1l1" + "b16" + "d1b1g6",
        "l8" + "b1d1r6b1d1r6" + "b1d1g2d1g3",
        "l4w1l3" + "b1d1r6b1d1r6" + "d1b1g1b1g4",
        "l3w1l1w1l2" + "b1d7b1d7" + "d1b1d1g1d2b2",        
        "l8" + "b16" + "b1d1b1g3d2",
        
        "l8" + "r4b1d1r6b1d1r2" + "b1d1g6",
        "l8" + "r4b1d1r6b1d1r2" + "d1b1g6",
        "l8" + "d4b1d7b1d3" + "d1b1d1g5",
        "l2w3l3" + "b16" + "b1d1g1d1g4",
        "l1w2l1w2l2" + "b1d1r6b1d1r6" + "d1b1g4d1g1",
        "l7w1" + "b1d1r6b1d1r6" + "d2b1g1d1b1g2",
        "l8" + "b1d7b1d7" + "b1d3b1d2b1",
        "l8" + "b16" + "b2d1b1d1b2d1",
    ]    
)

dragonwarrior_animation = animation_settings(
    sprite_list=[[DWHeroPrincessSouth01, 
                  DWHeroPrincessSouth02],
                 [DWKingSouth01,
                  DWKingSouth02],
                 [DWDragonLordSouth01,
                  DWDragonLordSouth02],
                ],
    bg_sprites=[DragonWarriorBG01,
                DragonWarriorBG02],
    xoffs=[[0, 0],
           [0, 0],
           [0, 0],
          ],
    yoffs=[[0, 0],
           [0, 0],
           [0, 0],
          ],
    frame_time=0.05,
    spbg_ratio=5,
    center=True,
    bg_scroll_speed=(0, -1),
    cycles_per_char=10,
    reversible=False,
    )

