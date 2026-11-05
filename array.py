# Assessment 3.2 - Array
# Last Name: AUDITOR
myArray = [None] * 7
size = 0

print("ARRAY - LIFO")
print("Enter each letter of your last name.")

while size < 7:
    letter = input("Enter a letter to insert: ").strip().upper()

    if letter == "DONE":
        break

    if len(letter) != 1 or not letter.isalpha():
        print("Please enter only one letter.")
        continue

    myArray[size] = letter
    size += 1

    print("Array:", myArray[:size])

print("\nInitial Array:", myArray[:size])
print("\nRemoving letters:")

while size > 0:
    input("Press Enter to remove the next letter...")

    removed = myArray[size - 1]
    print("Removed:", removed)

    myArray[size - 1] = None
    size -= 1

    print("Remaining Array:", myArray[:size])

print("\nThe array has zero active elements (size = 0).")