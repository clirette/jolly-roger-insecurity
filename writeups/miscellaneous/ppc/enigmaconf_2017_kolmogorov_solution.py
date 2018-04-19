from pwn import *
s = remote("enigma2017.hackcenter.com",49593) # Create socket
s.recvuntil("of ")                            # Receive data until number of first letters
num = int(s.recv(4))                          # Get the count to generate of the first letter
s.recvuntil(" \'")                            # Skip until first letter
firstlet = s.recv(1)                          # Grab the first letter
s.recvuntil("single \'")                      # Skip to before second letter
secondlet = s.recv(1)                         # Grab the second letter
s.send(firstlet*num + secondlet)              # Send what server expects
print s.recvall()                             # Print what we get back--should be the flag
