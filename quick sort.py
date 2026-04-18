def quick_sort(self,arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    left =[]
    right =[]
    for i in range(1,len(arr)):
        if arr[i]<pivot:
            left.append(arr[i])
        if arr[i]>pivot:
            right.append(arr[i])
    return quick_sort(left) + pivot + quick_sort(right)

n=int(input("Enter the array to be quick sort:"))
arr=list(map(int,input().split()))
sorted_arr = quick_sort(arr)
print(sorted_arr)