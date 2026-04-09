class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            if num not in frequency:
                frequency[num] = 0
            
            frequency[num]+=1
        
        ordered_frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

        res = []
        counter = 0
        for num, _ in ordered_frequency.items():
            res.append(num)
            counter += 1

            if counter == k:
                break


        return res