# change the values to see how the code works 
string = "heystranger"
myfloat = 20.0
myint = 20

if string == "heystranger": #if the string is heystranger then the below line will get executed
    print("String: %s" % string) #the %s indicates that a string is being printed and the % string refers to 
    #the name of the specific string that is being printed 

if isinstance(myfloat, float) and myfloat == 20.0: #if myfloat is of type float (true) and myfloat 
    #is greater than 0 then execute the next line
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)


