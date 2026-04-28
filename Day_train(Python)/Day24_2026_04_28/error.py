try:
    x = int(input("請輸入一個整數: "))
    y = int(input("請輸入另一個整數: "))
    print(x/y)

except (ZeroDivisionError,ValueError):
    print("數字有誤請調整")
finally:
    print("程式結束")