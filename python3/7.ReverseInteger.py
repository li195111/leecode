'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

Constraints:
-2^31 <= x <= 2^31 - 1
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x >= -2**31 and x <= 2**31-1:
            sl = list(str(x))
            if '-' == sl[0]:
                res = -int(''.join(sl[1::][::-1]))
            else:
                res = int(''.join(sl[::-1]))
            if res >= -2**31 and res <= 2**31-1:
                return res
            else:
                return 0
        else:
            return 0
    
if __name__ == "__main__":
    result = Solution().reverse(1534236469)
    print (result)