class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)
        print(f"Pushed: {item}")

    def fun_pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.list.pop()

    def top(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.list[-1]

    def is_empty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)

s = Stack()
s.push(15)
s.push(20)
s.push(38)

print(f"Top element: {s.top()}")  
print(f"Popped element: {s.fun_pop()}")       
print(f"Top element after pop: {s.top()}") 
text=input("Enter: ")
stack=[]
for ch in text:
    stack.append(ch)

rev=""
while stack:
    rev+= stack.pop()
print("String in reverse order: ", rev)    

#====================================== Question#2 ======================================================
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.queue.pop(0)

    def top(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
q = Queue()
q.enqueue("Alice")
q.enqueue("Bob")
q.enqueue("Charlie")

print(f"Front element: {q.top()}")        
print(f"Dequeued element: {q.dequeue()}")  
print(f"Front element after dequeue: {q.top()}") 

#=============================================== Question#3=======================================
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # Target not found

numbers = [6,12,17,23,38,45,77,84,90]  
target_val = int(input("Enter targetted Value: ")) 

result = binary_search(numbers, target_val)

if result != -1:
    print(f"Element {target_val} found at index {result}.")
else:
    print(f"Element {target_val} not found in the array.")