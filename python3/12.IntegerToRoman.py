class Solution:
  def intToRoman(self, num: int) -> str:
    roman_maps = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
    roman = ''
    rep = num
    rem = num
    for n, s in roman_maps.items():
      rep = rem // n
      rem = rem % n
      roman += s * rep
    return roman
  
if __name__ == '__main__':
  print(Solution().intToRoman(3))
  print(Solution().intToRoman(58))
  print(Solution().intToRoman(1994))
  # print(Solution().intToRoman(2580))
  # print(Solution().intToRoman(3999))
