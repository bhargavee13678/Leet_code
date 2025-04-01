class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        r=s.split()
        last_item=r.pop()
        return (len(last_item))
        