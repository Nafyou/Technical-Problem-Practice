class Solution:
    def isValid(self, s: str) -> bool:
        openings = {'(':')','[':']','{':'}'}
        stack = []
        
        for letter in s:
            if letter in openings:
                stack.append(letter)
            else:
                if len(stack) == 0:
                    return False
                if openings[stack.pop()] != letter:
                    return False
        if len(stack) != 0:
            return False
        return True