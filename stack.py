# Assessment 3.2 - Stack
# Last Name: AUDITOR
myStack = []

print("STACK - LIFO")
print("Enter each letter of your last name.")
print("Type DONE when finished.\n")

while len(myStack) < 7:
    letter = input("Enter a letter to push: ").strip().upper()

    if letter == "DONE":
        break

    if len(letter) != 1 or not letter.isalpha():
        print("Please enter only one letter.")
        continue

    myStack.append(letter)
    print("Stack:", myStack)

print("\nFinal Stack:", myStack)
print("\nRemoving letters:")

while len(myStack) > 0:
    input("Press Enter to pop the next letter...")

    removed = myStack.pop()
    print("Popped:", removed)
    print("Remaining Stack:", myStack)

print("\nThe stack is empty.")