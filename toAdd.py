numbers = raw_input("Gimme some numbers, separated by spaces: ")
toAdd = numbers.split(" ")
finalAdd = 0
try:
    for num in toAdd:
        finalAdd += float(num)

    print(finalAdd)

except ValueError:
    print("Only numbers please!")
