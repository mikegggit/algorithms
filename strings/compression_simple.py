#!/usr/bin/python

def compress(s):
  """returns a string representing repeated chars as [char][count].  
  
  For example, string aaabbbb => a3b4.
  """
  last = None
  count = 0

  result = ""

  for c in s:
    if not last:
      last = c
      count += 1

    elif last == c:
      count += 1
    else:
      result += last
      result += str(count)
      last = c
      count = 1
  
  result += c
  result += str(count)
  return result

if __name__ == "__main__":
  s = "aaabbbbbcdda"
  sc = compress(s)
  print(s)
  print(sc)
