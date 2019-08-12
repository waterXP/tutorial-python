#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

a = [31, 41, 59, 26, 41, 58, 7]
for j in range(len(a) - 1):
  t = j
  for i in range(j + 1, len(a)):
    if a[t] > a[i]:
      t = i
  if t != j:
    a[t], a[j] = a[j], a[t]
print('sorted:', a)
