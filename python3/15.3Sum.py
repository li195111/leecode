from typing import List
from collections import Counter
from bisect import bisect_left
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
          return []
        res = []
        c = Counter(nums)
        nums = sorted(c)
        if nums[0] > 0 or nums[-1] < 0:
          return []
        
        n = len(nums)
        if c[0] >= 3:
          res.append([0,0,0])
        
        for k, v in c.items():
          if v >= 2 and -2*k in c and k != 0:
            res.append([k,k,-2*k])
        # Three different, [-, +, +], [-, -, +], [-, 0, +]
        for i, n in enumerate(nums):
          if n >= 0 or i == n - 2:
            break
          two_sum_target = -n
          min_middle_val = two_sum_target - nums[-1]
          max_middle_val = two_sum_target / 2
          left = bisect_left(nums, min_middle_val, i+1)
          right = bisect_left(nums, max_middle_val, left)
          for v in nums[left:right]:
            if two_sum_target - v in c:
              res.append([n,v,two_sum_target-v])
        return res
      
if __name__ == '__main__':
  print(Solution().threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]])
  print(Solution().threeSum([]) == [])
  print(Solution().threeSum([0]) == [])
  print(Solution().threeSum([1]) == [])
  print(Solution().threeSum([2,3,1]) == [])
  print(Solution().threeSum([0,0,0]) == [[0,0,0]])
