#!/usr/bin/python

import random
def ls(ar, v):
  """Performs linear search of an array ar for value v.

  Returns:
    index of the found item, or None if not found.
  """
  for i, x in enumerate(ar):
    if v == x:
      return i

if __name__ == "__main__":
  ar=[random.randint(0,100) for i in range(0, 10)]
  print(ar)
  v = 50
  i = ls(ar, v)
  if i:
    print("Found [ar={}, v={}, idx={}]".format(ar, v, i))
  else:
    print("Not found [ar={}, v={}]".format(ar, v))
