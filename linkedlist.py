# Assessment 3.2 - Linked List
# Last Name: AUDITOR
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add a node at the end
    def add(self, letter):
        newNode = Node(letter)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = newNode

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("NULL")


myList = LinkedList()
count = 0

print("LINKED LIST")
print("Enter each letter of your last name.")
print("Type DONE when finished.\n")

while count < 7:
    letter = input("Enter a letter to add: ").strip().upper()

    if letter == "DONE":
        break

    if len(letter) != 1 or not letter.isalpha():
        print("Please enter only one letter.")
        continue

    myList.add(letter)
    count += 1

    print("Linked List:", end=" ")
    myList.display()

print("\nInitial Linked List:")
myList.display()

print("\nTraversing the linked list:")

while myList.head is not None:
    input("Press Enter to display the next node...")

    print("Displayed:", myList.head.data)

    myList.head = myList.head.next

    print("Remaining List:", end=" ")
    myList.display()

print("\nThe linked list is empty because head = None.")