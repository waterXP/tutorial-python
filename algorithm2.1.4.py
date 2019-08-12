#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

x = [1, 0, 1, 1, 0]
y = [0, 1, 1, 0, 0]
r = []
carry = 0
for i in range(len(x)):
  s = x[i] + y[i] + carry
  if s > 1:
    carry = 1
    s -= 2
  else:
    carry = 0
  r.append(s)
r.append(carry)
print('value:', r)
