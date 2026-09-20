class Queue:
    def __init__(self,size):
        self.size=size
        self.queue=[0]*size
        self.front=self.rear=-1

    def enqueue(self,item):
        if (self.rear+1)%self.size==self.size:
            print("queue is full")

        elif self.front==-1:
            self.front=self.rear=0
            self.queue[self.rear]=item

        else:
            self.rear=(self.rear+1)% self.size
            self.queue[self.rear]=item

    def dequeue(self):
        if self.front==-1:
            print("queue is empty")

        elif self.front==self.rear:
            print("item deleted was: ",self.queue[self.front])
            self.front=self.rear=-1

        else:
            print("item deleted was: ",self.queue[self.front])
            self.front=(self.front+1)%self.size


    def display(self):
        if self.front==-1:
            print("queue is empty")

        else:
            i=self.front
            print("queue elements: ",end=" ")

            while True:
                print(self.queue[i],end=" ")
                if i==self.rear:
                    break
                i=(i+1)%self.size

            print()

cq=Queue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)  
cq.display()
cq.dequeue()
cq.dequeue()
cq.display()
cq.enqueue(60)
cq.enqueue(70)
cq.display()

