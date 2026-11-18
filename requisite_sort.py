"基础排序算法"
# 排序算法专题(重点!)
# 选择排序
# 依次遍历全数组找出最小的元素放到第i个位置
def selection_sort(nums):
    n = len(nums)
    for i in range(n-1):
        # m:标记从索引i到n-1的最小值
        m = i
        for j in range(i+1, n):
            # 更新最小值范围:1到n,即全数组
            if nums[j] < nums[m]:
                m = j
        # 元素交换
        nums[i], nums[m] = nums[m], nums[i]
    return nums
# 通过(标答)

# 冒泡排序
# 从左向右"冒泡"到合适的位置，记录每轮是否发生交换
# 没有交换说明有序
def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        # 当n-1个排好后剩下一个的位置已经是有序的
        swapped = False
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

# 插入排序
# 取出无序元素加入有序队列
def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        # i从1起,因为nums[0]本身是有序的
        key = nums[i]
        # key保存将要插入的值
        j = i - 1
        # j是有序部分的尾标
        while j >= 0 and nums[j] > key:
            # 从后往前查找
            nums[j+1] = nums[j]
            # 当key小于nums[j],将nums[j](大的数)后挪
            # 索引更新为j+1
            j -= 1
            # 继续向前找
        nums[j+1] = key
        # 这里j+1是因为nums[j]刚好比key大,跳出了while循环
        # 所以j+1指向需要插入的位置
    return nums
# 通过(标答)

# 快速排序
# 分治与双指针:将数组分成左右,使所有左边元素小于右边
def qsort(nums):
    # 原地排法,空间复杂度低
    n = len(nums)
    R = n - 1
    L = 0
    i, j = L, R
    # 初始化双指针,选取中间值作为基准量
    key = nums[(L + R) // 2]
    while i <= j:
        # 左指针在右指针左侧
        while nums[i] < key:
            i += 1
        while nums[j] > key:
            j -= 1
        # 如果数据符合区间,指针向另一端靠近
        # 发现不符合条件的数据时指针停下
        if i <= j:
            # 两指针都找到目标后执行交换,继续遍历
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    # 检查区间是否穷尽,否则递归处理
    if j > L:
        qsort(L, j)
    if i < R:
        qsort(i, R)    
    return
# 三段式递归速排,占空间大但简明易懂
def quicksort(arr):  
    if len(arr) <= 1:  
        return arr  
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]  
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot]  
    return quicksort(left) + middle + quicksort(right)  
# 标答通过

# 归并排序
def merge_sort(L, R):
    def merge(L, mid, R):
        global a, b
        i = L
        j = mid + 1
        t = 0
        while (i <= mid and j <= R):
            if a[i] > a[j]:
                b[t] = a[j]
                j += 1
            else:
                b[t] = a[i]
                i += 1
            t += 1
        while i <= mid:
            b[t] = a[i]
            i += 1
            t += 1
        while j <= R:
            b[t] = a[j]
            j += 1
            t += 1
        for i in range(t):
            a[L+i] = b[i]
    if L < R:
        mid = (L + R) // 2
        merge_sort(L, mid)
        merge_sort(mid+1, R)
        merge(L, mid, R)
# n = int(input())
# a = list(map(int, input().split()))
# b = [0] * len(a)
# merge_sort(0, n-1)
# print(*a)
# 标答通过