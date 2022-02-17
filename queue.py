# Queue = enqueue, dequeue, isFull, isEmpty
queue = []

# For queue from rear end
def enqueueR():

    if len(queue)==n:
        print('Queue is full!')
        print("---------------------------------------------------------------------------------------------------")

    else:
        queue.append(input("Enter the element:"))
        print(queue)
        print("---------------------------------------------------------------------------------------------------")

def dequeueR():

    if len(queue) == 0:
        print('Cannot dequeue! The queue is empty')
        print("---------------------------------------------------------------------------------------------------")


    else:
        queue.pop(0)
        print(queue)
        print("---------------------------------------------------------------------------------------------------")

def isFullR():

    if len(queue) == n:
        print('The queue is Full')
        print("---------------------------------------------------------------------------------------------------")

    else:
        print(f'{n-len(queue) } element/elements can be inserted')
        print("---------------------------------------------------------------------------------------------------")

def isEmptyR():

    if len(queue) == 0:
        print('The queue is empty')
        print("---------------------------------------------------------------------------------------------------")

    else:
        print(f'There are {len(queue)} elements in queue')
        print("---------------------------------------------------------------------------------------------------")

# For queue from front end

def enqueueF():

    if len(queue)==n:
        print('Queue is full!')
        print("---------------------------------------------------------------------------------------------------")

    else:
        queue.insert(0,input("Enter the element:"))
        print(queue)
        print("---------------------------------------------------------------------------------------------------")

def dequeueF():

    if len(queue) == 0:
        print('Cannot dequeue! The queue is empty')
        print("---------------------------------------------------------------------------------------------------")


    else:
        queue.pop()
        print(queue)
        print("---------------------------------------------------------------------------------------------------")

def isFullF():

    if len(queue) == n:
        print('The queue is Full')
        print("---------------------------------------------------------------------------------------------------")

    else:
        print(f'{n-len(queue) } element/elements can be inserted')
        print("---------------------------------------------------------------------------------------------------")

def isEmptyF():

    if len(queue) == 0:
        print('The queue is empty')
        print("---------------------------------------------------------------------------------------------------")

    else:
        print(f'There are {len(queue)} elements in queue')
        print("---------------------------------------------------------------------------------------------------")


n = int(input("Enter the size of the queue:"))
end = int(input("How do you wint to insert elements in the queue\n1.Rear End(<-----)\n2. Front End(----->)\n"))

if end == 1:

    while True:

        inp = int(input("Enter the operation to be performed\n1.Enqueue\n2.Dequeue\n3.Queue is full\n4.Queue is empty\n5.Quit\n"))

        if inp == 1:
            enqueueR()

        elif inp == 2:
            dequeueR()

        elif inp == 3:
            isFullR()

        elif inp == 4:
            isEmptyR()

        elif inp == 5:
            break

        else:
            print('Invalid input')
elif end == 2:

    while True:

        inp = int(input(
            "Enter the operation to be performed\n1.Enqueue\n2.Dequeue\n3.Queue is full\n4.Queue is empty\n5.Quit\n"))

        if inp == 1:
            enqueueF()

        elif inp == 2:
            dequeueF()

        elif inp == 3:
            isFullF()

        elif inp == 4:
            isEmptyF()

        elif inp == 5:
            break

        else:
            print('Invalid input')

else:
    print("Enter Valid Input")
