'''두개의 스택를 이용해 큐 구현하는 방법을 설명해보세요. 구현된 큐 연산의 수행시간도 분석해주세요.'''

class QueueUsingTwoStacks:
    def __init__(self):
        self.stack_in = []  # 요소를 삽입하는 스택
        self.stack_out = []  # 요소를 꺼내는 스택

    def enqueue(self, value):
        self.stack_in.append(value)  # 스택1에 요소 추가

    def dequeue(self):
        if not self.stack_out:  # 스택2가 비어 있으면
            while self.stack_in:  # 스택1에서 스택2로 요소 이동
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:  # 스택2가 여전히 비어 있으면
            raise IndexError("Queue Underflow")  # 큐가 비어 있음
        return self.stack_out.pop()  # 스택2에서 요소 제거

# 테스트 코드
def test_queue():
    q = QueueUsingTwoStacks()

    # Enqueue 연산
    for i in range(5):
        q.enqueue(i)
        print(f"Enqueued {i}")

    # Dequeue 연산
    while True:
        try:
            print(f"Dequeued {q.dequeue()}")
        except IndexError:
            print("Queue is empty.")
            break

test_queue()
