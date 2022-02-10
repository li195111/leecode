from quad_tree import QuadTreeNode, List, Grid

class Solution:
    def traverse(self, node:QuadTreeNode):
        out = [[node.isLeaf, node.val]]
        self.traverse_quad_tree(node, lambda v: out.append(v))
        return out
    
    def traverse_quad_tree(self, node:QuadTreeNode, callback):
        if node is None: return
        if not node.topLeft is None:
            callback([node.topLeft.isLeaf, node.topLeft.val])
        if not node.topRight is None:
            callback([node.topRight.isLeaf, node.topRight.val])
        if not node.bottomLeft is None:
            callback([node.bottomLeft.isLeaf, node.bottomLeft.val])
        if not node.bottomRight is None:
            callback([node.bottomRight.isLeaf, node.bottomRight.val])
        if not node.topLeft is None and not node.topLeft.isLeaf:
            self.traverse_quad_tree(node.topLeft, callback)
        if not node.topRight is None and not node.topRight.isLeaf:
            if node.topLeft.isLeaf:
                self.empty(4, callback)
            self.traverse_quad_tree(node.topRight, callback)
        if not node.bottomLeft is None and not node.bottomLeft.isLeaf:
            if node.topLeft.isLeaf and node.topRight.isLeaf:
                self.empty(8, callback)
            elif node.topRight.isLeaf:
                self.empty(4, callback)
            self.traverse_quad_tree(node.bottomLeft, callback)
        if not node.bottomRight is None and not node.bottomRight.isLeaf:
            if node.topLeft.isLeaf and node.topRight.isLeaf and node.bottomLeft.isLeaf:
                self.empty(12, callback)
            elif node.topRight.isLeaf and node.bottomLeft.isLeaf:
                self.empty(8, callback)
            elif node.bottomLeft.isLeaf:
                self.empty(4, callback)
            self.traverse_quad_tree(node.bottomRight, callback)
    
    def empty(self, times, callback):
        for _ in range(times):
            callback(None)
            
    def construct(self, grid: List[List[int]]) -> QuadTreeNode:
        if grid is None: return
        flat = [j for i in grid for j in i]
        val = int(1 in flat)
        isLeaf = int((val and not 0 in flat) or sum(flat)==0)
        if isLeaf:
            return QuadTreeNode(val, isLeaf)
        n = len(grid)
        return QuadTreeNode(val, 
                            isLeaf,
                            self.construct([row[:n//2] for row in grid[:n//2]]),
                            self.construct([row[n//2:] for row in grid[:n//2]]),
                            self.construct([row[:n//2] for row in grid[n//2:]]),
                            self.construct([row[n//2:] for row in grid[n//2:]]))
    
if __name__ == "__main__":
    s = Solution()
    
    grid = [[0,1],[1,0]]
    ans = [[0,1],[1,0],[1,1],[1,1],[1,0]]
    c = s.traverse(s.construct(grid))
    print (f"{Grid(grid)}\nConstruct: {c} {c == ans}")
    
    grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    ans = [[0,1],[1,1],[0,1],[1,1],[1,0],None,None,None,None,[1,0],[1,0],[1,1],[1,1]]
    c = s.traverse(s.construct(grid))
    print (f"{Grid(grid)}\nConstruct: {c} {c == ans}")

    grid = [[1,1],[1,1]]
    ans = [[1,1]]
    c = s.traverse(s.construct(grid))
    print (f"{Grid(grid)}\nConstruct: {c} {c == ans}")

    grid = [[0]]
    ans = [[1,0]]
    c = s.traverse(s.construct(grid))
    print (f"{Grid(grid)}\nConstruct: {c} {c == ans}")

    grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
    ans = [[0,1],[1,1],[1,0],[1,0],[1,1]]
    c = s.traverse(s.construct(grid))
    print (f"{Grid(grid)}\nConstruct: {c} {c == ans}")
