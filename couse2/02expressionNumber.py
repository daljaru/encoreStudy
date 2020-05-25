
'''
Finn은 요즘 수학공부에 빠져 있습니다.
수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

1 = 1
2 = x
3 = 1+2         1로 시작하는 첫수... 2개짜리.. 1개건너뛰고 나옴  n개자리는 n(1+n)/n번째 부터 나온다. 그리고 n-1번째 단위로 하나씩 나오게 됨.
4 = x
5 = 2+3
6 = 1+2+3       1로 시작하는 첫수... 3개짜리.. 2개건너뛰고 나옴
7 = 3+4
8 = x
9 = 2+3+4, 4+5
10 = 1+2+3+4    1로 시작하는 첫수... 4개짜리.. 3개건너뛰고 나옴
11 = 5+6
12 = 3+4+5
13 = 6+7
14 = 2+3+4+5
15 = 7+8, 4+5+6 , 1+2+3+4+5 1로 시작하는 첫수... 5개짜리.. 4개건너뛰고 나옴.
16 = x
17 = 8+9
18 = 5+6+7, 3+4+5+6

n개자리는 n(1+n)/n번째 부터 나온다. 그리고 n-1번째 단위로 하나씩 나오게 됨.

만약 15로 지정했다하면.

n(1+n)/2이 15이하인 n을 먼저 계산하고. 15에선ㄴ 2개짜리, 3개짜리, 4개짜리, 5인 n이 산출되게 된다.
2개짜리는 15 - n(1+n)이 2로 나누어 떨어지면 +1

3개짜리는 15 - n(1+n)이 3으로 나누어 떨어지면 +1 ... 나머지도 이렇게 간다.
'''
'''
pseudo code
def solution(n):

    for i in range(n):
        i(1+i)/2 <= n 인 i를 구하고 
        n - i(1+i)/2 가 i로 나누어 떨어지면 총합을 1 추가한다. 
    return answer

'''
# def solution(n):
#     total = 0
#     for i in range(2, n+1):  #i개 짜리가 있는지 검사합니다.
#         print("i: {}".format(i))
#         sum = (i*(1+i))//2
#         print("sum: {}".format(sum))
#         if sum <= n:
#             print("sum이 n보다 작으니까, {}개 짜리가 있을 수 있습니다.".format(i))
#             if (n - sum) % i == 0:
#                 print("{}의 연속된 자연수 합 리스트에 있습니다.".format(n))
#                 total += 1
#                 print("total: {}".format(total))
#         else:
#             break
#
#     return total+1
#
#
# print(solution(15))

def solution(n):
    total = 0
    for i in range(2, n+1):
        sum = (i*(1+i))//2
        if sum <= n:
            if (n - sum) % i == 0:
                total += 1
        else:
            break
    return total+1


print(solution(15))