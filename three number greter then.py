a=int(input("enter the first number :- "))
b=int(input("enter the second number :- "))
c=int(input("enter the third number :- "))

if a>b:
    if a>c:
        print("a is greater then both b and c")
    else:
        print("a is greater then a but smaller then c")

else:
    if b>c:
        print("b is greater then both a and c")
    else:
        print("c is greater then both a and b")
