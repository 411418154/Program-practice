openator = input("請輸入你要的運算符號，+ (加) - (減) * (乘) / (除) : ")
num1 = float(input("請輸入第一個數字 : "))
num2 = float(input("請輸入第二個數字 : "))

if openator == '+':
    result = num1 + num2
elif openator == '-':
    result = num1 - num2
elif openator == '*':
    result = num1 * num2
elif openator == '/':
    result = num1 / num2
else:
    print("運算符無效請重新輸入")

print(f"運算結果是: {round(result)}")