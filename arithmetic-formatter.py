from ast import Num


def formatter(list, answers = False) :
  answers = ''
  
  for item in list :
    splitItem = item.split()
    
    if splitItem[1] == '+' :
      answers = int(splitItem[0]) + int(splitItem[2])
    
    print(f'{splitItem[0]}\n{splitItem[1]} {splitItem[2]}\n-------\n{answers}\n')

formatter(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
formatter(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)