
for x in reversed(range(1,11)):
    print(x)

credit_card = "1524-5515-1516-5115"
for x in credit_card:
    if(x == 9):
        continue
        # break
    else:
        print(x)

# 字典
# 健 key: 值 value
my_disk = {"a": 1,"b": 2,"c": 3}
for x in my_disk:
    print(x)

for key,value in my_disk.items():
    print("key :",key)
    print("value :",value)