import sys
sys.path.append("../")
from settings import (NES_PALETTE_HEX, animation_settings)
from core import sprite

ColScottOConnorWalkRight01 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "d":NES_PALETTE_HEX[0, 6],
        "l":NES_PALETTE_HEX[1, 6],
        "w":NES_PALETTE_HEX[3, 0],
    },
    matrix = [
        "x14b6x2",
        "x11b3d1l5b1x1",
        "x7b4d1l9b1",
        "x4b3d1l13b1",
        "x2b2d1l16b1",
        "x1b1d1l14w1l1w1l1b1",
        "b1d1l1d3l7d3l3w1b1x1",
        "x1b1d1b3d8w2d1l1b3x1",
        "x2b1x3b6d1w4d2b1x2",
        "x11b1d1w3d3b1x2",
        "x10b1d1w3d4b1x2",
        "x10b1d1w2d1w2d2b1x2",
        "x10b1d1w5d1l2b1x1",
        "x11b1d1w4d1l2b1x1",
        "x10b1d4w3d1b1x2",
        "x9b1d4w1d4b1x2",
        "x10b1d2w4d1b1x3",
        "x11b1d1w5d1b1x2",
        "x12b1d1w4d1b1x2",
        "x12b1d2w4b1x2",
        "x11b1d1w6b1x2",
        "x10b1d1w7b1x2",
        "x10b1d1w1d1w4b1x3",
        "x9b1d1l1d1w1d2w2b1x3",
        "x8b1d1l3d1w3b1x4",
        "x8b1d1l3d2b2x5",
        "x9b1d1l3d1b1x6",
        "x10b1d5b1x5",
        "x11b2d1l2b1x5",
        "x13b3x6",
    ]
)

ColScottOConnorWalkRight02 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "d":NES_PALETTE_HEX[0, 6],
        "l":NES_PALETTE_HEX[1, 6],
        "w":NES_PALETTE_HEX[3, 0],
    },
    matrix = [
        "x15b5x5",
        "x13b2d1l4b1x4",
        "x11b2d1l7b1x3",
        "x9b2d1l9b1x3",
        "x7b2d1l11b1x3",
        "x4b3d1l9w1l1w1l1b1x3",
        "x1b3d1l9d3l2w1b1x4",
        "b1d1l10d4w1d2b1x2b2x1",
        "x1b1d4l4d2w1d2w3d1b1x1b1l2b1",
        "x2b4d4w2d3w3d1b3l2b1",
        "x6b2d1w3d3w4b1w2d1l1b1",
        "x8b1d1w1d5w7d1b1",
        "x9b1d6w6d1b1x1",
        "x10b2w2d4w3d1b1x2",
        "x10b1d4w1d4b1x4",
        "x9b1d7b3x5",
        "x9b1d2w2d4b1x6",
        "x7b2d1w5d2w2b1x5",
        "x5b2d2w6d2w2b1x5",
        "x2b3d2w7d2w4b1x4",
        "x1b1d3w1d1w7b1d1w4b1x4",
        "b1d1l2d1w8b2d1w5b1x3",
        "b1d1l2d1w1d1w5b1x1b1d1w5b1x3",
        "b1d1l2b1w1d1w4b1x3b1d1w3d1b1x3",
        "b1d1l1b3w1d1w1b2x4b1d4w1b1x3",
        "x1b2x3b3x6b1d1w3b1x4",
        "x16b1d3b1x4",
        "x17b1d1l2b1x3",
        "x17b1d1l3b1x2",
        "x17b6x2",
    ]
)

ColScottOConnorWalkRight03 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "d":NES_PALETTE_HEX[0, 6],
        "l":NES_PALETTE_HEX[1, 6],
        "w":NES_PALETTE_HEX[3, 0],
    },
    matrix = [
        "x14b5x2",
        "x12b2d1l4b1x1",
        "x10b2d1l7b1",
        "x9b1d1l9b1",
        "x8b1d1l10b1",
        "x7b1d1l7w1l1w1l1b1",
        "x1b2x2b2d1l6d2l2w1b1x1",
        "b1d1l1b2d1l6d1w2d1l1b3x1",
        "x1b1d1l8d1w4d2b1x2",
        "x2b1d2l4d3w3d3b1x2",
        "x3b2d4b1d1w3d4b1x2",
        "x5b5d1w2d1w3b2x2",
        "x9b1d2w5l2b1x1",
        "x10b1w1d1w4l2b1x1",
        "x9b1d7b2x2",
        "x9b1d2w3d2b1x3",
        "x8b1d2w5b1x4",
        "x9b1d1w6b1x3",
        "x10b1d1w5b1x3",
        "x10b1d1w6b1x2",
        "x10b1d2w5b1x2",
        "x9b1d3w5b1x2",
        "x8b1d3w6b1x2",
        "x8b1d2w1d1w4b1x3",
        "x8b1d3w2d2w1b1x3",
        "x9b1d3w3b1x4",
        "x9b1d2l1d2b1x5",
        "x9b1d1l3b1x6",
        "x10b1l4b1x5",
        "x11b4x6",
    ]
)

ColScottOConnorWalkRight04 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "d":NES_PALETTE_HEX[0, 6],
        "l":NES_PALETTE_HEX[1, 6],
        "w":NES_PALETTE_HEX[3, 0],
    },
    matrix = [
        "x16b4x5",
        "x13b3l4b1x4",
        "x11b2d1l7b1x3",
        "x8b3d1l9b1x3",
        "x6b2d1l12b1x3",
        "x4b2d1l10w1l1w1l1b1x3",
        "x1b3d1l9d3l2w1b1x4",
        "b1d1l10d2w2d1l1b3x4",
        "x1b1d5l3d2w5d2b1x2b2x1",
        "x2b5d3b1d1w4d3b1x1b1l2b1",
        "x7b4w2d6b2d1l2b1",
        "x9b1d1w1d1w3d2b1d2w1d2b1",
        "x9b1d1w5l2d1w5b1",
        "x9b1d2w4l2d2w3b1x1",
        "x10b1d3w2d4w1d2b1x1",
        "x9b1d6w1d4b2x2",
        "x9b1d3w5b3x4",
        "x7b2d1w1d2w6b1x5",
        "x5b2d2w3d2w6b1x4",
        "x4b1d2w6d1w6b1x4",
        "x3b1d1w8d1w7b1x3",
        "x2b1d2w7b2d1w6b1x3",
        "x1b1d1l2d1w5b1x1b1d1w7b1x2",
        "x1b1d1l2b1w4b1x2b1d1w6d1b1x2",
        "x1b1d1l1b1x1b4x4b1d1w3d2w1b1x2",
        "x2b2x10b1d1w1d2w2b2x2",
        "x15b1d1w3d1l1b1x2",
        "x16b1d3l3b1x1",
        "x17b2d1l4b1",
        "x18b1d4b1x1",
        "x19b4x2",
    ]
)

KabukiQuantumFighterBG01 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "p":NES_PALETTE_HEX[0, 4],
        "o":NES_PALETTE_HEX[1, 7],
        "l":NES_PALETTE_HEX[2, 7],
        "g":NES_PALETTE_HEX[3, 11],
    },
    matrix = [
        "b16" + "b4p1o1l1o3b1p1b2p1b1",
        "b4p1b3p1b3p1b1p1b1" + "b1o1b2p1l1o3p1o1p1b4",
        "b2p1b13" + "b1o1b1p1o1l1o5p2b1p1b1",
        "b16" + "b1p1b1p1o2b1o2b1o2b4",
        "b5p1b5l1b4" + "b1p1b1p2b2o1p1b2p2b3",
        "b1p1b5p1b5p1b2" + "b1o1b1p1o1b2l1o1b2o1p1b1p1b1",
        "b5p1b5p1b4" + "b1o1b1o1p1b2l1o1b2o2b3",
        "b2o1b2p1b2p1b2p1b2p1b1" + "b5o1l1b2o2b3p1b1",
        "p1b1l1b5p1b5p1b1" + "b1o1b4o1b2o1b6",
        "b2o1b1p3b1p1b1o1l1o1b1p1b1" + "b1p1b2o1b2l1o1b2o1b2p1b1",
        "b16" + "b5o1b4o1b5",
        "b1p2o1p1b1p4b1p1l1p2b1" + "b1o1b1o1b1o1b4o1b3p1b1",
        "b16" + "b1p1b1l1b2o1b2o1b2p1b1p1b1",
        "b1p4b1p2o1p1b1p4b1" + "b1p1b1o2b2l1o1b2p2b3",
        "b16" + "b1p1b1l1o1b1l1o3b1o1p1b1p1b1",
        "b1l1p3b1p4b1p2o1p1b1" + "b1p1b1o2b1o1l1o1p1b1p1o1b3",

        "b16" + "b3o2b1o3p1b1o1p1b1p1b1",
        "b2p1b1o1l1o1b1p1b1p3b1p1b1" + "b1o1b1l1o1b1l1o3b1p1b2p1b1",
        "p1b1p1b5p1b5p1b1" + "b1o1b1o2b1o3p1b1p2b1p1b1",
        "b2p1b2p1b2p1b2o1b2p1b1" + "b1p1b1o2b1l1o3b1p2b3",
        "b5p1b5o1b4" + "b1p1b1o2b1o1l1o2b1o1p1b1p1b1",
        "b1p3b3p1o1p1b3p3" + "b1o1b1l1o1b1l1o2p1b1p1b2p1b1",
        "b5p1b5p1b4" + "b1p1b1o2b1l2o1p1b1o1p1b3",
        "b2o1b2p1b2p1b2p1b2p1b1" +"b4o1b1o1p1l1o1b1p1o1b1p1b1",
        "p1b1l1b5p1b5p1b1" + "b3p1b2p4b1p2b3",
        "b2o1b1p3b1p1b1o1l1o1b1p1b1" + "b1p1b2p1b2o1b1p1b1p1b2p1b1",
        "b16" + "b3p1b2p1b1p1b3p1b1p1b1",
        "b1p2o1p1b1p4b1p1l1p2b1" + "b1p1b1p1b12",
        "b16" + "b7p1b4p1b3",
        "b1p4b1p2o1p1b1p4b1" + "b16",
        "b16" + "b16",
        "b1g15" + "b1g15",
    ]
)

KabukiQuantumFighterBG02 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "r":NES_PALETTE_HEX[2, 8],
        "l":NES_PALETTE_HEX[2, 9],
        "g":NES_PALETTE_HEX[1, 11],
    },
    matrix = [
        "b1g1b4g4b6" + "b16",
        "b1g1b1g1l1b1g2b1g1b2g1b3" + "b16",
        "b3g2b6g1b4" + "b16",
        "b1g1b1g1l1b1g2b1g1b1g2b1g1b1" + "b16",
        "b1g1b4l1g2b7" + "b16",
        "b1g1b1g1l1b1g2b1g1b2g1b1g1b1" + "b16",
        "b3g2b6g1b4" + "b16",

        "b1g1b1g1l1b1l1g2b2g1b2g1b1" + "b16",
        "b1g1b4g4b6" + "b16",
        "b1g1b1g1l1b1g2b1g1b2g1b3" + "b8g8",
        "b3g2b6g1b4" + "b8g1l1g1l2g2l1",
        "b1g1b1g1l1b1g2b1g1b1g2b1g1b1" + "b8g2b1g3b1g1",
        "b1g1b4l1g2b7" + "b8g1b1g2b2g2",
        "b1g1b1g1l1b1g2b1g1b2g1b1g1b1" + "b16",
        "b3g2b6g1b4" + "b16",

        "b1g1b1g1l1b1l1g2b2g1b2g1b1" + "b16",
        "b1g1b4g4b6" + "b16",
        "b1g1b1g1l1b1g2b1g1b2g1b3" + "b16",
        "b3g2b6g1b4" + "b16",
        "b1g1b1g1l1b1g2b1g1b1g2b1g1b1" + "b16",
        "b1g1b4l1g2b7" + "b16",
        "b1g1b1g1l1b1g2b1g1b2g1b1g1b1" + "b16",
        "b3g2b6g1b4" + "b16",

        "b1g1b1g1l1b1l1g2b2g1b2g1b1" + "b16",
        "b1g1b4g4b6" + "b16",
        "b1g1b1g1l1b1g2b1g1b2g1b3" + "b8g8",
        "b3g2b6g1b4" + "b8g1l1g1l2g2l1",
        "b1g1b1g1l1b1g2b1g1b1g2b1g1b1" + "b8g2b1g3b1g1",
        "b1g1b4l1g2b7" + "b8g1b1g2b2g2",
        "b1g1b1g1l1b1g2b1g1b2g1b1g1b1" + "b16",
        "b3g2b6g1b4" + "b16",
        "r16" + "r16",
    ]
)

kabukiquantumfighter_animation = animation_settings(
    sprite_list=[[ColScottOConnorWalkRight01,
                  ColScottOConnorWalkRight02,
                  ColScottOConnorWalkRight03,
                  ColScottOConnorWalkRight04],
                ],
    bg_sprites=[KabukiQuantumFighterBG01,
                KabukiQuantumFighterBG02,],
    xoffs=[[0, -1, 0, -1],
          ],
    yoffs=[[0, -1, 0, 0],
          ],
    frame_time=0.030,
    spbg_ratio=5,
    center=True,
    bg_scroll_speed=(1, 0),
    cycles_per_char=5,
    reversible="horizontal",
    )

