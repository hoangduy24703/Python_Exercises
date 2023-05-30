try:
    str = str(input())
    list_str = str.split()
    list_int = map(int, list_str)
    print(sum(list_int))
except:
    print('Invalid data type!')