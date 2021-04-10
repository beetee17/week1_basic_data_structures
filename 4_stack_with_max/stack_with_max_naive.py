#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        # auxilary stack that keeps track of maximums 
        self.max_stack = []
        
    def Push(self, a):
        self.__stack.append(a)
       
        if len(self.max_stack) == 0:
            # add to max_stack if list is empty or if value is at least the current max
            self.max_stack.append(a)
        elif a >= self.max_stack[-1]:
            self.max_stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        item = self.__stack.pop()

        # remove from max_stack if popped value was equal to current max 
        if item == self.max_stack[-1]:
            self.max_stack.pop()
            
        return item
        

    def Max(self):
        if len(self.__stack) == 0:
            raise AssertionError
        return self.max_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
