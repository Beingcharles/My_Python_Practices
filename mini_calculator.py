a=int(input("a: "))
b=int(input("b: "))
i=input("add/sub/mul/div/mod/exp: ")
if(i=="add"):
    print(a+b)
elif(i=="sub"):
    print(a-b)
elif(i=="mul"):
    print(a*b)
elif(i=="div"):
    print(a/b)
elif(i=="mod"):
    print(a%b)
elif(i=="exp"):
    print(a**b)
else:
    print("invalid calculation")
