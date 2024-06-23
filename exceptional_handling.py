try:
    a=int(input())
    b=int(input())
    c=a/d
except ValueError as e:
    print ("Value Error",e)
except Exception:
    print("Something wrong")
finally:
    print ("Done")
