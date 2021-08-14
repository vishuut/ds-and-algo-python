def logAllNumbersAndTherePairs(arr):
	
	print("The numbers are: \n")
	
	for num in arr:
		print(num)
		
	print("The pairs are: \n")
	
	for i in range(0, len(arr)):
		for j in range(0, len(arr)):
			print(arr[i], "-", arr[j])
	
myArray = [1,2,3,4,5,6]

logAllNumbersAndTherePairs(myArray);

# The Big O calculation for this function will be O(n) for the first loop and O(n^2) for the second and nested loop. So the total will be:
# O(n + n^2) 
# But according to the 4th rule of Big O calculation, we don't need to care for the non-dominanat term, which is O(n) in this case.
# So we can drop it and the actuall Big O for this function becomes: O(n^2)
