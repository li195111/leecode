class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if not s or n == 1:
            return s
        p = s[0]
        lp = len(p)
        i = 0
        while i < n:
            j = i+1
            try:
                p_idx = s[j:].index(s[i])
                while lp < n:
                    j = j+p_idx+1
                    word = s[i:j]
                    wn = len(word)
                    if word[:wn//2] == word[wn-wn//2:][::-1] and lp < wn:
                        p = word
                        lp = len(p)
                    p_idx = s[j:].index(s[i])
            except ValueError:
                pass
            i+=1
        return p

if __name__ == "__main__":
    # 對稱、左右一致
    ans = Solution().longestPalindrome("babad")
    print (ans == 'bab' or ans == 'aba')
    ans = Solution().longestPalindrome("cbbd")
    print (ans == 'bb')
    ans = Solution().longestPalindrome("banana")
    print (ans == 'anana')
    ans = Solution().longestPalindrome("bbbbbb")
    print (ans == 'bbbbbb')
    ans = Solution().longestPalindrome("bad")
    print (ans == 'b')
    ans = Solution().longestPalindrome("ac")
    print (ans == 'a')
