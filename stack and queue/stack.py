class stack:
    def __init__(self):
        self.items=[]
        return
    def isempty(self):
        return self.items==[]
    def pushh(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def printitems(self):
        print(self.items)
ss=stack()
l=1
while(l==1):
    x=int(input("Enter the choice:1.Push\t 2.pop \t3.isempty\t4.Display:\n"))

    if(x==1):
        p=input("Enter the item to be pushed")
        ss.pushh(p)
        ss.printitems()
        


    elif(x==2):
        if(ss.isempty()==True):
            print("Stack is empty")
        else:
            n=ss.pop()
            print(n)


    elif(x==3):
        if(ss.isempty()==True):
            print("Stack is empty")
        else:
            print("Stack is not empty")
            ss.printitems()
    else:
        ss.printitems()



    
