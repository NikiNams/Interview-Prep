#Binary search
def binary_search(arr,x, start, end):
	if(end>=start):
		mid = int((start+end)/2)
		if(arr[mid]==x):
			return(mid)
		elif(x>arr[mid]):
			return binary_search(arr,x,mid+1,end)
		elif(x<arr[mid]):
			return binary_search(arr,x,start,mid-1)
	else:
		return(-1)

n = int(input())
a = [int(arr_temp) for arr_temp in input().strip().split(' ')] #Taking input as array/list
x=int(input())

length = len(a)-1 #Finding the length to pass it as the last index of the array
result = binary_search(a,x,0,length)
if(result==-1):
	print("The number is not present in the array")
else:
	print('The number found is at index %d'  %result)
