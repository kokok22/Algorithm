## 한 번의 거래로 낼 수 있는 최대 이익을 산출하라


def maxProfit(prices):
    profit = 0
    min_price = 10000

    # 앞으로 가면서 비교를 하는 것이다.
    for price in prices:
        # 비교할 때 min, max로 하자
        min_price = min(price, min_price)
        profit = max(price - min_price, profit)

    return profit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))