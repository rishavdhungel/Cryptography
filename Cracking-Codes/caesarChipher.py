message = str(input("Input message to encrypt or decrypt."))
buffer = ''
key = 14
symbols="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
mode = int(input(("Enter 1 for encryption mode and 2 for decryption: ")))
for symbol in message:
    if symbol in symbols:
        bufferIndex =''
        symbolIndex = symbols.find(symbol)
        if mode == 1:
            bufferIndex = symbolIndex + key
        elif mode == 2:
            bufferIndex = symbolIndex - key
        else:
            print("Wrong Input")
        if bufferIndex >= len(symbols):
            bufferIndex = bufferIndex - len(symbols)
        elif bufferIndex < 0:
            bufferIndex = bufferIndex + len(symbols)
        buffer += symbols[bufferIndex]
    else:
        buffer += symbol
print(buffer)
