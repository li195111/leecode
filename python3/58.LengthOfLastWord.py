class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
      
if __name__ == '__main__':
  print(Solution().lengthOfLastWord('Hello World') == 5)
  print(Solution().lengthOfLastWord('   fly me   to   the moon  ') == 4)
  print(Solution().lengthOfLastWord('luffy is still joyboy') == 6)
