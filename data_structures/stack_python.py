__author__ = 'liusong'
import heapq


class Stack1:
    """
    First in, last out.
    Last in, first out.
    """

    def __init__(self, test_list):
        self.test_list = test_list
        self.push_list = []
        self.pop_list = []

    def push(self):
        print "Start to push: {0}".format(self.test_list)
        for i in self.test_list:
            self.push_list.append(i)
            print self.push_list
        return self.push_list

    def pop(self):
        t_list = self.push_list
        print "Start to pop: {0}".format(t_list)
        len_push = len(t_list)

        j = len_push - 1
        for i in range(len_push):
            self.pop_list.append(t_list[j])
            j -= 1
            print self.pop_list
        return self.pop_list

    def pop2(self):
        print "\nStart to pop: {0}".format(self.push_list)
        for i in range(len(self.push_list)):
            self.push_list.pop()
            print self.push_list
        return self.push_list


class Queue:
    def __init__(self, size=5):
        self.size = size
        self.queue = []
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.rear == 0

    def isFull(self):
        return self.rear == self.size

    def add(self, obj):
        if self.isFull():
            raise Exception("The queue is Full now!")
        else:
            self.queue.append(obj)
            self.rear += 1
            print self.rear

    def pop(self):
        if self.isEmpty():
            raise Exception("The queue is Empty now!")
        else:
            self.queue.pop(0)
            self.rear -= 1
            return self.queue

    def show(self):
        print(self.queue)


def test_Stack1():
    test_l = [1, 2, 3, 4, 5, 6]
    object_stack = Stack1(test_l)

    print "=================="
    print object_stack.push_list, object_stack.pop_list
    print "=================="
    object_stack.push()
    object_stack.pop2()


def test_heapq():
    heap = []
    data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    heapq.heappush(data, 55)
    print data
    heapq.heappop(data)
    print data


def test_Queue():
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    q.show()
    q.add(4)
    q.show()
    q.add(5)
    q.show()
    #q.add(6)
    #q.show()

    # pop test
    for i in range(5):
        q.pop()
        q.show()
    q.pop()
    q.show()

if __name__ == "__main__":
    #test_Stack1()
    #test_heapq()
    test_Queue()


