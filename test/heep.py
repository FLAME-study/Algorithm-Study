
#   1. 새로운 원소 삽입
def insert_heap(heep,value): #A 리스트에 24까지 추가됩니다.
   heap.append(value)
   heapify_up(heap, len(heap) - 1)  # 재정렬

   #2. 재정렬(Hapify up) 

def heapify_up(heap, index):
    parent = (index - 1) // 2
    while index > 0 and heap[index] > heap[parent]:
        heap[index], heap[parent] = heap[parent], heap[index]
        index = parent
        parent = (index - 1) // 2

insert(max_heap, 24) 

print("Max-Heap after inserting 24:", max_heap)

#3. Extract-Max-Heap
#   1. 최대 값 추출
# 3. Extract-Max-Heap
def extract_max(heap):
    if len(heap) == 0:
        return None  # 힙이 비어있으면 None 반환
    max_value = heap[0]  # 루트 노드 (최대 값) 저장
    last_value = heap.pop()  # 마지막 원소 제거
    if len(heap) > 0:
        heap[0] = last_value  # 마지막 원소를 루트에 이동
        max_heapify(heap, 0)  # 힙 재정렬
    return max_value

#  4. 재정렬(Max-Heapify)
def max_heapify(heap, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    
    if left < len(heap) and heap[left] > heap[largest]:
        largest = left
    if right < len(heap) and heap[right] > heap[largest]:
        largest = right
        
    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        max_heapify(heap, largest)  # 재귀 호출

# 최대 값 추출
extracted_max = extract_max(max_heap)
print("Extracted max:", extracted_max)  #결과 84
print("Heap after extracting max:", max_heap) #결과 [24, 22, 19, 10, 5, 17, 6, 9, 3]


#1. 높이가 $h$인 힙의 최대 최소 원소의 수는 각각 얼마인가요?
def heap_element_counts(h):
    # 1. 최대 원소의 수
    max_elements = 1  # 최대 원소는 항상 1개 (루트 노드)

    # 2. 최소 원소의 수
    min_elements = 2 ** h  # 최소 원소의 수는 2^h (리프 노드의 최소 수)
    max_elements_in_last_level = 2 ** h  # 마지막 레벨에서 최대 원소 수
    max_possible_elements = min_elements + (max_elements_in_last_level - 1)  # 최대 원소 수 (리프 노드 포함)
    
    return max_elements, min_elements, max_possible_elements

# 예시: 높이 h가 3일 때
h = 3
max_count, min_count, max_possible_count = heap_element_counts(h)

print(f"높이 {h}인 힙의 최대 원소의 수: {max_count}")
print(f"높이 {h}인 힙의 최소 원소의 수: {min_count}")
print(f"높이 {h}인 힙의 최대 가능 원소의 수: {max_possible_count}")

