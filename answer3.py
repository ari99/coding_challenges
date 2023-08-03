from typing import List

# https://leetcode.com/submissions/detail/1005708616

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currentMinPrice = float("inf")
        currentMaxPrice = 0
        for price in prices:
            if price < currentMinPrice:
                #print("setting min/max " + str(price))
                currentMinPrice = price
                currentMaxPrice = price

            if price> currentMaxPrice:
                #print("setting max " + str(price))
                currentMaxPrice = price

                if currentMaxPrice-currentMinPrice > maxProfit:
                    maxProfit = currentMaxPrice-currentMinPrice
                #print("current max is " + str(maxProfit))
        return maxProfit