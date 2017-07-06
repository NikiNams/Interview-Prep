def Selection_Sort(arr):
	for i in range(0,len(arr)):
		min = i
		for j in range(i+1, len(arr)):
			if(arr[j]<arr[min]):
				min=j
		arr[i], arr[min]  =arr[min], arr[i] #swapping the elements


print("Enter the array seperated with spaces")
arr = [int(arr_temp) for arr_temp in input().split(' ')]
Selection_Sort(arr)
print(arr)