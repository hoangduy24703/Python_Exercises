try:
    import math
    while True:
        print('Linear equation: 1 \nQuadratic equation: 2')
        choice = int(input())
        if choice == 1 or choice == 2:
            break
        else:
            print("Please type 1 or 2 only")
    if choice == 1:
        a, b = map(float, input().split())
        print('x = %f' % (-b/a))
    elif choice == 2:
        a, b, c = map(float, input().split())

        if a == 0 and b == 0 and c == 0:
            print('Vo so nghiem')
        elif c==0:
            print('Vo nghiem')
        delta = b*b - 4*a*c
        if delta < 0:
            print('Vo nghiem')
        elif delta == 0:
            print('x0 = %f' % (-b/(2*a)))
        else:
            print('x1 = %f' % ((-b+math.sqrt(delta))/(2*a)))
            print('x1 = %f' % ((-b-math.sqrt(delta))/(2*a)))
except:
    print("Error")