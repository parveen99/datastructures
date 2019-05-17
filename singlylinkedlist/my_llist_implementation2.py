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
    def insertfront(self,data):
        
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node



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
print("Before insertion at front")
list1.printlist()

print("After insertion at front")

list1.insertfront(6)
list1.printlist()
    
