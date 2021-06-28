'''
분해 : for 문 이용, 1~100까지 더함, 누적 합이 1000이상이 되는 시작 시점, 합 변수

패턴인식 : for문을 이용하여 1~100을 더한다.
           누적 합계가 1000이상이 되는 시점을 구한다.

추상화 : for문을 초기값 1 끝값 101, 간격 1 로 설정한다.
         if 조건문을 사용하여 1000이상이 되는 시점을 만들어낸다.
         합변수 = 0 
알고리즘(의사코드)

합변수 = 0 
for i in range(1,101,1):
   합변수 = 합변수 + i
   if sum >= 1000:
      break로 멈춤
1~100의 합에서 최초로 1000이 넘는 위치 출력
'''

# 자동화

sum = 0
for i in range(1,101,1):
    sum = sum + i
    if sum >= 1000:
        break
print(f"1~100의 합에서 최초로 1000이 넘는 위치: {i}")

   
