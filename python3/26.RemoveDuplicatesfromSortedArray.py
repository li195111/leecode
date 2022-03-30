from typing import List


class Solution:

  def removeDuplicates(self, nums: List[int]) -> int:
    try:
      for i in range(len(nums) - 1):
          while nums[i] in nums[i + 1:]:
            nums.pop(i)
    except IndexError:
      pass
    return len(nums)


if __name__ == '__main__':
  print(Solution().removeDuplicates([1, 1, 2]))
  print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
