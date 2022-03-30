'''
find max height

'''
from typing import List


class Solution:

  def maxArea(self, height: List[int]) -> int:
    n = len(height)
    if n == 2:
      return min(height)
    l = 0
    r = n - 1
    max_area = 0
    while l < r:
      area = min(height[l], height[r]) * abs(r - l)
      max_area = max(max_area, area)
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1
      print (l, r)
    return max_area


if __name__ == '__main__':
  print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
  print(Solution().maxArea([1, 1]))
  print(Solution().maxArea([2, 3, 10, 5, 7, 8, 9]))
  print(Solution().maxArea([2, 3, 4, 5, 18, 17, 6]))
