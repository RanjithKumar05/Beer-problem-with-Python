def MinimumBottlesCode():
  quantity = int(input("Quantity please : "))
  nums = [7, 5, 10 ]
  minBottles = 0
  result = 0
  for i in range(len(nums)):
      perfectDivs = quantity // nums[i]
      remaining = quantity % nums[i]
      if (remaining == 0):
              minBottles = perfectDivs
      elif (remaining == 5):
              minBottles = perfectDivs + 1
      elif (remaining == 7):
              minBottles = perfectDivs + 1
      elif (remaining > 7 and remaining < 10):
              minBottles = perfectDivs + remaining % 7 + 1
      elif (remaining > 5 and remaining < 7):
              minBottles = perfectDivs + remaining % 5 + 1
      elif (remaining < 5): 
              minBottles = perfectDivs + remaining
      if (i == 0):
          result = minBottles
      if (result > minBottles):
          result = minBottles
  return result
res = MinimumBottlesCode()
print(res)