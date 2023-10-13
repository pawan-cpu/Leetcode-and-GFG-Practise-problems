#User function Template for python3

class Solution:
    def __init__(self):
        self.floor_value = -1  # Initialize the floor_value to -1.

    def find_floor_value(self, node, target_value):
        if not node:
            return

        if node.data == target_value:
            self.floor_value = target_value
            return

        if node.data < target_value:
            # If the node's value is less than the target value, update the floor_value if needed.
            self.floor_value = max(self.floor_value, node.data)
            self.find_floor_value(node.right, target_value)
        else:
            # If the node's value is greater than the target value, explore the left subtree.
            self.find_floor_value(node.left, target_value)

    def floor(self, root, target_value):
        self.find_floor_value(root, target_value)
        return self.floor_value


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def insert(tree, val):
    if(tree==None):
        return Node(val)
    if(val< tree.data):
        tree.left= insert(tree.left, val)
    elif(val > tree.data):
        tree.right= insert(tree.right, val)
    return tree
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr= list(map(int, input().split()))
        root = None
        for k in arr:
            root=insert(root, k)
        s=int(input())
        obj = Solution()
        print(obj.floor(root,s))
# } Driver Code Ends