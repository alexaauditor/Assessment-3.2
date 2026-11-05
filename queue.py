# Assessment 3.2 - Queue
# Last Name: AUDITOR
from collections import deque

myQueue = deque()

print("QUEUE - FIFO")
print("Enter each letter of your last name.")
print("Type DONE when finished.\n")

while len(myQueue) < 7:
    letter = input("Enter a letter to enqueue: ").strip().upper()

    if letter == "DONE":
        break

    if len(letter) != 1 or not letter.isalpha():
        print("Please enter only one letter.")
        continue

    myQueue.append(letter)
    print("Queue:", list(myQueue))

print("\nFinal Queue:", list(myQueue))
print("\nRemoving letters:")

while len(myQueue) > 0:
    input("Press Enter to dequeue the next letter...")

    removed = myQueue.popleft()
    print("Dequeued:", removed)
    print("Remaining Queue:", list(myQueue))

print("\nThe queue is empty.")