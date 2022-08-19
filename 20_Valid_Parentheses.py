class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')',
        '{','}','[', and ']', determine if the input string is valid.

        An input string is valid if:
            1. Open brackets must be closed by the same type of brakcets.
            2. Open brackets must be closed in the correct order.

        Example:
            s = "(]"
            returns False
            s = "()[]{}"
            returns True
        """
        #create a dictionary with keys = left side and vals = right
        dictionary = {0: None,'{':'}','(':')','[':']'}
        #initialize stack to not pop empty stack
        stack = [0]
        #For each character in in string, if it is a key, add it to the stack.
        #If it is not a key, pop the stack and check if the char is the value of the popped key.
        for char in s:
            if char in dictionary:
                stack.append(char)
            else:
                if dictionary[stack.pop()] != char:
                    return False
        #return if stack is 'empty'
        return stack == [0]