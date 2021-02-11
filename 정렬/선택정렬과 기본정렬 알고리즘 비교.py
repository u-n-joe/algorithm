import time
from random import randint

# 배열에 1~100 사이의 랜덤한 정수 10000개 삽입
array = []
for _ in range(10000):
    array.append(randint(1, 100))

start_time = time.time()  # 선택 정렬 알고리즘 측정 시작

# 선택 정렬 알고리즘
for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):  # i+1 에서 부터 array 의 길이까지
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

end_time = time.time()  # 선택 정렬 알고리즘 측정 종료
print(f' 선택정렬 시간 : {end_time - start_time}')

# 배열 초기화
array = []
for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()

# 기본정렬 라이브러리 성능 측정
sorted(array)

end_time = time.time()
print(f' 기본정렬 시간 : {end_time-start_time}')

