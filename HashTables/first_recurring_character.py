# Find first recurring character

# My solution including array
def firstRecurringCharacter(input):
  if not isinstance(input,list):
    return input
  
  matchArray = []
  for i in input:
    if i not in matchArray:
      matchArray.append(i)
    else:
      return i
  return "undefined"
    


# Solution using Hash Table
def firstRecurringCharacter2(input):
  
  matchArray = {}
  
  for i in range(len(input)):
    if input[i] in matchArray: # search input[i] as key in matchArray hash table
      return input[i]
    else:
      matchArray[input[i]] = i # update matchArray hash table with input[i] and i as key, value respectively.
  return "undefined"
      
      

print(firstRecurringCharacter([2,5,1,2,3,5,1,2,4]))
print(firstRecurringCharacter2([2,5,1,2,3,5,1,2,4]))

