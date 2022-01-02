# MergeSorted Arrays

# classic solution(in-depth)
# interview style question

def mergeSortedArrays(arr1, arr2):
  
  merged_array = []

  i = 0
  j = 0

  while i < len(arr1) and j < len(arr2): # to ensure we do not overrun indexes
    if arr1[i] < arr2[j]:
      merged_array.append(arr1[i])
      i += 1
    else:
      merged_array.append(arr2[j])
      j += 1

  return merged_array + arr1[i:] + arr2[j:] 
  # doing the comparison between arr1[i] and arr2[j] might not cover last index values, hence the return statement has arr1[i:] and arr2[j:] to capture values at those indexes.

mas = mergeSortedArrays([1,3,4,30,54], [5,6,7,45])
print(mas)


# simple solution
# def mergeSortedArrays(arr1, arr2):

#   final = []

#   for x in arr1:
#     final.append(x)

#   for x in arr2:
#     final.append(x)

#   return sorted(final)

# print(mergeSortedArrays([0,3,4,31], [3,4,6,30]))
