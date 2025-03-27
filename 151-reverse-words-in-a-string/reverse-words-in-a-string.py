class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split() 
        lists = s[::-1]  
        
        return ' '.join(lists) 
        
        sentence=' '.join([word for word in lists])

        return sentence
        