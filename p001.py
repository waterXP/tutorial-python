#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: UTF-8 -*-

for i in range(1, 5):
  for j in range(1, 5):
    if (i == j):
      continue
    for k in range(1, 5):
      if (j != k) and (k != i):
        print(i,j,k)
