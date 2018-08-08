import sys
sys.path.append("../")
from settings import (NES_PALETTE_HEX, animation_settings)
from core import sprite

FF1WarriorFieldSouth01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "r":NES_PALETTE_HEX[1, 7],
        "s":NES_PALETTE_HEX[3, 7],
    },
    matrix = [
        "x5b6x5",
        "x4b1r6b1x4",
        "x3b1r8b1x3",
        "x3b1r7b1r1x3",
        "x3b1r1s1r6b1x3",
        "x3b1r1s2r1s1r4x3",
        "x3b1r1b2s1b3r1b1x3",
        "x2b3s1b1s2b1s1r1b2x2",
        "x1b1r2b2s4b2r2b1x1",
        "x2b2r2b4r1s2b1x2",
        "x1b1s2r3b2r2s2b1x2",
        "x1b1s2b1r5b3x3",
        "x2b3s3r1s2b2x3",
        "x4b1r3b1r2b2x3",
        "x4b1r3b4x4",
        "x5b1r2b5x3"
    ]    
)

FF1WarriorFieldSouth02 = FF1WarriorFieldSouth01.hflip(rows=range(8, 16))

FF1BlackMageFieldSouth01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "l":NES_PALETTE_HEX[1, 2],
        "y":NES_PALETTE_HEX[2, 8],
        "s":NES_PALETTE_HEX[3, 7],
    },
    matrix = [
        "x7b2x7",
        "x6b1y2b1x6",
        "x4b3y2b3x4",
        "x2b2y2b1y2b1y2b2x2",
        "x1b1y3b1y4b1y3b1x1",
        "x1b1y12b1x1",
        "x2b1y10b1x2",
        "x2b3y6b3x2",
        "x1b1l2b2s1b2s1b2l2b1x1",
        "b2l3b6l4b1",
        "b1l1b1s2l1b4l5b1",
        "b1l1b1s2b2l3s2l3b1",
        "b1l1b2l1b1l1b3s2l3b1",
        "x1b1l1b1l1b1l5b1l3b1",
        "x2b1l1b4l3b1l3b1",
        "x2b3s3b5l1b1x1"
    ]    
)

FF1BlackMageFieldSouth02 = FF1BlackMageFieldSouth01.hflip()

FF1WhiteMageFieldSouth01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[3, 0],
        "s":NES_PALETTE_HEX[3, 7],
    },
    matrix = [
        "x6b1w2b1x6",
        "x5b1w4b1x5",
        "x4b1w6b1x4",
        "x4b1w6b1x4",
        "x3b1w2b4w2b1x3",
        "x3b1w1b1s4b1w1b1x3",
        "x2b1w2b2s2b2w2b1x2",
        "x2b2w1s1b1s2b1s1w1b2x2",
        "x2b1w1b1w1s4w1b1w2b1x1",
        "x1b1w1s2b1w4b1w4b1",
        "b1w2s2w1b4w1b1w1s1w1b1",
        "b1w2b2w1b1w3b1w1s2w1b1",
        "b1w2b2w1b1w2b2w1b2w1b1",
        "b2w1b2w1b3w2b1w1b1w1b1",
        "b2w1b1w1b1s1w4b1w1b1w1b1",
        "x1b1w1b5s3b1w1b1x2"
    ]    
)

FF1WhiteMageFieldSouth02 = FF1WhiteMageFieldSouth01.hflip()

FF1MonkFieldSouth01 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "y":NES_PALETTE_HEX[2, 8],
        "l":NES_PALETTE_HEX[1, 2],
        "s":NES_PALETTE_HEX[3, 7],
    },
    matrix = [
        "x5b6x5",
        "x4b1y6b1x4",
        "x3b1y8b1x3",
        "x3b1y8b1x3",
        "x3b1y8b1x3",
        "x3b1y3s2y3b1x3",
        "x3b1y1b2s1b3y1b1x3",
        "x2b3s1b1s2b1s1y1b2x2",
        "x1b2s1l1b1s4b1s3b1x1",
        "x1b1s2l1s1b4s1l1s3b1",
        "x1b1s1b1l2s4l2s3b1",
        "x3b1l8b1s2b1",
        "x3b1l5b6x1",
        "x3b1l4b1l3b1x3",
        "x3b1l4b5x3",
        "x4b1l3b6x2"
        
    ]    
)

FF1MonkFieldSouth02 = FF1MonkFieldSouth01.hflip(rows=range(8, 16))

FinalFantasyBG01 = sprite(
    palette = {
        "r":NES_PALETTE_HEX[1, 10],
        "n":NES_PALETTE_HEX[1, 8],
        "b":NES_PALETTE_HEX[0, 13],
        "g":NES_PALETTE_HEX[0, 0],
        "h":NES_PALETTE_HEX[1, 0],
        "l":NES_PALETTE_HEX[3, 1],
        "w":NES_PALETTE_HEX[3, 0],
        "y":NES_PALETTE_HEX[2, 8],
    },
    matrix = [
        "r8" + "b1h5b1h1b2h5b1" + "b8",
        "r8" + "h1g6b2g2b2g2h1" + "w8",
        "n1r7" + "h1g6b1g1b1g3b1g1h1" + "g8",
        "r8" + "b16" + "g1b2g3b2",
        "r8" + "h2b2h2b1h5b2h2" + "b8",
        "r5n2r1" + "g3b1h1g6h1b1g3" + "g8",
        "r8" + "b1g2b2g2b1g3b2g3" + "g8",
        "r8" + "b16" + "g8",
        "r8" + "b1h6b3h4b1h1" + "g8",
        "r8" + "b1g6h1b1h1g5b1" + "g8",
        "n1r7" + "b2g4b1g1b1h1g5b1" + "g8",
        "r8" + "b16" + "w8",
        "r8" + "h4b2h5b1h2b1g1" + "g1b2g3b2",
        "r5n2r1" +"g3h1b1g6b1h1g2b1" + "g8",
        "r8" + "g3b2g3b1g2b2g2b1" + "g4b4",
        "r8" + "b16" + "g3b5",
        
        "b1r1b2r4" + "b1h5b1h1b2h5b1" + "l1w1l6",
        "r4b2r2" + "h1g6b2g2b2g2h1" + "l8",
        "r6b1r1" + "h1g6b1g1b1g3b1g1h1" + "l6w2",
        "r6b1r1" + "b16" + "l8",
        "r5b1r1b1" + "h2b2h2b1h5b2h2" + "l1w2l5",
        "r6b2" + "g3b1h1g6h1b1g3" + "l8",
        "r6b2" + "b1g2b2g2b1g3b2g3" + "l1w1l6",
        "r5b3" + "b16" + "l8",
        "r5b3" + "b1h6b3h4b1h1" + "l1w1l6",
        "r2b1r1b4" + "b1g6h1b1h1g5b1" + "l8",
        "r1b6r1" + "b2g4b1g1b1h1g5b1" + "l6w2",
        "b5r3" + "b16" + "l8",
        "b5r3" + "h4b2h5b1h2b1g1" + "l1w2l5",
        "n2b6" +"g3h1b1g6b1h1g2b1" + "l8",
        "n2b6" + "g3b2g3b1g2b2g2b1" + "l1w1l6",
        "b6r2" + "b16" + "l8",
    ]    
)

FinalFantasyBG02 = sprite(
    palette = { 
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[3, 0],
        "g":NES_PALETTE_HEX[0, 0],
        "l":NES_PALETTE_HEX[0, 1],
    },
    matrix = [
        "b8" + "b16" +                                    "b8",
        "w5b1w2" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" +         "b1w7",
        "g5b1w1g1" + "b1g1b1g1b1g1b1g1b1g1b1g1b1g1b1g1" + "b1w1g6",
        "g5b1w1g1" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" +       "b1w1g6",
        "g5b1w1g1" + "b1g1b1g1b1g1b1g1b1g1b1g1b1g1b1g1" + "b1w1g6",
        "g5b1w1g1" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" +       "b1w1g6",
        "g5b1w1g1" + "b1g1b1g1b1g1b1g1b1g1b1g1b1g1b1g1" + "b1w1g6",
        "g5b1w1g1" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" +       "b1w1g6",
        "b6w1g1" + "b16" +                                "b1w1g6",
        "b1w6g1" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" +         "b1w1g6",
        "b1w6g1" + "b1g1b1g1b1g1b1g1b1g1b1g1b1g1b1g1" +   "b1w1g6",
        "b1w1g6" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" +         "b1w1g6",
        "b1w1g6" + "b1g1b1g1b1g1b1g1b1g1b1g1b1g1b1g1" +   "b1w1g6",
        "b1w1g6" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" +         "b1w1g6",
        "b1w1g6" + "b1g1b1g1b1g1b1g1b1g1b1g1b1g1b1g1" +   "b1w1g6",
        "b8" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" +             "b8",
        
        "b8" + "b16" + "b8",
        "b8" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" + "b3l1b4",
        "b8" + "b1g1b1g1b1g1b1g1b1g1b1g1b1g1b1g1" + "b8",
        "b8" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" + "b8",
        "b8" + "b1g1b1g1b1g1b1g1b1g1b1g1b1g1b1g1" + "b8",
        "b8" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" + "b8",
        "b8" + "b1g1b1g1b1g1b1g1b1g1b1g1b1g1b1g1" + "b8",
        "b8" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" + "b8",
        "b8" + "b16" + "b8",
        "b8" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" + "b8",
        "b8" + "b1g1b1g1b1g1b1g1b1g1b1g1b1g1b1g1" + "b5l1b2",
        "b6l1b1" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" + "b8",
        "b8" + "b1g1b1g1b1g1b1g1b1g1b1g1b1g1b1g1" + "b8",
        "b2l1b5" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" + "b8",
        "b8" + "b1g1b1g1b1g1b1g1b1g1b1g1b1g1b1g1" + "b8",
        "b8" + "b2g1b1g1b1g1b3g1b1g1b1g1b1" + "b8",
    ]    
)

finalfantasy_animation = animation_settings(
    sprite_list=[[FF1WarriorFieldSouth01,
                  FF1WarriorFieldSouth02],
                 [FF1BlackMageFieldSouth01,
                  FF1BlackMageFieldSouth02],
                 [FF1MonkFieldSouth01, 
                  FF1MonkFieldSouth02],
                 [FF1WhiteMageFieldSouth01,
                  FF1WhiteMageFieldSouth02],
                ],
    bg_sprites=[FinalFantasyBG01],
    xoffs=[[0, 0],
           [0, 0],
           [0, 0],
           [0, 0]], 
    yoffs=[[0, 0],
           [0, 0],
           [0, 0],
           [0, 0]],
    frame_time=0.055,
    spbg_ratio=4,
    center=True,
    bg_scroll_speed=(0, -1),
    cycles_per_char=5,
    reversible=False,
    )

