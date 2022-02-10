from typing import Optional
from btree import BTreeNode, BTree

class Solution:
    def diameterOfBinaryTree(self, root: Optional[BTreeNode]) -> int:
        self.ans = 0
        self.diameters = {}
        self.diameter(root)
        return self.ans
        
    def diameter(self,node:BTreeNode):
        if (not node is None) and (not node.val is None):
            l = self.diameter(node.left)
            r = self.diameter(node.right)
            if (not node.left is None) and (not node.left.val is None):
                l = self.diameters[node.left] + 1
            if (not node.right is None) and (not node.right.val is None):
                r = self.diameters[node.right] + 1
            self.diameters[node] = max([l,r])
            ans = sum([l,r])
            self.ans = max([self.ans,ans])
            return ans
        return 0
    
if __name__ == "__main__":
    ans = 3
    tree = BTree.from_root([1,2,3,4,5])
    n = Solution().diameterOfBinaryTree(tree.root)
    print (f"Diameter: {n} {n == ans}")
    
    ans = 0
    tree = BTree.from_root([1])
    n = Solution().diameterOfBinaryTree(tree.root)
    print (f"Diameter: {n} {n == ans}")
    
    ans = 3
    tree = BTree.from_root([4,1,None,2,None,3])
    n = Solution().diameterOfBinaryTree(tree.root)
    print (f"Diameter: {n} {n == ans}")
    
    ans = 1
    tree = BTree.from_root([1,2])
    n = Solution().diameterOfBinaryTree(tree.root)
    print (f"Diameter: {n} {n == ans}")
    
    ans = 2
    tree = BTree.from_root([4,2,None,1,3])
    n = Solution().diameterOfBinaryTree(tree.root)
    print (f"Diameter: {n} {n == ans}")

    ans = 8
    tree = BTree.from_root([4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2])
    n = Solution().diameterOfBinaryTree(tree.root)
    print (f"Diameter: {n} {n == ans}")
    
    pass
