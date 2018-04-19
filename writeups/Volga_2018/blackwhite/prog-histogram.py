#!/usr/bin/env python2
#### reads pgm (ascii) file, for each byte of 255, treat that as a 1 bit
### then write to bw.output

import pandas
from collections import Counter

f = open("bw.pgm","r")
outfile = open("bw.output","wb")
output = list()

for line in f.readlines():
    count=0
    byte=0
    val=0
    for pixel in line.split(" "):
        if pixel == "255":
            val += 1 << (count%8)
        if (count%8)==7:
            output.append(val)
            val = 0
            byte+=1
        count += 1

#bb = bytearray(output)
outfile.write(str(output))

df = pandas.DataFrame.from_dict(Counter(output), orient='index')
ax = df.plot(kind='bar')
fig = ax.get_figure()
fig.savefig('output.pdf')
