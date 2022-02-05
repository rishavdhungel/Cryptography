#!usr/bin/python3
message = "This is a message that is to be reversed"
buffer = ''
#method 1
for i in range (1,len(message)+1):
    buffer += message[-i]
print (buffer)


#method 2

buffer2 = ''
length = len(message)-1
while(length >=0):
    buffer2 += message[length]
    length -= 1 
print(buffer2)


