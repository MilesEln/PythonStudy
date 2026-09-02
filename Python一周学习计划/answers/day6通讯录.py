# Day 6 练习参考答案：简易通讯录
# 要求：字典存 3 个联系人 → 支持查询 → 新增一个联系人 → 打印整个通讯录

# 字典：键是姓名，值是电话，像真的通讯录一样"按名字查号码"
phone_book = {
    "妈妈": "13800000001",
    "爸爸": "13800000002",
    "姐姐": "13800000003"
}

# 查询：先用 in 判断键是否存在，避免 KeyError 报错
name = input("请输入要查询的姓名：")
if name in phone_book:
    print(f"{name}的电话是：{phone_book[name]}")
else:
    print("没有找到该联系人")

# 新增：对一个不存在的键赋值，就是往字典里添加新条目
new_name = input("请输入要新增的姓名：")
new_number = input("请输入电话：")
phone_book[new_name] = new_number

# 遍历：items() 可以同时取出每一对的键和值
print("最新通讯录：")
for n, num in phone_book.items():
    print(f"{n}：{num}")
