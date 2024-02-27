for x in range(1, 101) :
    if x % 3 == 0 and x % 5 == 0 :
        print("Buzz")
    elif x % 3 == 0 :
        print(x**2)
    elif x % 5 == 0 :
        print(x**3)
    elif x % 3 == 0 and x % 5 == 0 :
        print("Buzz")
    else:
        print(x)
