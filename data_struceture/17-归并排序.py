def merge_sort(list_data):
    if len(list_data) <= 1:
        return list_data
    count = int (len(list_data)/2)
    left  = merge_sort(list_data[:count])
    right = merge_sort(list_data[count:])
    return merge(left,right)

def merge(left,right):
    l,r = 0,0
    result=[]
    while l < len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l = l+1 
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])
    return result
if __name__ == "__main__":
    nums = [10,1,35,61,89,36,55] 
    print(merge_sort(nums))
  