# 建立字典
menu = {
    "披薩" : 300,
    "爆米花" : 200,
    "薯條" : 90,
    "洋芋片" : 60,
    "蘇打水" : 60,
    "軟麵包條" : 120,
    "檸檬水" : 90,
}

# 建立初始值
cart = []
total = 0

# 列印菜單
print("      菜單      ")
print("================")
for item , price in menu.items():
    print(f"{item} : {price}")

# 詢問購買商品
while True:
    food = input("請輸入菜單項目(輸入Q退出):")
    if food.lower() == "q":
        break
    elif menu.get(food) is None:
        print("沒有這個商品")
    else: # 物品放購物車，錢放入和加上total
        cart.append(food)
        total += menu.get(food)
        print(food , end=" ")
print(f"您的商品 : {', '.join(cart)} ")
print(f"總共 : {total} 元!")