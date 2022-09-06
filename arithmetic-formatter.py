from ast import Num


def isAddition(one, two) :
  try : return int(one) + int(two)
  except : return False

def isSubtraction(one, two) :
  try : return int(one) - int(two)
  except : return False

def formatter(list, answers = False) :
  answer = ''
  
  for item in list :
    splitItem = item.split()
    
    if answers :  
      if splitItem[1] == '+' :
        try : answer = isAddition(splitItem[0], splitItem[2])
        except : print('NUMBER NOT PROVIDED')
      
      if splitItem[1] == '-' :
        try : answer = isAddition(splitItem[0], splitItem[2])
        except : print('NUMBER NOT PROVIDED')
    
    print('{:>7}\n{:<3}{:>4}\n{:^7}\n{:>7}\n'.format(splitItem[0], splitItem[1], splitItem[2], '-------', answer))

formatter(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
formatter(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)