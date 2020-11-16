class Node:
    def __init__(self, val, min):
        self.val = val
        self.min = min

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        

    def push(self, x: int) -> None:
        if len(self.data) == 0:
            self.data.append(Node(x, x))
        else:
            top = self.top_node()

            if x < top.min:
                self.data.append(Node(x, x))
            else:
                self.data.append(Node(x, top.min))
        
    def pop(self) -> None:
        self.data.pop().val

    def top(self) -> int:
        return self.top_node().val
    
    def top_node(self):
        return self.data[len(self.data)-1]

    def getMin(self) -> int:
        return self.top_node().min