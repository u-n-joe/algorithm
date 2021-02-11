'''
[문제]
'큰 수의 법칙'은 일반적으로 통계 분야에서 다루어지는 내용이지만 정훈이는 본인만의 방식으로 다르게 사용하고 있다.
동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 법칙의 특징이다.

예를 들어 순서대로 2, 4, 5, 4, 6으로 이루어진 배열이 있을 때 M이 8이고, K가 3이라고 가정하자.
이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과
는 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5인 46이 된다.

단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다. 예를 들어 순서 대로
3, 4, 3, 4, 3으로 이루어진 배열이 있을 때 M이 7이고 K가 2라고 가정하자. 이 경우 두 번째
원소에 해당하는 4와 네 번째 원소에 해당하는 4를 번갈아 두번씩 더하는 것이 가능하다. 결과적으로
4 + 4 + 4 + 4 + 4 + 4 + 4인 28이 도출된다.

배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 정훈이의 큰 수의 법칙에 따른 결과를 출력하시오.

[입력 조건]
1. 첫째 줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어지며 각 자연수는 공백으로 구분한다.

2. 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1이상 10000이하의 수로 주어진다.

3. 입력으로 주어지는 K는 항상 M보다 작거나 같다.

[출력 조건]
첫째 줄에 큰 수의 법칙에 따라 더해진 답을 출력

[입력 예시]
5 8 3
2 4 5 4 6

[출력 예시]
46
'''

# [방법 1]
'''
# 입력으로 주어지는 K는 항상 M보다 작거나 같다. 즉, [ M >= K ]
N = 5
M = 8
K = 3
list = [2, 4, 5, 4, 6]
count = 0
sort_list = sorted(list, reverse=True)
while True:
    for i in range(1, M + 1):  # for문 1~8
        if i % (K + 1) == 0:
            count += sort_list[1]
        else:
            count += sort_list[0]
    break

print(count)
'''

# [방법 2]
'''
# n m k 를 공백구분해서 받기
n, m, k = map(int, input().split())

# n개의 수를 공백으로 구분해서 입력받기.
data = list(map(int, input().split()))

data.sort()  # 숫자 정렬
first = data[n - 1]  # 가장 큰수
second = data[n - 2]  # 두번째 큰수
result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:  # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때 마다 1씩 감소
    if m == 0:  # m 이 0이라면 반복문 탈출
        break
    result += second # 두번째로 큰 수를 한번 더하기.
    m -= 1 # 더할때 씩 빼기.
print(result)
'''

# [방법 3]
'''
list1 = [6,4,3,2,5]
a = sorted(list1,reverse=True)
first = a[0]
second = a[1]
m = 8
k = 3

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:  # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때 마다 1씩 감소
        print(m)
    if m == 0:  # m 이 0이라면 반복문 탈출
        break
    result += second # 두번째로 큰 수를 한번 더하기.
    m -= 1 # 더할때 씩 빼기.
print(result)
'''

# [방법 4]
'''
list1 = [6, 4, 3, 2, 5]
a = sorted(list1, reverse=True)
first = a[0]
second = a[1]
m = 8
k = 3

count = int(m / (k + 1)) * k  # (8/4)*3 = 6 번
#count += m % (k + 1)  # 8%4 = 0

result = 0
result += (count) * first  # 가장 큰수 더하기
result += (m - count) * second  # 두번째 큰수 더하기.

print(result)
'''
