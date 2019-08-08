#!/Library/Frameworkds/Python.framework/Versions/3.6/bin/python3
# -*- coding: UTF-8 -*-

# INSERT-SORT
a = [5, 2, 4, 6, 1, 3]
for j in range(1, len(a)):
  key = a[j]
  i = j - 1
  while i >= 0 and a[i] > key:
    a[i + 1] = a[i]
    i -= 1
  a[i + 1] = key
print('sorted:', a)
