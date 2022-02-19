class Solution:
    def myAtoi(self, s: str) -> int:
        d = ''
        for w in s.strip():
            if (d and w in '+-') or (w not in '0123456789+-'):
                break
            d += w
        if d in '+-':
            return 0
        return max((-2**31),min(2**31-1,int(d)))


if __name__ == "__main__":
    pass
    ans = Solution().myAtoi("42")
    print (ans == 42)
    ans = Solution().myAtoi("   -42")
    print (ans == -42)
    ans = Solution().myAtoi("4193 with words")
    print (ans == 4193)
    ans = Solution().myAtoi("words and 987")
    print (ans == 0)
