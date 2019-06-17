#!/usr/bin/python

def reverse(a):
  """Use two pointers starting from opposite ends of an array"""
  
  li = 0
  ri = len(a) -1
  
  while li <= ri:
    temp = a[li]
    a[li] = a[ri]
    a[ri] = temp

    li += 1
    ri -= 1
  
if __name__ == "__main__":
  s = "abcd"
  sa = [s[i] for i in range(len(s))]
  
  print(sa)
  reverse(sa)
  print(sa)
