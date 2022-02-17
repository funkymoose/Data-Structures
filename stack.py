# Stacks using list

stack = []

def push():

    if len(stack)==n:
        print('Stack is full!')
        print("---------------------------------------------------------------------------------------------------")

    else:
        stack.append(input("Enter the element:"))
        print(stack)
        print("---------------------------------------------------------------------------------------------------")

def pop_element():

    if len(stack) == 0:
        print('Cannot Pop! The stack is empty')
        print("---------------------------------------------------------------------------------------------------")


    else:
        stack.pop()
        print(stack)
        print("---------------------------------------------------------------------------------------------------")

def top():

    if len(stack) == 0:
        print('The stack is empty')
        print("---------------------------------------------------------------------------------------------------")

    else:
        print(stack[-1])
        print("---------------------------------------------------------------------------------------------------")

def isEmpty():

    if len(stack) == 0:
        print('The stack is empty')
        print("---------------------------------------------------------------------------------------------------")

    else:
        print('There are elements in stack')
        print("---------------------------------------------------------------------------------------------------")

n = int(input("Enter the size of stack:"))

while True:

    inp = int(input("Enter the operation to be performed\n1.Push\n2.Pop\n3.Top Element\n4.Check if stack is empty\n5.Quit\n"))

    if inp == 1:
        push()

    elif inp == 2:
        pop_element()

    elif inp == 3:
        top()

    elif inp == 4:
        isEmpty()

    elif inp == 5:
        break

    else:
        print('Invalid input')


