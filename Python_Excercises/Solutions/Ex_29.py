a, b = map(int, input().split())
for num in range(a,b+1):
    if num%5 == 0:
        print(num, end = " ")