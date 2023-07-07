from typing import List


class Solution:

  def letterCombinations(self, digits: str) -> List[str]:
    if not digits:
      return []
    digit_map = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
    results = []
    digits = [digit_map[digi] for digi in digits]
    
    def add_loop(prefix, i):
      results = []
      for w in digits[i]:
        if len(digits)-1 > i:
          results.extend(add_loop(prefix + w, i+1))
        else:
          results.append(prefix + w)
      return results

    results = add_loop('', 0)
    return results
  
if __name__ == '__main__':
  print(Solution().letterCombinations('23') ==
        ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
  print(Solution().letterCombinations('') == [])
  print(Solution().letterCombinations('2') == ['a', 'b', 'c'])
