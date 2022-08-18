from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the
        price of a given stock on the ith day.
        You want to maximize your profit by choosing a single day
        to buy one stock and choosing a different day in the future
        to sell that stock.
        Return the maximum profit you can achieve from this transaction.
        If you cannot achieve any profit, return 0.
        """
        #set max to 0 and min to infinity
        max_profit, min_price = 0,float('inf')
        #for each price in prices
        for price in prices:
            #set min_price to the minimum of current price and min price
            min_price = min(min_price,price)
            profit = price - min_price
            #get maximum between profit and max_profit
            max_profit = max(profit,max_profit)
        #return max profit
        return max_profit