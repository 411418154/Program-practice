# list set tuple
#建立列表
good = []
price = []

# 迴圈輸入內容
while True:
    goods = input(f"請輸入想購買的物品 :")
    if goods.lower() == "q":
        break
    prices = float(input(f"請輸入{goods}的價格 :"))
    good.append(goods)
    price.append(prices)

# 商品列表
print("商品列表 : ", end = "")
for x in good:
    print(x , end = " ")
print()

# 價格列表
print("價格列表 : ", end = "")
for x in price:
    print(x , end = " ")
print()

# 印出商品代號和價格
for index, good in enumerate(good):
    print(f"第 { index + 1} 商品是 {good} , 價格是 {price[index]:.2f}")

# 總和價格
total = sum(price)
print("總價格是 : ", total)