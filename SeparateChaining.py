def separateChaining(hashSize, arr, sizeOfArray):
  hashtable = [[]for i in range(hashSize)]
  for data in arr:
    key = data % hashSize
    hashtable[key].append(data)
  return hashtable
