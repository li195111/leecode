from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      n = len(nums)
      while val in nums:
        nums.remove(val)
        n -= 1
      return n

if __name__ == '__main__':
  print(Solution().removeElement([3,2,2,3],3))
  print(Solution().removeElement([0,1,2,2,3,0,4,2],2))
