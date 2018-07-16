import sys
sys.path.append("../")
from settings import (NES_PALETTE_HEX, animation_settings)
from core import sprite

DWHeroPrincess01 = sprite(
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

DWHeroPrincess02 = sprite(
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

dwbg_1 = sprite(
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

dragonwarrior_animation = animation_settings(
    sprite_list=[DWHeroPrincess01, DWHeroPrincess02],
    bg_sprite=dwbg_1,
    xoff=0,
    yoff=0,
    frame_time=0.05,
    spbg_ratio=5,
    center=True,
    bg_scroll_speed=(0, -1),
    )

