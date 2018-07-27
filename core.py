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


def display_sprite(dispmatrix, sprite, bg_sprite=None, xoff=0, yoff=0, center=True, fill_color=None, display=True, clear=False, xsize=32, ysize=32):

    if clear:
        dispmatrix.Clear()

    if bg_sprite:
        bg_array = bg_sprite.export_array()
    
    elif fill_color:
        bg_array = np.full((xsize, ysize, 3), convert_hex_to_rgb_tuple(fill_color), dtype=np.uint8)
  
    else:
        bg_array = np.full((xsize, ysize, 3), convert_hex_to_rgb_tuple("000000"), dtype=np.uint8)
    
    array = fill_array(array=sprite.export_array(bg="010101"), 
                       bg_array=bg_array, 
                       center=center,
                       xoff=xoff,
                       yoff=yoff)
    array = np.where(array == (1, 1, 1), bg_array, array)        

    if display:    
        dispmatrix.SetImage(Image.fromarray(array_disp, mode="RGB"))
    
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
    

def animate_sprites(dispmatrix, sprite_list, bg_sprites, frame_time, spbg_ratio=1, cycles=0, 
                    center=True, xoffs=0, yoffs=0, bg_scroll_speed=(0, 0), transition=False, 
                    transition_arr=None, cycles_per_char=5, cycle_all=False, xsize=32, ysize=32, 
                    clear=True):
    
    if clear:
        dispmatrix.Clear()
        
    #Randomly choose from one of the supplied backgrounds
    if bg_sprites:
        if len(bg_sprites):
            bg_sprite = np.random.choice(bg_sprites)
        else:
            bg_sprite = bg_sprites
        bg_arr = bg_sprite.export_array()
    else:
        bg_arr = np.full((xsize, ysize, 3), convert_hex_to_rgb_tuple("000000"), dtype=np.uint8)

    #If cycle_all cycle through all sprites on random background
    if cycle_all:
        arr_list = []
        cnt = 0
        for character, xoff, yoff in zip(sprite_list, xoffs, yoffs):
            if cnt == 0:
                arr02 = display_sprite(dispmatrix=dispmatrix, 
                                       sprite=character[0], 
                                       bg_sprite=bg_sprite, 
                                       center=center,
                                       xoff=xoff[0],
                                       yoff=yoff[0],
                                       display=False)
            char_series = [fill_array(array=spr.export_array(bg="010101"), 
                                            bg_array=bg_arr, 
                                            center=center,
                                            xoff=x,
                                            yoff=y) for (spr, x, y) in zip(character, xoff, yoff)] * cycles_per_char            
            arr_list.extend(char_series)
            cnt += 1

    #Default, select random sprite and background
    else:
        choice = np.random.randint(0, len(sprite_list))
        arr02 = display_sprite(dispmatrix=dispmatrix, 
                               sprite=sprite_list[choice][0], 
                               bg_sprite=bg_sprite, 
                               center=center,
                               xoff=xoffs[choice][0],
                               yoff=yoffs[choice][0],
                               display=False)

        arr_list = [fill_array(array=spr.export_array(bg="010101"), 
                                      bg_array=bg_arr, 
                                      center=center,
                                      xoff=x,
                                      yoff=y) for (spr, x, y) in zip(sprite_list[choice], xoffs[choice], yoffs[choice])]
        
    if transition:   
        perform_transition(dispmatrix=dispmatrix,
                           arr_one=transition_arr,
                           arr_two=arr02,
                          )
        
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
    

def perform_transition(dispmatrix, arr_one, arr_two, trans_speed=0.02):

    def wipe():
        axis = np.random.choice([0, 1])
        side = np.random.choice([1, -1])
        dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))
        for x in range(arr_one.shape[axis])[::side]:
            dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))
            if axis == 0:
                arr_one[x, :] = arr_two[x, :]
            elif axis == 1:
                arr_one[:, x] = arr_two[:, x]
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

    def diagonal_wipe():
        forward = np.random.choice([True, False])
        if forward:
            for x, y in zip(range(arr_one.shape[0] * 2 + 1), range(arr_one.shape[1] * 2 + 1)):
                dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))
                for x1, y1 in zip(range(x)[::-1], range(y)):
                    arr_one[min(x1, arr_one.shape[0] - 1) , min(y1, arr_one.shape[1] - 1)] =\
                    arr_two[min(x1, arr_one.shape[0] - 1) , min(y1, arr_one.shape[1] - 1)]
                time.sleep(trans_speed)
        else:
            for x, y in zip(range(-1 * arr_one.shape[0], arr_one.shape[0])[::-1], range(-1 * arr_one.shape[1], arr_one.shape[1])[::-1]):
                dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))
                for x1, y1 in zip(range(x, arr_one.shape[0])[::-1], range(y, arr_one.shape[1])):
                    arr_one[max(x1, 0) , max(y1, 0)] =\
                    arr_two[max(x1, 0) , max(y1, 0)]
                time.sleep(trans_speed)
        dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))

    def checkerboard():
        frac = np.random.choice([4, 8])
        xfrac, yfrac = int(arr_one.shape[0] / frac), int(arr_one.shape[1] / frac)
        xs = np.arange(0, arr_one.shape[0], xfrac)
        ys = np.arange(0, arr_one.shape[1], yfrac)
        checkers = [(x, y) for x in xs for y in ys]
        np.random.shuffle(checkers)

        for x, y in checkers:
            dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))
            arr_one[x:x+xfrac, y:y+yfrac] = arr_two[x:x+xfrac, y:y+yfrac]
            time.sleep(trans_speed)
        dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))

    def cross_swirl():
        forward = np.random.choice([True, False])
        for z in range(int(arr_one.shape[0])):
            if forward:
                series = zip(np.linspace(z, (arr_one.shape[0] - 1 - z), arr_one.shape[0]), 
                             range(arr_one.shape[1]),
                             range(arr_one.shape[0]),
                             np.linspace(z, (arr_one.shape[1] - 1 - z), arr_one.shape[1])[::-1])
            else:
                series = zip(np.linspace(z, (arr_one.shape[0] - 1 - z), arr_one.shape[0])[::-1], 
                             range(arr_one.shape[1]),
                             range(arr_one.shape[0]),
                             np.linspace(z, (arr_one.shape[1] - 1 - z), arr_one.shape[1]))            
            for x1, y1, x2, y2 in series:
                dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))
                x1 = int(np.round(x1, 0))
                y2 = int(np.round(y2, 0))
                arr_one[x1, y1] = arr_two[x1, y1]
                arr_one[x2, y2] = arr_two[x2, y2]
        dispmatrix.SetImage(Image.fromarray(arr_one, mode="RGB"))
    
    np.random.choice([wipe,
                      random_pixels,
                      diagonal_wipe,
                      checkerboard,
                      cross_swirl])()       
