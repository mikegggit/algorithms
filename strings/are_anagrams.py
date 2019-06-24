#!/usr/bin/python

def areAnagrams(l, r):
  """Uses a hashtable, with keys designed to hold ascii codes.

  Space complexity is O(1).

  Time complexity is O(n).

  Theoretically, we could sort both strings and compare them letter by letter from left
  to right, but this would require O(nlog(n)) time.
  """
  if l is None or r is None:
    return False

  if len(l) != len(r):
    return False

  m = [0] * 256

  for c in l:
    m[ord(c)] += 1

  for c in r:
    m[ord(c)] -= 1

  for i, v in enumerate(m):
    if v != 0:
      return False

  return True

if __name__ == "__main__":
  print(areAnagrams("listen", "silent"))

