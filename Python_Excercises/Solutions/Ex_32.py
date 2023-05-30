n = int(input())
ASCII_code = 65
cnt = 0
for i in range (n,0, -1):
    str = "  "*(i-1)
    print(str, end = ' ')
    for j in range(i,i+cnt+1):
        print(chr(ASCII_code), end = ' ')
        ASCII_code+=1
        if chr(ASCII_code) == 'Z':
            ASCII_code = 65
    print()
    cnt += 2