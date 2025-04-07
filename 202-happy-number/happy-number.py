class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        
        def get_next(num):
            return sum(int(digit)**2 for digit in str(num))
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1  