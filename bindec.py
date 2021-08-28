
def decbin(n):
    return bin(n).replace("0b", "")
    
def bindec(val): 
    return int(val, 2) 
   
if __name__ == '__main__':
    print(decbin(7))
    print(decbin(15))
    print(bindec('111'))

