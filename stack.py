li =[]
def push():
    val = int(input("Enter the value to be added:"))
    li.append(val)
    print("Value added successfully")
def pops():
    if not li:
        print("Stack is empty")
    else:
        li.remove(li[len(li)-1])
        print("Removed successfully")
def peek():
    if not li:
        print("Stack is empty")
    else:
        print(li[-1])
def prints():
    print(li)
while input("Press y to continue: ")=='y':
    print("Press 1 to Push")
    print("Press 2 to Pop")
    print("Press 3 to Peek")
    print("Press 4 to Print")
    n = int(input("Which option u want to select: "))
    if n==1:
        push()
    if n==2:
        pops()
    if n==3:
        peek()
    if n==4:
        prints()

