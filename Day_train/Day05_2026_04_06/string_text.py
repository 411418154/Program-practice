username = input("請輸入使用者名稱:")

if len(username) > 12:
    print("你的使用者名稱超過12個字符")
elif " " in username:
    print("你的名稱中有空格")
elif not username.isalpha():
    print("你的使用者名稱中有數字")
else:
    print(f"歡迎 {username}")