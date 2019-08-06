#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# -*- coding: UTF-8 -*-

# i > j
for i in range(13, 85):
  if 168 % i == 0:
    j = 168 / i
    if (i + j) % 2 == 0 and (i - j) % 2 == 0:
      m = (i + j) / 2
      n = (i - j) / 2
      x = n * n - 100
      print(x)
