class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)

        if size <= 2:
            return [0,1]
        res = []
        for i in range(size):
            res.append(i)
            remaining = target - nums[i]

            for j in range(i+1, size):
                if nums[j] == remaining:
                    res.append(j)
                    break
            if len(res) == 2:
                break
            else:
                res.pop()
        
        return res[:]