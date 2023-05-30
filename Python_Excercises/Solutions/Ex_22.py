a, b, c =map(float, input().split())
if a + b < c or a + c < b or b + c < a:
    print('Invalid triangle')
else:
    if a == b and b == c:
        print('Equilateral triangle')
    elif a == b or b == c or c == a:
        print('Isosceles triangle')
    elif a*a == b*b + c*c or b*b == a*a + c*c or c*c == b*b + a*a:
        print('Right triangle')
    elif a*a > b*b + c*c or b*b > a*a + c*c or c*c > b*b + a*a:
        print('Acute triangle')
    else:
        print('Obtuse triangle')