import sys
sys.path.append("../")
from settings import (NES_PALETTE_HEX, animation_settings)
from core import sprite

RedDragonNorthEast01 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "y":NES_PALETTE_HEX[2, 7],
        "r":NES_PALETTE_HEX[1, 7],
    },
    matrix = [
        "b1x31",
        "b2x30",
        "b1r1b1x29",
        "x1b1r1b2x11b1x15",
        "x1b1y1r2b3x3b1x3b1r1b1x14",
        "x1b1r1y1r1y1r2b4x1b2r2b1x14",
        "x2b1r1y1r1y1r1y1r1b4r1y1r1b1x14",
        "x2b1y1r1y1r1y1r1b1r1b1x1b1r1y1r1b1x14",
        "x2b1r1y1r1y1r1b1r1b1r1b2r2b2x2b1x11",
        "x3b1r1y1r1b1r2b1r1b1r1y1b1x1b1x1b2x11",
        "x3b1r2b1r1y1b1r5b1x1b2r1b2x10",
        "x4b2r1y1r1b1r1b1r3b2r2b2r1b1x9",
        "x4b1r2y1r1b2r1y1r5b1r1b1r2b2x7",
        "x5b1r2b1r1b1r1y1r1b1r2b1r2b1r1y1r2b2x5",
        "x6b1r1b1r2y1r2b1r1b1r1y1r1b1r2y1r1y1r1b2x3",
        "x7b1r3y1r1b1r1b1r2y1r1b1r1y1r1y1r1y1r1y1b3",
        "x8b1r1y1r3b1r2y2r1b1r2y1r1y1r1b3x2",
        "x8b1y1r2b2r6b1r1y1r1b3x5",
        "x7b1r3b1x2b4r2b1r1b2x8",
        "x7b1r2b1x7b4x10",
        "x6b1r2b1x10b1x11",
        "x6b1r1b1x11b1x11",
        "x5b1r1b1x24",
        "x4b1r1b1x25",
        "x3b1r1b1x26",
        "x3b1r1b1x26",
        "x2b1r1b1x27",
        "x3b1x28",
    ]
)

GoldDragonNorthEast01 = RedDragonNorthEast01.swap_palette(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "y":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[2, 8],
    },)

BronzeDragonNorthEast01 = RedDragonNorthEast01.swap_palette(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "y":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[2, 1],
    },)

RedDragonNorthEast02 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "y":NES_PALETTE_HEX[2, 7],
        "r":NES_PALETTE_HEX[1, 7],
    },
    matrix = [
        "x16b1x6",
        "x15b1r1b1x5",
        "x13b2r2b1x5",
        "x11b3r1y1r1b1x5",
        "x13b1r1y1r1b1x5",
        "x12b2r2b2x5",
        "b8x3b2r1y1b1x1b1x5",
        "x1b1r6b4r1y1r1b1x1b1x5",
        "x2b1r1y1b1r1b1r6b1x8",
        "x3b1r2b1r1y1r1b1r1y1r1b2x7",
        "x4b2r1y1r1b1r5b2x6",
        "x5b1r1y1r1b1r1y1r1b1r3b1x5",
        "x6b1r6b1r1y1r1b2x4",
        "x7b1r2y1r1b1r2y1r1b1r1b1x3",
        "x7b1r1y1r4y1r1b1r1b1r1b1x2",
        "x6b1r4b4r1b1r2y1r1b1x1",
        "x6b1r2b2x4b8",
        "x5b1r2b1x14",
        "x5b1r1b1x15",
        "x5b1r1b1x15",
        "x4b1r1b1x16",
        "x3b1r1b1x17",
        "x3b1r1b1x17",
        "x2b1r1b1x18",
        "x1b1r1b1x19",
        "x2b1x20",
    ]
)

GoldDragonNorthEast02 = RedDragonNorthEast02.swap_palette(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "y":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[2, 8],
    },)

BronzeDragonNorthEast02 = RedDragonNorthEast02.swap_palette(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "y":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[2, 1],
    },)

RedDragonNorthEast03 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "y":NES_PALETTE_HEX[2, 7],
        "r":NES_PALETTE_HEX[1, 7],
    },
    matrix = [
        "x15b1x7",
        "x8b1x5b1r1b1x6",
        "x5b4x3b2r2b1x6",
        "x3b2r2b2x2b2r1y1r1b1x6",
        "b3r2b1r1b1r1b1x2b1r1y1r1b1x6",
        "x1b1r2b1r1b1r1y1b1x2b1r2b2x6",
        "x2b2r2b1r1y1r1b2r1y1b1x1b1x6",
        "x2b1r1y1b1r3y1r2y1r1b1x2b1x5",
        "x3b1r1b1y1r1b1r1b1r3b5x4",
        "x3b2r2b1r1b1r1y1r2y1r2b1r1b1x3",
        "x3b2r1b1r2b1r1y1r1b1r1y2b1r1b1x3",
        "x2b1x2b1r1y1r2y1r2b1r3b1r2b1x2",
        "x6b1r3y1r1b1r1b1r2b1r2b1x2",
        "x7b1r1y1r4b1y1b1r1b1r2b1x1",
        "x7b1y1r2b2r1b1r1b1r1b1r2b2",
        "x6b1r3b1x2b1r2b1y1b1r1b1x2",
        "x6b1y1r1b1x4b3r2b1x3",
        "x5b1r2b1x7b3x4",
        "x5b1r1b1x8b1x6",
        "x4b1r1b1x16",
        "x2b2r1b1x17",
        "x1b1r2b1x18",
        "b1r1b2x19",
        "x1b1x21",
    ]
)

GoldDragonNorthEast03 = RedDragonNorthEast03.swap_palette(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "y":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[2, 8],
    },)

BronzeDragonNorthEast03 = RedDragonNorthEast03.swap_palette(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "y":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[2, 1],
    },)

RedDragonNorthEast04 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "y":NES_PALETTE_HEX[2, 7],
        "r":NES_PALETTE_HEX[1, 7],
    },
    matrix = [
        "x4b1x24",
        "x4b2x23",
        "x4b1r1b1x22",
        "x3b1r1y1r1x22",
        "x3b1r2y1r1b1x1b1x18",
        "x3b1r1y1r1y1r1b2x18",
        "x3b1r2y1r1b1r1b1x4b1x13",
        "x2b1r2y1r1b1r1b1x4b1r1b1x12",
        "x2b1r1y1r1b1r1y1b1x2b2r2b1x12",
        "x2b1r2b1r1y1r1b1x1b2r1y1r1b1x12",
        "x2b1r1b1r1y2b1r1b1x1b1r1y1r1b1x12",
        "x1b1r1b1r1y3b1r2b2r2b2x12",
        "x1b2r2y3b1y2r2y1r1b2x1b2x1b1x2b5",
        "x1b1x1b2r1y2b1r2b1r4b2r1b5r3b1x1",
        "x5b1r1y1b1r1b1r1y1r2y1r2b1r2b1r2y1r1y1b1x1",
        "x6b1r1b1r1b1r1y1r1b1r1y1b1r1y1r1b1r1y1r1y1b1x2",
        "x6b1r1b1y1r1y1r2b1r1b1r2y1r1b1r2y1b1x3",
        "x7b2r2y1r1b1r1b1r2y2r1b1r1y1r1b1x3",
        "x8b1r1y1r1y1r1b1r2y3r1b1y1r1b1x4",
        "x7b1r1y1r2b2r4y2r1b1r1b1x5",
        "x6b1r4b1x2b4r1y1r1b1r1b1x5",
        "x6b1r2b2x6b3r1b2x6",
        "x5b1r2b1x11b2x7",
        "x4b1r1b2x13b1x7",
        "x3b1r1b1x23",
        "x2b1r1b1x24",
        "x2b1r1b1x24",
        "x1b1r1b1x25",
        "b1r1b1x26",
        "x1b1x27",
    ]
)

GoldDragonNorthEast04 = RedDragonNorthEast04.swap_palette(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "y":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[2, 8],
    },)

BronzeDragonNorthEast04 = RedDragonNorthEast04.swap_palette(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "y":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[2, 1],
    },)

DragonStrikeBG01 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "g":NES_PALETTE_HEX[1, 9],
        "l":NES_PALETTE_HEX[2, 11],
        "s":NES_PALETTE_HEX[0, 8],
    },
    matrix = [
        "b1g7b1g3b1g15b1g3",
        "g14b1g4b1g10b1g1",
        "g4b1g5b1g13l1g1b1g5",
        "b1g5b1g8b1g8b1g6b1",
        "g2b1g18b1g10",
        "g7b1g4b1g10l1g4b1g3",
        "g16b1g2b1g3b1g8",
        "g4b1g3b2g22",

        "g8b5l1b1g17",
        "g6b1g2b1g1l2b4g1b1g2b1g10",
        "l1g1b1g6b2g1l1b2g1l1b2g5b1g3b1g3",
        "b1g6b1g2b1g1b2l2b4g1b1g8b1g1",
        "g9b5g3l2b4g3b1g5",
        "g5b1g4b3g1b1g1l2g1l1g1l1g1b2g6b1",
        "g3b1g7b1g3l1b1g2l1b1l3b2g6",
        "g10b4g1b1l1g1l1b1g1l2b1g1l1b3g3",

        "b1g7b1g2b2g1b2g1b1g1b1g1l1b2l2b1l1b2g1b1",
        "g10b1g1b5g1b1g1b5g1l3b2g1",
        "g4b1g1l1g7b2g2l1g1l1b1g1b1l1g2l1b1g1b1g1",
        "b1g5b1g6b2g1b2g1l1g2l1g2l1g2b1l1b1g1",
        "g2b1g10b3g1b1g2b1l1g1b2g1l1g2l1b1g1",
        "g7b1g3s3b3g1b3g3b2l1b1g2b2",
        "g9s3b1s1b6g2l1g1b1l1b2l1g1b1g1",
        "g4b1g1s10b3g2l1g1b1l1g1b1g2b2g1",

        "g2s13b2g1b1l1g1b2g1b1g2l1g1b1g2",
        "g5s6b1s2b7g1b2g1l1g2b2g1b1",
        "g4b1g2s2g1s6b4g1b1g1b1g1b2g1b1g3",
        "g6b1g4s3b1s2b2g1b5g1b3g3",
        "b1g1b1g10s3b5g1b2g1b3g4",
        "g7b1g8s1b3g1b1g2b3g5",
        "g11b1g6b1g1b5g4b1g2",
        "g4b1g27",
    ]
)

dragonstrike_animation = animation_settings(
    sprite_list=[[RedDragonNorthEast01,
                  RedDragonNorthEast02,
                  RedDragonNorthEast03,
                  RedDragonNorthEast04],
                 [GoldDragonNorthEast01,
                  GoldDragonNorthEast02,
                  GoldDragonNorthEast03,
                  GoldDragonNorthEast04],
                 [BronzeDragonNorthEast01,
                  BronzeDragonNorthEast02,
                  BronzeDragonNorthEast03,
                  BronzeDragonNorthEast04],
                ],
    bg_sprites=[DragonStrikeBG01],
    xoffs=[[-1, 4, 3, 0],
           [-1, 4, 3, 0],
           [-1, 4, 3, 0],
          ],
    yoffs=[[1, 3, 2, -1],
           [1, 3, 2, -1],
           [1, 3, 2, -1],
          ],
    frame_time=0.050,
    spbg_ratio=3,
    center=True,
    bg_scroll_speed=(1, 1),
    cycles_per_char=5,
    reversible=False,
    )

