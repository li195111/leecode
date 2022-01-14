class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= -2**31 and x <= 2**31-1:
            sl = list(str(x))
            if '-' == sl[0]:
                return False
            return int(''.join(sl[::-1])) == x
        else:
            return False
        
if __name__ == "__main__":
    result = Solution().isPalindrome(132)
    print (result)