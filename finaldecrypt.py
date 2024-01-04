from AESdecrypt import *
import stego

newFilename = "encoded.png"
decodedFilename = "decodedFile"

print("Decoding...")
stego.decodeLSB(newFilename, decodedFilename)
print("Decoding finished.")

AESdecryption()