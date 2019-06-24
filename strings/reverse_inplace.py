#!/usr/bin/python

def reverse(s):
  a = [c for c in s]
  i,j = 0, len(a) - 1

  while i < j:
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    i += 1
    j -= 1

  return "".join(a)

if __name__ == "__main__":
  s = "hello there!"
  print(reverse(s))
