#輸入數學四算，然後程式計算得出結果
print()
expression = input("請輸入四則運算式 or 按下'r'鍵離開：")
while (expression != "r"):
    print()
    print ("你的四則運算式",expression,",答案是：", eval(expression))
    print()
    expression = input("請輸入四則運算式 or 按下'r'鍵離開：")