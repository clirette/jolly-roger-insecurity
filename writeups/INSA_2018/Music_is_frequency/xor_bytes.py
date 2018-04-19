#!/usr/bin/python
#### 4/6/2018 m.toups
#
# read in bytes from input1 and input2, XOR each byte (up to numbytes)

import sys

if len(sys.argv) != 4: # len 3 is: cmdname input1 input2 numbytes
    print("usage: {} input1 input2 numbytes".format(sys.argv[0]) )
    sys.exit(1)

with (open (sys.argv[1],'r')) as fd:
    barray = bytearray(fd.read())
    with (open(sys.argv[2],'r')) as fd2:
        barray2 = bytearray(fd2.read())
        for i in range(int(sys.argv[3])):
            print("byte {:4s}: {:4s} XOR {:4s} == {:4s}".format(hex(i),hex(barray[i]),hex(barray2[i]),hex(barray[i] ^ barray2[i])))
