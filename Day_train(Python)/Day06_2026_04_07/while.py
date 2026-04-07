name = input("請輸入你的名字:")

# 假如 while 後面的判斷成立就繼續迴圈，不成立就跳出迴圈
# 只要條件是 True，就一直做
# 條件變成 False，就停止
while name == "":
    name = input("你沒輸入成功，請輸入你的名字:")
print(f"你的名字是{name}")

# 範例二
food = input("請輸入你喜歡吃的食物: ")
while food != "q":
    print(f"你喜歡的食物是{food}")
    food = input("請輸入你喜歡吃的食物: ")
print("再見")