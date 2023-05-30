try:
    a = float(input())
    b = float(input())
    c = float(input())

    if a + b > c and a + c > b and b + c > a :
        print("Valid triangle")
    else:
        print("Invalid triangle")
except:
    print("Invalid data type !")