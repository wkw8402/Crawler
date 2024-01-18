import time

a = time.time()
c = time.ctime(a)
# print(c)

l = time.localtime()
# print('current hour = ' + str(l.tm_hour))

s = time.strftime('%Y %m', l)
# print(s)

name = 'Kim'
print('Hi, %s' %name)
print(f'Hi, {name}')

import datetime
d = datetime.datetime(2022, 10, 1)
n = datetime.datetime.now()
print(n)