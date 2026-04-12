# list 列表 有順序，可以重複，可以修改

fruits = ["蘋果" , "橘子" , "柳橙" , "香蕉"]

for x in fruits:
    print(x, end=" ")
print()

# 增加欄位
fruits.append("芭樂")
print(fruits)

# 減少欄位
fruits.remove("香蕉")
print(fruits)

# index
fruits.append("蘋果")
print(fruits.index("蘋果"))
print(fruits.count("蘋果"))

# 列表倒轉
fruits.reverse()
print(fruits)

# set 沒有固定順序，不能重複，可以新增、刪除元素
fruits_set = {"蘋果", "橘子" , "柳橙"}
for fruit in fruits_set:
    print(fruit , end = " ")
print()

if "蘋果" in fruits_set:
    print("裡面有蘋果")
else:
    print("裡面沒有蘋果")

# tuple 元組 有順序，可以重複，不能修改
fuits_tuple = ("蘋果" , "橘子" , "柳橙" , "香蕉")
result = fuits_tuple.count("蘋果")
print(result)