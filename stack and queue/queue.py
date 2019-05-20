class queue:
    def __init__(self):
        self.items=[]
        return
    def isempty(self):
        return self.items==[]
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        return self.items.pop(0)
    def printitems(self):
        print(self.items)
ss=queue()
l=1
while(l==1):
    x=int(input("Enter the choice:1.ENqueue\t 2.DEqueue \t3.isempty\t4.Display:\n"))

    if(x==1):
        p=input("Enter the item to be pushed")
        ss.enqueue(p)
        ss.printitems()
        


    elif(x==2):
        if(ss.isempty()==True):
            print("Queue is empty")
        else:
            n=ss.dequeue()
            print(n)


    elif(x==3):
        if(ss.isempty()==True):
            print("Queue is empty")
        else:
            print("Queue is not empty")
            ss.printitems()
    else:
        ss.printitems()



    
