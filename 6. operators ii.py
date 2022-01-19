#5. Identity operators: is, is not
#is - return true if variable of same object. and is not is its reverse.
# we use identity operators with " type() " function.

x = 5 #int
if(type(x) is int):
    print("correct!") # output
else:
    print("incorrect!")
y=7.8 #float
if(type(y) is int):
    print("correct!")
else:
    print("incorrect!") # output
    
#______________________________________________________________________    
#6. Membership operators: in , not in
#in - if value found return true, not in - return true if value not found.

list = [1,2,3,4,5]
a = 5

if(a in list):
     print("a is in the list.") #output
else:
    print("a is not in the list.")

a = 6 #change the value

if(a not in list):
    print("a is not in the list.")#output
else:
    print("a is in the list.")
#________________________________________________________________________
    
#7. Bitwise operators: & (and), |(or), ^(XOR), ~(not), <<(zero fill left shift), >>(signed right shift)
#video link: https://youtu.be/4zOh2BkyxpM?list=PLmRclvVt5DtmcLF3ywxKg692lhfD6SUOr&t=480
# x & y, X|y, x^y, x~y, x<<y, x>>y
# x^y(xor)----> 0-0--0,0-1--1,1-0--1,1-1--0
# 1 step left shift--  x<<1  ---> 0000 0110--0000 1100
# 1 step right shift-- x>>1  ---> 0000 0110--0000 0011 
