# https://leetcode.com/submissions/detail/951705400/

from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wonAll = set()
        lostOne = set()
        lostMoreThanOne = set()
        for match in matches:
            looser = match[1]
            winner = match[0]
            if looser in lostOne:
                lostOne.remove(looser)
                lostMoreThanOne.add(looser)
            elif looser in wonAll:
                wonAll.remove(looser)
                lostOne.add(looser)
            elif looser not in lostMoreThanOne:
                lostOne.add((looser))

            if winner not in lostOne and \
                    winner not in lostMoreThanOne:
                wonAll.add(winner)

        return [sorted(wonAll), sorted(lostOne)]