#https://leetcode.com/submissions/detail/1017975962

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            chars = list(s)
            chars.sort()
            key = ''.join(chars)
            groups[key].append(s)
        result = []
        for group in groups:
            result.append(groups[group])
        return result
