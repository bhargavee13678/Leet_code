class Solution(object):
    def romanToInt(self, s):
      fetch={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
      result=0
      preval=0
      for char in s:
        value=fetch[char]
        if value>preval:
          result += value -2*preval
        else:
          result += value
        preval=value
      return result
        