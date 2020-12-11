a=int(input("enter a number :-"))

b=int(a/100)

c=a%100

d=int(c/10)

e=c%10

f=(b*b*b)+(d*d*d)+(e*e*e)

if a==f:
    print("the number is armstrong number")
else:
    print("the number is not armstrong number")