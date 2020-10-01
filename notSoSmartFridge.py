#Smart Fridge

fridge_contents = [
    "Milk",
    "Cheese",
    "Lettuce",
    "Beer"
]

fridge_item = input(f"\nWhich item from your fridge would you like to check for?: ")

if fridge_item in fridge_contents:
    print(f"\nYes, you have {fridge_item} in your fridge!")
else:
    print(f"\nUnfortunately, you are completely out of {fridge_item}!")
    response = input(f"\nWould you like to add {fridge_item} to the fridge? Y or N: ")
    if response == "Y":
        fridge_contents.append(fridge_item)
        print(f"\nYour fridge_contents now contains:")
        print(*fridge_contents, sep = "\n")
    else:
        print(f"\nThat is fine, we'll all starve!")

response = input(f"\nWould you like to remove anything from the fridge? Y or N: ")

if response == "Y":
    remove_item = input(f"\nWhat would you like to remove?: ")
    if remove_item in fridge_contents:
        fridge_contents.remove(remove_item)
        print(f"\nOK. {remove_item} has been removed.\nYour fridge now contains:")
        print(fridge_contents)
    else:
        print(f"\nSorry, that item doesn't exist")
        print(f"\nYour fridge currently only contains {fridge_contents}")
else:
    print(f"\nOf course, just leave everything to go mouldy")
