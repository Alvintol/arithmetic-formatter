def formatter(list, answers = False) :
  for item in list :
    splitItem = item.split()
    print(splitItem)

formatter(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
formatter(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)