import node as n
import math

floor = math.floor

class Heap():

    def __init__(self, values=[]):
        '''
        Creates new Binary Min Heap of Node objects
        Nodes can be added by passing the costs as a list into the constructor or by using the add method
        '''
        self.heap = []
        for i in values:
            self.add(i)

    def add(self, val):
        '''
        This method adds nodes to the heap, either passed as individual numeric values OR as a list of numeric values
        '''

        if type(val) == list:
            for v in val:
                self.add(v)

            return

        self.heap

        i = len(self.heap)

        if type(val) == int:
            self.heap.append(n.Node(val))
        elif type(val) == n.Node:
            self.heap.append(val)

        if len(self.heap) == 1:
            return

        while True:
            if i == 0:
                return

            if self.heap[i].cost < self.heap[floor((i-1)/2)].cost:
                temp = self.heap[i]
                self.heap[i] = self.heap[floor((i-1)/2)]
                self.heap[floor((i-1)/2)] = temp
                i = floor((i-1)/2)

            else:
                return

    def __heapify(self, index):
        root = index
        right_sub = 2 * index + 2
        left_sub = 2 * index + 1

        if left_sub < len(self.heap) and self.heap[left_sub].cost < self.heap[root].cost:
            root = left_sub
            
        if right_sub < len(self.heap) and self.heap[right_sub].cost < self.heap[root].cost:
            root = right_sub


        if root != index:
            temp = self.heap[root]
            self.heap[root] = self.heap[index]
            self.heap[index] = temp

            self.__heapify(root)

    def pop(self):
        '''
        This method removes and returns the smallest element of the heap
        '''
        val = self.heap[0]

        self.heap = [self.heap[-1]] + self.heap[1:len(self.heap)-1]

        self.__heapify(0)

        return val

    def peak(self):
        '''
        This method returns the root element of the heap
        '''
        val = self.heap[0]

        return val

    def print_heap(self):
        '''
        This method is used to print out the heap, showing each nodes cost
        '''
        s = '['
        for h in self.heap:
            s = s + str(h.cost) + ', '

        if s != '[':
            s = s[:-2] + ']'
        else:
            s = s + ']'

        print(s)


def main():
    '''
    Test Code, only runs when this python file is run directly
    '''
    h = Heap()
    h.print_heap()
    h.add([6,14,45,78,18,47,53,83,91,81,77,84,99,64])
    h.print_heap()
    print(h.peak())
    h.add(3)
    h.print_heap()
    h.pop()
    h.print_heap()



if __name__ == '__main__':
    main()