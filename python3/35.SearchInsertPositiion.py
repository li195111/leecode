from typing import List
from bisect import bisect_left

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # return bisect_left(nums, target)
        if target in nums:
          return nums.index(target)
        l = 0
        r = len(nums) -1
        while l <= r:
          p = l + (r-l) // 2
          if nums[p] == target:
            return p
          elif nums[p] < target:
            l = p + 1
          else:
            r = p - 1
        return l
      
if __name__ == '__main__':
  print(Solution().searchInsert([1,3,5,6], 5) == 2)
  print(Solution().searchInsert([1,3,5,6], 2) == 1)
  print(Solution().searchInsert([1,3,5,6], 7) == 4)
