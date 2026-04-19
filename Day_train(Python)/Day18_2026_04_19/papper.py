import random

player = None
computer = None
running = True
chose = ("剪刀","石頭","布")

while running:
    player = input("請輸入你要出的拳(剪刀，石頭，布): ")
    while player not in chose:
        player = input("請重新輸入你要出的拳(剪刀，石頭，布): ")
    computer = random.choice(chose)
    print(f"你出{player}，電腦出{computer}")
    if (player == computer):
        print("平局")
    elif (player == "石頭" and computer == "布"):
        print("你輸了")
    elif (player == "布" and computer == "剪刀"):
        print("你輸了")
    elif (player == "剪刀" and computer == "石頭"):
        print("你輸了")
    else:
        print("你贏了!!")
    play_again = input("你還要再玩一次嗎?(y / n): ").lower()
    if not play_again == "y":
        running = False

print("謝謝你玩我的遊戲!!")