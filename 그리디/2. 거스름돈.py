'''
[문제]
당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜이 동전이 무한히 존재 한다고 가정한다.
손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈은 N은 항상 10의 배수이다.
'''

'''
[문제 해설]
이 문제는 그리디 알고리즘을 이용해 풀 수 있는 대표적인 문제로 간단한 아이디어만 떠올릴 수 있다면 문제를 해결할 수 있는 문제이다.
그것은 " 가장 큰 화폐 단위부터 돈을 거슬러 주는 것 " 이다.
N원을 거슬러 줘야 할 때, 가장 먼저 500원으로 거슬러 줄 수 있을 만큼 거슬러준다. 그 다음 100원, 50원, 10원 순으로 거슬러 줄 수 있을 만큼 거슬러 주면 
최소의 동전 개수로 모두 거슬러 줄 수 있다.
'''
import time
# [방법 1]

N = 1260
count = 0
start_time = time.time()
while True:
    print(f'{N},{count}')
    if N >= 500:  # 500 보다 높을 경우
        print("500원")
        N -= 500
        count += 1
        print(N)
    elif N < 500 and N >= 100:  # 500 과 100의 사이일 경우
        print("100원")
        N -= 100
        count += 1
        print(N)
    elif N < 100 and N >= 50:
        print("50원")
        N -= 50
        count += 1
        print(N)
    else:
        print("10원")
        N -= 10
        count += 1
        print(N)
        break
end_time = time.time()
print(f'count : {count}, [방법 1]걸린 시간: {end_time-start_time}')

# [방법 2]
N = 1260
count = 0

coin_types = [500, 100, 50, 10]  # 큰 거스름 돈 부터 거슬러주면 횟수가 적으므로 작은 순서대로 나열한다.
start_time = time.time()

for coin in coin_types:
    # print(N//coin)  # 1260/500 = 2 >> 1260//500 = 2   // 연산자는 나눈 몫값만 가져옴.
    count += N//coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    # print(f'1 : {N}')
    N %= coin  # %은 나눈뒤 나머지 값을 반환한다. 즉 1260/500 = 2(몫), 260(나머지)
    # print(f'2 : {N}')
end_time = time.time()
print(f'count : {count}, [방법 2]걸린 시간: {round(end_time-start_time,10)}')