"""
https://leetcode.com/problems/min-stack/submissions/1999657432/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""
class Node():
    def __init__(self, val, min_val):
        self.val = val
        self.min_val = min_val

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(Node(val, val))
        else:
            min_val = min(self.stack[-1].min_val, val)
            self.stack.append(Node(val, min_val))

    def pop(self) -> None:
       if self.stack:
           self.stack.pop() 

    def top(self) -> int:
       if self.stack:
           return self.stack[-1].val 
       else:
           return None

    def getMin(self) -> int:
        return self.stack[-1].min_val if self.stack else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # return -3
minStack.pop()
print(minStack.top())    # return 0
print(minStack.getMin()) # return -2