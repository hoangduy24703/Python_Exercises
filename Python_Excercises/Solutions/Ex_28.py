# Sửa đề thành in toàn bộ bảng cửu chương
for i in range(1,10):
    print('The times table for %d' % i)
    for j in range(1, 10):
        print('{} * {} = {}' .format(i,j,i*j))