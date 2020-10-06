"""
Assignment 2 

Create a function that has:
* at least 3 assignments
* at least one if instruction
* at least one repetitive instruction
-------------------------------------
Test at: `repl.it <https://repl.it/@Paulg2/BoringCyberDeals>`_
"""

def bubble_sort(array:list):
  """
  Sorts the given array in place
  """
  for _ in range(len(array)):
    for index in range(1,len(array)):
      if array[index-1]>array[index]:
        aux=array[index-1]
        array[index-1]=array[index]
        array[index]=aux

array=[3,2,1,5,8]
bubble_sort(array)
print(array)
