class Solution:
    def isValid(self, s: str) -> bool:
        openners = ['(', '{', '[']
        closers = [')', '}', ']']
        valid_matching = {openners[i]:closers[i] for i in range(len(openners))}
        #mapping is indices
        # we want something like stack, to pop last element if matching otherwise return False
        length= len(s)
        stack = []
        for i in range(length):
            # if openner
            if s[i] in openners:
                stack.append(s[i])
            elif s[i] in closers:
                # if closer matches openner on top of stack -> pop
                if not stack or s[i] != valid_matching[stack.pop()]:
                    return False
            else:
                # Invalid Input:
                return False
            i += 1
        
        return not stack
        