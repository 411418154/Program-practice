def say_hello():
    print("hello world")

for i in range(3):
    say_hello()

name1 = input("請輸入你的名字:")

def greeting(name):
    print(f"你好! {name}")

greeting(name1)

def add(x , y):
    return x + y
sum = add(3,2)
print(sum)