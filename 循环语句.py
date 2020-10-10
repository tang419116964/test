# 迭代list
from functools import reduce

a = ['1',1,'woeo',2.22]
for i in a:
    print(i)
print('---------------------------')
# 迭代dict enumerate函数可以提供index 下标
dic = {'1':'11','2':'2eee','three':'333'}
for k,v in dic.items():
    print('%5s %5s' %(k,v))
print('---------------------------')
for i,j in enumerate(dic):
    print('%5s %5s %5s' %(i,j,dic[j]))
print('---------------------------')
# lambda 函数 和内置函数的使用
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
for i in filter(lambda e:e%2==0,foo):
    print(i,end=" ")
print()
print('---------------------------')
for i in map(lambda e:e**2,foo):
    print(i,end=" ")
print()
print('---------------------------')
print(reduce(lambda x,y:x+y,foo))
print('---------------------------')
# 循环元组
collection = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]
for item in collection:
    print(item[0],item[1],item[2])
print('---------------------------')
for item in collection:
    it1 ,it2 ,it3 = item
    print(it1 ,it2 ,it3)
print('---------------------------')
for it1 ,it2 ,it3 in collection:
    print(it1 ,it2 ,it3)
print('---------------------------')

# range()的使用
for i in range(0,5,2):
    print(i)
print('---------------------------')
lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
print(lst[1::2])
for i in range(0,len(lst),3):
    print(lst[i])
print('---------------------------')

# while 循环
while True:
    print('done')
    break

n=0
while n<4:
    print(n)
    n=n+1
print('---------------------------')
