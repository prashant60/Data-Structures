class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class linked:
    def __init__(self):
        self.head=None
        self.head2=None

    def create(self,lst):
        if self.head is None:
            self.head=Node(lst[0],None)

        for i in range(1,len(lst)):
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=Node(lst[i],None)

    def reverse(self):
        while self.head:
            if self.head2 is None:
                self.head2=Node(self.head.data,None)
                self.head=self.head.next
            else:
                self.head2=Node(self.head.data,self.head2)
                self.head=self.head.next

    def print_fwd(self):
        if self.head is None:
            return
        curr=self.head
        while curr.next:
            print(curr.data, end=" ---> ")
            curr=curr.next
        print(curr.data)
        print()

    def print_rev(self):
        if self.head2 is None:
            return
        curr=self.head2
        while curr.next:
            print(curr.data, end=" ---> ")
            curr=curr.next
        print(curr.data)
        print()

lst=[1,2,3,4,5,6,7,8,544,43,2324,124]
link=linked()
link.create(lst)
print("The original List is : ")
link.print_fwd()
link.reverse()
print()
print("The reversed List is : ")
link.print_rev()
