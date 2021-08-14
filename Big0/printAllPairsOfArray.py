def logAllPairs(arr):
	for i in range(0, len(arr)):
		for j in range(0, len(arr)):
			print(arr[i], "-", arr[j])
	
myArray = [1,2,3,4,5,6]

logAllPairs(myArray);
