# pip install Pillow
# python pixelize.py path_in width height

from PIL import Image
import sys
import os

def pixelize(file_in, width, height):
    im = Image.open(file_in)
    pixelized = im.resize((width, height), Image.NEAREST)
    
    for i in range(len(file_in) - 1, 0, -1):
        if file_in[i] == '.':
            index = i
            break
    file_out = file_in[:index] + "_pixelized" + file_in[index:]
    while os.path.exists(file_out):
        # remove current file if this name already exists
        os.remove(file_out)
    pixelized.save(file_out)

if __name__=='__main__':
    file_in = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    pixelize(file_in, width, height)