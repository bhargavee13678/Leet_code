class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
       
        count=0
        list_s=list(s)
        list_t=list(t)
        for i in list_s:
            if i in list_t:
                list_t.remove(i)
                count +=1
            else:
                return False
        if count ==len(s) and len(s)==len(t):
            return True
        else:
            return False
        