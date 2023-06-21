def insert_sort(nums):
    for i in range(1,len(nums)):
        for j in range(i,0,-1):
            if nums[j] < nums[j-1]:
                nums[j],nums[j-1] =nums[j-1],nums[j]
if __name__ == "__main__":
    nums = [10,1,35,61,89,36,55]
    insert_sort(nums)
    print(nums)