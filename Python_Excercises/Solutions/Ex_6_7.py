try:
    num = float(input())
    points = int(input())
    print('{0:.{1}f}'.format(num,points))
    #print(round(num,points))
except:
    print('Invalid data type!')