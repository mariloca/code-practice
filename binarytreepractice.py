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

def maxValue(root):
    while root.right:
        root=root.right
    return root.val

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
def printPaths(root):



def mirror(root):
    if root==None: return False
    tmp=root.right
    root.right=root.left
    root.left=tmp
    mirror(root.left)
    mirror(root.right)

def doubleTree(root):
    if root==None: return
    #creat a copy of current node
    newleft=Node(root.val)
    #save lchild and rchild of current node
    oldleft=root.left
    oldright=root.right
    #make old left child to new node's left
    newleft.left=oldleft
    #make new node to current lchild
    root.left=newleft
    #use old children in the recursive to avoid maximum recursion depth exceeded
    doubleTree(oldleft)
    doubleTree(oldright)

def sameTree(root1,root2):
    if root1==None or root2==None or root1.val!=root2.val:
        return False
    else:
        return True
    return sameTree(root1.left,root2.left) and sameTree(root1.right,root2.right)

def countTrees(n):
    #base case
    if n==0 or n==1: return 1
    count=0
    for i in range(1,n+1):
        count+=countTrees(i-1)*countTrees(n-i)
    return count

'''
Parent to lchild: pass parent.val as new max
Parent to rchild: pass parent.val as new min
lchild to parent: pass lchild.val as new min
rchild to parent: pass rchild.val as new max
'''
def isBST(root):
    if root==None:return True
    maxV=float('inf')
    minV=float('-inf')
    return isBSThelper(root,minV,maxV)
def isBSThelper(root,min,max):
    if root==None: return True
    if root.val<=min or root.val>=max:
        return False
    return isBSThelper(root.left, min,root.val) and isBSThelper(root.right,root.val,max)

#build a tree
root = Node(11)
root=insert(root,8)
root=insert(root,19)
root=insert(root,4)
root=insert(root,9)
root=insert(root,12)
root=insert(root,20)

root2=Node(12)
root2=insert(root2,7)
root2=insert(root2,8)


root3 = Node(11)
root3=insert(root3,8)
root3=insert(root3,19)
root3=insert(root3,4)
root3=insert(root3,9)
root3=insert(root3,12)
root3=insert(root3,20)
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
doubleTree(root)
printTree(root)
result=sameTree(root,root2)
print(result)
res=countTrees(10)
print(res)
print('max value of the tree', maxValue(root))
'''
print('is BST', isBST(root2))
