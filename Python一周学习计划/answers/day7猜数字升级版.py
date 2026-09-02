# Day 7 项目 A 参考答案：升级版猜数字
# 升级点：答案随机生成、记录猜测次数、可以重复玩

import random   # 引入随机数模块，这样每局答案都不一样

def play_game():
    """玩一局猜数字，猜对后返回"""
    answer = random.randint(1, 100)  # 随机生成 1~100 的整数
    count = 0                        # 记录这局猜了几次

    while True:
        guess = int(input("猜一个1到100的数字："))
        count += 1                   # 每猜一次，计数加 1

        if guess > answer:
            print("大了！")
        elif guess < answer:
            print("小了！")
        else:
            print(f"恭喜猜对了！共用了{count}次")
            break   # 猜对，结束本局（跳出内层 while）

# 外层循环控制"要不要再玩一次"
while True:
    play_game()    # 调用函数玩一局，玩完回到这里
    again = input("要不要再玩一次？(y/n)：")
    if again != "y":
        print("感谢游玩，再见！")
        break      # 不想再玩，跳出外层循环，程序结束
