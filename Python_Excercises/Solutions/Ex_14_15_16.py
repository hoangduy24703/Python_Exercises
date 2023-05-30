try:
    print("Person 1: ")
    Person_1 = {"Name" : str(input()), "Height" : int(input())}
    print("Person 2: ")
    Person_2 = {"Name" : str(input()), "Height" : int(input())}
    if Person_1["Height"] > Person_2["Height"]:
        print("%s is taller than %s" % (Person_1["Name"], Person_2["Name"]))
    elif Person_1["Height"] < Person_2["Height"]:
        print("%s is taller than %s" % (Person_2["Name"], Person_1["Name"]))
    else:
        print("The same height")
except:
    print("Invalid data type !")

