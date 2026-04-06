# 數學加減
apples = 10
apples += 1
print(f"加1顆後，現在有 {apples} 顆蘋果")
apples -= 2
print(f"減2顆後，現在有 {apples} 顆蘋果")

# 數學乘法
apples *= 2
print(f"乘以2後，現在有 {apples} 顆蘋果")

# 數學除法
apples /= 3
apples = int(apples)
print(f"除以3後，現在有 {apples} 顆蘋果")

# 數學平方
apples **= 2
print(f"2平方後，現在有 {apples} 顆蘋果")

# 數學餘法
apples %= 5
print(f"2餘法後，現在有 {apples} 顆蘋果")

# pow 次方
print (f"二的五次方是 {pow(2 , 5)}")

# max ， min 最大最小值
x = [6 , 2 , 4]
print(f"X的最大值是 {max(x)}")
print(f"X的最小值是 {min(x)}")

# 四捨五入 round
a = 3.14
print(f"3.14四捨五入是 {round(a)}")
a = 3.5
print(f"3.5四捨五入是 {round(a)}")

# abs 絕對值
c = -4
print(f"-4的絕對值是 {abs(c)}")

# 四捨五入進階 ，無條件進位，無條件捨去
import math
x = 9.5
print(f"使用 round 四捨五入 {round(x)}")
print(f"使用 math.ceil 無條件進位四捨五入 {math.ceil(x)}")
print(f"使用 math.floor 無條件捨去四捨五入 {math.floor(x)}")

# 用 math 模塊呼叫 pi
print(f"用 math 模塊呼叫圓周率 {math.pi}") 

# 計算圓的周長
radius = float(input("請輸入圓的半徑:"))
C = 2 * math.pi * radius
print(f"圓的周長是 {round(C,2)}")