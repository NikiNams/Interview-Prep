def Bubble_Sort(arr):
	swap=1 #Initialize swap to start the while loop
	while(swap!=0):
		swap=0
		count+=1
		for i in range(0,len(arr)-1):
			if(arr[i]>arr[i+1]):
				arr[i],arr[i+1] = arr[i+1],arr[i] #Swapping elements
				swap+=1


print("Enter the array seperated with spaces")
arr = [int(arr_temp) for arr_temp in input().split(' ')]
Bubble_Sort(arr)
print(arr)
