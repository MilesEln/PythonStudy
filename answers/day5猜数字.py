# Day 5 项目参考答案：猜数字游戏
# 规则：程序心里想一个 1~100 的数字，玩家来猜，
#       每次提示"大了"或"小了"，直到猜对为止

answer = 42   # 程序心里想的数字，先固定写死一个

# while True 表示一直循环，什么时候停由循环体里的 break 决定
# 适合"不知道要猜几次"这种场景
while True:
    guess = int(input("猜一个1到100的数字："))

    if guess > answer:
        print("大了！")      # 猜大了，提示后进入下一轮循环
    elif guess < answer:
        print("小了！")
    else:
        print("恭喜猜对了！")
        break                # 猜对了，用 break 跳出循环

# 选做升级：让答案每次随机。
# 在文件最上面加一行：import random
# 然后把上面的 answer = 42 改成：answer = random.randint(1, 100)
