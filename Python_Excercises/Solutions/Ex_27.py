a, b = map(int, input().split())
sum = 0
num = a
while num <= b:
    sum+=num
    num+=1
print('Sum = %d' % sum)