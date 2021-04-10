# python3


class StackWithMax():
    def __init__(self):
        self.__stack = []
        # auxilary stack that keeps track of maximums 
        self.max_stack = []
    
    def isEmpty(self):
        return True if len(self.__stack) == 0 else False

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
            return -1
        return self.max_stack[-1]



class Queue_with_Stacks():
    # see https://stackoverflow.com/questions/69192/how-to-implement-a-queue-using-two-stacks
    def __init__(self):
        self.stack1 = StackWithMax()
        self.stack2 = StackWithMax()
    def enqueue(self, a):
        # enter new item to the queue
        
        self.stack1.Push(a)

    def dequeue(self):
        # get item that was first in queue

        if self.stack1.isEmpty() and self.stack2.isEmpty():

           raise AssertionError

        elif not self.stack2.isEmpty():
            return self.stack2.Pop()
        
        else:

            while not self.stack1.isEmpty():
                self.stack2.Push(self.stack1.Pop())

            return self.stack2.Pop() 


    def get_max(self):
        return max(self.stack1.Max(), self.stack2.Max())

def max_sliding_window_naive(sequence, m):
    maximums = []
    Q = Queue_with_Stacks()
    for i in sequence[:m]:
        Q.enqueue(i)

    maximums.append(Q.get_max())
    
    for i in range(m, len(sequence)):
        Q.enqueue(sequence[i])
        Q.dequeue()

        maximums.append(Q.get_max())

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

