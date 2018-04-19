#!/usr/bin/python3
#### 4/6/2018 m.toups
#
# read in bytes from input, use notes from frere_jacques
# to come up with XOR pattern to decode private key!

import sys

frere_jacques = [ # list of frequencies for each note of song
        349, 392, 440, 349, # F G A F
        349, 392, 440, 349, # F G A F
        440, 466, 523, # A Bb C
        440, 466, 523, # A Bb C
        523, 587, 523, 466, 440, 349, # C D C Bb A F
        523, 587, 523, 466, 440, 349, # C D C Bb A F
        349, 262, 349, # F C F
        349, 262, 349 # F C F
        ] # I guess we could have made a dictionary of notes -> freqs ....

fj = list() # this is ugly, need to split 349 into a byte of 0x01 (256) and 0x5d (93)

for (a,b) in zip([ x >> 8 for x in frere_jacques ],[ x & 0xff for x in frere_jacques ]):
    fj.append(a)
    fj.append(b)

decrypted_input = bytearray()

if len(sys.argv) != 4: # len 4 is: cmdname input output numbytes
    print("usage: {} input output numbytes".format(sys.argv[0]) )
    sys.exit(1)

# now the interesting part begins

with (open (sys.argv[1],'r')) as fd:
    barray = bytes(fd.read(),"ascii")
    for i in range(int(sys.argv[3])):
        # for each byte i of input, we will XOR it with either 0x30 or 0x31
        # 0x30 when BIT of frere_jacques is 0, 0x31 when BIT is 1
        # every 16 bytes of input, we move to the next note (8 bytes, half a note, fj has two entries per note)
        b = ((i % 512) //8) # increase byte for every 8 iterations ( // is for integer division )
        bit = 7 - (i % 8) # which bit? 0->shift 7, 1-> shift 6, 2 -> 5, 3 -> 4, 4->3 , 5->2, 6 -> 1, 7 -> 0
        decrypted_input.append(barray[i] ^ 0x30 + ((fj[b] >> bit) & 1)) # do the XOR !

# done, now write it out

with (open(sys.argv[2],'wb')) as of:
    of.write(decrypted_input)
