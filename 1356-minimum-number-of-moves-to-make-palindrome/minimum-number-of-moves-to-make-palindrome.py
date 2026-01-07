class Solution(object):
    def minMovesToMakePalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        match = 0
        s = list(s)
        start = 0
        end = len(s)-1

        while start < end :
            k = end
            
            while k > start and s[k] != s[start]:
                k -= 1
            
            if k == start:
                s[start],s[start+1] = s[start + 1],s[start]
                match += 1
            
            else:
                while k < end:
                    s[k], s[k+1] = s[k+1], s[k]
                    k += 1
                    match += 1

                start += 1
                end -= 1
        return match 