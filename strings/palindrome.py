#!/usr/bin/python

def isPalindrome(s):
  if s is None or len(s) < 2:
    return True

  i, j = 0, len(s) - 1

  while i < j:
    if s[i] != s[j]:
      return False
    i += 1
    j -= 1

  return True

if __name__ == "__main__":
  print(isPalindrome("abcdefedcba"))
  print(isPalindrome("abcdefabcdef"))
