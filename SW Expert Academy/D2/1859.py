## 가장 큰 이득을 볼 수 있는 매입과 매매를 하자

# 뒤에서 부터 큰 애들이 나오면 빼주는 방식으로 진행
def sale(prices):
   result = 0
   max = 0

   for price in prices[::-1]:
       if max < price:
           max = price
       else:
           result += max-price
   return result

T = int(input())

for i in range(T):
    num = int(input())
    prices = list(map(int, input().split(' ')))

    print("#{} {}".format(i+1, sale(prices)))