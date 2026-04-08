# 本金
amount = 0
while amount <= 0:
    amount = float(input("請輸入你的本金 : "))
    if amount <= 0:
        print("你的本金不能小於等於 0 ，請再輸入一次")
print(f"你的本金:{amount:.2f}")

# 利率
rate = 0
while rate <= 0:
    rate = float(input("請輸入你的利率 : "))
    if rate <= 0:
        print("你的利率不能小於等於 0 ，請再輸入一次")
print(f"你的利率:{rate:.2f}")

# 年限
time = 0
while time <= 0:
    time = float(input("請輸入你的年限 : "))
    if time <= 0:
        print("你的年限不能小於等於 0 ，請再輸入一次")
print(f"你的年限:{time:.2f}")

# 總金額
total = amount * (1 + (rate / 100)) ** time
print(f"你的總金額:{total:.2f}")