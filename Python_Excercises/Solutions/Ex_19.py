num1, oper, num2 = input().split()
num1 = float(num1)
num2 = float(num2)

if oper == '+':
    print('%f %s %f = %f' % (num1, oper, num2, num1+num2))
elif oper == '-':
    print('%f %s %f = %f' % (num1, oper, num2, num1-num2))
elif oper == '*':
    print('%f %s %f = %f' % (num1, oper, num2, num1*num2))
elif oper == '/':
    if num2 != 0:
        print('%f %s %f = %f' % (num1, oper, num2, num1/num2))    
    else:
        print('Error')
