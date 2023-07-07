from typing import List

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    i = 1
    n = len(nums)
    c = max_sum = nums[0]
    while i < n:
      c = max(nums[i], nums[i] + c)
      max_sum = max(max_sum, c)
      i += 1
    return max_sum

if __name__ == '__main__':
  print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
  print(Solution().maxSubArray([1]) == 1)
  print(Solution().maxSubArray([5,4,-1,7,8]) == 23)
  print(Solution().maxSubArray([-1]) == -1)
