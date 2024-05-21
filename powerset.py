def powerset(nums):
  x = len(nums)
  powerset = []
  for i in range(1 << x):
    powerset.append([nums[j] for j in range(x) if (i & (1 << j))])
        
  return powerset

nums1 = [1,2,3]
powerset(nums1)                                  #output = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
