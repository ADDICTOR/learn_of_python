def selector_sort(nums):
    for j in range(0,len(nums)-1): 
        min_index = j
        for i in range(min_index+1,len(nums)):
            if nums[i] < nums[min_index]:
                min_index = i
        nums[j],nums[min_index] = nums[min_index],nums[j]

if __name__ == "__main__":
    nums = [10,1,35,61,89,36,55]
    selector_sort(nums)
    print(nums)