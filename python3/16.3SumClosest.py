from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.KSumClosest(nums, 3, target)
      
    def KSumClosest(self, nums: List[int], k: int, target: int) -> int:
        N = len(nums)
        if N == k:
            return sum(nums[:k])

        # target too big
        current = sum(nums[-k:])
        if current <= target:
            return current

        # target too small
        current = sum(nums[:k])
        if current >= target:
            return current
       
        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key = lambda x: x[1])[0]

        closest = current
        for i, x in enumerate(nums[:-k+1]):
            if i>0 and x == nums[i-1]:
                continue
            current = self.KSumClosest(nums[i+1:], k-1, target - x) + x
            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current

        return closest
      
if __name__ == '__main__':
  print(Solution().threeSumClosest([-1,2,1,-4], 1) == 2)
  print(Solution().threeSumClosest([0,0,0], 1) == 0)
  print(Solution().threeSumClosest([0,1,2], 3) == 3)
  print(Solution().threeSumClosest([1,1,-1], 0) == 1)
  print(Solution().threeSumClosest([1,1,1,1], 0) == 3)
  print(Solution().threeSumClosest([1,1,1,0], 100) == 3)
