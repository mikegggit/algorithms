#!/usr/bin/python

def rotateClockwiseOne(a):
  """rotates an array clockwise (right) one position.

  for example:
  rotateClockwiseOne(abcdef) = fabcde
  """

  if len(a) == 1:
    return
 
  prev = None
 
  for i in range(len(a)):

    # store old val at index i first...
    old = a[i]

    if i == 0:
      prev = a[len(a) - 1]
    
    a[i] = prev

    prev = old

def rotateCClockwiseOne(a):
  """rotates an array counter-clockwise (left) one position.

  for example:
  rotateCClockwiseOne(abcdef) = bcdefa
  """
  if len(a) == 1:
    return

  # new val to assign to current
  prev = None

  # old the val of current before re-assignment
  old = None

  for i in range(len(a)-1,-1,-1):
    old = a[i]

    if i == len(a) - 1:
      next = a[0]

    a[i] = next
    next = old

if __name__ == "__main__":
  s = "hello there"

  a = [c for c in s]
  rotateClockwiseOne(a)
  print("".join(a))
  rotateClockwiseOne(a)
  print("".join(a))
  rotateClockwiseOne(a)
  print("".join(a))
  rotateClockwiseOne(a)
  print("".join(a))
  rotateClockwiseOne(a)
  print("".join(a))

  rotateCClockwiseOne(a)
  print("".join(a))
  rotateCClockwiseOne(a)
  print("".join(a))
  rotateCClockwiseOne(a)
  print("".join(a))
  rotateCClockwiseOne(a)
  print("".join(a))
  rotateCClockwiseOne(a)
  print("".join(a))

  
