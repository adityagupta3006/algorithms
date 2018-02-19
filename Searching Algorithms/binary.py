array = [2,3,4,10,40,55]
search = 55
def binarySearch (arr, l, r, x):
    mid = l + (r - 1)/2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binarySearch(arr, l, mid-1, x)
    else:
        return binarySearch(arr, mid+1, r, x)
    
print binarySearch(array,0, len(array)-1, search)