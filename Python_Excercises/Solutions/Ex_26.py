a, b = map(int, input().split())
sum = 0
for number in range(a,b+1):
    sum+=number
print('Sum = %d' % sum)