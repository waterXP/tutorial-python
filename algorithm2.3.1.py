#!/usr/local/bin/python3
# -*- coding: UTf-8 -*-

# MERGE(a, p, q, r)
def merge(a, p, q, r):
  l1 = a[p : q + 1] + [float('inf')]
  l2 = a[q + 1 : r + 1] + [float('inf')]
  i = j = 0
  for k in range(p, r + 1):
    if l1[i] < l2[j]:
      a[k], i = l1[i], i + 1
    else:
      a[k], j = l2[j], j + 1

# MERGE-SORT(a, p, r)
def mergeSort(a, p, r):
  q = (p + r) // 2
  if p < q:
    mergeSort(a, p, q)
  if q + 1 < r:
    mergeSort(a, q + 1, r)
  merge(a, p, q, r)

a = [16, 9, 10, 77, 11, 15, 33]
if 0 < len(a) - 1:
  mergeSort(a, 0, len(a) - 1)
print('sorted:', a)
