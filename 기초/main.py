
# 시간과 메모리 측정
import time
start_time = time.time()  # 측정 시작

list = [1,2,3,45,5]
for i in list:
    for j in list:
        print(i+j)

end_time = time.time()  # 측정 종료
print(f'time : {end_time-start_time}')



# 실수(float) 1개를 입력받아 저장한 후,
# 저장되어 있는 값을 소수점 셋 째 자리에서 반올림하여
# 소수점 이하 둘 째 자리까지 출력하시오.
'''
i = float(input())
print(round(i,2))
'''

# 2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력해보자.
'''
a, b = input(), input()
print(b, a)
'''


# 정수(int) 2개를 입력받아 그대로 출력해보자.
'''
a ,b  = input(), input()
print(a,b)
'''