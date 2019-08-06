#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: UTF-8 -*-

i = int(input('profit:'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [.01, .015, .03, .05, .075, .1]
r = 0
for idx in range(0, 6):
  if i > arr[idx]:
    r += (i - arr[idx]) * rat[idx]
    print((i - arr[idx]) * rat[idx])
    i = arr[idx]
print('total: ', r)
