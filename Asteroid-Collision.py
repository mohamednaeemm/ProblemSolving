class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            while True:
                if not stack or ast > 0 or stack[-1] < 0:
                    stack.append(ast)
                    break
                
                elif ast < 0 and stack[-1] > 0:
                    if abs(ast) == stack[-1]:
                        stack.pop()
                        break
                    elif abs(ast) > stack[-1]:
                        stack.pop()
                        continue
                    else:
                        break
                else:
                    stack.append(ast) 
                    break
        
        return stack