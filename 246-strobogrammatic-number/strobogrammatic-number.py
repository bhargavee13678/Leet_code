class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dictionary = {"1":"1", "6":"9", "9":"6", "8":"8", "0":"0"}

        pointer_1 = 0
        pointer_2 = len(num)-1

        while pointer_1 <= pointer_2:
            if num[pointer_1] not in dictionary:
                return False
            
            if dictionary[num[pointer_1]] != num[pointer_2]:
                return False
            
            pointer_1 += 1
            pointer_2 -= 1
        
        return True