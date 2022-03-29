from typing import List
import math

class Solution:
  
  def sort_j_side(self, i, j, s, e, d):
    for j in range(s,e,d):
      self.output[i][j] = self.seq[self.si]
      self.si += 1
    return i, j
    
  def sort_i_side(self, i, j, s, e, d):
    for i in range(s,e,d):
      self.output[i][j] = self.seq[self.si]
      self.si += 1
    return i, j
  
  def stringSequence2square(self, seq:List[str]):
    self.seq = seq
    n = len(self.seq)
    r = int(math.sqrt(n))
    assert r**2 == n
    self.output = [['-1' for _ in range(r)] for _ in range(r)]
    self.si = 0
    i = 0
    j = 0
    
    for l in range(r,r//2,-1):
      i, j = self.sort_j_side(i, j, r-l, l, 1)
      i, j = self.sort_i_side(i, j, r-l+1, l, 1)
      i, j = self.sort_j_side(i, j, l-2, r-l-1, -1)
      i, j = self.sort_i_side(i, j, l-2, r-l, -1)

    max_l = max([len(s) for s in self.seq])
    return '\n'.join([' '.join([' ' *(max_l-len(rv)) + rv for rv in row]) for row in self.output])
  
if __name__ == "__main__":
  print (Solution().stringSequence2square([str(i) for i in range(81)]))