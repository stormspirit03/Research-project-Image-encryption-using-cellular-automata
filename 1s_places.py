# Function to reverse a string 
def reverse(string): 
    string = string[::-1] 
    return string 

# Python3 program to Split string into characters 
def split(word): 
    return list(word) 


# reversed binary strings upto 256
for x in range(1,256):
    str=reverse(bin(x)[2:].zfill(8))
    list1=(split(str)) 
    
## print 1's places     
    for i in range(len(list1)):
        if list1[i]=='1':
            print(i,end=",")
    print()    
  
