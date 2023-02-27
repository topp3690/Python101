Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=================== RESTART: E:/Python/TestPython/turtle1.py ===================

================ RESTART: E:/Python/TestPython/gui_tk-chatgpt.py ===============
Your name is: test

=============== RESTART: E:/Python/TestPython/gui_tk-chatgpt2.py ===============
Expense added: 1.0 test
text = input("อยากบันทึกอะไร: ")
อยากบันทึกอะไร: test
text
'test'
name = 'Uncle'
print(name)
Uncle
type(name)
<class 'str'>
name.lower()
'uncle'
>>> friend = 'สมชาย'
>>> money = 10
>>> print(friend + 'ยืมเงิน ' + money + ' บาท')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(friend + 'ยืมเงิน ' + money + ' บาท')
TypeError: can only concatenate str (not "int") to str
>>> print(friend + 'ยืมเงิน ' + money.str() + ' บาท')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(friend + 'ยืมเงิน ' + money.str() + ' บาท')
AttributeError: 'int' object has no attribute 'str'
>>> print(friend + 'ยืมเงิน ' + str(money) + ' บาท')
สมชายยืมเงิน 10 บาท
>>> print('{}ยืมเงิน {} บาท'.format(friend,money))
สมชายยืมเงิน 10 บาท
>>> print(f'{friend}ยืมเงิน {money} บาท')
สมชายยืมเงิน 10 บาท
>>> money = 1454541111534
>>> print(f'{money:,}')
1,454,541,111,534
>>> print(f'{money:,.2f}')
1,454,541,111,534.00
>>> import math
>>> math.pi
3.141592653589793
>>> math.pi * (5**2)
78.53981633974483
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2023, 2, 12, 21, 23, 14, 622031)
>>> datetime.now().strftime('%Y%m%d %H:%M')
'20230212 21:24'
>>> import random
>>> random.randint(1,7)
7
>>> store=['ป้าส้ม','ป้าเล็ก','ลุงดำ']
>>> random.choice(store)
'ลุงดำ'
