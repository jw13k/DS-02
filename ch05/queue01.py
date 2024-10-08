capacity = 5
array = [None] * (capacity + 1)
# 데이터 관리 포인트
# rear - 데이터를 큐에 입력하는 위치
# front - 데이터를 큐에서 꺼내는 위치

# 초기상태
rear = 0        # array에서 0번쨰는 사용하지 않을 것이다.
front = 0

# 큐에 데이터 넣기
rear = rear + 1
array[rear] = 10    # 큐에 데이터 10을 추가

rear = rear + 1
array[rear] = 20    # 큐에 데이터 20을 추가

# 큐 확인
print(array)
# 마지막 데이터 추가 위치
print("마지막 데이터 추가 위치는 ", rear)

# 큐에서 데이터 꺼내기
front = front + 1
temp = array[front]
print("꺼내온 데이터는 ", temp)