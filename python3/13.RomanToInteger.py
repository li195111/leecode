
ROMAN = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
class Solution:
    def romanToInt(self, s: str) -> int:
        sl = list(s)
        ns = len(sl)
        i = 0
        idx = 0
        while idx < ns:
            r = ROMAN[sl[idx]]
            if idx+1 < ns:
                nr = ROMAN[sl[idx+1]]
                if nr > r:
                    r = nr - r
                    idx += 1
            i += r
            idx += 1
        return i
    
if __name__ == "__main__":
    result = Solution().romanToInt("III")
    print (result)