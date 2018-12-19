
# name =input('输入name:')
# age =input('输入age:')
# print('My name is:%s,and I\'m %s old'%(name,age))

# num_1 = input('请输入num_1:')
# num_2 = input('请输入num_2:')
# print('num_1 + num_2 ='+str(int(num_1) + int(num_2)))
# num1 =int(num_1)
# num2 =int(num_2)
# print('num_1 + num_2 = %s'%(num1+num2))
# print('num_1 * num_2 = %s'%(num1*num2))
# print('num_1 / num_2 = %s'%(num1/num2))
# print('num_1 // num_2 = %s'%(num1//num2))
# # print('num_1 % num_2 = '+ str(num1%num2))
# # print('num_1 ** num_2 = %s'%(num1**num2))
# boy = True
# girl = False
# a = int(boy)
# b = int(girl)
# c = str(boy)
# d = str(girl)
# # print(a,b,c,d)
# print(bool(0))
# print(bool(74))
# print(bool(-3))
# print(bool('4'))
# print(bool(4.23))
import os
# import sys
# chr


# buy1 = '买一个西瓜'
# buy2 = '买一斤包子'
'''
while True:
    a = (input('输入成绩：'))
    if a.isdigit():    #float没办法判断啊
        score = float(a)
        if score>90:
            print('优')
        elif score<90 and score>=80:
            print("良")
        elif score<80 and score>=60:
            print('及格')
        else:
            print('不及格！差')
    else:
        print('请输入整数')
        
while True:
    year = int(input('输入年份：'))
    if year%4 == 0 and year%100 != 0 or year%400 ==0:
        print(year,'是一个闰年')
    else:
        print(year,'不是闰年')
'''
# i=1
# sum=0
# while i<=10:
#     sum=i+sum
#     print(sum)
#     i+=1
'''
while True:
    sum=0
    avg=0
    i=1
    c=input('输入数字 or exit：')
    while c !='exit':
        c=int(c)
        sum=sum+c
        avg=sum/i
        i+=1
        c = input('输入数字 or exit：')
    else:
        print('求和：',sum)
        print('平均值：',avg)
        break
'''
# i=1
# sum=0
# avg=0
# while True:
#     _input=input("输入数字或exit:")
#     if  _input != 'exit':
#         sum =int(_input)+sum
#         avg=sum/i
#         i+=1
#     elif _input =='exit' and i==1:
#         print('你妹啊，没输入数字让我算个球啊！')
#         break
#     else:
#         print('求和：',sum)
#         print('平均值',avg)
#         break
# a='---------'
# b="|"
# print(a+'\n1 x 1= 1 %s'%b)
# print(a*2+'\n1 x 2= 1 %s2 x 2= 4 %s'%(b,b))
# print(a*3+'\n1 x 3= 3 %s2 x 3= 6 %s3 x 3= 9 %s'%(b,b,b))
# print(a*4+'\n1 x 4= 4 %s2 x 4= 8 %s3 x 4= 12 %s4 x 4= 16 %s'%(b,b,b,b))
# print(a*5+'\n1 x 1= 1'+b)

# a = {x: {y: z}}
# a = {}
# b = {}
# for x in range(1,3,1):
#     for y in range(1,3,1):
#         z = x * y
#         b = {}
#         b[y] = z
#         a[x]=b
# print(a)
# x=1
# for y in range(1,10,1):
#     z = x * y
#     b[y] = z
#     a[x]=b
# print(a)
#
import pickle
import sys
import os
a = {}
b = {}
for x in range(1,10):
    for y in range(1,10):
        z = x * y
        b[y] = z
        f=open('dict','rb')
        pickle.load(f)
        a[x] = b
        pickle.dump(a,f)
        f.close()
f=open('dict','r',encoding='utf-8')
a=pickle.loads(f.readlines())
print(a)
f.close()


