from ast import Num


def isAddition(one, two) :
  try : return int(one) + int(two)
  except : False

def isSubtraction(one, two) :
  try : return int(one) - int(two)
  except : return False

def formatter(list, answers = False) :
  answer = ''
  
  for item in list :
    splitItem = item.split()
    
    if splitItem[1] == '+' :
      try : isAddition(splitItem[0], splitItem[2])
      except : print('NOT A NUMBER')
    
    if splitItem[1] == '-' :
      try : isAddition(splitItem[0], splitItem[2])
      except : print('NOT A NUMBER')
    
    print(f'{splitItem[0]}\n{splitItem[1]} {splitItem[2]}\n-------\n{answers}\n')

formatter(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
formatter(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)