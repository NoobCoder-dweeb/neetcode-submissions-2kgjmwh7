class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = None
        if len(nums) == 2:
            return [0,1]

        mapper = {}

        for i in range(len(nums)):
            rem = target - nums[i]
            j = mapper.get(rem, -1)

            if j < 0:
                mapper[nums[i]]= i
            else:
                return sorted([i, j])