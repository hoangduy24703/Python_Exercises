try:
    fin = open('Ex_23_input.txt','r')
    list = fin.read().split()
    a, b, c = map(float, list)
    if a + b < c or a + c < b or b + c < a:
        message = 'Invalid triangle'
    else:
        if a == b and b == c:
            message = 'Equilateral triangle'
        elif a == b or b == c or c == a:
            message =  'Isosceles triangle'
        elif a*a == b*b + c*c or b*b == a*a + c*c or c*c == b*b + a*a:
            message =  'Right triangle'
        elif a*a > b*b + c*c or b*b > a*a + c*c or c*c > b*b + a*a:
            message = 'Acute triangle'
        else:
            message = 'Obtuse triangle'
except:
    message = 'Error'

fout = open('Ex_23_output.txt','w')
fout.write(message)