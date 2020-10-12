class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        res = str(nums[0]) + "/(" + str(nums[1])
        for i in range(2, len(nums)):
            res += "/" + str(nums[i])
        res += ")"
        return res