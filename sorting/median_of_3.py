#!/usr/bin/python

def mot(ar):
  # sort ar
  if ar[1] > ar[0]:
    temp = ar[1]  
    ar[1] = ar[0]
    ar[0] = temp

  if ar[2] > ar[1]:
    temp = ar[2]  
    ar[2] = ar[1]
    ar[1] = temp

  if ar[1] > ar[0]:
    temp = ar[1]  
    ar[1] = ar[0]
    ar[0] = temp

  return ar[1]
 
if __name__ == "__main__":
  ar = [50,1000,100]
  print(mot(ar))
