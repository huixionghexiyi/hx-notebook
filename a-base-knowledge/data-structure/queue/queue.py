class MyCircularQueue:
    '''
    设计循环队列的思路：FIFO 先进先出
    用两个指针head和tail，初始化为-1；
    每入队一个数，tail+1；
    每出队一个数，head+1；如果head==tail，说明队列为空了，都置为-1；
    若head == -1 ，则为空；
    tail+1==head，则满了。
    '''
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.tail = -1
        self.head = -1
        self.data = [-1]*k
        self.size = k


    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail=(self.tail+1)%self.size
        self.data[self.tail]=value
        return True
        
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        self.head = (self.head+1)%self.size
        return True


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        self.head =(self.head)%self.size
        return self.data[self.head]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        self.tail = (self.tail)%self.size
        
        return self.data[self.tail]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head == -1
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.tail+1)%self.size == (self.head)%self.size