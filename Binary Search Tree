class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def calculate_sum(self):
        s=0
        if self.left:
            s+=self.left.calculate_sum()
        if self.right:
            s+=self.right.calculate_sum()

        return s+self.data

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.post_order_traversal()
        if self.right:
            elements+=self.right.post_order_traversal()
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements=[]
        
        elements.append(self.data)

        if self.left:
            elements+=self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()

        return elements

    def delete1(self,val):
        if val==self.data:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete1(min_val)
        
        elif val<self.data:
            if self.left:
                self.left=self.left.delete1(val)
        else:
            if self.right:
                self.right=self.right.delete1(val)

        return self

    def delete2(self,val):
        if val==self.data:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            max_val=self.left.find_max()
            self.data=max_val
            self.left=self.left.delete2(max_val)
        
        elif val<self.data:
            if self.left:
                self.left=self.left.delete2(val)
        else:
            if self.right:
                self.right=self.right.delete2(val)

        return self

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())

    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:",numbers_tree.calculate_sum())
    print("Post order traversal gives this sorted list:",numbers_tree.post_order_traversal())
    print("Pre order traversal gives this sorted list:",numbers_tree.pre_order_traversal())
   # numbers_tree.delete1(20)
    numbers_tree.delete2(34)
    print(numbers_tree.in_order_traversal())
