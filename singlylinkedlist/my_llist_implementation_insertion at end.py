class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def printlist(self):
        tempo=self.head
        while(tempo):
            print(tempo.data)
            tempo=tempo.next
    def insertend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    
            



        
list1=Linkedlist()
list1.head=Node(1)
sec=Node(2)
third=Node(8)
fourth=Node(11)
fifth=Node(12)

list1.head.next=sec
sec.next=third
third.next=fourth
fourth.next=fifth
print("Before insertion at end")
list1.printlist()
print("After insertion at end")
list1.insertend(7)
list1.printlist()
