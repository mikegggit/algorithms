#!/usr/bin/python

def isRotationOf(s1, s2):
  """Returns True if s1 is a rotation of s2"""
  if len(s1) != len(s2):
    return False

  # Potential rotation match must have same first char. 
  for i in range(len(s1)):
    print(i)
    if s1[i] == s2[0]:
      # Test for potential rotation...
      il = None
      result = True
      for ir in range(len(s1)):
        if il is None:
          il = i
        elif il == len(s1) - 1:
          il = 0
        else:
          il += 1
       
        if s1[il] != s2[ir]:
          result = False
          break

      if result:	  
        return True

  # No rotation found...
  return False 
        
if __name__ == "__main__":
  s1 = "abcdefg"
  s2 = "cdefgab"

  print(isRotationOf(s1, s2))

