class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)  # Minimum possible capacity
        right = sum(weights)  # Maximum possible capacity
        
        while left < right:
            mid = (left + right) // 2
            curr_days = 1  # Start with 1 day
            curr_weight = 0
            
            for w in weights:
                if curr_weight + w > mid:
                    curr_days += 1
                    curr_weight = w
                else:
                    curr_weight += w
            
            if curr_days > days:
                left = mid + 1
            else:  # curr_days <= days
                right = mid
                
        return left