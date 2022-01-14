from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            v = target - nums[i]
            if v in d:
                return [d[v],i]
            else:
                d[nums[i]] = v
                
    
if __name__ == "__main__":
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    out = solution.twoSum(nums, target)
    print (out)
    nums = [3,2,4]
    target = 6
    out = solution.twoSum(nums, target)
    print (out)
    nums = [3,3]
    target = 6
    out = solution.twoSum(nums, target)
    print (out)
    nums = [3,2,3]
    target = 6
    out = solution.twoSum(nums, target)
    print (out)