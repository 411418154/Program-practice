import random

# randint()
print(random.randint(1,10))

# random
print(random.random())

# 列表中隨機選擇一個元素
options = ["剪刀","石頭","布"]
rand_options = random.choice(options)
print(rand_options)

# 將列表打亂
card = ["2","3","4","5","6","7"]
random.shuffle(card)
print(card)