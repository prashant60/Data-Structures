class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class linked_list:
    def __init__(self):
        self.head=None

    def print(self):
        if self.head is None:
            print("Empty List")
            return
        else:
            curr=self.head
            while curr:
                print(curr.data,"--->", end=" ")
                curr=curr.next

    def begin(self,data):
        new_node=Node(data,self.head)
        self.head=new_node

    def end(self,data):
        if self.head is None:
            new_node=Node(data,None)
            self.head=new_node
            return
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=Node(data,None)

    def middle(self,pos,data):
        if self.head is None or pos==0:
            ll.begin(data)
        else:
            c=0
            curr=self.head
            while curr:
                if c==pos-1:
                    new_node=Node(data, curr.next)
                    curr.next=new_node
                    break
                else:
                    curr=curr.next
                    c+=1
            else:
                print("Index value out of range") 
                raise Exception("Index out of range")

    def delet(self,pos):
        if self.head is None:
            print("List is Empty")
        elif pos==0:
            self.head=self.head.next
        else:
            c=0
            curr=self.head
            while curr.next:
                if c==pos-1:
                    curr.next=curr.next.next
                    break
                else:
                    c+=1
                    curr=curr.next
            else:
                print("Index value out of range") 
                raise Exception("Index out of range")

    def ins_lst(self,listt):
        self.head=None
        for i in listt:
            self.end(i)

ll=linked_list()
ll.delet(3)
ll.begin("Dog")
ll.begin("Cat")
ll.begin("Horse")
ll.end("Cow")
ll.end("Bird")
ll.middle(2,"Goat")
ll.delet(4)
ll.print()
print()
lstt=["My", "Name", "Is", "Prashant"]
ll.ins_lst(lstt)

ll.print()  
