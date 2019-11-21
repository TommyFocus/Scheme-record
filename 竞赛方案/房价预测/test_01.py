def bubblesort(arr):
	for i in range(1, len(arr)):
		for j in range(0, len(arr)-i):
			# 从第一个开始，两两比较，将较大的放到后面，直到最后
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr