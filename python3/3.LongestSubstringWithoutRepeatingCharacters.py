class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = s.split()
        for subs in ss:
            sub = subs[0]
            
        return
    
if __name__ == "__main__":
    print (Solution().lengthOfLongestSubstring("abcabcbb") == 3)
    print (Solution().lengthOfLongestSubstring("bbbbb") == 1)
    print (Solution().lengthOfLongestSubstring("pwwkew") == 3)
    