# google interview question(python answer)

# suggested approach
# def hasPairWithSum(arr, sum):

#     myset = list()

#     for i in range(len(arr)):
#         if arr[i] in myset:
#             print(True)
#         else:
#             myset.append(sum - arr[i])
#             print(False)

# hasPairWithSum([1,2,3,4], 3)

# My approach
def hasPairWithSum(arr, sum):

    myset = set()

    for i in arr:
        if i in myset:
            print(True)
        else:
            myset.add(sum - i)
            print(False)


hasPairWithSum([1,2,3,4], 7)