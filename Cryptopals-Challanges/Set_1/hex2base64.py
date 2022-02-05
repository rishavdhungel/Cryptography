#!usr/bin/python3
from binascii import hexlify, unhexlify
from base64 import b64encode
'''
Rule:
Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
'''
hexInput = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
expectedOutput = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

#string to bytes
unHexed = unhexlify(hexInput)
decodedOutput =(b64encode(unHexed)).rstrip()
hexed = hexlify(unHexed)
print(unHexed)
print(hexed)
print(decodedOutput)

