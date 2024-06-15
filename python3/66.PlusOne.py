from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        insert = False
        for i in range(n-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                insert = False
                break
            else:
                digits[i] = 0
                if i == n-1:
                    insert = True
        if insert:
            digits.insert(0, 1)
        return digits

if __name__ == '__main__':
    s = Solution()
    digits = [1,2,3]
    out = s.plusOne(digits)
    assert out == [1,2,4]
    digits = [4,3,2,1]
    out = s.plusOne(digits)
    assert out == [4,3,2,2]
    digits = [9]
    out = s.plusOne(digits)
    assert out == [1,0]
    digits = [9,9]
    out = s.plusOne(digits)
    assert out == [1,0,0]
    print("All passed")