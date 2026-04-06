name = "code 程式"

# 幾個字元
length = len(name)
print(f"全名共有幾個字{length}")

# 找出空格
space_find = name.find(" ")
print(f"空格出現在 {space_find} 第幾個字元")

# 讓字串第一個字變大寫，讓字串全部變大寫，讓字串全部變小寫
name_capitalizad = name.capitalize()
print("全名第一個字變大寫",name_capitalizad)

name_low = name.lower()
print("全字變小寫",name_low)

name_upp = name.upper()
print("全字變大寫",name_upp)

# count 找字串裡有幾個
name_cou = name.count(" ")
print(f"有 {name_cou} 個空白")

# replace 替換字串內容
name_re = name.replace(" ","-")
print(f"替換掉空白變成- :{name_re}")