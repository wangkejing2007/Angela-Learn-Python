titles = ['主機', '螢幕', '鍵盤']
prices = ['$9,999', '$2,999', '$399']

# for i in range(len(prices)):
#     print(titles[i] + '：' + prices[i])

# for i in range(len(prices)):
#     print(titles[i] + '：' + prices[i])

for t, p in zip(titles, prices):
    print(t + '：' + p)