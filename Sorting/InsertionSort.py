def Insertion_Sort(arr):
	for i in range(1,len(arr)):
		key = arr[i]
		j=i-1
		while(arr[j]>key and j>=0):
			arr[j+1]=arr[j]
			j=j-1
		arr[j+1]=key


print("Enter the array seperated with spaces")
arr = [int(arr_temp) for arr_temp in input().split(' ')]
Insertion_Sort(arr)
print(arr)
