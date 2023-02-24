stack=[]
choice=0
e=0
def push_stack(w):
    stack.append(e)
    print(f"Your element {e} has been pushed")
def pop_stack():
    stack.pop()
    print("The element has been poped")

while True:
    print("What do you wanna do ??")
    print("1: Push")
    print("2: Pop")
    print("3: Peek")
    print("4: Display")
    print('5: Exit")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        e=int(input("Enter the number you wanna push:"))
        push_stacks(e)
    elif choice ==2:
        pop_stack()
    elif choice == 3:
        for i in range(len(stack),,-1):
            if stack != []:
                print (stack[1])
            else:
                print("Your stack is empty please push some element")
    elif choice ==4:
        for i in range((len(stack))-1-1,-1,-1):
            print(stk[i])
    elif choice ==5 :
        return
    else :
        print ("that's a  wrong choice , please choose btw 1 to 5")
    
