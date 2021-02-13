class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

#insert node in the tree
def insert(root,val):
    if root == None:
        return Node(val)
    if val > root.val:
        root.right = insert(root.right, val)
    else:
        root.left = insert(root.left, val)
    return root


def size(root):
    if root==None: return 0
    left=size(root.left)
    right=size(root.right)
    return left+right+1

def maxDepth(root):
    if root==None: return 0
    left=size(root.left)
    right=size(root.right)
    if left>=right:
        return left
    else:
        return right

def minValueIterative(root):
    while root.left:
        root=root.left
    return root.val

def minValueRecursive(root):
    #base case, find the left most leaf Node
    if root.left==None:
        return root.val
    return minValueRecursive(root.left)

#inorder print tree
def printTree(root):
    if root==None:return
    printTree(root.left)
    print(root.val)
    printTree(root.right)

#postorder print tree
def printPostorder(root):
    if root==None:return
    printPostorder(root.left)
    printPostorder(root.right)
    print(root.val)

def hasPathSum(root, sum):
    #base case:reach leaf node
    if root==None: return False
    sum-=root.val
    #find path:reach leaf node and sum==0
    if root.left==None and root.right==None and sum==0:
        return True
    #check either left or right child of the root
    return hasPathSum(root.left,sum) or hasPathSum(root.right,sum)

#8



def mirror(root):
    if root==None: return False
    tmp=root.right
    root.right=root.left
    root.left=tmp
    mirror(root.left)
    mirror(root.right)

def doubleTree(root):
    if root==None: return False
    '''
    if root.left:
        newlchild=Node(root.val)
        oldlchild=Node(root.left.val)
        print('newlchild',newlchild.val,'oldlchild',oldlchild.val)
    '''
    print(root.val)
    doubleTree(root.left)
    doubleTree(root.right)

#build a tree
root = Node(11)
root=insert(root,8)
root=insert(root,19)
root=insert(root,4)
root=insert(root,9)
root=insert(root,12)
root=insert(root,20)

'''
print('size of the tree', size(root))
print('max depth of the tree', maxDepth(root))
print('min value of the tree', minValueRecursive(root))
printTree(root)
printPostorder(root)
result=hasPathSum(root,23)
print(result)

mirror(root)
printTree(root)
'''
doubleTree(root)
printTree(root)
