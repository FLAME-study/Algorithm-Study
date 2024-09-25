'''2. 큐의 `Underflow`와 `Overflow`를 검사하는 연산을 작성해주세요.'''

class Queue:
    def __init__(self, size):
        self.size = size  # 큐의 최대 크기
        self.queue = [None] * size  # 큐를 저장할 배열
        self.front = 0  # 큐의 앞쪽 인덱스
        self.rear = -1  # 큐의 뒤쪽 인덱스
        self.count = 0  # 현재 큐의 요소 개수

    def is_full(self):
        return self.count == self.size  # 큐가 가득 찼는지 검사

    def is_empty(self):
        return self.count == 0  # 큐가 비어있는지 검사

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue Overflow")  # 큐가 가득 차면 예외 발생
        self.rear = (self.rear + 1) % self.size  # 큐의 뒤쪽 인덱스 업데이트
        self.queue[self.rear] = value  # 큐에 요소 추가
        self.count += 1  # 요소 개수 증가

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow")  # 큐가 비어있으면 예외 발생
        value = self.queue[self.front]  # 큐의 앞쪽 요소를 꺼내옴
        self.front = (self.front + 1) % self.size  # 큐의 앞쪽 인덱스 업데이트
        self.count -= 1  # 요소 개수 감소
        return value

# 테스트 코드
def test_queue():
    size = 5
    q = Queue(size)

    # Enqueue 연산
    for i in range(size):
        q.enqueue(i)
        print(f"Enqueued {i}")

    # 큐가 가득 찼을 때 예외 처리
    try:
        q.enqueue(5)  # 큐가 가득 차면 오버플로우 발생
    except OverflowError as e:
        print(e)

    # Dequeue 연산
    while not q.is_empty():
        print(f"Dequeued {q.dequeue()}")

    # 큐가 비어있을 때 예외 처리
    try:
        q.dequeue()  # 큐가 비어 있으면 언더플로우 발생
    except IndexError as e:
        print(e)

test_queue()
