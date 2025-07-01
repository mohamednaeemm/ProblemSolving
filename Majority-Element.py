class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsSet = {}
        n = len(nums) // 2
        for num in nums:
            numsSet[num] = numsSet.get(num, 0) + 1
            if numsSet[num] > n:
                return num
        return max(numsSet, key=numsSet.get)