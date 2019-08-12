#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

# INSERT-SORT
a = [31, 41, 59, 26, 41, 58]
for j in range(1, len(a)):
  t = a[j]
  i = j - 1
  while i >= 0 and a[i] < t:
    a[i + 1] = a[i]
    i -= 1
  a[i + 1] = t
print('sorted:', a)
