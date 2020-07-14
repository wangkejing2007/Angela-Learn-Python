def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fibo()

for i in range(20):
    # 從產生器取出費式數列前 20 個數字
    print(next(f))
