class TwoStacks:
    def __init__(self, size):
        self.size = size  # 배열의 크기
        self.arr = [None] * size  # 배열 생성
        self.top1 = -1  # 스택 1의 가장 위쪽 인덱스
        self.top2 = size  # 스택 2의 가장 위쪽 인덱스

    def push1(self, value):
        if self.top1 + 1 == self.top2:  # 스택 1과 스택 2의 충돌 검사
            raise OverflowError("Stack 1 Overflow")
        self.top1 += 1  # 스택 1의 top 인덱스 증가
        self.arr[self.top1] = value  # 값 저장

    def push2(self, value):
        if self.top2 - 1 == self.top1:  # 충돌 검사
            raise OverflowError("Stack 2 Overflow")
        self.top2 -= 1  # 스택 2의 top 인덱스 감소
        self.arr[self.top2] = value  # 값 저장

    def pop1(self):
        if self.top1 == -1:  # 스택 1이 비어 있는지 확인
            raise IndexError("Stack 1 Underflow")
        value = self.arr[self.top1]  # 값 저장
        self.top1 -= 1  # top 인덱스 감소
        return value

    def pop2(self):
        if self.top2 == self.size:  # 스택 2가 비어 있는지 확인
            raise IndexError("Stack 2 Underflow")
        value = self.arr[self.top2]  # 값 저장
        self.top2 += 1  # top 인덱스 증가
        return value

def test_two_stacks():
    size = 15  # 배열의 크기
    stacks = TwoStacks(size)  # TwoStacks 클래스 인스턴스 생성
    
    print("Testing Stack 1:")
    # 스택 1에 요소 추가
    for i in range(8):  # 최대 8개 요소 추가
        stacks.push1(i)
        print(f"Pushed {i} into Stack 1")
    
    # 스택 1에서 요소 삭제
    while True:
        try:
            value = stacks.pop1()
            print(f"Popped {value} from Stack 1")
        except IndexError:
            print("Stack 1 is empty.")
            break
    
    print("\nTesting Stack 2:")
    # 스택 2에 요소 추가
    for i in range(8, 14):  # 최대 6개 요소 추가
        stacks.push2(i)
        print(f"Pushed {i} into Stack 2")
    
    # 스택 2에서 요소 삭제
    while True:
        try:
            value = stacks.pop2()
            print(f"Popped {value} from Stack 2")
        except IndexError:
            print("Stack 2 is empty.")
            break

# 테스트 실행
test_two_stacks()
