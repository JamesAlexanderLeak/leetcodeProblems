from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate the value of an arithmetic expression in
        Reverse Polish Notation.
        Valid operators are +,-,*, and /. Each operand may
        be an integer or another expression.

        Example:
        tokens = ["2","1","+","3","*"]
        output: 9
        Explanation: ((2 + 1) * 3) = 9
        """
        #solve using stack
        stack = []
        #iterate through tokens getting chars
        for c in tokens:
            #if cases for operands
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            #only store integers in stack, pop if an arithmetic
            #operator is seen and push result onto stack.
            else:
                stack.append(int(c))
        return stack[0]