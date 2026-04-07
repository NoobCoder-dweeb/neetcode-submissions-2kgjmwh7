class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)

        if size <= 2:
            return [0,1]
        
        res =[]
        hmap = {}

        for i, val in enumerate(nums):
            
        # check if there is a complement
            remaining = target - val
            j = hmap.get(remaining, -1)

            if j == -1:
                hmap[val] = i
            else:
                return sorted([i,j])

        # if not then add to hmap 
                


        return res