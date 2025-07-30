class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = [] 

        for curr_day in range(n):
            while stack and temperatures[curr_day] > temperatures[stack[-1]]:
                prev_day = stack.pop() 
                ans[prev_day] = curr_day - prev_day  
            stack.append(curr_day)  
        
        return ans