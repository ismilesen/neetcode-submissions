class Solution:
    def isValid(self, s: str) -> bool:
        # Check if the length is odd; if so, it's immediately invalid
        if len(s) % 2 != 0:
            return False
            
        stack = []
        # Mapping closing brackets to opening brackets
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element if the stack is not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                # If the mapping doesn't match the top of the stack, it's invalid
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, so push it to the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched perfectly
        return not stack
