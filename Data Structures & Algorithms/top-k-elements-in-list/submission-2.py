class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        frequency = Counter(nums)
        most_frequency = [v[0] for v in frequency.most_common(k)]

        return most_frequency