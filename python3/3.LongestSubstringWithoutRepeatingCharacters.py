class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        if s == "":
            return max_len
        sub = s[0]
        for idx in range(1,len(s)):
            if not s[idx] in sub:
                sub += s[idx]
            else:
                max_len = max(max_len,len(sub))
                sub = sub[sub.index(s[idx])+1:] + s[idx]
        max_len = max(max_len,len(sub))
        return max_len
    
if __name__ == "__main__":
    print (Solution().lengthOfLongestSubstring("abcabcbb") == 3)
    print (Solution().lengthOfLongestSubstring("bbbbb") == 1)
    print (Solution().lengthOfLongestSubstring("pwwkew") == 3)
    print (Solution().lengthOfLongestSubstring("") == 0)
    print (Solution().lengthOfLongestSubstring(" ") == 1)
    print (Solution().lengthOfLongestSubstring("au") == 2)
    print (Solution().lengthOfLongestSubstring("dvdf") == 3)
    print (Solution().lengthOfLongestSubstring("aabaab!bb") == 3)
    