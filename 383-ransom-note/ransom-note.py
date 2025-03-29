class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        letter_count_magazine = {}
        
        for char in magazine:
            letter_count_magazine[char] = letter_count_magazine.get(char, 0) + 1
        
        for char in ransomNote:
            if char not in letter_count_magazine or letter_count_magazine[char] == 0:
                return False
            letter_count_magazine[char] -= 1
        
        return True
        