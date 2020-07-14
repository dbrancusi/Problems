def isSubSetSum(arr, n, target):
  if target == 0:
    return True
  if n == 0 and target !=0:
    return False
  print(arr, n, target)

  if arr[n-1] > target:
    return isSubSetSum(arr, n-1, target)
  else:
    return isSubSetSum(arr, n-1, target - arr[n-1]) or isSubSetSum(arr, n-1, target)