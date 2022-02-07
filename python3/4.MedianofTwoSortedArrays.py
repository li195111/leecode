from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sort = sorted(nums1 + nums2)
        n = len(sort)
        m = n // 2
        if n % 2 == 0:
            return (sort[m-1] + sort[m]) / 2
        return sort[m] / 1
    
if __name__ == "__main__":
    print (Solution().findMedianSortedArrays(nums1 = [1,3], nums2 = [2]) == 2)
    print (Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]) == 2.5)
    print (Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4,6]) == 3)
    print (Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4,6,7]) == 3.5)
    