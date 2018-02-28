def mergeSort(arr, l, h):
    if l < h:
        result = arr
        m = (l + h)/2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, h)
        left = arr[:m]
        right = arr[m:]
        i = 0
        j = 0
        k = 0
        
        while i <len(left) and j<len(right):
            if left[i] < right[j]:
                result[k] = left[i]
                i += 1
            else:
                result[k] = right[j]
                j+=1
            k+=1

        while i<len(left):
            result[k] = left[i]
            i += 1
            k += 1
        
        while j<len(right):
            result[k] = right[j]
            j += 1
            k += 1
        
        return result
array = [90, 10, 50, 40, 70, 20]
answer = mergeSort(array, 0, len(array)-1)
print answer