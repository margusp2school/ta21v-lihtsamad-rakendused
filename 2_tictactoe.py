game = [
    ".", ".", ".",
    ".", ".", ".",
    ".", ".", "."
]

print(game[0] + game[1] + game[2])
print(game[3] + game[4] + game[5])
print(game[6] + game[7] + game[8])

next_position = input("Please type what position: ")

# line 14 and 17 are same. Please make "1" and "2" to int (using int() function and -1)
if next_position == "1":
    game[0] = "X"

if next_position == "2":
    game[1] = "X"    

# this is same as on line 7. make this a function
print(game[0] + game[1] + game[2])
print(game[3] + game[4] + game[5])
print(game[6] + game[7] + game[8])