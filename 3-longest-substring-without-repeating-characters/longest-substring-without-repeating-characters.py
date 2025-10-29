class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index_map = {}

        window_start = 0
        max_len = 0

        for window_end in range(len(s)):
            char = s[window_end]
            if char in char_index_map and char_index_map[char] >= window_start:
                window_start = char_index_map[char] + 1
            char_index_map[char] = window_end

            current_len = window_end - window_start + 1
            max_len = max(current_len,max_len
            )
        return max_len
            