import sys
sys.path.append("../")
from settings import (NES_PALETTE_HEX, animation_settings)
from core import sprite

TrevorBelmontWalkLeft01 = sprite(
    palette = { 
        "p":NES_PALETTE_HEX[3, 7],
        "o":NES_PALETTE_HEX[1, 7],
        "d":NES_PALETTE_HEX[0, 7],
    },
    matrix = [
        "x3d5x8",
        "x2d2o4d1x7",
        "x2d2p1d5x6",
        "x3d2p1o1d4x5",
        "x3d1p2o2d5x3",
        "x3d1p1o1d6o1d1x2",
        "x3d3p1o3d1o2d1x2",
        "x4d1p1d3o4d2x1",
        "x2d1x2d2p1d2o2d3x1",
        "d2p1d1x1d1p3d4p2d1",
        "d1p2d2p3d4o1p2d1",
        "d1o1p1o2p2d5o1p1d1x1",
        "x1d1p1o3d8x2",
        "x2d5o1p3d1x4",
        "x6d1p2d4x3",
        "x6d8x2",
        "x5d9x2",
        "x4d1p1o1d7x2",
        "x3d1p1o2d2p3d1x3",
        "x2d1p1o2d1x1d1p3d1x3",
        "x2d1p1o1d1x3d1p2d1x3",
        "x2d4x3d1p3d1x2",
        "x2d1p1o1d1x4d3o1d1x1",
        "x2d3o1d1x3d1p1o2d1x1",
        "x2d1p1o2d1x4d3o1d1",
        "x2d1p1o2d1x5d1o2d1",
        "x2d2o2d1x5d2o1d1",
        "d2p1o2d1x6d1o2d1",
        "d1p1o3d1x5d1o3d1",
        "d6x5d5",
    ]   
)

TrevorBelmontWalkLeft02 = sprite(
    palette = { 
        "p":NES_PALETTE_HEX[3, 7],
        "o":NES_PALETTE_HEX[1, 7],
        "d":NES_PALETTE_HEX[0, 7],
    },
    matrix = [
        "x2d4x6",
        "d2o4d1x5",
        "d2p1d5x4",
        "x1d2p1o1d4x3",
        "x1d1p2o2d3x3",
        "x1d1p1o2d4x3",
        "x1d4p1o3p1x2",
        "x3d1p1o2d3x2",
        "x2d1p1o2d2p2d1x1",
        "x2d1o2d2p3d1x1",
        "x2d1o2d3p3d1",
        "x2d1o1d5p2d1",
        "x3d1p1d2o3p1d1",
        "x2d1p3o4p1d1",
        "x2d1p3o3d2x1",
        "x3d8x1",
        "x3d8x1",
        "x3d7x2",
        "x3d1o1d1p3d1x2",
        "x3d1o1d1p3d1x2",
        "x3d1o1d1p2d1x3",
        "x3d1o1d1p2d1x3",
        "x3d6x3",
        "x5d1p1o2d1x2",
        "x5d1p1d2o1d1x1",
        "x6d1p1o2d1x1",
        "x6d1p1o2d2",
        "x6d1p1o1d3",
        "x5d1p1o2d1o1d1",
        "x5d1o3d1o1d1",
        "x5d7",
    ]   
)

TrevorBelmontWalkLeft03 = sprite(
    palette = { 
        "p":NES_PALETTE_HEX[3, 7],
        "o":NES_PALETTE_HEX[1, 7],
        "d":NES_PALETTE_HEX[0, 7],
    },
    matrix = [
        "x2d4x11",
        "d2o4d1x10",
        "d2p1d5x9",
        "x1d2p1o1d3x9",
        "x1d1p2o2d6x5",
        "x1d1p1o3d3o3d1x4",
        "x1d3o1d3o2d3x4",
        "x2d1p1d3p1o1d2o1p1d1x3",
        "x2d1p1d2p1o2d1o1p3d1x2",
        "x2d1o1p2o3d2p4d1x1",
        "x1d2o5d5p1o1d1x1",
        "d1p2d1o3d6o2d1x1",
        "d1p1d1o1d7p2o2d1x1",
        "d1p1o1d3p2o2d1p3d1x2",
        "x1d2x2d3o2d2p2d1x2",
        "x5d9x3",
        "x5d1o1d7x3",
        "x5d1p1o2d4x4",
        "x4d1p3d2o2d1x4",
        "x3d1p3d2o3d1x4",
        "x3d1p2d4p1o1d1x4",
        "x2d5x2d5x3",
        "x2d1p1o1d2x2d1o3d2x2",
        "x2d5x2d4o1d1x2",
        "x2d1p1o2d1x3d1o4d1x1",
        "x2d1p1o2d1x4d1o4d1",
        "x2d1p1o1d1x6d2o2d1",
        "x1d1p1o2d1x6d1o2d2",
        "d1p1o3d1x5d1o3d1x1",
        "d6x5d5x1",
    ]   
)

GrantDanastyWalkRight01 = sprite(
    palette = { 
        "p":NES_PALETTE_HEX[3, 7],
        "r":NES_PALETTE_HEX[1, 5],
        "b":NES_PALETTE_HEX[0, 13],
    },
    matrix = [
        "x15b4x1",
        "x13r1b1r3p1b1",
        "x12r1x1b2r3b1",
        "x9b5r1p3b2",
        "x8b1p2b3p1r1p4",        
        "x7b1p3b3p1r1p3b1",
        "x6b1p4b3p1b1r1p2b1",
        "x5b1p4b4r1x1b3x1",
        "x4b1p2b8x5",
        "x4b1p3b1p1b4x3b3",
        "x5b1p2r1p3b5p2b1",
        "x5b3r1p3b2r1p1r1p2b1",
        "x5b8r2p1r1b2x1",
        "x5b1r5b6x3",
        "x5b1r8b1x5",        
        "x5b3r6p1b1x4",
        "x5b8r1p1b1x4",
        "x4b1r3b1x2b1r3b1x4",
        "x4b1r3b1x2b1r2b1x5",
        "x1b3r3p1b1x2b1r2b1x5",        
        "b1p2b1r2p1b1x2b4x6",
        "b1p3b3x3b1p2b1x6",
        "b1p1b3x5b1p3b1x5",
        "b1p3b1x6b2p2b1x4",
        "b5x6b5x4",
    ]   
)

GrantDanastyWalkRight02 = sprite(
    palette = { 
        "p":NES_PALETTE_HEX[3, 7],
        "r":NES_PALETTE_HEX[1, 5],
        "b":NES_PALETTE_HEX[0, 13],
    },
    matrix = [
        "x11b4x1",
        "x8r2b1r3p1b1",
        "x10b2r3b1",
        "x6b5p3b2",
        "x4b6p1r1p4",
        "x3b4p1b2p1r1p3b1",
        "x2b4p3b1p1b1r1p2b1",
        "x1b1p1b3p3b2x1b3x1",
        "x1b2p1b2p3b2x5",
        "b1r2b1p1b1p2b5x3",
        "b1r3b2p4r1p2b1x2",
        "b1r4b2p2b1r1p2b1x2",
        "b1r5b8x2",
        "x1b1r6b2x6",
        "x2b2r6b1x5",
        "x3b3r3p1b1x5",
        "x3b1r1b2r2p1b1x5",
        "x2b1r2b1r3b1x6",
        "x1b1r2b1r3b1x7",
        "x1b3r3b1x8",
        "b4p2b1x9",
        "b1p1b1p4b1x8",
        "b1p1b1p5b1x7",
        "b9x7",
    ]   
)

GrantDanastyWalkRight03 = sprite(
    palette = { 
        "p":NES_PALETTE_HEX[3, 7],
        "r":NES_PALETTE_HEX[1, 5],
        "b":NES_PALETTE_HEX[0, 13],
    },
    matrix = [
        "x11r1x2b4x2",
        "x12r1b1r3p1b1x1",
        "x13b2r3b1x1",
        "x13b1p3b2x1",
        "x8b6r1p4x1",
        "x6b7p1r1p3b1x1",
        "x5b4p2b2p1b1r1p2b1x1",
        "x4b1p1b3p3b1p1b5x1",
        "x4b1p1b3p3b2x3b3",
        "x5b5p2b5p2b1",
        "x5b1p3b1r1p2b1p2r1p2b1",
        "x4b1r1b5p5r1b1p1b1",
        "x4b1r4b3p4b3x1",
        "x4b1r4b7x4",
        "x4b1r4b3r1b1x6",
        "x4b1r3b3r3b1x5",
        "x4b1r3b3r3p1b1x4",
        "x4b1r3b1x1b2r2p1b1x4",
        "x4b2r2b1x2b2r2b1x4",
        "x3b4p1b1x2b1r2b1x5",
        "x1b3r3p1b1x1b1r3b1x5",
        "b1p2b1r3b1x2b2p1b1x6",
        "b1p2b4x3b1p2b1x6",
        "b1p1b2x6b1p3b1x5",
        "b1p3b1x6b2p2b1x4",
        "b5x6b5x4"
    ]   
)

SyphaBelnadesWalkRight01 = sprite(
    palette = { 
        "w":NES_PALETTE_HEX[3, 0],
        "d":NES_PALETTE_HEX[1, 2],
        "b":NES_PALETTE_HEX[2, 1],
    },
    matrix = [
        "x5d1w2b1x6",
        "x4d1w4b2x4",
        "x4d1w3b1d3x3",
        "x4d1w2b1d2w1d1x3",
        "x4d1w1b1d2w1d2x3",
        "x3d2w1b1d2b1w1x4",
        "x3d1w3b1d2b1x4",
        "x3d1w2d1w1b1d1x5",
        "x2d1w4d4x4",
        "x2d1w6d3x3",
        "x2d1w5d1w1b1d3x1",
        "x2d1w5d1w1b1d1w2d1",
        "x2d1w5d1w1b1d1b1w1d1",
        "x2d1w4b1w2b1d3x1",
        "x2d2w3d1w1b1d1x4",
        "x2d3b2d1w1b1d1x4",
        "x1d1w1d4w2b1d1x4",
        "x1d1w2d3w2b1d1x4",
        "x1d1w7b1d1x4",
        "x1d1w7b1d1w1x3",
        "x1d1w7b1d1w1x3",
        "x1d1w6b1d1b1w1x3",
        "x1d1w6b1d1b1w1x3",
        "x1d1w4d1w1b1d1b1w1x3",
        "x1d1w1b3d1w1b1d1b1w1x3",
        "x1d5w1b1d2b1w1x3",
        "d1w1d3w2b1d2b1d1w1x2",
        "d1w5b1d4w1d2x1",
        "d1w4b1d3b1w1d1b1w1x1",
        "d2w1b2d9x1",
    ]   
)

SyphaBelnadesWalkRight02 = sprite(
    palette = { 
        "w":NES_PALETTE_HEX[3, 0],
        "d":NES_PALETTE_HEX[1, 2],
        "b":NES_PALETTE_HEX[2, 1],
    },
    matrix = [
        "x4d1w2b1x5",
        "x3d1w4b2x3",
        "x3d1w3b1d3x2",
        "x3d1w2b1d2w1d1x2",
        "x3d1w1b1d2w1d2x2",
        "x2d2w1b1d2b1w1x3",
        "x2d1w3b1d2b1x3",
        "x2d1w2d1w1b1d1x4",
        "x1d1w4d1w1b1d1x3",
        "x1d1w5d1w1d1x3",
        "x1d1w4d1w1d2b1x2",
        "x1d1w3d1w2b1d1b1x2",
        "x1d1w3d1w2b1d3x1",
        "x1d1w2d1w3b1d1w2d1",
        "x1d1b1d2w3b1d1b1w1d1",
        "x1d3w3b1d4x1",
        "x1d2w4b1d2x3",
        "x1d1w5b1d1b1x3",
        "x1d1w5b1d1b1x3",
        "x1d1w4b1d1b1w1x3",
        "x1d1w2d1w1b1d1b1w1x3",
        "x1d1w2d1w1b1d1b1w1x3",
        "d1w3d1w1b1d1b1w1x3",
        "d1w2d1w1b1d1b2w1x3",
        "d1w2d1w1b1d1b2w1x3",
        "d1w1b1d1w1b1d1b2w1x3",
        "d1b1d1w1b1d2b2w1x3",
        "d3w1b1d3b1w1x3",
        "x1d1w2b1d5x3",
        "w3b1d2b1w3x3",
        "w2b1d7x3"
    ]   
)

SyphaBelnadesWalkRight03 = sprite(
    palette = { 
        "w":NES_PALETTE_HEX[3, 0],
        "d":NES_PALETTE_HEX[1, 2],
        "b":NES_PALETTE_HEX[2, 1],
    },
    matrix = [
        "x5d1w2b1x5",
        "x4d1w4b2x3",
        "x4d1w3b1d3x2",
        "x4d1w2b1d2w1b1x2",
        "x4d1w1b1d2w1d2x2",
        "x3d2w1b1d2b1w1x3",
        "x3d1w3b1d2b1x3",
        "x2d1w1b1d1w2b1d1x4",
        "x2d1b1d1w1b1d1w2b1x3",
        "x1d3w2b1d2b1d1x3",
        "x1d1w3b1d2b3d1x2",
        "x1d1w2b1d7x2",
        "x1d1w2b1d1b1w1d1w2x3",
        "x1d1w1b1d1b2w1d1b1w1x3",
        "x1d1w1b1d1b2w1d4x2",
        "x1d1w1b1d1b2w1d3x3",
        "x1d1w1b1d2b1w1d3x3",
        "x1d1w1b1d6w1x3",
        "x1d1w1b1d5b1w1x3",
        "x1d1w1b1d5b2w1x2",
        "x1d1w1b1d5b2w1x2",
        "x1d1w1b1d3b1d1b2w1x2",
        "x1d1w1b1d3b1w1d1b1w1x2",
        "x1d1w1b1d3b2w1b1w1x2",
        "x1d1w1b1d3b4w1x2",
        "x1d1w1b1d2w1b3d2x2",
        "x1w1b1d2b3d2w3x1",
        "d1w1b1d5w2d4",
        "d1w1d2b1w3d4b1w1",
        "d14",
    ]   
)

Castlevania3BG01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "g":NES_PALETTE_HEX[1, 0],
        "d":NES_PALETTE_HEX[0, 12],
    },
    matrix = [
        "b2d1g3d1b3d1g2d1g2" + "d1b3d1b1d1b2g3d3b1",
        "b2g3d2b3g2d2g2" + "g1b7g4d3b1",
        "b2g3d3b2g1d4g1" + "d1b5d1b1g3d4b1",
        "b2d1g1d3b3g1d4g1" + "g1b3d3b1g3d4b1",
        "b2d5b3g1d4g1" + "g1d3b2d1b1g3d4b1",
        "b3d2b5g1d5" + "g1d1b4d1b2g1d4b2",
        "b10g1d1g1d3" + "g1b5d1b3d1b5",
        "b10g1d4g1" + "d1b5d1b3d1b1d2b2",
        "b10g1d5" + "d1b5d1b2g1b1d1b2d1b1",
        "b10d2g1d3" + "d1b5d1b2g2d1b2d1b1",
        "b10d1g2d3" + "d1b3d1b1d1b2g3b2d1b1",
        "b10d2g1b3" + "b4d2b3g3d3b1",
        "b10d2g1b1d1g1" + "g1b3d1b1d1b2g3d2b2",
        "b11d1b2d2" + "d1b2d2b2d1b1g1d4b2",
        "b13d2b1" + "d1b6d1b8",
        "b2d1b4d1b2d4b2" + "g4b6g2d3b1",
        "d1b5d2b1d6b1" + "d2g2d1b4g3d3b1",
        "b2g2b1d3b1d2g1d3b1" + "d2g2d2b2g4d3b1",
        "b1d2g1b1d3b2g3d1g1b1" + "d2g1d3b2g3d4b1",
        "d3g1b1d3b1d1g4d1b1" + "d2g2d2b2g3d4b1",
        "d3g1b1d3b1d1g4b1d1" + "d2g2d2b2g3d4b1",
        "d3g1b1g3b2g4d1b1" + "d2g2d2b3g1d4b2",
        "d4b1d3b2g4d1b1" + "d2g2d1b5d1b5",
        "d3g1b1d3b2g4d1b1" + "d3g1b1d3b2d1b1d2b2",
        "d4b2d2b2d1g3d1b1" + "d4b2d2b1g1b1d1b2d1b1",
        "b1d2b4d1b2g3d2b1" + "b1d2b4d1b1g2d1b2d1b1",
        "b1d2b4d1b2g3d3" + "b1d2b4d1b1g3b2d1b1",
        "b2d1b7d1g1d3b1" + "b2d1b6g3d3b1",
        "b1d3b2d1b3d5b1" + "b1d3b2d1b2g3b2b2",
        "b1d1b1d1b2d1b4d2b3" + "b1d1b1d1b2d1b2g1d4b2",
        "b16" + "b16",
        "b16" + "b16",
    ]    
)

Castlevania3BG02 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "g":NES_PALETTE_HEX[1, 10],
        "d":NES_PALETTE_HEX[0, 2],
        "l":NES_PALETTE_HEX[1, 1],
        "r":NES_PALETTE_HEX[1, 0],
        "w":NES_PALETTE_HEX[3, 0],
        "o":NES_PALETTE_HEX[0, 8],
        "p":NES_PALETTE_HEX[3, 7],
    },
    matrix = [
        "b6o1b1o8" + "b2o1b1o2b2o1b1d2o4",
        "b7d1o8" + "b7o3b2d1o3",
        "b3o1b3o9" + "o1b1o3b1o1b1o3b1o2d1o1",
        "b2o2b2o6b1o1b2" + "b8o4p1d1b2",
        "o1b1o3b1o4b1o1b2o2" + "b1o2b1o3b1o1d2o3b1o1",
        "o5b1o3b6o1" + "b9p1b6",
        "o5b1o3b7" + "b2o13b1",
        "o6b1o1b8" + "o16",
        "o1b1d2o4b2o1b1o2b2" + "o16",
        "o2b2d1o3b7o1" + "o16",
        "o3b1o2d1o2b1o3b1o1b1" + "o10b1o5",
        "o4p1d1b10" + "o13b2o1",
        "o1d2o3b1o1b1o2b1o3b1" + "o16",
        "b1p1o6b8" + "o16",
        "o7b3o6" + "o9b3o4",
        "b16" + "b1g5b3g5b2",
        "l1w3l1w1l1d1l1w3l1w1l1d1" + "g16",
        "l16" + "g1b2g4b1g1b2g4b1",
        "b16" + "g1b2g2b3g1b2g2b3",
        "d7b1d7b1" + "b1g1b4g1b2g1b4g1b1",
        "d1l5d1b1d1l5d1b1" + "g2b1g3b2g2b1g3b2",
        "l7d1l7d1" + "b1g1b2g2b2b1g1b2g2b2",
        "l7d1l7d1" + "l1b7l1b7",
        "d1l6b1d1l6b1" + "l1b1g3b3l1b1g3b3",
        "l5d1l1d1l5d1l1d1" + "l2b1g1b2l1b1l2b1g1b2l1b1",
        "l5d1l1d1l5d1l1d1" + "l3b1l1b1l1b1l3b1l1b1l1b1",
        "l4d1l2d1l4d1l2d1"+ "l4b1l2b1l4b1l2b1",
        "l2d4l1d1l2d4l1d1" + "b1l1b3l1b3l1b3l1b2",
        "l6d1b1l6d1b1" + "l6b2l6b2",
        "d7b1d7b1" + "r2b1r1b2r1b1r2b1r1b2r1b1",
        "d7b1d7b1" + "b16",
        "b16" + "b16",
    ]    
)

TrevorWalkLeftSeries_sprites = (TrevorBelmontWalkLeft01,
                                TrevorBelmontWalkLeft02,
                                TrevorBelmontWalkLeft03,
                                TrevorBelmontWalkLeft02,
                                )
TrevorWalkLeftSeries_xoffs = (-1, 0, -2, 0)
TrevorWalkLeftSeries_yoffs = (0, 0, 0, 0)

GrantWalkLeftSeries_sprites = (GrantDanastyWalkRight01.hflip(),
                               GrantDanastyWalkRight02.hflip(),
                               GrantDanastyWalkRight03.hflip(),
                               GrantDanastyWalkRight02.hflip(),
                              )
GrantWalkLeftSeries_xoffs = (-1, 0, -1, 0)
GrantWalkLeftSeries_yoffs = (4, 4, 3, 4)

SyphaWalkLeftSeries_sprites = (SyphaBelnadesWalkRight01.hflip(),
                               SyphaBelnadesWalkRight02.hflip(),
                               SyphaBelnadesWalkRight03.hflip(),
                               SyphaBelnadesWalkRight02.hflip(),
                              )
SyphaWalkLeftSeries_xoffs = (0, 0, -1, 0)
SyphaWalkLeftSeries_yoffs = (0, 0, 0, 0)

castlevania3_animation = animation_settings(
    sprite_list=[TrevorWalkLeftSeries_sprites,
                 GrantWalkLeftSeries_sprites,
                 SyphaWalkLeftSeries_sprites],
    bg_sprites=[Castlevania3BG01,
                Castlevania3BG02],
    xoffs=[TrevorWalkLeftSeries_xoffs,
          GrantWalkLeftSeries_xoffs,
          SyphaWalkLeftSeries_xoffs],
    yoffs=[TrevorWalkLeftSeries_yoffs,
          GrantWalkLeftSeries_yoffs,
          SyphaWalkLeftSeries_yoffs],
    frame_time=0.05,
    spbg_ratio=3,
    center=True,
    bg_scroll_speed=(-1, 0),
    cycles_per_char=5,
    reversible="horizontal",
    )
