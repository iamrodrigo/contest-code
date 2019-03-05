class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL(object):
    def __init__(self):
        self.root = None

    def createNode(self, value):
        return Node(value)

    def rotateRight(self, node):
        left = node.left
        rightLeftChild = left.right
        node.left = rightLeftChild
        node.height = self.retrace(node)
        left.height = self.retrace(left)
        left.right = node


        return left

    def rotateLeft(self, node):
        right = node.right
        leftRightChild = right.left
        node.right = leftRightChild
        right.left = node

        node.height = self.retrace(node)
        right.height = self.retrace(right)

        return right

    def insert(self, value):
        self.root = self.insert_implementation(self.root, value)

    def balance(self, node):
        balance = self.heightOfChildren(node)

        if balance  > 1:
            # Right Right
            if self.height(node.right) >= 0:
                self.rotateRight(node)
            # Left Right
            else:
                node.left = self.rotateLeft(node.left)
                node = self.rotateRight(node)
        elif balance < -1:
            # Left Left
            if self.height(node.left) <= 0:
                node = self.rotateLeft(node)
            # Right Left
            else:
                node.right = self.rotateRight(node.right)
                node = self.rotateLeft(node)

        return node

    def insert_implementation(self, node, value):
        if not node:
            node = self.createNode(value)
        elif value > node.value:
            node.right = self.insert_implementation(node.right, value)
        else:
            node.left = self.insert_implementation(node.left, value)

        node.height = self.retrace(node)
        return self.balance(node)

    def height(self, node):
        return node.height if node else 0

    def retrace(self, node):
        return max(self.height(node.left), self.height(node.right)) + 1

    def heightOfChildren(self, node):
        return self.height(node.left) - self.height(node.right)

    def search_recursive(self, value):
        return self.search_recursive_implementation(value, self.root)

    def search_recursive_implementation(self, value, node):
        if node is None:
            return node
        elif(node.value == value):
            return node
        elif(node.value > value):
            return self.search_recursive_implementation(value, node.left)
        else:
            return self.search_recursive_implementation(value, node.right)


    def search_iterative(self, value):
        node = self.root

        while node is not None:
            if node.value == value:
                return node
            elif node.value > value:
                node = node.left
            else:
                node = node.right

    def preorder(self):
        self.preorder_implementation(self.root)
        print '\n'

    def preorder_implementation(self, node):
        if node is None:
            return

        print node.value,
        self.preorder_implementation(node.left)
        self.preorder_implementation(node.right)

    def inorder(self):
        self.inorder_implementation(self.root)
        print '\n'

    def inorder_implementation(self, node):
        if node is None:
            return

        self.inorder_implementation(node.left)
        print node.value,
        self.inorder_implementation(node.right)

    def postorder(self):
        self.postorder_implementation(self.root)
        print '\n'

    def postorder_implementation(self, node):
        if node is None:
            return

        self.postorder_implementation(node.left)
        self.postorder_implementation(node.right)
        print node.value,

    def depth(self):
        return self.depth_implementation(self.root)

    def depth_implementation(self, node):
        pass
        #reimplement

    def breadthFirst(self):
        nodes = [self.root]

        while len(nodes):
            node = nodes.pop(0)
            print node.value

            if node.left is not None:
                nodes.append(node.left)

            if node.right is not None:
                nodes.append(node.right)

    def delete(self, value):
        self.root = self.delete_implementation(self.root, value)

    def delete_implementation(self, node, value):

        if not node:
            return node

        if node.value > value:
            node.left = self.delete_implementation(node.left, value)
        elif node.value < value:
            node.right = self.delete_implementation(node.right, value)
        else:
            tempNode = node
            if not node.left and not node.right:
                node = None
            elif not node.right:
                node = node.left
            elif not node.left:
                node = node.right
            else:
                parentNode = node
                tempNode = node.left
                while tempNode and tempNode.right:
                    parentNode = tempNode
                    tempNode = tempNode.right

                parentNode.right = None
                tempNode.left = node.left
                tempNode.right = node.right
                node , tempNode = tempNode, node

            del tempNode

        node.height = self.retrace(node)
        return self.balance(node)

a = -1

avl = AVL()
#avl.insert(9)
#avl.insert(1)
#avl.insert(10)
#avl.insert(0)
#avl.insert(5)
#avl.insert(11)
#avl.insert(-1)
#avl.insert(2)
#avl.insert(6)


"""
0                   9
                /         \
1             1           10
            /     \     /     \
2          0       5  11      NULL    
         /   \    /  \   
3       -1  NULL  2    6
"""

# RR Insertion
avl.insert(10) #A
avl.insert(20) #Ar
avl.insert(5)  #B
avl.insert(7)  #Br
avl.insert(3)  #C
avl.insert(1)  #Cl, balance activated


while a != 0:
    print "Binary Search Tree"
    print "1. Insert (Recursive)"
    print "2. Insert (Iterative)"
    print "3. Search (Recursive)"
    print "4. Search (Iterative)"
    print "5. Preorder"
    print "6. Inorder"
    print "7. Postorder"
    print "8. Depth"
    print "9. Height"
    print "10. Breadth First"
    print "11. Delete node"
    print "12. Min"
    print "13. Max"
    print "0. Exit"
    a = input("Choose an option: ")

    if a == 1:
        avl.insert(input("Introduce value to append: "))
    if a == 2:
        pass
        #avl.insert_iterative(input("Introduce value to append: "))
    if a == 3:
        print 'YES' if avl.search_recursive(input("Introduce value to search: ")) else 'NO'
    if a == 4:
        print 'YES' if avl.search_iterative(input("Introduce value to search: ")) else 'NO'
    if a == 5:
        avl.preorder()
    if a == 6:
        avl.inorder()
    if a == 7:
        avl.postorder()
    if a == 8:
        print avl.depth()
    if a == 9:
        print avl.height()
    if a == 10:
        avl.breadthFirst()
    if a == 11:
        avl.delete(input("Introduce node to delete: "))


