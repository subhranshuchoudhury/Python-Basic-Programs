#operators perform specific operation. eg. addition, multiplication, division.
#operand are the variables.

#1 Arithmetic Operators: +, -, *, /, %, **, //
#**-> power, //-> floor Division--remove the decimal values. 2.6 --> 2

a = 3
b = 4
c = a**b #change acording to you.
print(c) #result should 81.

#2 Relational Operator/Comparison Operator, Result: true/false
#operators are: >,<,==,!=,<>,<=,>= .

a = 3
b = 3
c = a==b #change acording to you.
print(c) #result should true.

#3 Assing Operators : =,+=,-=,/=,*=,%=

a = 10
b = 20
a += b
print(a) #output: 30

#4 Logical Operators: and, or, not
#AND - it return true if all the statements are true.
#OR - it return true if any statemrnt is true.
#NOT - it reverse the return true to false and false to true.

a = 10
b = 20
c = 30
d = ((a>b)and(a>c))
print(d) #output -- false
