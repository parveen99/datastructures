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
    def insertmid(self,prevnode,newdata):
        if prevnode is  None:
            print("prev node not there in linked list")
            return
        new_node=Node(newdata)
        new_node.next=prevnode.next
        prevnode.next=new_node







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
print("Before insertion at middle")
list1.printlist()

list1.insertmid(list1.head.next,3)
print("After insertion at middle")
list1.printlist()
