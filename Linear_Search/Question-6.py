class Solution:
    def targetIndices(self, nums: [int], target: int) -> [int]:
       return [i for i, x in enumerate(sorted(nums)) if x == target]
