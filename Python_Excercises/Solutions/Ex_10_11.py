try:
    fin = open("Ex_10_11_input.txt","r")
    name = fin.readline().rstrip('\n')
    age = int(fin.readline())
    age+=20
    fout = open("Ex_10_11_output.txt","w")
    fout.write('The next 20 years, %s wil be %d years old' % (name,age))

except:
    print('Error')