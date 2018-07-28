import sys
sys.path.append("../")
from settings import (NES_PALETTE_HEX, animation_settings)
from core import sprite

RyuClimb01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 8],
        "l":NES_PALETTE_HEX[1, 2],
        "p":NES_PALETTE_HEX[3, 13],
    },
    matrix = [
        "x5b4x5b2",
        "x4b1l4b1x3b1p2",
        "x5b1l4b1x2b1p2",
        "x4b1l1b1l2b2x1b2p1b1",
        "x4b1l2b1p2b5x1",
        "x4b1p1b1l2b1p1b3x2",
        "x3b1l3b1l1b1p2b1x3",
        "x3l3p2b1p2b1x2b2",
        "x2b1l2b1p3b2x2b1p2",
        "x2l3b1p4b1x1b2p2",
        "x1b1l4b1p4b3p1b1",
        "x1b1l3b3p2b4x2",
        "x1l6b2p1b3x3",
        "b1l5b2l1b3l1b1x2",
        "b1l3b3l7b1x1",
        "x1l1b2l3b1l1b1l2b3x1",
        "x1b1l5b2l1b4x2",
        "x1b1l3b3l1b1x1b3x2",
        "x1b1l2b1l3b1x2b4x1",
        "x2b1l6b1x2b2p1b1",
        "x3b1l5b1x2b2p1b1",
        "x4b1l5b1x1b1p2b1",
        "x5b3l2b1x1b1p1b1x1",
        "x6b1l2b2x2b2x1",
        "x7b4x5",
        "x8b4x1b1x2",
        "x9b4p1b1x1",
        "x10b3p1b1x1",
        "x10b2p2b1x1",
        "x10b1p2b1x2",
        "x11b2x3"
        
    ]    
)

RyuClimb02 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 8],
        "l":NES_PALETTE_HEX[1, 2],
        "p":NES_PALETTE_HEX[3, 13],
    },
    matrix = [
        "x5b4x7",
        "x4b1l4b1x6",
        "x5b1l4b1x5",
        "x4b1l1b1l2b2x5",
        "x4b1l2b1p2b1x3b2",
        "x4b1p1b1l2b1x3b1p2",
        "x3b1l3b1l1b1x2b2p2",
        "x3l3p2b2x1b3p1b1",
        "x2b1l2b1p4b4x2",
        "x2l3b1p5b2x3",
        "x1b1l4b1p2b3x4",
        "x1b1l3b4x7",
        "x1l6b2x7",
        "b1l5b3x7",
        "b1l3b3l2b3x4",
        "x1l1b2l4b2l2b1x3",
        "x1b1l8b2l1b1x2",
        "x1b1l10b1l1b1x1",
        "x2b1l10b2x1",
        "x3b3l4b1l2b1x2",
        "x6b4l3b1x2",
        "x9b4x3",
        "x10b3x3",
        "x10b3x1b1x1",
        "x11b3p1b1",
        "x11b3p1b1",
        "x11b2p2b1",
        "x11b1p2b1x1",
        "x12b2x2"
        
    ]    
)

NinjaGaidenBG01 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "g":NES_PALETTE_HEX[1, 0],
        "d":NES_PALETTE_HEX[0, 0],
        "l":NES_PALETTE_HEX[3, 2],
        "r":NES_PALETTE_HEX[1, 7],
        "h":NES_PALETTE_HEX[2, 7],
    },
    matrix = [
        "b1r1h1r1h1r1h1r1b1r1h1r1h1r1h1r1b1r1h1r1" + "g8d1l1g2",
        "b1h1r3b1r1b2h1r3b1r1b2h1r2" + "g8d1l1g2",
        "b1r1b1r1b1r3b1r1b1r1b1r3b1r1b1r1" + "g8d1l2g1",
        "b20" + "g8d1l1g2",
        "h1r1h1r1b1r1h1r1h1r1h1r1b1r1h1r1h1r1h1r1" + "g8d1l1g2",
        "r2b1r1b1h1r4b1r1b1h1r4b1r1" + "g8d1l2g1",
        "r1b1r1b3r1b1r1b1r1b3r1b1r1b1r1b1" + "g8d1l1g2",
        "b20" + "g8d1g1l1g1",
        
        "b1r1h1r1h1r1h1r1b1r1h1r1h1r1h1r1b1r1h1r1" + "g8d1l1g2",
        "b1h1r3b1r1b2h1r3b1r1b2h1r2" + "g8d1l1g2",
        "b1r1b1r1b1r3b1r1b1r1b1r3b1r1b1r1" + "g8d1l2g1",
        "b20" + "g8d1l1g2",
        "h1r1h1r1b1r1h1r1h1r1h1r1b1r1h1r1h1r1h1r1" + "b1l1g2b2l1g1d1l1g2",
        "r2b1r1b1h1r4b1r1b1h1r4b1r1" + "g3b1l1g3d1l2g1",
        "r1b1r1b3r1b1r1b1r1b3r1b1r1b1r1b1" + "g8d1l1g2",
        "b20" + "g8d1g1l1g1",
        
        "b1r1h1r1h1r1h1r1b1r1h1r1h1r1h1r1b1r1h1r1" + "g8d1l1g2",
        "b1h1r3b1r1b2h1r3b1r1b2h1r2" + "g8d1l1g2",
        "b1r1b1r1b1r3b1r1b1r1b1r3b1r1b1r1" + "g8d1l2g1",
        "b20" + "g8d1l1g2",
        "h1r1h1r1b1r1h1r1h1r1h1r1b1r1h1r1h1r1h1r1" + "g8d1l1g2",
        "r2b1r1b1h1r4b1r1b1h1r4b1r1" + "g8d1l2g1",
        "r1b1r1b3r1b1r1b1r1b3r1b1r1b1r1b1" + "g8d1l1g2",
        "b20" + "g8d1g1l1g1",
        
        "b1r1h1r1h1r1h1r1b1r1h1r1h1r1h1r1b1r1h1r1" + "g8d1l1g2",
        "b1h1r3b1r1b2h1r3b1r1b2h1r2" + "g8d1l1g2",
        "b1r1b1r1b1r3b1r1b1r1b1r3b1r1b1r1" + "g8d1l2g1",
        "b20" + "g8d1l1g2",
        "h1r1h1r1b1r1h1r1h1r1h1r1b1r1h1r1h1r1h1r1" + "b1l1g2b2l1g1d1l1g2",
        "r2b1r1b1h1r4b1r1b1h1r4b1r1" + "g3b1l1g3d1l2g1",
        "r1b1r1b3r1b1r1b1r1b3r1b1r1b1r1b1" + "g8d1l1g2",
        "b20" + "g8d1g1l1g1"
    ]    
)


NinjaGaidenBG02 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "g":NES_PALETTE_HEX[1, 0],
        "d":NES_PALETTE_HEX[0, 0],
        "w":NES_PALETTE_HEX[3, 0],

        "r":NES_PALETTE_HEX[0, 7],
        "e":NES_PALETTE_HEX[1, 7],
        "y":NES_PALETTE_HEX[2, 8],
        
        "h":NES_PALETTE_HEX[1, 7],
    },
    matrix = [
        "d1g1b1d1b6g1b1g2b1g1b5" + "y2r1b1r2b1e1r1e2",
        "d1b2d1b5g1d1b1g1b1d1b3d1b2" + "y1b2r1b1r1b1e1r1e1r1",
        "g1d1b1d1b3d1g1d1b3d1b7" + "y2b2r2b1e1r3",
        "d1b2d1b1d1g1d2g1d1b1g1d1b3d1b3" + "b1y1b1r1b1r1b1e1r1e1y1",
        "g2b1d1g1b2d1w1b1d1b1g1b3g1b1d1b2" + "r1y2b1r2b1e1r1e2",
        "d2b1d1g2b1d2g1d1b4d1b1g1d1b2" + "r2y1b2r1b1e1r3",
        "d1b2d1g1d1g2d1b1d1b2g1d1b1g1d1b3" + "r1b1y3r1b1e1r1b1r1",
        "g1b2d1g1d4b2d1g1d1g1d1g1b2d1b1" + "r2b1r1b1r1b1e1r3",
        
        "d2b1d1g2d1g1d1g1b1d1g1d1g2d2b1d1b1" + "y2r1b1r2b1e1r1e2",
        "g1b2d1g1d4b2d1g1d1g1d1g1b2d1b1" + "y1b2r1b1r1b1e1r1e1r1",
        "d1b2d1g1d1g3d1b1d1g1d4b2d1b1" + "y2b2r2b1e1r3",
        "d1g1b1d1g1d4b2d1g1d1g1w1d1g1b1d1b1" + "b1y1b1r1b1r1b1e1r1e1y1",
        "d1b2d1g1d1b1d1g2b1d1g1d1g2d1b2d1b1" + "r1y2b1r2b1e1r1e2",
        "d2b1d1g2d4b1d1g1d5b1d1b1" + "r2y1b2r1b1e1r3",     
        "g1b2d1g1d2g1d1b2d1g1d1b1d1g1b2d1b1" + "r1b1y3r1b1e1r1b1r1",
        "d2b2g1d1g1d1g1b2d1g1d4b2d1b1" + "r2b1r1b1r1b1e1r3",
        
        "b4g1d1g2d2b1d1g2d1g1d1g1b1d1b1" + "y2r1b1r2b1e1r1e2",
        "b2d1b1g1d1g1d1g1b2d1g1d4b2d1b1" + "y1b2r1b1r1b1e1r1e1r1",
        "b4g1d4b2d1g1d1g3d1b1d1b1" + "y2b2r2b1e1r3",
        "b1d1b2g1d1g1w1d1g1b1d1g1d4b2d1b1" + "b1y1b1r1b1r1b1e1r1e1y1",
        "g1b1d1b1g1d1g2d1b2d1g1d1b1d1g2b1d1b1" + "r1y2b1r2b1e1r1e2",
        "b1g1d1b1g1d5b1d1g2d4b1d1b1" + "r2y1b2r1b1e1r3",
        "g1d1b2g1d1b1d1g1b2d1g1d2g1d1b2d1b1" + "r1b1y3r1b1e1r1b1r1",
        "g1b2d1g1d1g1b1d2b2g1d1g1d1g1b2d1b1" + "r2b1r1b1r1b1e1r3",
        
        "d2b1d1g2b1g1d1b3g1d1g2d2b1d1b1" + "y2r1b1r2b1e1r1e2",
        "g1b2d1g1b1w1d1b1d1b2g1d1g1d1g1b2d1b1" + "y1b2r1b1r1b1e1r1e1r1",
        "d1b2d3g1d2b3g1d4b2d1b1" + "y2b2r2b1e1r3",
        "d1g1b1d1g1d1b1d1b4g1b1g1w1d1g1b1d1b1" + "b1y1b1r1b1r1b1e1r1e1y1",
        "d1b2d2b7g1d1g2d1b2d1b1" + "r1y2b1r2b1e1r1e2",
        "d2b1d1b2d1b3g1d1g1d5b1d1b1" + "r2y1b2r1b1e1r3",
        "g1b2d1b1d1g1d1b1g1d2b1d1b1d1g1b2d1b1" + "r1b1y3r1b1e1r1b1r1",
        "d1b2d1b8g1d1g1b1d2b3" + "r2b1r1b1r1b1e1r3",
    ]    
)

ninjagaiden_animation = animation_settings(
    sprite_list=[[RyuClimb01, RyuClimb02],
                ],
    bg_sprites=[NinjaGaidenBG01, 
                NinjaGaidenBG02],
    xoffs=[[0, 0],
          ],
    yoffs=[[1, 0],
          ],
    frame_time=0.05,
    spbg_ratio=3,
    center=True,
    bg_scroll_speed=(0, 1),
    cycles_per_char=5,
    reversible=False,
    )
