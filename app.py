PARKING_PLACES = 7
FREE_PLACE = 3

print("#"*PARKING_PLACES*5)

for place_index in range(1, PARKING_PLACES + 1):
    print("| X |", end="") if FREE_PLACE != place_index else print("|   |", end="")
print("\n","#"*PARKING_PLACES*5, sep="")