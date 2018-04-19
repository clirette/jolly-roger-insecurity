#!/usr/bin/env python2
#### reads pgm (ascii) file, for each byte of 255, treat that as a 1 bit
### then write to bw.output

inf = open("bw.pgm","r")
outfile = open("bw.output","wb")
output = list()

for line in inf.readlines():
    count=0
    byte=0
    val=0
    for pixel in line.split(" "):
        if pixel == "255":
            #print ("bit " + str(count) + " is a " + str(pixel))
            val += 1 << (count%8)
            #print (" adding " + str(val) + " to byte " + str(byte))
        if (count%8)==7:
            output.append(val)
            val = 0
            byte+=1
        count += 1

#bb = bytearray(output)
outfile.write(str(output))

print ("list avg is: " + str(sum(output,0.0) / len(output)))
