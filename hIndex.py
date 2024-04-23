def hIndex(citations):
  citations.sort()
  n = len(citations)
  i = 1
  while (i <= n):
    if citations[n - i] < i :
      break
    i += 1
  return i - 1

citations1 = [3,0,6,1,5]               #Output: 3
