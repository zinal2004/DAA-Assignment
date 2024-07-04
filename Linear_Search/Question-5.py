class Solution:
    def maximumWealth(self, accounts:[[int]]) -> int:
         return max(sum(customer) for customer in accounts)
