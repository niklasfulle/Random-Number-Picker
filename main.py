import random
import sys

count: int = 54

numbers = []
for i in range(1,count+1):
    numbers.append(i)

def pickRandomNumber() -> int:
  index = random.randint(0,len(numbers) - 1)
  number = numbers[index]
  numbers.pop(index)
  
  return number

while 1:
  key = input("press enter to get a new number")  # or raw_input in python2
  if key == "":
    if(len(numbers) > 0):
      print("your number is: ", pickRandomNumber())
    else: 
      print("all numbers taken")
      sys.exit()
  else:
      print("press enter to get a new number")