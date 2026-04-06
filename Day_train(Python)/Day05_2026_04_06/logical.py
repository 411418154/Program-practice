# and 的用法
temp = int(input("請輸入溫度: "))

if temp > 0 and temp < 19: # 要兩個都是True才會執行
    print("溫度是偏冷的記得穿外套")
elif temp > 19 and temp < 30:
    print("溫度是適宜，溫暖的，開心玩")
elif temp > 30 and temp < 40:
    print("溫度是炎熱的，注意體溫，以防中暑")
else:
    print("溫度差異大，可以在家好好休息")

# or 的用法
import random

num = random.randint(1,4)
print(num)

if num == 2 or num == 4:# 其中一個是 True 就會執行
    print("你中獎了!!")
else:
    print("你沒中獎，好可惜")