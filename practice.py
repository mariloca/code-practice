'''
We'll define a "root-to-leaf path" to be a sequence of nodes in a tree starting with the root node
and proceeding downward to a leaf (a node with no children). We'll say that an empty tree contains
no root-to-leaf paths. So for example, the following tree has exactly four root-to-leaf paths:
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

Root-to-leaf paths:
   path 1: 5 4 11 7
   path 2: 5 4 11 2
   path 3: 5 8 13
   path 4: 5 8 4 1

For this problem, we will be concerned with the sum of the values of such a path -- for example,
the sum of the values on the 5-4-11-7 path is 5 + 4 + 11 + 7 = 27.

Given a binary tree and a sum, return true if the tree has a root-to-leaf path such that adding up
all the values along the path equals the given sum. Return false if no such path can be found.
(Thanks to Owen Astrachan for suggesting this problem.)

int hasPathSum(struct node* node, int sum) {
'''

'''
Approach:
Use DFS to traverse the tree from root to leaf;
Each time when we find a root, subtract the value from the target sum;
When we find the leaf node, check if the current sum==0, if yes then we find a path, return True
'''
def hasPathSum(root,sum):
    if root==None: return False ##
    #subtract the root.val from the sum
    sum -= root.val
    #base case: when find a leaf node and sum==0
    if root.left==None and root.right==None and sum==0:
        return true
    #recur to root.left or root.right
    return hasPathSum(root.left,sum) or hasPathSum(root.right,sum)

'''
TEST CASES
[5,4,8,11,null,7,2,13,null,null,4,null,1], sum=27, return true
[5,4,8,11,null,7,2,13,null,null,4,null,1], sum=20, return false
[],sum=3, return
'''
