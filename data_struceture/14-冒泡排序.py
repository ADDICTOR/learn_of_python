def bubble_sort(array):
    count = len(array)-1
    for i in range(count):
        temp_c = True
        for j in range(count-i):
            if num[j] > num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]
                temp_c =False
        if temp_c:
            print('比较了{}次'.format(i))
            break
if __name__ == "__main__":
    num = [10,1,35,61,89,36,55]
    se(num)
    print(num)