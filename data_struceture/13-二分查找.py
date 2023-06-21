def binary_search(find_value,args):
    # 记录列表查找的范围
    begin = 0
    end = len(args)-1
    # 比较是否我们要查找的数据
    while begin <= end:
        # 计算中间的索引号
        mid = (begin+end)//2
        if args[mid] == find_value:
            return mid
        elif args[mid] > find_value:
            end = mid -1
        else:
            begin = mid + 1
    return -1


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8]
    print(binary_search(69,nums))