array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'x']

# O(n*m) - time complexity
# O(2) - simplified to O(1) - space complexity
# def match_array(arr1, arr2):
  # print(f"comparing {arr1} with {arr2}")
  # for x in arr1:
    # for y in arr2:
      # if x == y:
        # return True
  # return False

# match_array(array1, array2)


#O(n+m) - better than O(n*m)
# O(n) - space complexity

#def my_solution(arr1, arr2):
#  store = {}

#  for i in arr1:
#    if not store.get(i):
#      store.update({i: "true"})

#  for j in arr2:
#    if store.get(j):
#      print(True)
#  return False

#my_solution(array1, array2)

def another_solution(arr1, arr2):
  hash = dict()

  for i in range(len(arr1)):
    hash[arr1[i]] = "true"

  for j in arr2:
    if j in hash:
      print(True)
  return False

another_solution(array1, array2)