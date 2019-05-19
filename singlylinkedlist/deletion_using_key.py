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
    def delete(self,data):
        key=data
        temp=self.head
        if(temp is not None):
            if(temp.data==key):
                self.head=temp.next
                temp=None
                return


        while(temp is not None):
            if(temp.data==key):
                break
            prev=temp
            temp=temp.next

        if(temp==None):
            return


        prev.next=temp.next
        temp=None
        











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
print("Before deletion")
list1.printlist()
print("After deletion")
list1.delete(8)
list1.printlist()
