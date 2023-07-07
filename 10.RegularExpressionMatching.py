import re
class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    res = re.match(p,s)
    if res:
      return s==res.group(0)
    return False

if __name__ == '__main__':
  print(Solution().isMatch('aa','a') == False)
  print(Solution().isMatch('aa','a*') == True)
  print(Solution().isMatch('ab','.*') == True)
  print(Solution().isMatch('ab','.*c') == False)
