#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

a = [9, 2, 41]
v = 41
find = False
for i in range(len(a)):
  if v == a[i]:
    find = True
    break
if find == True:
  print('this sit:', i)
else:
  print('not find')
