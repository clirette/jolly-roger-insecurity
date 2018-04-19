#!/bin/bash

unzip music-is-frequency.zip # start by unzipping
base64 -d src/flag.enc > flag # base64 decode the ciphertext

# decode private key using song notes to determine XOR pattern
python3 ./xor_notes.py src/privatekey.bin decoded_privkey.pem 1674

# now use decoded_privkey.pem to decrypt flag using RSA
openssl rsautl -decrypt -inkey decoded_privkey.pem -in flag -raw

echo && echo Flag found!
