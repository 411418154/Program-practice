import os

str = r"C:\Users\User\Desktop\Program practice\Day_train(Python)\Day25_2026_04_29"
print(str)

if os.path.exists(str):
    print("路徑存在")
elif os.path.isfile(str):
    print("此路徑為檔案")
elif os.path.isdir(str):
    print("此路徑為目錄")