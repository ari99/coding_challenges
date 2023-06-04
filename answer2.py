# https://leetcode.com/submissions/detail/963273111/
from collections import defaultdict
from typing import List

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        neighbors = defaultdict(list)
        for e in edges:
            if e[0] not in restricted and e[1] not in restricted:
                neighbors[e[0]].append(e[1])
                neighbors[e[1]].append(e[0])

        stack = [0]
        reachable = 1
        seen = set([0])

        while stack:
            node = stack.pop()
            for n in neighbors[node]:
                if n not in seen:
                    reachable += 1
                    stack.append(n)
                    seen.add(n)

        return reachable
