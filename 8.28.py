#1
'''
import math
r = eval(input("r="))
s=2*r*math.sin(math.pi/5)
a=5*s*s/(4*math.tan(math.pi/5))
print(a)
'''
#2
'''
import math
(x1,y1) = eval(input('x1,y1'))
(x2,y2) = eval(input('x2,y2'))
x1 = math.radians(x1)
x2 = math.radians(x2)
y1 = math.radians(y1)
y2 = math.radians(y2)
d=6371.01*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
print(d)
'''

#3
'''
import math
s=eval(input('s='))
a=(5*s*s)/(4*math.tan(math.pi/5))
print(a)
'''
#4
'''
import math
n=eval(input('n='))
s=eval(input('s='))
a=(n*s*s)/(4*math.tan(math.pi/5))
print(a)
'''
#5
'''
n=eval(input('n= (0~127):'))
ascii= chr(n)
print(ascii)
'''
#6
'''
name=str(input('姓名: '))
hours=eval(input('一周工作时间: '))
pay=eval(input('每小时报酬: '))
fr=eval(input('联邦预扣税率: '))
sr=eval(input('州预扣税率: '))

a=hours*pay
b=a-(a*fr+a*sr)
print('name: ',name)
print('一周工作时间: ',hours)
print('每小时报酬:  $',pay)
print('税前报酬:  $',a)
print('联邦预扣税率: ',fr)
print('州预扣税率: ',sr)
print('税后报酬:  $',round(b,2))
'''
#7
n=eval(input('输入一个四位数'))
a=n//1000
b=(n-a*1000)//100
c=(n-a*1000-b*100)//10
d=n-a*1000-b*100-c*10
print(str(d)+str(c)+str(b)+str(a))

