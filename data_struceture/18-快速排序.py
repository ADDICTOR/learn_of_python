def quick_sort(nums):
    if len(nums) >=2:
        mid = nums[len(nums)//2]
        left ,right =[],[]
        nums.remove(mid)
        for d in nums:
            if d < mid:
                left.append(d)
            else:
                right.append(d)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return nums
if __name__ == "__main__":
    nums = [10,1,35,61,89,36,55]
    print(quick_sort(nums))
