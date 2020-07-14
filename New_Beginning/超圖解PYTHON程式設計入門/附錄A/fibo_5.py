import time

buf = [None] * 1000


def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        if buf[n] != None:
            return buf[n]
        else:
            val = fibo(n-1)+fibo(n-2)
            buf[n] = val
            return val


# def fibo(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)


old = time.time()
val = fibo(200)
print(f'計算結果：{val}')
diff = time.time() - old
print(f'花費時間：{round(diff, 4)}秒')
