# https://www.programiz.com/dsa/algorithm 
# Algorithm 1
# num1 = int(input("declare number 1 :"))
# num2 = int(input("declare number 2 :"))

# sum = num1 + num2   
# print("sum is " + str(sum))

#############################################
# Algorithm 2
# a = int(input("declare a number 1 :"))
# b = int(input("declare b number 2 :"))
# c = int(input("declare c number 3 :"))

# if a>b :
#     if a >c:
#         print("a is the largest number")
#     else :
#         print(" c is the largest number")
# else :
#     if b >c :
#         print("b is the largest number")
#     else :
#         print("c is the greatest number") 

#############################################
# Algorithm 3
import math
# a = input("declare a number :")
# b = input("declare b number :")
# c = input("declare c number :")
# d = (b*b) - 4*a*c

# if d >= 0 :
#     r1 = (-b+ math.sqrt(d)) /2
#     r2 = (-b - math.sqrt(d)) /2
# else :  
#     rp = -b/2*a
#     ip = math.sqrt((-d)/2*a) # i didnt understand this math section
#     print(rp + ip)


#############################################
# Algorithm 4
#############################################
# Algorithm 5
#############################################
# Algorithm 6

##########################################################################################
# stack implementation in python

# creating a stack
# def create_stack():
#     stack = []
#     return stack

# # creating an empty stack
# def check_empty(stack):
#     return len(stack) == 0

# # adding items into the stack   
# def push(stack,item):
#     stack.append(item)
#     print("pushed item : " + item)

# # removing an element from the stack
# def pop(stack):
#     if(check_empty(stack)):
#         return "stack is empty"
#     return stack.pop()

# stack = create_stack()
# push(stack,str(1))
# push(stack,str(2))
# push(stack,str(3))
# push(stack,str(4))
# print("popped item " + pop(stack))
# print("stack after popping an element: " + str(stack))


##########################################################################################
# queue implementation in python

class Queue:
    def __init__(self):
        self.queue = []

    # add an element
    def enqueue(self,item):
        self.queue.append(item)

    # remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    
    # display the queue
    def display(self):
        print(self.queue)
    def size(self):
        return(len(self.queue))
    
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display()

q.dequeue()

print("after removing an element")
q.display()