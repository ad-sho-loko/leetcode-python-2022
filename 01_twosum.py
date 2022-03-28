class Solution1:
    def twoSum(self, nums: [int], target: int) -> [int]:
        already = {}
        for i, n in enumerate(nums):
            if n in already:
                return [already[n - target], i]
            already[n - target] = i
        return []
