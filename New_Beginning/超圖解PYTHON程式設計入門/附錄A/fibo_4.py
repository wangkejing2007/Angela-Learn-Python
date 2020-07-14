import time


def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)


old = time.time()    # 取得目前時間
val = fibo(33)       # 建議先從小一點的數值開始測試
diff = time.time() – old  # 計算時間差
print(f'第33個數字是：{val}')
print(f'花費時間：{round(diff, 4)}秒')
