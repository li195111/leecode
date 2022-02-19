class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = {}
        i = 0
        while i < len(s):
            c = 0
            while c < numRows-1 and i < len(s):
                r = 0
                while r < numRows and i < len(s):
                    if c == 0 or r == numRows-1-c:
                        if r in rows:
                            rows[r] += s[i]
                        else:
                            rows[r] = s[i]
                        i += 1
                    else:
                        rows[r]+=''
                    r += 1
                c += 1
        return ''.join(rows.values())
        
if __name__ == "__main__":
    pass
    ans = Solution().convert("PAYPALISHIRING",3)
    print (ans == 'PAHNAPLSIIGYIR')
    ans = Solution().convert("PAYPALISHIRING",4)
    print (ans == 'PINALSIGYAHRPI')
    ans = Solution().convert("A",1)
    print (ans == 'A')
