from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs or strs == []:
            return ""
        preix = strs[0]
        for i in range(1,len(strs)):
            while(preix != ""):
                try:
                    if strs[i].index(preix) == 0:
                        break
                    else:
                        preix = preix[:-1]
                except:
                    preix = preix[:-1]
        return preix
    
if __name__ == "__main__":
    solution = Solution().longestCommonPrefix(["flower","flow","flight"])
    print (solution, solution == 'fl')
    solution = Solution().longestCommonPrefix(["dog","racecar","car"])
    print (solution, solution == '')
    solution = Solution().longestCommonPrefix([""])
    print (solution, solution == '')
    solution = Solution().longestCommonPrefix(["a"])
    print (solution, solution == 'a')
    solution = Solution().longestCommonPrefix(["cir","car"])
    print (solution, solution == 'c')
    solution = Solution().longestCommonPrefix(["dog","racecar","docar"])
    print (solution, solution == '')