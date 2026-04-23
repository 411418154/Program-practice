def add(*args):#不限輸入函數的數字
    total = 0
    for arg in args:
        print(f"arg : {arg}")
        total += arg
    return total
print(add(1,2,3))

def print_info(**kwargs):
    for key , value in kwargs.items():
        print(f"key : {key} value : {value}")

print_info(name = "alice" , age = 23  ,occupation = "工程師")