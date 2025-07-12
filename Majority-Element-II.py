class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        dicNums = {}
        n = len(nums)
        ans = []
        
        for num in nums:
            dicNums[num] = dicNums.get(num, 0) + 1
        
        for key in dicNums:
            if dicNums[key] > n // 3:
                ans.append(key)
        
        return ans