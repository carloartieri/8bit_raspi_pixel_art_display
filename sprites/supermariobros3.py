import sys
sys.path.append("../")
from settings import (NES_PALETTE_HEX, animation_settings)
from core import sprite

TanookiMarioWalkRight01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "s":NES_PALETTE_HEX[3, 6],
        "r":NES_PALETTE_HEX[1, 7],
    },
    matrix = [
        "x9b2x3b2x5",
        "x9b1s1b6x4",
        "x9b1s2b1r4b1x3",
        "x8b1r1s2r5b1x3",
        "x7b1r2s1r7b1x2",
        "x7b1r10b1x2",
        "x6b1r11b1x2",
        "x6b1r6b4r1b1x2",
        "x6b1r5b1s2b1s1b1x3",
        "x6b1r5s3b1s1b3x1",
        "x6b1r5s8b1",
        "x7b1r4s2b1s5b1",
        "x7b1r4s1b3s3b2",
        "x8b2r2s3b5x1",
        "x8b4r1s4b1x3",
        "x8b1r2b6x4",
        "x7b1r5b1s3b1x3",
        "x7b1r4b1s5b1x2",
        "x7b1r4b1s5b1x2",
        "x5b4r4b1s3b1s1b1x1",
        "x3b2s2r1b2r3b4s2b1x1",
        "x2b2r1s3b1r1b3r2s4b1x1",
        "x1b2s1r2s1b1r8s3b1x1",
        "b2s3r1b2r10b1x2",
        "b1r2s2b1x2b1r9b1x2",
        "b1r3b1x4b1r6b2x3",
        "b2r2b1x4b1r5b1x5",
        "x1b3x5b1s6b1x4",
        "x9b8x4"   
    ]   
)


TanookiMarioWalkRight02 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "s":NES_PALETTE_HEX[3, 6],
        "r":NES_PALETTE_HEX[1, 7],
    },
    matrix = [
        "x10b1x5b1x5",
        "x9b1s1b5s1b1x4",
        "x9b1s2r5b1x4",
        "x8b1s3r6b1x3",
        "x8b1s2r7b1x3",
        "x8b1r10b1x2",
        "x7b1r11b1x2",
        "x7b1r6b4r1b1x2",
        "x7b1r5b1s1b1s1b2x3",
        "x7b1r4b1s2b1s1b3x2",
        "x7b1r4b1s7b1x1",
        "x8b1r3s2b1s5b1x1",
        "x8b1r3s1b4s2b3",
        "x9b2r1s3b5x2",
        "x8b1r2b2s4b1x4",
        "x7b1r4b5x5",
        "x7b1r3b3r3b1x1b1x2",
        "x6b1r3b1s3b1s3b1s1b1x1",
        "x6b1r2b1s5b1s2b1s1b1x1",
        "x3b4r2b1s5b1s3b1x2",
        "x1b2s1r2b2r2b1s3b1s4b1x2",
        "b2r1s1r2s1r1b2r1b3s5b1x2",
        "b1r2s1r2s1b1r7s3r1b1x2",
        "b1r2s2r1b3r7b1r3b1x1",
        "b2r2b2x1b1s1b1r4b2r4s1b1",
        "x1b3x3b1s1b1r3b1x1b1r4s1b1",
        "x7b1s2b3x3b1r2s1b1x1",
        "x8b1s4b1x2b1s2b1x2",
        "x9b5x3b2x3"   
    ]   
)

TanookiMarioWalkRight03 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "s":NES_PALETTE_HEX[3, 6],
        "r":NES_PALETTE_HEX[1, 7],
    },
    matrix = [
        "x9b2x2b4x1b1x4",
        "x8b1s2b2r4b1s1b1x3",
        "x8b1s3r6s1b1x3",
        "x8b1s3r7b1x3",
        "x8b1s2r9b1x2",
        "x7b1r12b1x2",
        "x7b1r6b5r1b1x2",
        "x7b1r5b1s1b1s1b1s1b2x2",
        "x7b1r4b1s2b1s1b1s1b1x3",
        "x7b1r4b1s7b1x2",
        "x8b1r3s2b1s5b1x2",
        "x8b1r3s1b4s2b3x1",
        "x9b1r3s2b5x3",
        "x10b3r1s4b1x4",
        "x9b1r3b6x1b2x1",
        "x8b1r10b1s2b1",
        "x7b1r3b3r3s3b1s1b1",
        "x7b1r2b1s3b1r1s4b1s1b1",
        "x1b7r1b1s5b1s3b3x1",
        "b2r1s2r2s1b2s5b1s2b1s2b1x1",
        "b1r2s2r2s2b2s3b1r6s1b1",
        "b1r2s2r2s1b1s1r1b3r7s1b1",
        "b2r1s2r2b2s1b1r10s1b1",
        "x1b7s2r1b1r3b3r2s1b2",
        "x7b1s1r3b3x3b4x1",
        "x7b1s1r1b2x11",
        "x8b2x13",
    ]   
)

TanookiMarioRunRight01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "s":NES_PALETTE_HEX[3, 6],
        "r":NES_PALETTE_HEX[1, 7],
    },
    matrix = [
        "x9b2x2b4x1b1x4",
        "x8b1s2b2r4b1s1b1x3",
        "x8b1s3r6s1b1x3",
        "x8b1s3r7b1x3",
        "x8b1s2r9b1x2",
        "x7b1r12b1x2",
        "x7b1r6b5r1b1x2",
        "x7b1r5b1s1b1s1b1s1b2x2",
        "x7b1r4b1s2b1s1b1s1b1x3",
        "x7b1r4b1s7b1x2",
        "x8b1r3s2b1s5b1x2",
        "x8b1r3s1b4s2b3x1",
        "x9b1r3s2b5x3",
        "x10b3s5b1x4",
        "x8b2r2b10x1",
        "x5b4r4b1r4b1s3b1",
        "x4b1s5r4b1r1s3b1s2b1",
        "x4b1s6r3b1s5b2x1",
        "x1b7s3r1b2r1s6b1x1",
        "b2r1s2r2b5r3s6b1x1",
        "b1r2s2r2s3b1r4s6b1x1",
        "b1r2s2r3s1b1r5s6b1x1",
        "b2r1s2r3b2r6s4b1x2",
        "x1b7x2b1r9b1x2",
        "x11b1r6b2x3",
        "x11b1r5b1x5",
        "x11b1s6b1x4",
        "x11b8x4"
        
    ]    
)

TanookiMarioRunRight02 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "s":NES_PALETTE_HEX[3, 6],
        "r":NES_PALETTE_HEX[1, 7],
    },
    matrix = [
        "x9b2x2b4x1b1x4",
        "x8b1s2b2r4b1s1b1x3",
        "x8b1s3r6s1b1x3",
        "x8b1s3r7b1x3",
        "x8b1s2r9b1x2",
        "x7b1r12b1x2",
        "x7b1r6b5r1b1x2",
        "x7b1r5b1s1b1s1b1s1b2x2",
        "x7b1r4b1s2b1s1b1s1b1x3",
        "x7b1r4b1s7b1x2",
        "x8b1r3s2b1s5b1x2",
        "x8b1r3s1b4s2b3x1",
        "x9b1r3s2b5x3",
        "x10b3s5b1x4",
        "x8b2r2b1r1b8x1",
        "x5b4r4b1r4b1s3b1",
        "x4b1s5r4b1r1s3b1s2b1",
        "x4b1s6r3b1s4b3x1",
        "x1b7s3r1b2r1s5b1x2",
        "b2r1s2r2b5r3s5b1x2",
        "b1r2s2r2s1b1r6s5b1x2",
        "b1r2s2r2s1b1r7s3r1b1x2",
        "b2r1s2r2b3r7b1r3b1x1",
        "x1b6x1b1s1b1r4b2r4s1b1",
        "x8b1s1b1r3b1x1b1r4s1b1",
        "x8b1s2b3x3b1r2s1b1x1",
        "x9b1s4b1x2b1s2b1x2",
        "x10b5x2b3x3"
        
    ]    
)

TanookiMarioRunRight03 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "s":NES_PALETTE_HEX[3, 6],
        "r":NES_PALETTE_HEX[1, 7],
    },
    matrix = [
        "x9b2x2b4x1b1x4",
        "x8b1s2b2r4b1s1b1x3",
        "x8b1s3r6s1b1x3",
        "x8b1s3r7b1x3",
        "x8b1s2r9b1x2",
        "x7b1r12b1x2",
        "x7b1r6b5r1b1x2",
        "x7b1r5b1s1b1s1b1s1b2x2",
        "x7b1r4b1s2b1s1b1s1b1x3",
        "x7b1r4b1s7b1x2",
        "x8b1r3s2b1s5b1x2",
        "x8b1r3s1b4s2b3x1",
        "x9b1r3s2b5x3",
        "x10b3s5b1x4",
        "x8b2r2b10x1",
        "x5b4r4b1r4b1s3b1",
        "x4b1s5r4b1r1s3b1s2b1",
        "x4b1s6r3b1s5b2x1",
        "x1b7s3r1b2r1s4b2x2",
        "b2r1s2r2b5r3s3b1s2b1x1",
        "b1r2s2r2s2b1r11s1b1",
        "b1r2s2r2s1b1s1r11s1b1",
        "b2r1s2r2b2s1r11s1b1",
        "x1b7s1r5b3r4s1b1",
        "x7b1s1r2b3x3b1r2s1b2",
        "x7b1s2b1x7b4x1",
        "x7b3x13"
        
    ]    
)

FrogMarioWalkRight01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "s":NES_PALETTE_HEX[3, 6],
        "g":NES_PALETTE_HEX[2, 10],
    },
    matrix = [
        "x10b2x1b2x5",
        "x9b1g1s1b1s1b1x5",
        "x8b1g1s2b1s2b1x4",
        "x8b1g1s1b1g1b1s1b1x4",
        "x8b1g1s1b1g1b1s1b1x4",
        "x7b1g8b1x3",
        "x6b1g9b1x3",
        "x6b1g6b3g1b1x2",
        "x5b1g5b5g1b1x2",
        "x5b1g4b3s3b2x2",
        "x5b1g4b2s2b1s1b1x3",
        "x5b1g3b3s2b1s1b3x1",
        "x3b2g1b1g2b3s7b1",
        "x2b1g3b1g2b2s2b1s5b1",
        "x1b1g5b1g2b1s1b3s3b2",
        "x1b1g8s4b5x1",
        "b1g8b2s5b1x3",
        "b1g3b2g4b6x4",
        "b1g2b1g2b1g3b1x9",
        "b1g5b1g3b1x9",
        "x1b1g4b1g3b1x9",
        "x2b1g2b3g1b3x8",
        "x1b1g6b1s3b1x7",
        "x1b12x7",
        
    ]   
)

FrogMarioWalkRight02 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "s":NES_PALETTE_HEX[3, 6],
        "g":NES_PALETTE_HEX[2, 10],
    },
    matrix = [
        "x10b2x1b2x5",
        "x9b1g1s1b1s1b1x5",
        "x8b1g1s2b1s2b1x4",
        "x8b1g1s1b1g1b1s1b1x4",
        "x8b1g1s1b1g1b1s1b1x4",
        "x7b1g8b1x3",
        "x6b1g9b1x3",
        "x6b1g6b3g1b1x2",
        "x5b1g5b5g1b1x2",
        "x5b1g4b3s3b2x2",
        "x5b1g4b2s2b1s1b1x3",
        "x5b1g3b3s2b1s1b3x1",
        "x6b1g2b3s7b1",
        "x5b2g2b2s2b1s5b1",
        "x4b1g2b1g2b1s1b3s3b2",
        "x3b1g6s4b5x1",
        "x2b1g6b2s5b1x3",
        "x2b1g2b1g4b6x4",
        "x1b1g3b5g2b1x7",
        "x1b1g4b1s3b1g1b1x7",
        "b1g5b1s4b1x8",
        "b1g6b2s2b1x8",
        "b1g6b1s2b1x9",
        "x1b1g5b3x10",
        "x1b1g4b1x13",
        "b1g4b1x14",
        "b1g3b2x14",
        "b2g4b1x13",
        "x1b6x13",        
    ]   
)

FrogMarioWalkRight03 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "s":NES_PALETTE_HEX[3, 6],
        "g":NES_PALETTE_HEX[2, 10],
    },
    matrix = [
        "x9b2x1b2x5",
        "x8b1g1s1b1s1b1x5",
        "x7b1g1s2b1s2b1x4",
        "x7b1g1s1b1g1b1s1b1x4",
        "x7b1g1s1b1g1b1s1b1x4",
        "x6b1g8b1x3",
        "x5b1g9b1x3",
        "x5b1g6b3g1b1x2",
        "x4b1g5b5g1b1x2",
        "x4b1g4b3s3b2x2",
        "x4b1g4b2s2b1s1b1x3",
        "x4b1g3b3s2b1s1b3x1",
        "x5b1g2b3s7b1",
        "x5b1g2b2s2b1s5b1",
        "x6b1g2b1s1b3s3b2",
        "x5b1g3s4b5x1",
        "x4b1g3b4s3b1x3",
        "x3b1g8b5x2",
        "x3b1g10b1s2b1x1",
        "x2b1g11b1s3b1",
        "x2b1g6b1g4b1s3b1",
        "x2b1g7b4x1b2s1b1",
        "x1b1g8b1x6b1x1",
        "b1g8b1x9",
        "b1g4b4x10",
        "b1g4b1x13",
        "b1g2b2x14",
        "b1g2b1x15",
        "x1b2x16",
    ]   
)

SuperMarioBros3BG01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "p":NES_PALETTE_HEX[3, 1],
        "g":NES_PALETTE_HEX[2, 10],
        "d":NES_PALETTE_HEX[1, 9],
        "l":NES_PALETTE_HEX[2, 1],
        "w":NES_PALETTE_HEX[3, 0],
    },
    matrix = [
        "w2l3w2b2w1l4w2" + "w2l3w2b2w1l4w2",
        "b2w3b2p2b1w5b1" + "b2w3b2p2b1w5b1",
        "p2b3p5b5p1" + "p2b3p5b5p1",
        "p16" + "p16",
        "p16" + "p16",
        "p16" + "p16",
        "p16" + "p16",
        "p16" + "p16",
        "p16" + "p16",
        "p16" + "p16",
        "p16" + "p16",
        "p5b6p5" + "p5b6p5",
        "p3b2g6b2p3" + "p3b2g6b2p3",
        "p2b1g10b1p2" + "p2b1g10b1p2",
        "p1b1g4b1g1b1g5b1p1" + "p1b1g4b1g1b1g5b1p1",
        "p1b1g4b1g1b1g5b1p1" + "p1b1g4b1g1b1g5b1p1",
        "b3g10b3" + "b3g10b3",
        "g3b2g6b2g3" + "g3b2g6b2g3",
        "g5b1g4b1g5" + "g5b1g4b1g5",
        "g6b1g2b1g6" + "g6b1g2b1g6",
        "g1b1g4b1g2b1g4b1g1" + "g1b1g4b1g2b1g4b1g1",
        "g1b1g5b2g5b1g1" + "g1b1g5b2g5b1g1",
        "g7b2g7" + "g7b2g7",
        "g7b2g7" + "g7b2g7",
        "g7b2g7" + "g7b2g7",
        "g7b2g7" + "g7b2g7",
        "g7b2g7" + "g7b2g7",
        "g7b2g7" + "g7b2g7",
        "g7b2g7" + "g7b2g7",
        "b7p1b8" + "b7p1b8",
        "g2b1g3b3g6b1" + "g2b1g3b3g6b1",
        "g11b1g4" + "g11b1g4",
    ]    
)

SuperMarioBros3BG02 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "p":NES_PALETTE_HEX[3, 13],
        "r":NES_PALETTE_HEX[2, 7],
        "l":NES_PALETTE_HEX[3, 1],
        "i":NES_PALETTE_HEX[2, 12],
        "w":NES_PALETTE_HEX[3, 0],
    },
    matrix = [
        "w7l2w3l1w3" + "w7l2w3l1w3",
        "w2l1w3l2w1b2w3l2" + "w2l1w3l2w1b2w3l2",
        "b1w2i4w2b1w1b2w3" + "b1w2i4w2b1w1b2w3",
        "w1b2w4b2w3l1b3" + "w1b2w4b2w3l1b3",
        "l1w2b4l2w4l3" + "l1w2b4l2w4l3",
        "l2w4l4w4l2" + "l2w4l4w4l2",
        "l3w4l4w4l1" + "l3w4l4w4l1",
        "l4w4l4w4" + "l4w4l4w4",
        "w1l4w4l4w3" + "w1l4w4l4w3",
        "w2l4w4l4w2" + "w2l4w4l4w2",
        "w3l4w4l4w1" + "w3l4w4l4w1",
        "w4l4w4l4" + "w4l4w4l4",
        "l1w4l4w4l3" + "l1w4l4w4l3",
        "l2w4l4w4l2" + "l2w4l4w4l2",
        "l3w4l4w4l1" + "l3w4l4w4l1",
        "l4w4l4w4" + "l4w4l4w4",
        "w1l4w4l4w3" + "w1l4w4l4w3",
        "w2l4w4l4w2" + "w2l4w4l4w2",
        "w3l4w4l4w1" + "w3l4w4l4w1",
        "w4l4w4l4" + "w4l4w4l4",
        "l1w4l4w4l3" + "l1w4l4w4l3",
        "l2w4l4w4l2" + "l2w4l4w4l2",
        "l3w4l4w4l1" + "l3w4l4w4l1",
        "l4w4l4w4" + "l4w4l4w4",
        "w1l4w4l4w3" + "w1l4w4l4w3",
        "w2l4w4l4w2" + "w2l4w4l4w2",
        "w3l4w4l4w1" + "w3l4w4l4w1",
        "w4l4w4l4" + "w4l4w4l4",
        "l1w4l4w4l3" + "l1w4l4w4l3",       
        "b16" + "b16",
        "r2p5r3p5r1" + "r2p5r3p5r1",
        "r3p5r3p5" + "r3p5r3p5",
    ]    
)

smb3_animation = animation_settings(
    sprite_list=[[TanookiMarioWalkRight01,
                 TanookiMarioWalkRight02,
                 TanookiMarioWalkRight03,
                 TanookiMarioWalkRight02],
                 [FrogMarioWalkRight01,
                  FrogMarioWalkRight02,
                  FrogMarioWalkRight03],
                ],
    bg_sprites=[SuperMarioBros3BG01,
                SuperMarioBros3BG02],
    xoffs=[[0, 0, 0, 0],
           [0, 0, 0],
          ],
    yoffs=[[0, 0, 0, 0],
           [1, 0, 0],
          ],
    frame_time=0.04,
    spbg_ratio=2,
    center=True,
    bg_scroll_speed=(1, 0),
    cycles_per_char=5,
    reversible="horizontal",
    )
