class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False
        MAP = {'(':')','[':']','{':'}'}
        idx = 0
        opened = [s[idx]]
        while idx < n-1:
            try:
                nexted = s[idx+1]
                if opened and nexted == MAP[opened[-1]]:
                    opened.pop(-1)
                elif nexted in MAP:
                    opened.append(nexted)
                else:
                    return False
            except:
                return False
            idx += 1
        return opened == []
            
if __name__ == "__main__":
    print (Solution().isValid("()"))
    print (Solution().isValid("()[]{}"))
    print (Solution().isValid("(]"))
    print (Solution().isValid("{[]}"))
    print (Solution().isValid("([)]"))
    print (Solution().isValid("(){}}{"))
    print (Solution().isValid("(([]){})"))
    print (Solution().isValid("("))
    print (Solution().isValid("(("))
    print (Solution().isValid("))"))
