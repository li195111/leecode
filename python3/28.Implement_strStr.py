class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
      
if __name__ == '__main__':
  print(Solution().strStr('hello', 'll') == 2)
  print(Solution().strStr('aaaaa', 'bba') == -1)
  