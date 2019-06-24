#!/usr/bin/python

def reverse(s):
  """Generates reversed version of s as a separate char array.

  Space complexity is O(n).

  Time complexity is O(n).
  """

  if s is None or len(s) < 2:
    return s

  result = [None] * len(s)

  j = 0
  for i in range(len(s) - 1, -1, -1):
    result[j] = s[i]
    j += 1

  return "".join(result) 


if __name__ == "__main__":
  s = "hello world!!!"
  print(reverse(s))


