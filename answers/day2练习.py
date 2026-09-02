# Day 2 练习参考答案
# 要求：定义姓名、年龄、身高、是否学生四个变量，
#       用 type() 打印它们的类型，再用 f-string 打印一段自我介绍

# 1. 定义四个变量，分别对应四种基本类型
name = "小明"          # str：文字要放在引号里
age = 18               # int：整数不带引号
height = 1.75          # float：带小数点的数
is_student = True      # bool：只有 True / False，首字母大写

# 2. type() 可以查看一个变量是什么类型
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>

# 3. f-string：引号前加 f，花括号 {} 里的变量会被替换成它的值
print(f"大家好，我叫{name}，今年{age}岁，身高{height}米，是学生：{is_student}")
