prices = [56.12, 142.12, 23.65, 34.37, 12.01, 10.8, 23, 4]

for price in prices:
    rub = int(price // 1)
    trifle = round((price - rub) * 100)
    print(f'{rub: 02d} руб {trifle:02d} коп', end=',')

prices.sort()
print('\n', prices)

order_prices = sorted(prices, reverse=True)
print(order_prices)
print(sorted(order_prices[0:5]))
