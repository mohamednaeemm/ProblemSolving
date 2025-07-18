class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        L = m - 1
        R = n - 1
        F = len(nums1) - 1

        while R >= 0:
            if L >= 0 and nums1[L] >= nums2[R]:
                nums1[F] = nums1[L]
                L -= 1
            else:
                nums1[F] = nums2[R]
                R -= 1
            F -= 1
        
        