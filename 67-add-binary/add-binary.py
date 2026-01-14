class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1 
        j = len(b) - 1
        carry = 0
        final = []

        while i>=0 or j>=0 or carry:
            val_a = int(a[i]) if i >=0 else 0
            val_b = int(b[j]) if j >=0 else 0

            total = val_a +val_b +carry
            carry = total //2
            final.append(str(total % 2))

            i -=1
            j -=1
        
        return "".join(final[::-1])