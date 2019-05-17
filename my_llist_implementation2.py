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
list1.printlist()


    
