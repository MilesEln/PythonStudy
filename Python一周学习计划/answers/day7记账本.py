# Day 7 项目 B 参考答案：简单记账本
# 功能：记收入 / 记支出 / 查看总额 / 退出

def show_menu():
    """打印功能菜单"""
    print("\n===== 记账本 =====")   # \n 表示先换一行，菜单更好看
    print("1. 记一笔收入")
    print("2. 记一笔支出")
    print("3. 查看总额")
    print("4. 退出")

records = []   # 列表存所有账目，每笔账是一个字典：{"type": ..., "amount": ..., "note": ...}

while True:
    show_menu()
    choice = input("请选择功能（1-4）：")

    if choice == "1":
        amount = float(input("收入金额："))
        note = input("备注（比如：零花钱）：")
        # 收入记为正数
        records.append({"type": "收入", "amount": amount, "note": note})
        print("已记录！")
    elif choice == "2":
        amount = float(input("支出金额："))
        note = input("备注（比如：午饭）：")
        # 支出记为负数，这样算总额时直接相加即可
        records.append({"type": "支出", "amount": -amount, "note": note})
        print("已记录！")
    elif choice == "3":
        total = 0
        for r in records:              # 逐个取出每笔账（字典）
            total += r["amount"]       # 用键 "amount" 取出金额累加
        print(f"当前总额：{total}元")
    elif choice == "4":
        print("再见！")
        break
    else:
        print("输入无效，请重新选择")
