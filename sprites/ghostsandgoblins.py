import sys
sys.path.append("../")
from settings import (NES_PALETTE_HEX, animation_settings)
from core import sprite

ArthurArmoredRunRight01 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 6],
        "o":NES_PALETTE_HEX[1, 8],
        "s":NES_PALETTE_HEX[3, 13],
    },
    matrix = [
        "x7b2w1b1x5",
        "x5b1w1b1w3b1x4",
        "x4b1w1b1w5x4",
        "x4w1b1w6x4",
        "x4w3b3w1b1x4",
        "x4w1b2s1b1s2b1x4",
        "x4b1w1o1s4b1x4",
        "x4b3o4b1x4",
        "x1b1w3b1w1b2o3x4",
        "b1w4b1w2b2o2x4",
        "b3w1b2w4b1w1b1x3",
        "b1w2b2w5b1w1b1x3",
        "b1w2b3w3b2w1b1x3",
        "b3w1b6r1b1x4",
        "x1w3b1r7b1w1x2",
        "x1b1w3b1w4r1w1b2x2",
        "x2b1w2b3w4b1x3",
        "x3b3w1b2w2b2x3",
        "x4b2w2b4w1b1x2",
        "x3b1w2b2x2b3x3",
        "x2b2w4x2b1w2b1x2",
        "x2b1w4b1x2b1w2b1x2",
        "x2b1w3b3x1b1w3b1x1",
        "x3b1w4b1x1b1w4b1",
    ]
)

ArthurArmoredRunRight02 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 6],
        "o":NES_PALETTE_HEX[1, 8],
        "s":NES_PALETTE_HEX[3, 13],
    },
    matrix = [
        "x7b2w1b1x5",
        "x5b1w1b1w3b1x4",
        "x4b1w1b1w5x4",
        "x4w1b1w6x4",
        "x4w3b3w1b1x4",
        "x4w1b2s1b1s2b1x4",
        "x4b1w1b1o4b1x4",
        "x4b3b1o3b1x4",
        "x2w3b1w1b2o3b1x1w2",
        "x1w1b1w2b1w2b2b2b1x1b1w1",
        "w3b1w1b1w3b2w1b2w2",
        "w1b4w5b1w1b1w3",
        "b1w1b4w3b2w1b2w1b1",
        "w3b9x2b1x1",
        "b1w4b1r5b1x4",
        "x1b1w2b2w3b3x4",
        "x2b5w1b1w2x5",
        "x4b1w1b3w2x5",
        "x4b1w2b1w2b2x4",
        "x4w1b1x1b1w4x4",
        "x7b1w2b2x4",
        "x8b2x6",
    ]
)

ArthurArmoredRunRight03 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 6],
        "o":NES_PALETTE_HEX[1, 8],
        "s":NES_PALETTE_HEX[3, 13],
    },
    matrix = [
        "x7b2w1b1x5",
        "x5b1w1b1w3b1x4",
        "x4b1w1b1w5x4",
        "x4w1b1w6x4",
        "x4w3b3w1b1x4",
        "x4w1b2s1b1s2b1x4",
        "x4b1w1b1o4b1x4",
        "x4b3b1o3b1x4",
        "x3b1w2b2b1o3x4",
        "x3w4b5x4",
        "x3b6w1b1w1x4",
        "x3b1w2b2w4x4",
        "x3b1w2b1w3b1w1b1x3",
        "x4b1w1b1w2b3x4",
        "x5b4r3b2x2",
        "x2b2x1b1w6b1w1b1x1",
        "x1b1w2b1x1b4w1b2w2b1",
        "x1b1w2b2w3b4w2b1",
        "b1w4b2w1b1x2b1w2b1x1",
        "b1w5b2x3b1w4",
        "b1w1b4x5b1w2b2"
    ]
)

ArthurNakedRunRight01 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 6],
        "o":NES_PALETTE_HEX[1, 8],
        "s":NES_PALETTE_HEX[3, 13],
    },
    matrix = [
        "x6o5x5",
        "x5o7x4",
        "x4o2s1b3s1o1x4",
        "x4o2s2b1s2x5",
        "x5s1o1s4x5",
        "x2o2x2b1o4x5",
        "x1o1s5b1o4x2s2",
        "o1s7o4s1o1s2",
        "s2x3s4o1s5x1",
        "s2o1x2o1s6o1s2x1",
        "x1s2o1x1o1s3o1s1o1x4",
        "x2s2x1o1s2o1s1o1x5",
        "x5r6x5",
        "x6s3r1x6",
        "x5s1o1s3x6",
        "x4s3o1s2x6",
        "x4s1x3s2x6",
        "x8s3o1x4",
        "x8o2x6",
    ]
)

ArthurNakedRunRight02 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 6],
        "o":NES_PALETTE_HEX[1, 8],
        "s":NES_PALETTE_HEX[3, 13],
    },
    matrix = [
        "x5o5x4",
        "x4o7x3",
        "x3o2s1b3s1o1x3",
        "x3o2s2b1s2x4",
        "x4s1o1s4x4",
        "x5b1o4x4",
        "x2s3o1b1o4x3",
        "x1s6b1o3x3",
        "x1s2x1o1s4o2x3",
        "s2x2o1s4o1s1x3",
        "s2x3s4o1s1x3",
        "x1s1o1x2o2s1o1s1o1x3",
        "x1s2o1x1s5x4",
        "x2o1s2r6x3",
        "x5r6x3",
        "x5o1s1o1r2o1x3",
        "x5s2x3s1o1x2",
        "x4o1s1o1x4s1x2",
        "x3o1s2x4o1s1x2",
        "x2s3x5s2x2",
        "x2o1s1o1x5s2o1x1",
        "x3s2o1x4o1s2o1",

    ]
)

ArthurNakedRunRight03 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 6],
        "o":NES_PALETTE_HEX[1, 8],
        "s":NES_PALETTE_HEX[3, 13],
    },
    matrix = [
        "x6o5x5",
        "x5o7x4",
        "x4o2s1b3s1o1x4",
        "x4o2s2b1s2x5",
        "x5s1o1s4x5",
        "x6b1o4x5",
        "x4o1s1b2o4x4",
        "x4s2o1b1o2s2x4",
        "x4o1s2b2o1s2x4",
        "x5s3o1s2x5",
        "x5o1s4b1o1x4",
        "x6o1s1o1b1o1x5",
        "x5r6x5",
        "x1s1o1x3r5s2x3",
        "x1s2o1x2s2r2s4x2",
        "s8x4o1s1x2",
        "s1x3s2o1x5s4",
        "x12s2x2",
    ]
)

GhostsAndGoblinsBG01 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "g":NES_PALETTE_HEX[2, 9],
        "d":NES_PALETTE_HEX[1, 9],
        "r":NES_PALETTE_HEX[1, 8],
        "y":NES_PALETTE_HEX[0, 0],
        "a":NES_PALETTE_HEX[1, 0],
    },
    matrix = [
        "b32",
        "b32",
        "b32",
        "b32",
        "b32",
        "b32",
        "b32",
        "b32",
        "b32",
        "b32",
        "b32",
        "b32",
        "b32",
        "b1y1b11y1b2" + "b16",
        "b1a1b1y1b2y1b4y1b1a1b2" + "b7a4y1b4",
        "b1a1b1a1b2a1b1y1b2a1b1a1b2" + "b5a7y1b3",
        "b1a1b1a1b2a1b1a1b2a1b1a3" + "b4a9y1b2",
        "a4b2a1b1a1b2a3y2" + "b3a11y1b1",
        "y4a2b1a4y3b1a1" + "b3a11y1b1",
        "a1y1a1y8b1a2b1a1" + "b2a2b5a6y1",
        "a1y1a1y1b1a1y1b1y1a1y1b1a1y1b1a1" + "b2a2b1y4b4a2y1",
        "a1y1a1y1b1a1y1b1y1a1y1b1a1y1b1a1" + "b2a1b1y2b1y6a2y1",
        "a1y1a1y1d1a1y1b1d1a1y1b1a1y1b1a1" + "b1a2b1y1b1y2b2y1b1y1a2y1",
        "a1y1d1y1d1a1y1d1b1a1d1b1y1d1b1d1" + "b1a2b1y3b1y2b2a3y1",
        "a1d2y1d2y1d1b1d2b1d1b2d1" + "b1a6y5a2y1b1",
        "d1b1d6b1d4b1d1b1" + "b1a13y1b1",
        "d1b2d5b1d4b1d1b1" + "a13y1b2",
        "d2b1d1b1d2b1d3b2d3" + "a13y1b2",

        "b3g1b1g1b3r1g1b1g1b1g1b1" + "b3g1b1g1b3r1g1b1g1b1g1b1",
        "b2r1g1b1g1d1b1g1r1g1r1g1d1r1g1" + "b2r1g1b1g1d1b1g1r1g1r1g1d1r1g1",
        "b1r1g1d1g2d1b1g1d1g1r1d1r2b1" + "b1r1g1d1g2d1b1g1d1g1r1d1r2b1",
        "r1g2r1d1g2b1d1g1r1d1g2r1d1" + "r1g2r1d1g2b1d1g1r1d1g2r1d1",
    ]
)


GhostsAndGoblinsBG02 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "u":NES_PALETTE_HEX[0, 2],
        "l":NES_PALETTE_HEX[2, 1],
    },
    matrix = [
        "u4b2l2u2b1l3b2" + "u4b2l2u2b1l3b2",
        "b6u3b1l1u3l2" + "b6u3b1l1u3l2",
        "b2l4b1u2b1u6" + "b2l4b1u2b1u6",
        "b1l1u5b3u6" + "b1l1u5b3u6",
        "b1l1u6b6u2" + "b1l1u6b6u2",
        "b1u6b2l5b2" + "b1u6b2l5b2",
        "b2u4b2l1u5l1b1" + "b2u4b2l1u5l1b1",
        "b8l1u5b1l1" + "b8l1u5b1l1",
        "b1l4u1b1l1u6b1u1" + "b1l4u1b1l1u6b1u1",
        "l1u5b1l1u6b1u1" + "l1u5b1l1u6b1u1",
        "u6b1l1u5b3" + "u6b1l1u5b3",
        "b1u5b7l3" + "b1u5b7l3",
        "b9l4u2l1" + "b9l4u2l1",
        "b1l6u1b1l1u6" + "b1l6u1b1l1u6",
        "l1u7b3u4b1" + "l1u7b3u4b1",
        "l1u4b3l2b6" + "l1u4b3l2b6",
        "u4b2l2u2b1l3b2" + "u4b2l2u2b1l3b2",
        "b6u3b1l1u3l2" + "b6u3b1l1u3l2",
        "b2l4b1u2b1u6" + "b2l4b1u2b1u6",
        "b1l1u5b3u6" + "b1l1u5b3u6",
        "u6b1u2b2u5" + "u6b1u2b2u5",
        "u2b1u3b2u2b1u5" + "u2b1u3b2u2b1u5",
        "b1u1b2u3b1u2b1u5" + "b1u1b2u3b1u2b1u5",
        "b4u1b1u1b1u3b1u2b1u1" + "b4u1b1u1b1u3b1u2b1u1",
        "b2u1b5u1b4u1b1u1" + "b2u1b5u1b4u1b1u1",
        "u1b8u1b6" + "u1b8u1b6",
        "b5u1b6u1b2u1" + "b5u1b6u1b2u1",
        "b16" + "b16",
        "u2b6u3b3u2" + "u2b6u3b3u2",
        "l3b1u3b1l3u1b1u1l2" + "l3b1u3b1l3u1b1u1l2",
        "l16" + "l16",
        "u4l3b1l4u4" + "u4l3b1l4u4",
    ]
)

GhostsAndGoblinsBG03 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[3, 0],
        "g":NES_PALETTE_HEX[1, 0],
        "o":NES_PALETTE_HEX[2, 7],
        "d":NES_PALETTE_HEX[0, 7],
        "l":NES_PALETTE_HEX[3, 7],
    },
    matrix = [
        "d2l1d1b7l2b3" + "b4l2b1d9",
        "d1l2d1b7l2b3" + "b4l1d1b1o1l4d1l3",
        "d1l2d1b7l2b3" + "b4l2b1o5d1o3",
        "d1l1d2b7l1d1b3" + "b4l2b1o5d1o3",
        "d1l2d1b7d1l1b3" + "b4l2b1d9",
        "d1l8d2l5" + "d1l3d1l1b1o1d1l7",
        "d1l2o6l1d1l1d1o3" + "o4l2b1o1d1o7",
        "d1l2d1b7l2b3" + "b4l2b1o1d1o7",
        "d1l2d1b7l2b3" + "b4d1l1b1d9",
        "d1l2d1b7d1l1b3" + "b4o1d1b1o1l4d1l3",
        "d1l2d1b7l2b3" + "b4o1d1b1o5d1o3",
        "d1l2d1b7l1d1b3" + "b4o1l1b1o5d1o3",
        "d1l2d1b7l1d1b3" + "b4o1l1b1d9",
        "d1o2d1b7l2b3" + "b4d1o1l1o1d1l7",

        "l5d1l5d1l4" + "d2l1d1l3o1d1o7",
        "l2o3d1l1o4d1l1o3" + "o1d2l1o3b1d1o7",
        "l1o4d1o5d1o4" + "o1d1l1o4b1d8",
        "b1d15" + "d7b1l4d1l3",
        "o2b14" + "b8o4d1o3",
        "o3b13" + "b8o4d1o3",
        "d16" + "d16",
        "d1l7d1l7" + "d1l7d1l7",
        "d1o7d1o7" + "d1o7d1o7",
        "d1o7d1o7" + "d1o7d1o7",
        "d16" + "d16",
        "l4d1l7d1l3" + "l4d1l7d1l3",
        "o4d1o7d1o3" + "o4d1o7d1o3",
        "o4d1o7d1o3" + "o4d1o7d1o3",

        "b1w7b1w7" + "b1w7b1w7",
        "b1w1g6b1w1g6" + "b1w1g6b1w1g6",
        "b1w1g6b1w1g6" + "b1w1g6b1w1g6",
        "b16" + "b16",
    ]
)


bg_null = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
    },
    matrix = ["b32"] *32
)

RedArremerFlightLeft01 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 6],
    },
    matrix = [
        "x11r2b1x10",
        "x7w1x2r4b1x1w1x7",
        "x6w2x2r4b1x1w2x6",
        "x6w2b1r6b1w2x6",
        "x6w2b2r2b2r1b1w2x6",
        "x6w2b2r1b2r2b1w2x6",
        "x3b6r7b5x3",
        "x2b1r5b1r3b2r7b1x2",
        "x1b1r6b5r1b1r7b1x1",
        "x1r3b2r3b1r3b1r4b2r3x1",
        "x1r2b4r2b4r2b1r1b4r2x1",
        "b1r3b1x2b1r8b1x2b1r3b1",
        "x1b1r1x4b1r8b1x4r1b1x1",
        "x7b1r8b1x7",
        "x8r8x8",
        "x8b1r6b1x8",
        "x6r12x6",
        "x1r2x1b1r14b1x1r2x1",
        "x1b1r5b10r5b1x1",
        "x2b1r3b1x10b1r3b1x2",
        "x3b1r1b1x12b1r1b1x3",
        "x4b1x14b1x4",
    ]
)
RedArremerFlightRight01 = RedArremerFlightLeft01.hflip()

RedArremerFlightLeft02 = sprite(
    palette = {
        "b":NES_PALETTE_HEX[0, 13],
        "w":NES_PALETTE_HEX[3, 0],
        "r":NES_PALETTE_HEX[0, 6],
    },
    matrix = [
        "x11r2b1x10",
        "x10r4b1x9",
        "x10r4b1x9",
        "x5w2x1b1r6b1x1w2x5",
        "x3w5b2r2b2r1b1w5x3",
        "x2w6b2r1b2r2b1w6x2",
        "x2w6b1r7w6x2",
        "x1w5b3r3b2r2b2w5x1",
        "b1w3b2r2b5r1b1r3b2w3b1",
        "w3b1r5b1r3b1r6b1w3",
        "w2b1r6b4r2b1r5b1w2",
        "w1b1r3b3r8b3r3b1w1",
        "w1b1r2b4r8b4r2b1w1",
        "w1b1r2b4r8b4r2b1w1",
        "w1b1r3b3r8b3r3b1w1",
        "w1x2r1b3x1b1r6b1x1b3r1x2w1",
        "x7r10x7",
        "x6r12x6",
        "x6r3b6r3x6",
        "x2r2b1r2b2x6b2r2b1r2x2",
        "x2b1r4b1x8b1r4b1x2",
        "x3b2r2b1x8b1r2b2x3",
        "x5b2x10b2x5",
    ]
)
RedArremerFlightRight02 = RedArremerFlightLeft02.hflip()

ghostsandgoblins_animation = animation_settings(
    sprite_list=[
                 [ArthurArmoredRunRight01,
                  ArthurArmoredRunRight02,
                  ArthurArmoredRunRight01,
                  ArthurArmoredRunRight03],
                 [RedArremerFlightRight01,
                  RedArremerFlightRight02],
                ],
    bg_sprites=[GhostsAndGoblinsBG02,
                GhostsAndGoblinsBG03],
    xoffs=[
           [0, 0, 0, 0],
           [0, 0],
          ],
    yoffs=[
           [0, 0, 0, 0],
           [0, 0],
          ],
    frame_time=0.04,
    spbg_ratio=3,
    center=True,
    bg_scroll_speed=(1, 0),
    cycles_per_char=5,
    reversible=False,
    )
