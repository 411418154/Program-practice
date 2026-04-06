# Boolean if-else 布林值判斷
for_sale = True
if for_sale:
    print("此項目正在出售")
else:
    print("此項目未在出售")

# 判斷年齡
age = int(input("請輸入你的年齡: "))

if age > 100:
    print("你太老了!!")

elif age >= 18 :
    print("你可以註冊!")

elif age <= 0:
    print("你在騙!你根本沒出生")

else:
    print("你年齡不夠，不能註冊")