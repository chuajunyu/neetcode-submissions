class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '}': '{', ']': '[', ')': '('
        }
        stack = []
        for b in s:
            if b in ']})':
                if stack and stack[-1] == pairs[b]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(b)

        return len(stack) == 0 
            
                
        