import stego

filename = "ciphertext.txt"
imageName = "dragon1.jpg"
newFilename = "encoded"
decodedFilename = "decodedFile"

print("Encoding...")
img = stego.encodeLSB(filename, imageName, newFilename)
print("Encoding finished.")