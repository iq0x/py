import readchar

##################################
#print("Reading a char:")
#print(repr(readchar.readchar()))
##################################

i = 1
while 1:
    i += 1
    key = readchar.readkey()
    print(key)
    if key == 'q':
        break
