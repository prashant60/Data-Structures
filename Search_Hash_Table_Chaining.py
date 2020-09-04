class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class linked_list:
    def __init__(self):
        self.head=None

    def add(self,val,index):
        if lstt[index] == -1:
            lstt[index]=Node(val,None)
        else:
            curr=lstt[index]
            while curr.next:
                curr=curr.next
            curr.next=Node(val,None)

    def print_hash(self):
        for i in range(l):
            if lstt[i]==-1:
                print(i)
            else:
                print(i, end=" ---> ")
                curr=lstt[i]
                while curr.next:
                    print(curr.data, end=" ---> ")
                    curr=curr.next
                print(curr.data)

    def search(self,val):
        rem=(sum(ord(i) for i in val))
        rem=rem%l
        if lstt[rem] == -1:
            print("Item",val,"not found")
            return
        else:
            curr=lstt[rem]
            while curr:
                if curr.data==val:
                    print("Item",val,"found")
                    return
                else:
                    curr=curr.next
            print("Item",val,"not found")



link=linked_list()
lst=['Prashant','Monika','Urvashi','Hemlata','Naresh','Goel','Bansal','Varun']
l=len(lst)
lstt=[-1]*l
for i in lst:
    x=(sum(ord(j) for j in i))
    link.add(i,x%l)

link.print_hash()


print()
link.search('Hemlata')
link.search('Sparsh')

