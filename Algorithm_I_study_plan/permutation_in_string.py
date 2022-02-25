from typing import Dict

class Solution:
    @staticmethod
    def _get_letter_counts_dict(s: str) -> Dict[str, int]:
        """
        Counts the number of occurences of each letter in s
        """
        result = {}
        for char in s:
            try:
                result[char] += 1
            except KeyError:
                result[char] = 0
        return result
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_letter_counts = self._get_letter_counts_dict(s1)
        left, right = 0, len(s1)
        
        while right <= len(s2):
            if self._get_letter_counts_dict(s2[left:right]) == s1_letter_counts:
                return True
            left += 1
            right += 1
            
        return False