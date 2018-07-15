import sys
import re
import time

from itertools import cycle, chain, repeat

import numpy as np
from PIL import Image

import rgbmatrix as rgb

class sprite():
    
    def __init__(self, palette, matrix):
        self.palette = palette
        self.matrix = matrix
        
        #Check that rows are all the same length and sex sprite size
        row_len = self.get_row_lengths()
        assert max(row_len) == min(row_len), "Matrix rows must all be the same length!"
        self.xsize = row_len[0]
        self.ysize = len(row_len)
        
    def get_row_lengths(self):
        """
        """
        row_sums = []
        for row in self.matrix:
            lengths = [re.sub("[^0-9]", "", i) for i in re.split("(\d+)", row)[:-1]]
            row_sums.append(np.sum([int(i) for i in lengths if i]))
            
        return row_sums
            
    def convert_hex_to_rgb_tuple(self, hexstring):
        """
        """
        hexstring = hexstring.replace("#", "")
        return tuple([int(hexstring[i:i+2], 16) for i in range(0, len(hexstring), 2)])

    def hflip(self, rows=None):
    
        if not rows:
            rows = range(len(self.matrix))

        outmat = []
        for i, row in enumerate(self.matrix):
            if i in rows:
                rowsplit = re.split("(\d+)", row)[:-1]
                rowjoin = ["".join(rowsplit[i:i+2]) for i in range(0, len(rowsplit), 2)]
                outmat.append("".join(rowjoin[::-1]))
            else:
                outmat.append(row)

        return sprite(palette=self.palette,
                      matrix=outmat)
    
    def export_array(self, bg=None):
        
        arr = np.zeros((self.xsize, self.ysize, 3), dtype=np.uint8)
        
        #If bg is specified replace xs with the background
        if bg:
            self.palette["x"] = bg
        else:
            self.palette["x"] = "000000"

        for y, row in enumerate(self.matrix):
            sp_split = re.split("(\d+)", row)[:-1]
            newrow = []
            for element in [sp_split[i:i+2] for i in range(0, len(sp_split), 2)]:
                newrow.extend([self.palette[element[0]]] * int(element[1]))
            for x, rgb in enumerate(newrow[::-1]):    
                arr[x, y] = self.convert_hex_to_rgb_tuple(rgb)

        return arr

    
def convert_hex_to_rgb_tuple(hexstring):
        """
        """
        hexstring = hexstring.replace("#", "")
        return tuple([int(hexstring[i:i+2], 16) for i in range(0, len(hexstring), 2)])

def display_sprite(dispmatrix, sprite, bg_sprite=None, xoff=0, yoff=0, center=True, fill_color=None, xsize=32, ysize=32, display=True, clear=False):

    if clear:
        dispmatrix.Clear()

    array = sprite.export_array()
    if center:
        xoff = (xsize - array.shape[0])/2
        yoff = (ysize - array.shape[1])/2

    if bg_sprite:
        bg_array = bg_sprite.export_array()
        array = sprite.export_array(bg="010101")
        ufill = np.full((int((bg_array.shape[0] - array.shape[0])/2.), array.shape[1], 3), convert_hex_to_rgb_tuple("010101"), dtype=np.uint8)
        if array.shape[0] % 2 == 0:
            bfill = np.full((int((bg_array.shape[0] - array.shape[0])/2.), array.shape[1], 3), convert_hex_to_rgb_tuple("010101"), dtype=np.uint8)
        else:
            bfill = np.full((int((bg_array.shape[0] - array.shape[0])/2.) + 1, array.shape[1], 3), convert_hex_to_rgb_tuple("010101"), dtype=np.uint8)
        if center:
            array = np.concatenate((ufill, array, bfill), axis=0)
            xoff = 0
            yoff = 0
        else:
            array = np.concatenate((array, ufill, bfill), axis=0)
            
        lfill = np.full((array.shape[0], int((bg_array.shape[1] - array.shape[1])/2.), 3), convert_hex_to_rgb_tuple("010101"), dtype=np.uint8)
        if array.shape[1] % 2 == 0:
            rfill = np.full((array.shape[0], int((bg_array.shape[1] - array.shape[1])/2.), 3), convert_hex_to_rgb_tuple("010101"), dtype=np.uint8)
        else:
            rfill = np.full((array.shape[0], int((bg_array.shape[1] - array.shape[1])/2.) + 1, 3), convert_hex_to_rgb_tuple("010101"), dtype=np.uint8)
        if center:
            array = np.concatenate((lfill, array, rfill), axis=1)
        else:
            array = np.concatenate((array, lfill, rfill), axis=1)

        array = np.where(array == (1, 1, 1), bg_array, array)
    
    elif fill_color:
        array = sprite.export_array(bg=fill_color)
        fill_array = np.full((xsize, ysize, 3), convert_hex_to_rgb_tuple(fill_color), dtype=np.uint8)
        dispmatrix.SetImage(Image.fromarray(fill_array, mode="RGB"), 0, 0)
            
    if display:
        dispmatrix.SetImage(Image.fromarray(array, mode="RGB"), yoff, xoff)
    
    return array

def fill_array(array, bg_array, center=True, xoff=0, yoff=0):
        ufill = np.full((int((bg_array.shape[0] - array.shape[0])/2.), array.shape[1], 3), convert_hex_to_rgb_tuple("010101"), dtype=np.uint8)
        if array.shape[0] % 2 == 0:
            bfill = np.full((int((bg_array.shape[0] - array.shape[0])/2.), array.shape[1], 3), convert_hex_to_rgb_tuple("010101"), dtype=np.uint8)
        else:
            bfill = np.full((int((bg_array.shape[0] - array.shape[0])/2.) + 1, array.shape[1], 3), convert_hex_to_rgb_tuple("010101"), dtype=np.uint8)
        if center:
            array = np.concatenate((ufill, array, bfill), axis=0)
        else:
            array = np.concatenate((array, ufill, bfill), axis=0)
            
        lfill = np.full((array.shape[0], int((bg_array.shape[1] - array.shape[1])/2.), 3), convert_hex_to_rgb_tuple("010101"), dtype=np.uint8)
        if array.shape[1] % 2 == 0:
            rfill = np.full((array.shape[0], int((bg_array.shape[1] - array.shape[1])/2.), 3), convert_hex_to_rgb_tuple("010101"), dtype=np.uint8)
        else:
            rfill = np.full((array.shape[0], int((bg_array.shape[1] - array.shape[1])/2.) + 1, 3), convert_hex_to_rgb_tuple("010101"), dtype=np.uint8)
        if center:
            array = np.concatenate((lfill, array, rfill), axis=1)
        else:
            array = np.concatenate((array, lfill, rfill), axis=1)

        array = np.roll(array, axis=0, shift=xoff)
        array = np.roll(array, axis=1, shift=yoff)

        return array

def animate_sprites(dispmatrix, sprite_list, bg_sprite, frame_time, spbg_ratio=1, cycles=0, center=True, xoff=0, yoff=0, bg_scroll_speed=(0, 0), xsize=32, ysize=32, clear=True):
    
    if clear:
        dispmatrix.Clear()

    if bg_sprite:
        bg_arr = bg_sprite.export_array()
    else:
        bg_arr = np.full((xsize, ysize, 3), convert_hex_to_rgb_tuple("000000"), dtype=np.uint8)
        
    #Convert sprites to arrays
    if isinstance(xoff, int):
        xoff_list = [xoff] * len(sprite_list)
    else:
        xoff_list = xoff
        
    if isinstance(yoff, int):
        yoff_list = [yoff] * len(sprite_list)
    else:
        yoff_list = yoff
    
    arr_list = []
    for spr, xoff, yoff in zip(sprite_list, xoff_list, yoff_list):
        arr_list.append(fill_array(array=spr.export_array(bg="010101"), 
                                   bg_array=bg_arr, 
                                   center=center,
                                   xoff=xoff,
                                   yoff=yoff))
    if spbg_ratio > 1:
        arr_list = list(chain.from_iterable(repeat(i, spbg_ratio) for i in arr_list))
    
    if not cycles:
        iterator = cycle(arr_list)
    else:
        iterator = chain.from_iterable(repeat(arr_list, cycles))
        
    for arr in iterator:
        array_disp = np.where(arr == (1, 1, 1), bg_arr, arr)        
        dispmatrix.SetImage(Image.fromarray(array_disp, mode="RGB"))

        bg_arr = np.roll(bg_arr, 
                         axis=0,
                         shift=bg_scroll_speed[0])
        bg_arr = np.roll(bg_arr, 
                         axis=1,
                         shift=bg_scroll_speed[1])
        time.sleep(frame_time)

    return array_disp

def transition(dispmatrix, arr_one, arr_two, trans_speed=0.02, trans_type=None):

    def vertical_wipe():
        side = np.random.choice([1, -1])
        dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))
        for x in range(arr_one.shape[1])[::side]:
            dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))
            arr_one[:, x] = arr_two[:, x]
            time.sleep(trans_speed)
        dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))

    def horizontal_wipe():
        side = np.random.choice([1, -1])
        dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))
        for x in range(arr_one.shape[0])[::side]:
            dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))
            arr_one[x, :] = arr_two[x, :]
            time.sleep(trans_speed)
        dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))
        
    def random_pixels():
        dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))
        pos = [(x, y) for x in range(arr_one.shape[0]) for y in range(arr_one.shape[0])]
        np.random.shuffle(pos)
        for x, y in pos:
            dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))
            arr_one[x, y] = arr_two[x, y]
            time.sleep(trans_speed/20.)
        dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))
    
    if not trans_type:
        np.random.choice([vertical_wipe,
                          horizontal_wipe,
                          random_pixels])()       
