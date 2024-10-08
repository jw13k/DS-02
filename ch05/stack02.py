# 일정 크기의 공간이 있어야 한다.
# 파이썬에서는 고정 크기의 배열 없다.
class StackClass:
    #파이썬에서 클래스의 생성자
    def __init__(self, cap):      #생성자가 파라미터 하나를 갖는다.
        self.capacity = cap
        self.array = [None] * self.capacity

        # 마지막 데이터 저장 위치
        self.top = -1        # 파이썬에서는 역방향 첨자(index)가 가능한 것에 주의
                # 스택 공간에 음수 첨자 사용을 제한해야 한다.
                # top = -1의 의미는 스택에 데이터 없다.

    def push(self, data):
        #print("변수 top id 확인:", id(top))
        if not self.isFull():
            self.top += 1     # 파이썬에는 단항연산자 ++top, top++ 없다.
            self.array[self.top] = data

    def pop(self):
        if not self.isEmpty():
            temp = self.array[self.top]
            #array[top] = None       #이 문장은 쓸데없다.
            self.top -= 1
            return temp
        else:
            return None

    def isEmpty(self):
        #if top = -1:
        #    return True
        #else:
        #    return False
        return self.top == -1

    def isFull(self):
        #if top == capacity - 1:
        #    return True
        #else:
        #    return False
        return self.top == (self.capacity - 1)

if __name__ == "__main__":
    #print("main의 top 변수 id:", id(top))
    #print("main의 array 변수 id:", id(array))
    # 클래스의 객체(인스턴스) 생성
    myStack = StackClass(5)
    myStack.push(10)
    myStack.push(20)
    print("스택에서 꺼낸 데이터는 ", myStack.pop())
    print(myStack.array)
