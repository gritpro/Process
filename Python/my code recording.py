# -*- coding: utf-8 -*-

print('你好，世界！') # 尝鲜

name=input('please enter your name')
print('hello',name) # 输入输出

print('''lin1
	lin2
	lin3''')  # '''...'''的格式表示多行内容

print('I\'m \"ok\"!')  # “\”多字符串

if age >= 18:
	print('adult')
else:
	print('teenager')  # 布尔值在条件判断中的运用

a = 'ABC'
b = a
a = 'XYZ'
print(b)  # 变量=的意义

s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('小明成绩提升了%d%%' %r)  # 格式化样式用%实现

s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('小明成绩提升了%.1f%%' %r)  # %.1f为小数点后几位

s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('你好,%s,你的成绩是%d分,相比去年提升%.2f%%' %('小明',s2,r))  # %s,%d,%f的综合运用

c = ['michael','bob','tracy']
c  # list有序合集样式

c = ['michael','bob','tracy']
len(c)  # len()函数获取list元素个数

c = ['michael','bob','tracy']
c[0]  
c[-1]
c[-2]  # 索引list每个位置的函数，正序从0开始，倒序从-1开始

c = ['michael','bob','tracy']
c.append('jack','paul')
c.insert(1,'lucy')
c.pop(2) 
c.[3] = 'wiliam'  # 依次为追加元素至末尾，将元素插入制定位置，删除制定位置元素,替换制定位置元素

c = ('michael','bob','tracy')
c[0]  # tuple和list的区别在[]与()上，只能提取，不能执行上述追加、插入、删除等动作

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0]) 
print(L[1][1])
print(L[-1][-1])
print(L[2][2])  # 分别打印Apple、python、lisa

height = 1.75
weight = 80.5
bmi = weight/height**2
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi >=25 and bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')  # 条件判断，python总是报错，注意冒号，调整了TAB4空格设置


sum = 0
for x in range(101):
    sum = sum + x
    print(sum)  # 循环if in

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
    print(sum)  # while循环

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('hello,%s!' %x)  # 依次按样式Hello, xxx!打印出每个名字

# break语句，未跑出1、2、3……最后到10，然后打印end的效果
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')  

# 自己写的一个死循环
n = 1
while n > 0:
    print(n)
    n = n + 1  

n1 = 255
n2 = 1000
print('%d的十六进制为%s' %(n1,hex(n1)),'%d的十六进制为%s' %(n2,hex(n2)))

##定义函数，不明觉厉，留坑
def quadratic(a,b,c):
    delta = b**2-4*a*c
    if delta < 0:
        print('无实解')
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return x1,x2   

pow(2,pow(2,15))
len(str(pow(2,pow(2,15))))

# month.py
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = input('请输入月份数：')
pos = (int(n) - 1) * 3
monthAbbrev = months[pos:pos+3]
print('月份简写是'+monthAbbrev+'.')

# 寻找一组数中的最大值
n = eval(input('数字个数？'))
max = eval(input('输入数字'))
for i in range(n-1)
    x = eval(input('输入数字'))
    if x > max
        max = x
    print('最大的数字是',max)

# def函数的演练
def happy():
    print("Happy Birthday to you!")

def singmike():
    happy()
    happy()
    print("Happy Birthday,dear Mike!")
    happy()

def singlily():
    happy()
    happy()
    print("Happy Birthday,dear lily!")
    happy()

def sing(person):
    happy()
    happy()
    print('Happy Birthday,dear',person + '!')
    happy()

def main():
    sing('mike')
    print()
    sing('lily')
    print()
    sing('lucy')

happy()
sigmike()
singlily()
main()

# 递归阶乘函数计算
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

fact(4)
fact(100)

# 字符串反转
def reverse(s):
    return reverse(s[1:]) + s[0] # 该函数会被报错，没有基例会无限递归
def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:] + s[0])

reverse('hello')
