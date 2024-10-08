# 일정 크기의 공간이 있어야 한다.
# 파이썬에서는 고정 크기의 배열 없다.
capacity = 5
array = [None] * capacity

# 마지막 데이터 저장 위치
top = -1        # 파이썬에서는 역방향 첨자(index)가 가능한 것에 주의
                # 스택 공간에 음수 첨자 사용을 제한해야 한다.
                # top = -1의 의미는 스택에 데이터 없다.

def push(data):
    #pass
    #top = 1
    global top      # 함수 밖에서 선언된 변수를 사용할 것이다.
    global array
    #print("변수 array id 확인:", id(array))
    #print("변수 top id 확인:", id(top))
    if not isFull():
        top += 1     # 파이썬에는 단항연산자 ++top, top++ 없다.
        array[top] = data

def pop():
    #pass
    global top
    global array
    if isEmpty():
        temp = array[top]
        #array[top] = None       #이 문장은 쓸데없다.
        top -= 1
        return temp
    else:
        return None

def isEmpty():
    #if top = -1:
    #    return True
    #else:
    #    return False
    return top == -1

def isFull():
    #if top == capacity - 1:
    #    return True
    #else:
    #    return False
    return top == (capacity - 1)

if __name__ == "__main__":
    push(10)
    push(20)
    print("스택에서 꺼낸 데이터는 ", pop())
    print(array)