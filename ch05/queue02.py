capacity = 5
array = [None] * (capacity + 1)

# 초기상태
rear = 0
front = 0

def isFull():
    global rear
    #return rear ==capacity
    if rear == capacity:
        return True
    else:
        print("Queue가 꽉참")
        return False

def isEmpty():
    global front
    #return front == capacity
    if front == capacity:
        return True
    else:
        print("Queue가 빔")
        return False

def enqueue(data):
    global rear
    global array
    if not isFull:
        rear += 1                  # 마지막에 데이터를 넣은 위치
        array[rear] = data
    else:
        print("FULL")

def dequeue():
    global front
    global array
    if not isEmpty:
        front += 1                 # 마지막에 데이터를 꺼낼 위치
        return array[front] 
    else:
        print("EMPTY")

if __name__ == "__main__":
    enqueue(10)
    enqueue(20)
    enqueue(30)
    enqueue(40)
    enqueue(50)
    enqueue(50)
    print(array)