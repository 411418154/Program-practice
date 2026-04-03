#integer 整數
number = 23
print(f"我的年齡是{number}")
print(type(number))

#float 浮點數
gpa = 3.3
print(f"我的gpa分是{gpa}")
print(type(gpa))

#string 字串
name = 'raylin'
print(f"我的名字是{name}")
print(type(name))

#boolean 布林值
answer = True # 或可以寫 1
nanswer = False # 或可以寫 0
print(f"檔案是否正確{answer}")
print(type(answer))
print(type(nanswer))

# 型態轉換 整數轉浮點
number = float(number)
print(f"整數轉浮點 {number}")
print(type(number))

# 型態轉換 浮點轉整數
gpa = int(gpa)
print(f"浮點轉整數 {gpa}")
print(type(gpa))


# 型態轉換 布林轉字串
answer = str(answer)
print(f"布林轉字串 {answer}")
print(type(answer))