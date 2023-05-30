try:
    fin = open("Ex_12_13_input.txt",'r')
    str = fin.read()
    list_line = str.splitlines()
    fout = open("Ex_12_13_output.txt",'w')
    fout.write(" ".join(list_line))
except:
    print("Invalid data type !")

