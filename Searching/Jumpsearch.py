import math

def jump_search(arr,x):
	length_arr = len(arr)
	if(length_arr>1):
		jump_size = int(math.sqrt(length_arr))
		count=0
		for i in range(0,length_arr,jump_size):
			if(arr[i]==x):
				return i
			elif(arr[i]>x):
				count=i-jump_size #To go back to last jump size to check if x is in between
				break
		#Check in between the jump spaces 	
		while(arr[count]<=x):
			if(arr[count]==x):
				return count
			count+=1

		return -1
	elif(arr[0]==x):
		return 0
	else:
		return -1




print("Enter the array separated by spaces")
a = [int(arr_temp) for arr_temp in input().strip().split(' ')] #Taking input as array/list
print("Enter the element to be searched for")
x=int(input())
result = jump_search(a,x)
if(result == -1):
	print("The number not found in array")
else:
	print("The number is found at index",result)
