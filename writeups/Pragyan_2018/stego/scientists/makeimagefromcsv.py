#!/usr/bin/python
# note: due to use of decode('hex') string method below,
#       this code won't work in python 3.x, only 2.x

# pragyan CTF 3/3/2018  mtoups
# idea: maybe each number in spreadsheet is an (r,g,b) tuple?
import sys
import csv # for reading input
from struct import unpack # helpful for making a tuple out of a hex string
from PIL import Image # PIL is Python Imaging Library

img=[] # will be a list of lists of tuples

if len(sys.argv) != 3: # len 3 is: cmdname input output
    print("usage: {} input.csv output.png".format(sys.argv[0]) )
    sys.exit(1)

with (open (sys.argv[1],'r')) as fd:
    reader=csv.reader(fd,delimiter=',') # can change delimiter if needed
    for row in reader: # row is a list of entries
        imgrow=[] # make list of 3-tuples (aka pixels) for each row
        for entry in row: # entry is a decimal value from spreadsheet cell
            e="{:06x}".format(int(entry)) # render as string of 6 hex chars
            imgrow.append(unpack('BBB',e.decode('hex'))) # make tuple, append
        img.append(imgrow) # add row to list of rows

width, height = len(img[0]), len(img) #len of 1st row, len of rows (cols)
pixels = sum(img, []) # quick & ugly: flatten list of lists

im = Image.new('RGB', (width,height)) # tell PIL type and size
im.putdata(pixels) # do it
imrot = im.rotate(180) # rotate 180
imflip = imrot.transpose(Image.FLIP_LEFT_RIGHT) # flip
imflip.save(sys.argv[2]) # save result to filename given on cmdline
                         # can be png/jpg or whatever depending on filename
