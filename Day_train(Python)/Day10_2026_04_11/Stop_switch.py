import  time

time.sleep(1)

my_time = int(input("請輸入秒數:"))

for x in range(my_time , 0 , -1):
    seconds = x % 60 # 沒整除的變秒數
    minutes = x // 60 % 60 # 秒數除 60 變分鐘
    print(f"{minutes:02}:{seconds:02}")
    time.sleep(1)
print("時間到了!")