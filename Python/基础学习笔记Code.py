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

# 温度转换
TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print('转换后的温度是{:.2f}C'.format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*(eval(TempStr[0:-1])) + 32
    print('转换后的温度是{:.2f}F'.format(F))
else:
    print('输入格式错误')

# Hello World的条件输出
Number = eval(input())
if Number == 0:
    print('Hello World')
elif Number > 0:
    print('he\nll\no \nwo\nrl\nd')
else:
    for i in "Hello World":
        print(i)

# PythonDraw.py
import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40.80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()

# 绘制八角图形
import turtle as t
t.pensize(2)
for i in range(8):
	t.fd(150)
	t.left(135)

# 获得用户输入的一个正整数输入，输出该数字对应的中文字符表示。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬0到9对应的中文字符分别是：零一二三四五六七八九
char = "零一二三四五六七八九"
n = eval(input())
for c in n:
    print(char[c],end="")

# 温度转换2
temp = input()
if temp[0] in ["C"]:
    F = eval(temp[1:])*1.8 + 32
    print("F{:.2f}".format(F))
elif temp[0] in ["F"]:
    C = (eval(temp[1:]) - 32) / 1.8
    print("C{:.2f}".format(C))
else:
    print('输入错误')

# 美元人民币转换
temp = input()
if temp[:3] in ["RMB"]:
    U = eval(temp[3:]) / 6.78
    print("USD{:.2f}".format(U))
elif temp[:3] in ["USD"]:
    R = eval(temp[3:]) * 6.78
    print("RMB{:.2f}".format(R))
else:
    print()	

# 天天向上的力量
dayup = pow(1.001,365)
daydown = pow(0.999,365)
print("向上:{:.2f},向下:{:.2f}".format(dayup,daydown))

# 天天向上的力量（使用变量）
dayfactor = 0.005 #百分值变化不用在逐行更改
dayup = pow(1 + dayfactor,365)
daydown = pow(1 - dayfactor,365)
print("向上：{:.2f},向下：{:.2f}".format(dayup,daydown))

# 天天向上工作日的力量
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup * (1 - dayfactor)
    else:
        dayup = dayup * (1 + dayfactor)
print("工作日的力量：{:.2f}".format(dayup))

# 天天向上A君每天进步1%，B君做五休二（休息退步1%），B君工作日要多努力
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数是：{:.3f}",format(dayfactor))

# 输入数字输出相应星期
weekstr = "一二三四五六七"
weeknumber = eval(input("请输入星期数字（1-7）："))
print("星期" + weekstr[weeknumber - 1])

a = eval(input())
n = pow(a,0.5)
print('{:+>30.3f}'.format(n))

# 身体质量指数BMI
height,weight = eval(input("请输入身高（米）和体重（公斤）[用逗号隔开]："))
bmi = weight / pow(height,2)
print("您的BMI值为：{:.2f}".format(bmi))
r1,r2 = "",""
if bmi < 18.5:
    r1,r2 = "偏瘦","偏瘦"
elif 18.5 <= bmi < 24:
    r1, r2 = "正常", "正常"
elif 24 <= bmi < 25:
    r1, r2 = "正常", "偏胖"
elif 25 <= bmi < 28:
    r1, r2 = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    r1, r2 = "偏胖", "肥胖"
else:
    r1, r2 = "肥胖", "肥胖"
print("BMI指标为：国际'{0}',国内'{1}'".format(r1,r2))

# 输出四色玫瑰数
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                n = pow(a,4)+pow(b,4)+pow(c,4)+pow(d,4)
                m = a * 1000 + b * 100 + c * 10 + d
                if n == m and len(str(m)) == 4:
                    print(m)

s = ""
for i in range(1000, 10000):
    t = str(i)
    if pow(eval(t[0]),4) + pow(eval(t[1]),4) + pow(eval(t[2]),4) + pow(eval(t[3]),4) == i :
        print(i)

# 100以内的素数之和
s = 0
for i in range(2,100):
    for n in range(2,i):
        if(i % n == 0):
            break
    else:
        s += i
print(s)

def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
sum = 0
for i in range(2,100):
    if is_prime(i):
        sum += i
print(sum)

# 绘制七段数码管
import turtle
def drawline(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawdate(date):
    for i in date:
        drawdigit(eval(i))
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawdate('20190820')
    turtle.hideturtle()
    turtle.done()
main()

# 绘制七段数码管美化
import turtle,time
def drawgap():
    turtle.penup()
    turtle.fd(5)
def drawline(draw):
    drawgap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)
def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawdate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write("年",font = ("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write("月", font=("Arial", 18, "normal"))
            turtle.fd(40)
        elif i == '+':
            turtle.write("日", font=("Arial", 18, "normal"))
        else:
            drawdigit(eval(i))
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawdate(time.strftime("%Y-%m=%d+",time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()

# 字符串反转
def rvs(s):
    if s == ""
        return s
    else:
        return rvs(s[1:])+s[0]

# 字符串反转简单式
s[::-1]

# 斐波那契数列
def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)
# 随机密码生成
import random
def genpwd(length):
    a = pow(10, length - 1)
    b = pow(10, length) - 1
    return "{}".format(random.randint(a, b))
length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))

# 连续质数计算
def prime(m):
    for i in range(2,m):
        if m % i == 0:
            return False
    return True
n = eval(input())
n_ = int(n)
n_ = n_+1 if n_ < n else n_
count = 5
while count > 0:
    if prime(n_):
        if count > 1:
            print(n_, end=",")
        else:
            print(n_, end="")
        count -= 1
    n_ += 1

# 基础统计值计算
def getnum():
    nums = []
    inumstr = input("请输入数字（回车退出）：")
    while inumstr != "":
        nums.append(eval(inumstr))
        inumstr = input("请输入数字（回车退出）：")
    return nums

def mean(numbers):
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)

def dev(numbers,mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1),0.5)

def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

n = getnum()
m = mean(n)
print("平均值:{},方差:{:.2},中位数:{}.".format(m,dev(n,m),median(n)))

# 数字不同数之和
ls = input()
s = set(ls)
n = 0
for i in s:
    n += eval(i)
print(n)

#词频统计
s = '''双儿 洪七公 赵敏 赵敏 逍遥子 鳌拜 殷天正 金轮法王 乔峰 杨过 洪七公 郭靖 
       杨逍 鳌拜 殷天正 段誉 杨逍 慕容复 阿紫 慕容复 郭芙 乔峰 令狐冲 郭芙 
       金轮法王 小龙女 杨过 慕容复 梅超风 李莫愁 洪七公 张无忌 梅超风 杨逍 
       鳌拜 岳不群 黄药师 黄蓉 段誉 金轮法王 忽必烈 忽必烈 张三丰 乔峰 乔峰 
       阿紫 乔峰 金轮法王 袁冠南 张无忌 郭襄 黄蓉 李莫愁 赵敏 赵敏 郭芙 张三丰 
       乔峰 赵敏 梅超风 双儿 鳌拜 陈家洛 袁冠南 郭芙 郭芙 杨逍 赵敏 金轮法王 
       忽必烈 慕容复 张三丰 赵敏 杨逍 令狐冲 黄药师 袁冠南 杨逍 完颜洪烈 殷天正 
       李莫愁 阿紫 逍遥子 乔峰 逍遥子 完颜洪烈 郭芙 杨逍 张无忌 杨过 慕容复 
       逍遥子 虚竹 双儿 乔峰 郭芙 黄蓉 李莫愁 陈家洛 杨过 忽必烈 鳌拜 王语嫣 
       洪七公 韦小宝 阿朱 梅超风 段誉 岳灵珊 完颜洪烈 乔峰 段誉 杨过 杨过 慕容复 
       黄蓉 杨过 阿紫 杨逍 张三丰 张三丰 赵敏 张三丰 杨逍 黄蓉 金轮法王 郭襄 
       张三丰 令狐冲 赵敏 郭芙 韦小宝 黄药师 阿紫 韦小宝 金轮法王 杨逍 令狐冲 阿紫 
       洪七公 袁冠南 双儿 郭靖 鳌拜 谢逊 阿紫 郭襄 梅超风 张无忌 段誉 忽必烈 
       完颜洪烈 双儿 逍遥子 谢逊 完颜洪烈 殷天正 金轮法王 张三丰 双儿 郭襄 阿朱 
       郭襄 双儿 李莫愁 郭襄 忽必烈 金轮法王 张无忌 鳌拜 忽必烈 郭襄 令狐冲 
       谢逊 梅超风 殷天正 段誉 袁冠南 张三丰 王语嫣 阿紫 谢逊 杨过 郭靖 黄蓉 
       双儿 灭绝师太 段誉 张无忌 陈家洛 黄蓉 鳌拜 黄药师 逍遥子 忽必烈 赵敏 
       逍遥子 完颜洪烈 金轮法王 双儿 鳌拜 洪七公 郭芙 郭襄 赵敏'''
ls = s.split()
d = {}
for i in ls:
    d[i] = d.get(i,1) + 1 #是指有i时返回其值，默认是0，+1能够累计次数；没有i时则返回0
name,nums = "",0
for k in d:
    if d[k] > nums:
        name,nums = k,d[k]
print(name)

# 自动轨迹绘制
import turtle as t
t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
#数据读取
detals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","")
    detals.append(list(map(eval,line.spilt(","))))
f.close()
#自动绘制
for i in range(len(detals)):
    t.pencolor(detals[i][3],detals[i][4],detals[i][5])
    t.fd(detals[i][0])
    if detals[i][1]:
        t.right(detals[1][2])
    else:
        t.left(detals[i][2])

# 不规则图形词云
import jieba
import wordcloud
import  scipy.misc import imread  # 自定义词云形状
mask = imread("chinamap.jpg")    # 导入词云形状图，需是白底
excludes = {}
f = open("新时代中国特色社会主义.txt","r",encoding = "utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = "".join(ls)
w = wordcloud.WordCloud(width = 1000,height = 700,\
                        background_color = "white",
                        font_path = "msyh.ttc",mask = mask
                        )
w.generate(txt)
w.to_file("grwordcloudm.png")

# 文本的平均列数
f = open("latex.log")
s,c = 0,0
for line in f:
    line = line.strip("\n")
    if line == "":
        continue
    s += len(line)
    c += 1
print(round(s/c))

# CSV格式清洗与转换
f = open("data.csv")
ls = f.readlines()
ls = ls[::-1]
lt = []
for item in ls:
    item = item.strip("\n")
    item = item.replace(" ", "")
    lt = item.split(",")
    lt = lt[::-1]
    print(";".join(lt))
f.close()
