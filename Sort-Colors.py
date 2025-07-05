class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                self.swap(nums, mid, low)
                low += 1
                mid += 1

            elif nums[mid] == 2:
                self.swap(nums, mid, high)
                high -= 1

            else:
                mid += 1

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
