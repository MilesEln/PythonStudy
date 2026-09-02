# Day 3 练习参考答案：两数计算器
# 要求：让用户输入两个数字，输出它们的加、减、乘、除结果

# input() 拿到的永远是字符串，要用 float() 转成数字才能做运算
# 用 float 而不是 int，是为了让用户输入小数时也能正常工作
a = float(input("请输入第一个数字："))
b = float(input("请输入第二个数字："))

# f-string 的花括号里可以直接写算式，Python 会先算出结果再填进去
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")  # / 的结果总是小数，比如 10 / 4 = 2.5
