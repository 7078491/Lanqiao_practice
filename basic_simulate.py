"基础与模拟"

# =================================== 基础 ==========================================

# 斐波纳契递归
def fib(n):
    if n <= 1: 
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b
n = int(input())
ans = fib(n)
print(ans)
# 斐波纳契数列

# 查找特定和索引
def index_find():
    n = int(input())
    nums = [int(i) for i in input().split()]
    target = int(input())
    num_list = []
    for i in range(n):
        if nums[i] < target:
            delta = target - nums[i]
            for j in range(i, n):
                # 本算法 j > i 恒成立
                if delta == nums[j]:
                    num_list.append([i, j])
    min_idx = float("inf")
    min_j = None
    for tup in num_list:
        i, j = tup
        if i < min_idx:
            min_idx = i
            min_j = j
    print(min_idx, min_j)
    return
# index_find()
# 通过
# 升级: map()函数, in, 字符串index方法

# 35FizzBuzz
def Fizz_Buzz():
    num = int(input())
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
    return
# Fizz_Buzz()
# 通过, 可以通过字符串拼接省去对15的取余判断

def vowel_check():
    s = input()
    n = len(s)
    m = ["a", "e", "i", "u", "o"]
    cnt = 0
    for i in range(1, n):
        r = s[i]
        c = s[i-1]
        if i == 1 and c in m:
            print("no")
            return
        elif i == n-1 and r not in m:
            print("no")
            return
        if c in m and r not in m:
            cnt += 1
        elif c not in m and r in m:
            cnt += 1
    if cnt == 3:
        print("yes")
        return

# 2019枚举
n = int(input())
ans = 0
for i in range(1, n+1):
    r = str(i)
    if '1' in r or '2' in r or '0' in r or '9' in r:
        ans += i
print(ans)
# 通过

# 气球改色(枚举)
"""n = int(input())
nums = sorted(list(map(int, input().split())))
# nums中的所有元素值在1～9间
count = [0] * 9
# 创建一个列表存储不同颜色的出现次数
for num in nums:
    count[num] += 1
print(n - max(count))"""
# 通过,注意避免使用过多的循环嵌套

n = int(input())
colors = input().split()
# colors是字符串列表
max_count = 0
# 记录最多次出现的颜色
for i in set(colors):
    # 调用count方法,找出最多次出现的颜色并更新变量
    if colors.count(i) >= max_count:
        max_count = colors.count(i)
print(n - max_count)

# 二叉树节点输出
n, q = map(int, input().split()) 
routine = []
for _ in range(q):
    S = input()
    routine.append(S)
for i in range(q):
    end = 1
    Sq = routine[i]
    for j in range(len(Sq)):
        r = Sq[j]
        if r == "L":
            end = 2 * end - 1
        elif r == "R":
            end = 2 * end
    print(end)

# =================================== 模拟 ==========================================

# 模拟:冰雹数,剪枝
N = int(input())
ans = 1
# 结果初始化
for start in range(1, N + 1):
    # 遍历从1~N所有的数,找出经过冰雹运算后的最大值
    # ps:n=1时直接进入下个for循环,不进入while
    # 当n>=2时,进入while循环并更新ans
    n = start
    while n != 1:
        if n > ans:
            ans = n          
            # 记录过程中出现过的最大数
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        # 重点,大量减少了计算量
        # 剪枝：n 已经小于 start，说明 n 这条链之前作为起点算过，
        # 它的最大值已被 ans 覆盖，不必继续
        if n < start:
            break
print(ans)
# 通过(注: 看清题意,这里要遍历1~N所有数)
    
# 模拟：电脑查词(队列的应用)
from collections import deque
M, N = map(int, input().split())
# 内存容量与文章词数
a = list(map(int, input().split()))
# 数字标记单词，如果整数相同那么单词相同
# 初始化队列和内存集合
q = deque()
s = set()
# 预设队列 长度为M
ans = 0
for x in a:
    if x in s:
        continue
    ans += 1
    if len(q) >= M: 
        old = q.popleft()
        s.remove(old)
    q.append(x)
    s.add(x)
# 输出需要查词典的次数
print(ans)
# 通过
    
# 奇怪数列,模拟(ps:逻辑很简单)
# 对给定的数字串，从左到右依次统计有几个连续数字
# 将数字个数和数字本身作为变换结果留下
# 初始数字序列和变换次数
s = input().strip()
n = int(input())
for _ in range(n):       
    # n次变换
    # 结果串初始化，重置指针
    result = ""         
    i = 0               
    while i < len(s):
        # 循环，向右遍历
        # i:连续数字左起索引
        j = i
        while j < len(s) and s[j] == s[i]:
            # 检查数字是否连续，增加计数
            j += 1
        # 连续串长 = 总长 - 原索引值
        count = j - i
        # 跳出循环说明这里数字连续中断，记录结果
        result += str(count) + s[i]
        # 连续长计数，数字本身
        i = j
        # 更新起点到下一段开头
    # 变换每次执行完毕更新用于处理的原串，方便再次变换
    s = result
print(s)