next_position = input("Please type what position: ")

if next_position == "1":
    print("x . .")
    print(". . .")
    print(". . .")

    next_position = input("Please type what position: ")

    if next_position == "1":
        print("CANT DO THE MOVE")

    elif next_position == "2":
        print("x o .")
        print(". . .")
        print(". . .")

        next_position = input("Please type what position: ")

        if next_position == "1":
            print("CANT DO THE MOVE")

        elif next_position == "2":
            print("CANT DO THE MOVE")

        elif next_position == "3":
            print("x o x")
            print(". . .")
            print(". . .")



    elif next_position == "3":
        print("x . o")
        print(". . .")
        print(". . .")


elif next_position == "2":
    print(". x .")
    print(". . .")
    print(". . .")    

elif next_position == "3":
    print(". . x")
    print(". . .")
    print(". . .")    

elif next_position == "4":
    print(". . .")
    print("x . .")
    print(". . .")       

elif next_position == "5":
    print(". . .")
    print(". x .")
    print(". . .")       

elif next_position == "6":
    print(". . .")
    print(". . x")
    print(". . .")       

elif next_position == "7":
    print(". . .")
    print(". . .")
    print("x . .")       

elif next_position == "8":
    print(". . .")
    print(". . .")
    print(". x .")       

elif next_position == "9":
    print(". . .")
    print(". . .")
    print(". . x")       