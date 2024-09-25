'''
브루트 포스 문제

양의 정수가 쓰여있는 N장의 카드가 있다.(3 <= N <= 100)
이 때 3장의 카드 합은 M을 넘지 않으면서 M과 최대한 가까운 값이어야 한다.
단, 10 <= M <=300,000

출력해야하는 결과
N장의 카드 중 3장을 뽑고, 뽑은 3장의 카드의 합을 출력

'''


N, M = map(int, input().split()) 
cards = list(map(int, input().split())) 
total_sum = 0

for i in range(N):
    for p in range(i + 1, N):
        for k in range(p + 1, N):
            current_sum = cards[i] + cards[p] + cards[k]
            if current_sum <= M and current_sum > total_sum:
                total_sum = current_sum

print(total_sum)