
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
stack=Stack()
while True:
    print("What do you wanna do ??")
    print("Press 1 for push")
    print("Press 2 for Pop")
    print("Press 3 for exit")
    do=int(input("What do you want to do?"))
    if do == 1:
        n=int(input("enter a number to push"))
        stack.push(n)
    elif do == 2:
        if stack.is_empty():
            print('Stack is empty.')
        else:
            print("Popped value",stack.pop())
    elif do ==3:
        print("**********************************❤Thank You For Using Us❤! Have nice day ahead!❤**********************************")
        break        
