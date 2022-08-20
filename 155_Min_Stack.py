class MinStack:
    """
    Design a stack that supports push, pop, top, and
    retrieving the minimum element in constant time.

    Implement the MinStack class:
        MinStack() initializes the stack object.
        void push(int val) pushes the element val onto the stack.
        void pop() removes the element on the top of the stack.
        int top() gets the top element of the stack.
        int getMin() retrieves the minimum element in the stack.
    
    You must implement a solution with O(1) time complexity for each function
    """
    def __init__(self):
        #initialize stack as a list
        self.q = []

    def push(self, val: int) -> None:
        #
        curMin = self.getMin()
        if curMin == None or val < curMin:
            curMin = val
        #store [(val,curMin)] in stack so each element has currentMin at the time it is pushed
        self.q.append((val,curMin))

    def pop(self) -> None:
        #calls pop list pop() function
        self.q.pop()

    def top(self) -> int:
        #returns top of stack
        #if empty, return None
        if len(self.q) == 0:
            return None
        #else return [0] value of top of stack (val).
        else:
            return self.q[-1][0]

    def getMin(self) -> int:
        #if empty, return None
        if len(self.q) == 0:
            return None
        #else, return top's second element (curMin)
        else:
            return self.q[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()