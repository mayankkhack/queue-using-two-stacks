
stack1 = []
stack2 = []

def enqueue(x):
    stack1.append(x)
    print(x, "inserted")

def dequeue():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())

    if not stack2:
        print("Queue is empty")
    else:
        print("Deleted element:", stack2.pop())

def display():
    print("Queue:", list(reversed(stack2)) + stack1)

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = int(input("Enter element: "))
        enqueue(x)

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")
