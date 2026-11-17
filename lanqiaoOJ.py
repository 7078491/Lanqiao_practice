"""
蓝桥杯测试题
备赛蓝桥杯，刷题不在多而在刷透。真正掌握需要主动复习 + 归纳。
一、复习的核心原则
原则	说明
重做 > 重看	看题解会产生"我懂了"的错觉，必须关掉答案自己重写
归纳 > 堆量	一类题吃透，胜过十道题各做一遍
限时 > 随意	蓝桥杯是限时赛，平时就要按考试节奏练
输出 > 输入	能给别人讲明白、能默写模板，才算真会
二、具体复习方法
1. 错题本 / 题单分类法（最重要）

按算法类型整理，而不是按做题时间：
text

动态规划/
  ├── 线性DP（LIS、LCS）
  ├── 背包（01、完全、多重）
  ├── 区间DP
  └── 树形DP
图论/
  ├── 最短路（Dijkstra、Floyd、SPFA）
  ├── 最小生成树（Prim、Kruskal）
  └── 拓扑排序
...

每道题记录：

    题目链接
    考察的算法
    关键思路（一句话）
    踩的坑 / 易错点
    代码模板

2. 三遍刷题法
遍数	做法	目标
第1遍	自己做，做不出看题解	理解思路
第2遍	隔 3~7 天，关答案重写	能独立写对
第3遍	隔 2~3 周，限时重写	形成肌肉记忆

第2、3遍如果写不出来，说明没真掌握，标记为重点复习。
3. 默写模板

蓝桥杯很多算法有固定模板，必须闭卷默写：

    快速排序 / 归并排序
    二分查找（左边界、右边界）
    Dijkstra / Floyd / 并查集
    01 背包 / 完全背包
    KMP / 快速幂 / 最大公约数
    树的遍历（前中后序、层序）

建议整理成一份自己的"模板卡"，考前反复默写。
4. 一题多解 + 变式训练

对经典题，尝试：
    换一种解法（如最短路用 Dijkstra 和 SPFA 各写一遍）
    改条件（如把"求最大值"改成"求方案数"）
    加约束（如加时间限制、数据范围变化）

这样能真正理解算法的适用边界。
5. 模拟赛 / 限时训练

    每周至少 1~2 次完整模拟（4 小时，按蓝桥杯赛制）
    用历年真题，严格计时
    赛后复盘：哪些题卡住、为什么、如何改进

三、推荐复习节奏（以 2 个月备赛为例）
阶段	时间	任务
第1阶段	2 周	按专题复习旧题，重做错题，默写模板
第2阶段	3 周	做新题 + 旧题第2遍，补薄弱专题
第3阶段	2 周	限时模拟，查漏补缺
第4阶段	1 周	只看错题本和模板，保持手感
四、蓝桥杯特别提示

    注意数据范围：蓝桥杯常考暴力 + 优化，看清 n 的范围决定算法。
    填空题占比高：很多题可以用暴力/数学推导，不一定要写完整程序。
    Python 组：注意 Python 的 int 无限精度、itertools、collections 等库的熟练使用。
    模板要熟到能默写：考场上没时间推导，直接套模板。
    多练真题：蓝桥杯历年真题风格固定，刷透真题比刷 LeetCode 更有效。

五、一句话总结

    刷过的题，隔几天重做一遍，按算法分类整理，默写模板，限时模拟。
"""

import sys
solved_problems = 51
# 目前所有完成的蓝桥算法题数
# 斐波纳契递归
# def fib(n):
#     if n <= 1: 
#         return n
#     a, b = 0, 1
#     for _ in range(2, n+1):
#         a, b = b, a + b
#     return b
# n = int(input())
# ans = fib(n)
# print(ans)
# 斐波纳契数列
# 字符串专题
# 唯一字符串判定
def solo_str():
    str_list = input()
    n = len(str_list)
    judge = True
    if n <= 100:
        for i in range(n):
            if i+1 < n:
                if str_list[i] == str_list[i+1]:
                    judge = False
                    break     
    if judge:
        print("YES")
    else:
        print("NO")
    return judge
# solo_str()
# 通过

# 字符串重排检测
def str_reset():
    str1 = input()
    str2 = input()
    judge = True
    n1 = len(str1)
    n2 = len(str2)
    if n1 != n2:
        print("NO")
        return
    elif n1 == n2:
        for i in range(n1):
            if str1[i] in str2:
                continue
            else: 
                print("NO")
                return
    if judge:
        print("YES")
    else:
        print("NO")
    return
# str_reset()
# 通过,也可用sort()处理

# 字符串翻转
def str_reverse():
    str1 = input()
    n = len(str1)
    str2 = []
    for i in range(n):
        str2.append(str1[n-i-1])
    print("".join(str2))
    return
# str_reverse()
# 通过,可用列表切片或者排序函数翻转

# 查找差异字符
def find_str():
    str1 = input()
    str2 = input()
    n1 = len(str1)
    n2 = len(str2)
    if n1 > n2:
        n = n1
        str_list = str1
        other = str2
    else: 
        n = n2
        str_list = str2
        other = str1
    for i in range(n):
        if str_list[i] not in other:
            print(str_list[i])
            break
        if str_list[i] in other:
            if other.count(str_list[i]) != str_list.count(str_list[i]):
                print(str_list[i])
                break
    return
# find_str()
# 通过

# 字符串压缩
def str_compress():
    str1 = input()
    target = ""
    i = 0
    while i < len(str1):
        j = i
        while j < len(str1) and str1[j] == str1[i]:
            # j:检查连续相同字符何处结束
            j += 1
        if j - i != 1:
            # j-i表示段长,即有多少个字符连续相同
            target += str1[i] + str(j - i)
        else:
            target += str1[i]
        i = j
    if target.isalpha():
        # 检查结果是否被压缩(是否全为英文字母)
        print("NO")
        return
    print(target)
    return 
# str_compress()
# 通过

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
"""
优美解法: map()函数, in, 字符串index方法
n=int(input())
s=list(map(int,input().split()))
target=int(input())
for num in s:
  if k-num in s:
    print(s.index(num),s.index(k-num))
    break
"""

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

# 贪心算法专题:
# 局部最优求全局最优
# 故障巡检
# T = input()
# best = 0
# # 记录最多走过格子数
# for fill in ('L', 'R'):
#     # 分别把L,R作为填充内容尝试
#     pos = 0
#     # 标记机器人位置
#     max_left = max_right = 0
#     # 机器人位置的最左和最右
#     for ch in T:
#         # 遍历指令串并先对?替换再检查
#         if ch == '?':
#             ch = fill
#         if ch == 'L':
#             # 从原点向左
#             pos -= 1
#         elif ch == 'R':
#             # 从原点向右
#             pos += 1
#         # 当L比R多时,最远的位置对应数小,反之则大
#         # pos 标记一次循环结束时机器人的位置
#         max_left = min(max_left, pos)
#         max_right = max(max_right, pos)
#     # 对比原来的0和向右向左的最远距离
#     best = max(best, max_right - max_left + 1)
# print(best)
# 通过

# LQ聚合
# n = int(input())
# s = list(input().strip())
# # 统计初始 LQ 聚合数，以及每个位置右边的 Q 数量
# # 这里先把?统一看成Q处理
# countL = 0
# ans = 0
# # 计算L，按左侧L的数量累加ans
# for r in s:
#     if r == 'L':
#         countL += 1
#     elif r == 'Q' or r == '?':
#         ans += countL   
# # 先算Q与?和的值
# rightQ = s.count('Q') + s.count('?')
# # 初始化目标最值
# max_ans = ans
# countL = 0  
# # 重置，再次扫描
# for i in range(n):
#     ch = s[i]
#     if ch == 'L':
#         countL += 1
#     elif ch == 'Q':
#         # 算完后丢到左边,右边Q-1
#         rightQ -= 1
#     else:  
#         # ch == '?',把原来看成Q改成看成L再算
#         # 算完丢左边,左边L+1
#         rightQ -= 1
#         # 原来作为 Q ，它和左边 cntL 个 L 配对了 cntL 次
#         # 改成 L 后，它和右边 rightQ 个 Q 配对 rightQ 次
#         ans = ans - countL + rightQ
#         countL += 1
#         if ans > max_ans:
#             # 更大的结果来更新最值
#             max_ans = ans
# print(max_ans)
# 通过

# 贪心: 最大比例(难)
# ps:本题高难，建议认真思考后再尝试手写。
# def gcd(a, b):
#     # 更相减损函数求最大公约数
#     while b:
#         a, b = b, a % b
#     return a
# def factorize(x):
#     # 质因数分解函数，返回{质数：指数}
#     res = {}
#     d = 2
#     while d*d <= x:
#         while x % d == 0:
#             res[d] = res.get(d, 0) + 1
#             x //= d
#         d += 1
#     if x > 1:
#         res[x] = res.get(x, 0) + 1
#     return res
# def solve():
#     n = int(input())
#     a = list(map(int, input().split()))
#     a = sorted(set(a))

#     if len(a) == 1:
#         print("1/1")
#         return

#     facts = []
#     prime_set = set()
#     for x in a:
#         f = factorize(x)
#         facts.append(f)
#         prime_set.update(f.keys())
#     numerator = 1
#     denominator = 1
#     for p in prime_set:
#         exps = [facts[i].get(p, 0) for i in range(len(a))]
#         # 所有指数相同，p 不在公比中
#         same = True
#         for e in exps:
#             if e != exps[0]:
#                 same = False
#                 break
#         if same:
#             continue

#         g = 0
#         for i in range(1, len(exps)):
#             diff = exps[i] - exps[i - 1]
#             if diff < 0:
#                 diff = -diff
#             g = gcd(g, diff)

#         if g == 0:
#             continue

#         if exps[-1] > exps[0]:
#             numerator *= p ** g
#         else:
#             denominator *= p ** g

#     g = gcd(numerator, denominator)
#     numerator //= g
#     denominator //= g
#     print(str(numerator) + "/" + str(denominator))

# solve()

# 思维题：方阵螺旋编号
# n, i, j = map(int, input().split())
# # 思路： 对边长为n的方阵,右上为n,右下为2n-1,左下为3n-2.
# # 方阵每次缩进，边长比相邻大方阵小2 n = n - 2
# # 处理考虑： 遍历找到i行j列所在的方阵边长 判断(i, j)所在的边类型及其偏移量

# # 层号(算到最近外边界的距离)
# k = min(i - 1, j - 1, n - i, n - j)
# nk = n - 2 * k              # 当前层边长
# start = n * n - nk * nk + 1  # 当前层左上角编号
# # 层内相对坐标（1..nk）
# r = i - k
# c = j - k
# if r == 1:                 # 上边
#     offset = c - 1
# elif c == nk:               # 右边
#     offset = (nk - 1) + (r - 1) # 上面走完向下折
# elif r == nk:               # 下边
#     offset = 2 * (nk - 1) + (nk - c) # 折完走下面
# else:                      # 左边
#     offset = 3 * (nk - 1) + (nk - r) # 走完下面折回来往上
# print(start + offset)
# 通过


# 动态规划专题
# 查找最长公共子字符串
def find_longest_constrs():
    # 依次遍历字符并检查相同字符(暴力算法)
    str1 = input()
    str2 = input()
    length = 0
    target = ""
    n1 = len(str1)
    n2 = len(str2)
    for i in range(n1):
        for j in range(n2):
            k = 0
            while k+i < n1 and k+j < n2:
                if str1[i+k] == str2[j+k]:
                    k += 1
                else:
                    break
            if k > length:
                length = k
                target = str1[i:i+k]
    print(target)
# dp算法
def dp_find_longest_constrs():
    str1 = input().strip()
    str2 = input().strip()
    m, n = len(str1), len(str2)
    # 记忆化搜索(+1避免索引越界)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0
    end_index = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # 转移方程
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0
    long_str = str1[end_index - max_len:end_index]
    print(long_str)
# 通过

# 3级台阶问题(3阶斐波纳契)
"""n = int(input())
dp = [0] * (n + 1)
def fib_count(n: int):
    global dp
    # ps: 注意3阶斐波纳契数列的初始三项
    if n == 1:
      return 1
    elif n == 2:
      return 2
    elif n == 3:
      return 4
    if dp[n] != 0:
      return dp[n]
    dp[n] = fib_count(n-1) + fib_count(n-2) + fib_count(n-3)
    return dp[n]
print(fib_count(n))
def count_ways(n):
    # 如果台阶高度为0，定义只有一种走法，即“不走”，所以返回1。
    if n == 0:
        return 1
    # 如果台阶高度为1，那么只有一种走法，即一步走到顶部。
    elif n == 1:
        return 1
    # 如果台阶高度为2，有两种走法：一步一阶走两次或直接两步走到顶部。
    elif n == 2:
        return 2
    # 创建一个长度为 n+1 的 dp 数组，并初始化所有元素为0。
    # dp[i] 将会保存到达第 i 个台阶的方法总数。
    dp = [0] * (n + 1)
    # 初始化前三个台阶的走法数量，因为这些是递推的基础。
    # 到达第0个台阶的方法数定义为1（即不动）。
    # 到达第1个台阶的方法数为1（只能一步走到）。
    # 到达第2个台阶的方法数为2（可以一步一阶走两次，或者一次两步）。
    dp[0], dp[1], dp[2] = 1, 1, 2 
    # 动态规划填充dp数组，从第3个台阶开始计算到第n个台阶。
    # 对于每一个台阶i，可以从i-1、i-2或i-3个台阶上来，
    # 所以到达第i个台阶的方法数等于到达前三个台阶的方法数之和。
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    # 返回dp[n]，即到达第n个台阶的方法总数。
    return dp[n]
N = int(input().strip())
print(count_ways(N))"""
# 通过

# 更小的数,dp(ps:模拟法能过四成)
# s = input()
# n = len(s)
# dp = [[0] * 5010 for _ in range(5010)]
# ans = 0
# # dp[i][j]表示翻转s[i]到s[j]后是否变小,是则填入1否则为0
# for k in range(1, n):
#     # 第k轮递推,k = j - i
#     for i in range(n - k):
#         # 子串从s[i]起,以s[j]结束
#         j = i + k
#         if s[i] < s[j]:
#             dp[i][j] = 0
#         elif s[j] < s[i]:
#             dp[i][j] = 1
#         elif s[j] == s[i]:
#             dp[i][j] = dp[i+1][j-1]
#         if dp[i][j] == 1:
#             ans += 1
# print(ans)
# 复杂度n2,子串计算结果相关

# 查找最长上升子序列
"""n = int(input())
nums = list(map(int, input().split()))
# 状态定义: dp[i]为以nums[i]结尾的最长递增子序列长度.
dp = [1] * (n+1)
pre = [-1] * (n+1)
for i in range(n):
    for j in range(i):
        if nums[j] < nums[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            pre[i] = j
end = dp.index(max(dp))
seq = []
while end != -1:
    seq.append((nums[end]))
    end = pre[end]
seq.reverse()
print(*seq)"""
# 通过

# 两个背包DP问题
# C, n = map(int, input().split())
# dp = [0] * (C + 1)
# # dp = [[0] * (C + 1) for _ in range(n+1)]
# # dp[k]表示当包的重量为k能获得的最大价值
# # 承重是整数,要完全覆盖
# w_list = [0] * (n+1)
# v_list = [0] * (n+1)
# for i in range(n+1):
#     # w表示重量,v表示对应价值
#     w_list[i], v_list[i] = map(int, input().split())
# # ========================================================
# # 完全背包
# for i in range(n):
#     # 遍历物品
#     for j in range(w_list[i], C + 1):
#         # 物品无限制,正序遍历,从能装下的当前物品开始
#         # dp[j - w]包含当前物品从而实现了再选
#         dp[j] = max(dp[j], dp[j - w_list[i]] + v_list[i])
#         # dp[j] 不选当前的情况 最优解
#         # dp[j - w] + v 消耗容量w换取价值v
# # ========================================================
# # 01背包
# # 3种主流实现方式.
# # 二维DP自下而上递推最标准.O(Cn)
# for i in range(C+1):
#     if w_list[i] < j:
#         dp[i][j] = dp[i-1][j]
#     else:
#         dp[i][j] = max(dp[i-1][j], dp[i-1][j - w_list[i]] + v_list[i])
# print(dp[n][C])
# # 滚动两行,介于二者间变体
# # 一维DP删去一维更简洁,遍历需要倒序.O(C)
# for i in range(n):
#     # 遍历物品
#     for j in range(C, w_list[i] - 1, -1):
#         dp[j] = max(dp[j], dp[j - w_list[i]] + v_list[i])
#         # 倒序遍历,选了的物品不能再选
# print(dp[C])
# 通过

# 01背包变种1
# C = 2022
# n = 10
# dp = [[[0] * 2024 for _ in range(n+1)] for _ in range(2024)]
# # 3维DP dp[i][j][k]表示从数1~i中取j个的符合方案有k个
# for i in range(0, 2023):
#     dp[i][0][0] = 1
#     # 特别注意初始化
# for i in range(1, 2023):
#     for j in range(1, n+1):
#         for k in range(1, 2023):
#             if k < i:
#                 dp[i][j][k] = dp[i-1][j][k]
#             else:
#                 dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k-i]         
# print(dp[2022][10][2022])

# 01背包变种2
# 小A点菜问题
# n, m = map(int, input().split())
# a = [0]
# while not len(a) > n:
#     t = [int(i) for i in input().split()]
#     a.extend(t)
# # 行数量不确定的读输入
# dp = [[0] * (m+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         if j == a[i]:
#             # 刚好够点,方案加一
#             dp[i][j] = dp[i-1][j] + 1
#         elif j < a[i]:
#             # 买不起,方案数不变
#             dp[i][j] = dp[i-1][j]
#         elif j > a[i]:
#             # 买的起,递归计算
#             dp[i][j] = dp[i-1][j] + dp[i-1][j-a[i]]
# print(dp[n][m])

# 01背包变种3
# 明日方舟大作战
# def main():
#     n, m, B = map(int, input().split())
#     att = []
#     cos = []
#     lif = []
#     for _ in range(n):
#         a, c = map(int, input().split())
#         att.append(a)
#         cos.append(c)
#     for _ in range(m):
#         l = int(input())
#         lif.append(l)
#     dp = [0] * (B+1)
#     max_lif = max(lif)
#     min_c = min(cos)
#     if B < min_c:
#         print(-1)
#         return
#     # 转化成一般01背包
#     for i in range(n):
#         for j in range(B, cos[i]-1, -1):
#             dp[j] = max(dp[j], dp[j - cos[i]] + att[i])
#     att_sum = dp[B]
#     ans = (max_lif + att_sum - 1) // att_sum
#     print(ans)

# 01背包变种4:搬砖问题
# def main():
#     data = sys.stdin.buffer.read().split()
#     if not data:
#         return
#     p = 0
#     n = int(data[p]); p += 1
#     bricks = []
#     for _ in range(n):
#         w = int(data[p]); v = int(data[p+1]); p += 2
#         bricks.append((w, v))

#     bricks.sort(key=lambda x: x[0] + x[1])
#     max_v = max(v for w, v in bricks)
#     max_w = max(w for w, v in bricks)

#     dp = [-1] * (max_v + max_w + 1)
#     dp[0] = 0
#     ans = 0
#     for w, v in bricks:
#         for j in range(max_v, -1, -1):
#             if dp[j] < 0:
#                 continue
#             if j <= v:
#                 nj = j + w
#                 if dp[j] + v > dp[nj]:
#                     dp[nj] = dp[j] + v
#                     if dp[nj] > ans:
#                         ans = dp[nj]
#     print(ans)

# main()


# 星光共鸣
# MOD = 10**9 + 7
# N, K = map(int, input().split())
# # dp[l][s]：当前长度下，末尾连续1长度为 l，共鸣数为 s 的方案数
# # 核心思想：
# #     共鸣数按"段"拆成 ∑L(L+1)/2，可增量累加
# #     填 1 时新增共鸣数恰为 新末尾连续 1 长度 = l+1；
# #     状态只需记"末尾连续 1 长度 l"和"累计共鸣数 s"；
# #     s ≥ K 截断到 K，最后取 s == K 的总和。
# # 先判 K>N(N+1)2 直接输出 0，可省大量无效计算。
# dp = [[0] * (K + 1) for _ in range(N + 1)]
# dp[0][0] = 1
# for t in range(N):
#     ndp = [[0] * (K + 1) for _ in range(N + 1)]
#     for l in range(t + 1):
#         for s in range(K + 1):
#             v = dp[l][s]
#             if v == 0:
#                 continue
#             # 填 0
#             ndp[0][s] = (ndp[0][s] + v) % MOD
#             # 填 1
#             ns = min(s + l + 1, K)
#             ndp[l + 1][ns] = (ndp[l + 1][ns] + v) % MOD
#     dp = ndp

# ans = sum(dp[l][K] for l in range(N + 1)) % MOD
# print(ans)

# dp计数:摆花
mod = 10 ** 6 + 7
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    a = list(map(int, data[2:2 + n]))

    # dp[j] = 前 i 种花摆 j 盆的方案数（滚动数组）
    dp = [0] * (m + 1)
    dp[0] = 1

    for i in range(n):
        ndp = [0] * (m + 1)
        for j in range(m + 1):
            # 第 i 种花放 k 盆，k 从 0 到 min(a[i], j)
            s = 0
            for k in range(0, min(a[i], j) + 1):
                s += dp[j - k]
            ndp[j] = s
        dp = ndp

    print(dp[m] % mod)

# 足球训练: 贪心dp
# 增加递归深度，防止某些极端情况
sys.setrecursionlimit(2000000)

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    a = [0] * n
    b = [0] * n
    idx = 2
    for i in range(n):
        a[i] = int(data[idx])
        b[i] = int(data[idx+1])
        idx += 2
        
    # 如果 m == 0，直接输出初始乘积
    if m == 0:
        ans = 1
        for i in range(n):
            ans = (ans * a[i]) % 998244353
        print(ans)
        return

    # 二分查找最终的比例阈值 X
    left = 0.0
    right = 1e18  # 比例最大可能是 b/a，设一个足够大的上界
    # 二分 100 次，保证精度绝对足够
    for _ in range(100):
        mid = (left + right) / 2.0
        total_days = 0
        
        # 计算如果阈值为 mid，所有人一共需要多少天
        for i in range(n):
            if b[i] == 0:
                continue
            # 根据公式推导：k_i = floor(1/mid - a_i/b_i)
            # 注意：如果 1/mid 比 a_i/b_i 还小，说明不需要训练，k_i = 0
            if mid > 1e-15:
                k = int(1.0 / mid - a[i] / b[i])
            else:
                k = m # 防止除以 0 或无穷大
                
            if k > 0:
                total_days += k
            if total_days > m:
                break # 剪枝，超出总天数直接退出
                
        if total_days <= m:
            # 说明阈值还可以更低（可以分配更多天）
            right = mid
        else:
            # 天数超了，阈值需要调高（少分配点）
            left = mid
            
    # 二分结束后，用这个阈值算出每个队伍大概分配几天
    ks = [0] * n
    total = 0
    for i in range(n):
        if b[i] == 0:
            continue
        if right > 1e-15:
            k = int(1.0 / right - a[i] / b[i])
        else:
            k = m
        if k > 0:
            ks[i] = k
            total += k
            
    # 可能还剩几天没用完，我们需要把剩下的天数分给当前比例最大的人
    # 这里剩下天数一定不超过 n，直接模拟即可
    import heapq
    # 手搓链表
    class Node:
        def __init__(self, idx):
            self.idx = idx
        def __lt__(self, other):
            i = self.idx
            j = other.idx
            return b[i] * (a[j] + ks[j] * b[j]) > b[j] * (a[i] + ks[i] * b[i])

    pq = []
    for i in range(n):
        if b[i] > 0:
            heapq.heappush(pq, Node(i))
            
    remain = m - total
    for _ in range(remain):
        if not pq:
            break
        node = heapq.heappop(pq)
        i = node.idx
        ks[i] += 1
        heapq.heappush(pq, node)

# 注:本题涉及到数学期望公式转化,分析可用DP算法
# DP概率期望:魔法骰子
# n = int(input())
# # 读入概率列表
# probs = list(map(float, input().split()))
# p = probs[5]
# # p(x = 6)
# q = 1.0 - p
# if p == 0:
#     # 若p为0,那么L的期望显然为0
#     print("0.00")
# elif p == 1:
#     # 若p为1,那么L的期望就是投掷次数n
#     print(f"{n:.2f}")
# else:
#     # 正式计算累加期望,预设为0,每轮加1-P_k
#     # 计算公式: E[L] = Σ_{k=1}^{n} (1 - P_k)
#     E = 0.0
#     pk = 1.0
#     # 初始pk=1(k=0)
#     f = [0.0] * (n + 1)
#     # 实际DP数组,f[i]记录前i次抛掷6连续最长小于k的概率
#     # 从1到n枚举阈值k
#     for k in range(1, n + 1):
#         pk *= p                      
#         # pk = p^k,k次幂,便于递推维护
#         f[0] = 1.0
#         # f[0]每轮重置再填
#         qpk = q * pk
#         # 当k给定时预计算q*pk,简化后续计算
#         for i in range(1, n + 1):
#             val = f[i - 1]
#             # 继承
#             if i == k:
#                 val -= pk
#                 # i = k,减去pk,排除非法情况
#             if i > k:
#                 val -= qpk * f[i - k - 1]
#                 # i > k 时再减去 q·p^k·f[i-k-1]
#             # 截断处理浮点误差
#             if val < 0.0:
#                 val = 0.0
#             elif val > 1.0:
#                 val = 1.0
#             # 回填数组
#             f[i] = val
#         E += 1.0 - f[n]
#         # 即1-pk累加k次
#     print(f"{E:.2f}")
# # L 作为输出标记6的连续出现次数
# # 求 L 关于 n 的期望

# n=int(sys.stdin.readline())
# p_list=list(map(float,sys.stdin.readline().split()))
# p=p_list[5] 
# # 读取输入 其中p为唯一需要用到的概率
# ans=0
# for k in range(1,n+1):
#     # dp[i] 表示前 i 次抛掷中，始终没有出现连续 k 个 6 的概率
#     pk=p ** k
#     dp=[0.00]*(n+1)
#     for i in range(n+1):
#         if i<k:
#             dp[i]=1
#         elif i==k:
#             dp[i]=1-pk
#         else:
#         # 状态转移：前一状态的合法概率 - 恰好在第 i 步不合法的概率
#         # 恰好在第 i 步不合法 = 前 i-k-1 步合法 * 第 i-k 步不是 6 * 最后 k 步全是 6
#             dp[i]=dp[i-1]-dp[i-k-1]*(1.00-p)*pk

#         ans+=(1.00-dp[n])
#     print(f"{ans:.2f}")

# 硬币组成问题
# a = list(map(int,input().split()))
# coin_num = a[0]
# sum_coin = a[1]
# coins = list(map(int,input().split()))
# dp = [0] * (sum_coin + 1)
# dp[0] = 1
# for coin in coins:
#   for i in range(coin, sum_coin + 1):
#     dp[i] += dp[i - coin]
# dp[0] = 0
# print(dp[sum_coin])
# 注意 dp[0] = 1
        
# dp:密码脱落
# s = input()
# # 给定当前的字符串,分析它是原始串删除最少几个字符得到的
# # 等价于找最长回文子序列:对给定的s,求最少删除几个字符得到回文串
# n = len(s)
# # dp[i][j] 表示 s[i..j] 的最长回文子序列长度
# # dp是二维表格,
# dp = [[0] * n for _ in range(n)]
# for i in range(n):
#     dp[i][i] = 1
# # 按子串长度从小到大填表
# for length in range(2, n + 1):
#     for i in range(n - length + 1):
#         # 填充对角线
#         j = i + length - 1
#         if s[i] == s[j]:
#             if length == 2:
#                 dp[i][j] = 2
#             else:
#                 dp[i][j] = dp[i+1][j-1] + 2
#         else:
#             dp[i][j] = max(dp[i+1][j], dp[i][j-1])
# lps = dp[0][n-1] if n > 0 else 0
# # lps标记最长的剩下回文子串
# print(n - lps)
# 通过
        
# data = sys.stdin.read().split()
# # 一次性读取所有数据
# s = data[0]
# # 资料
# n = int(data[1])
# # 密码数与密码表
# passwords = data[2:2+n]
# L = len(s)
# window_count = {}
# # 初始化窗口字典
# for i in range(L - 7): # 窗口范围:0~L-8
#     sig = ''.join(sorted(s[i:i+8]))
#     # 连取8个字符排序,生成列表再拼成签名字sig
#     # 签名与密码字符是完全对应的(无序)
#     window_count[sig] = window_count.get(sig, 0) + 1
#     # 检查签名sig是否存在;已存在则对旧值+1,否则初始化sig的值为0,结果返回字典
# total = 0
# # 目标结果数
# for pwd in passwords:
#     # 遍历密码,检查sig匹配情况
#     # 如果存在sig,从字典获取值;否则+0
#     sig = ''.join(sorted(pwd))
#     total += window_count.get(sig, 0)
# print(total)
# 密文搜索       


# 查找含有最多k个字符的最长子串,返回长度
def find_longest_str():
    s0 = input()
    k = int(input())
    length = 0
    # length记录目标子串长度
    n = len(s0)
    if k >= n:
        print(n)
        return
    elif k <= 0:
        print(0)
        return
    else:
        for i in range(n):
            seen = set()
            # seen统计已经记录的不同字符数
            for j in range(i, n):
                seen.add(s0[j])
                if len(seen) > k:
                    break
                cur_len = j - i + 1
                if cur_len > length:
                    length = cur_len
        print(length)
# find_longest_str()
# 通过
    
# 最大股票利润问题
# n = int(input())
# a = list(map(int, input().split()))
# min_price = a[0]
# # 找到最低买入价
# ans = a[1] - a[0]
# # 初始化利润值
# for i in range(1, n):
#     ans = max(ans, a[i] - min_price)
#     # 利润更新为当第i天卖出（已有的最低价买入）
#     min_price = min(min_price, a[i])
#     # 最低价更新
# print(ans)
# 通过

    
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

# n = int(input())
# colors = input().split()
# # colors是字符串列表
# max_count = 0
# # 记录最多次出现的颜色
# for i in set(colors):
#   # 调用count方法,找出最多次出现的颜色并更新变量
#   if colors.count(i) >= max_count:
#     max_count = colors.count(i)
# print(n - max_count)

# k倍区间问题
"""一开始看到这题标签是暴力，
就想都没想先前缀和再枚举每一区间，
结果超时了，然后看了题解才知道，
前缀和是基本要想到了，但是后面不能暴力枚举，要用用点技巧（不知道是不是数学技巧），
反正我想了好久。好了，说一下我的总结吧！就是再加一个数组记录这个余数的前缀区间有几个
（至于为什么后面会说），然后我们在想一下当两个数除以K的余数相同时，
将他们相减之后是不是能被K整除（如：k=3,a1=4,b=7），
我们会惊奇的发现是可以的，利用这个技巧，
我们可以在求前缀和的时候判断一下这个前缀区间模上K的余数，并计数（cnt[]）
,然后再想一下，我们用前缀和求任意一个区间是怎么求得？这样当我们再在判断余数的时候，
加上之前也是这个余数的前缀区间的集合数量，因为只要我这个有和前面任何一个余数相同，
都能得到一个被K整除的区间（并且还不一样），利用这个我们可得到优化。
"""
# n, k = map(int, input().split())
# a = []
# for _ in range(n):
#     x = int(input())
#     a.append(x)
# # hash实现
# cnt = {}
# cnt[0] = 1
# pre = 0
# ans = 0
# for num in a:
#     pre = (pre + num) % k
#     ans += cnt.get(pre, 0)
#     cnt[pre] = cnt.get(pre, 0) + 1
# print(ans)
# 运行超时.改进思路:前缀和.hash

"""n, m = map(int, input().split())
line2 = input().split()
a = [int(x) for x in line2[:m]] 
a = a + [None] * (n - m)
b = list(map(int, input().split()))
# 原地排序
i = m - 1          # A 有效部分的最后一个下标
j = len(b) - 1     # B 的最后一个下标
k = n - 1          # A 最终填入位置
while i >= 0 and j >= 0:
    if a[i] > b[j]:
        a[k] = a[i]
        i -= 1
    else:
        a[k] = b[j]
        j -= 1
    k -= 1
while j >= 0:
    a[k] = b[j]
    j -= 1
    k -= 1
print(*a)

result = sorted(a + b)
print(*result)"""

# 杂志拼信问题
# mag = input()
# let = input()
# for r in set(let):
#     if let.count(r) > mag.count(r):
#         print("NO")
#         break
# else:
#     print("YES")
# 通过

# 图书编码与读者需求问题
"""n, q = map(int, input().split())
book_codes = []
# 书的编号,单层列表
idxs = []
# 读者需求,单层列表
les = []
# 需求码长度单层列表
for _ in range(n):
    book_code = input()
    book_codes.append(book_code)
for _ in range(q):
    l, idx = map(int, input().split())
    idx = str(idx)
    idxs.append(idx)
    les.append(l)
targets = [0] * (q + 1)
# 读者需要图书最小编号
for i in range(q):
    codes = []
    # 存储所有需要的书
    for j in range(n):
        if len(book_codes[j]) >= les[i] and book_codes[j].endswith(idxs[i]):
            codes.append(int(book_codes[j]))
    if codes:
        targets[i] = min(codes)
    else:
        targets[i] = -1
for k in range(q):
    print(targets[k])"""
# 通过
    
# 一维青蛙跳杯问题BFS
# s1 = input().strip()
# s2 = input().strip()
# # 算出从s1变成s2需要步数
# # *空 W白 B黑
# # 青蛙可选：到相邻3个内的空杯子 
# from collections import deque
# def frog_bfs(start, target):
#     # start:初始状态, target:目标状态
#     if start == target:
#         # 如果初始状态就是目标状态,直接返回0步
#         return 0
#     q = deque([(start, 0)])
#     # 队列中存储状态和步数(双端队列)
#     visited = {start}
#     # 已访问集合，入队标记
#     while q:
#         # 队列不空，扩展
#         s, d = q.popleft()
#         # 出队
#         e = s.index('*')                
#         # 唯一的空杯位置
#         for p in range(len(s)):
#             # 遍历所有位置，尝试交换
#             if s[p] == '*':
#                 # 跳过空的
#                 continue
#             if 1 <= abs(p - e) <= 3:    
#                 # 距离 1/2/3 合法,交换 p 和 e
#                 lst = list(s)
#                 # 字符换成列表方便交换
#                 lst[p], lst[e] = lst[e], lst[p]
#                 # 状态转移
#                 ns = ''.join(lst)
#                 # 新局面字符串生成
#                 if ns == target:
#                     # 目标找到，返回结果步数
#                     return d + 1
#                 if ns not in visited:
#                     # 更新已访问
#                     visited.add(ns)
#                     q.append((ns, d + 1))
#     return -1   # 不可达（本题一般有解）
# print(frog_bfs(s1, s2))
# 通过

# BFS:AB对换,卡片换位
# 对于二维的 拼成一维处理
# 用e标记空位，只要实现AB位置互换即可
# s1 = input().rstrip('\n')
# s2 = input().rstrip('\n')
# s0 = s1 + s2
# def ab_bfs(start):
#     q = deque([(start, 0)])
#     visited = {start}
#     rows = 2
#     cols = 3
#     a = start.index('A')
#     b = start.index('B')
#     while q:
#         s, d = q.popleft()
#         e = s.index(' ')
#         er, ec = divmod(e, cols) 
#         # 输入a,b,返回a对b的商和余数元组
#         # 一维变高维,获得空位序列号
#         for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
#             nr, nc = er+dr, ec+dc
#             if not (0 <= nr < rows and 0 <= nc < cols):
#                 continue # 越界
#             p = nr * cols + nc # 邻居的一维下标折算
#             if s[p] == ' ': # 空位只有1个
#                 continue
#             lst = list(s)
#             lst[e], lst[p] = lst[p], lst[e]
#             ns = ''.join(lst)
#             if ns[a] == 'B' and ns[b] == 'A':
#                 # AB完成对换
#                 return d + 1
#             if ns not in visited:
#                 visited.add(ns)
#                 q.append((ns, d+1))
#     return -1
# print(ab_bfs(s0))
# 通过;如果这里的rols变为n,cols变为m,

# BFS:长草
n, m = map(int, input().split())
land = ''.join(input().strip() for _ in range(n))
# 一行读入，len(land) = m * n
k = int(input())
def grass_bfs(land, k, m, n):
    grid = list(land)         
    q = deque()
    for i in range(n * m):
        if grid[i] == 'g':
            q.append(i)        
            # 一维下标遍历g
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for _ in range(k):
        size = len(q)
        if size == 0:
            # 无草需要扩散
            break
        for _ in range(size):
            i = q.popleft()
            r, c = divmod(i, m)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    p = nr * m + nc
                    if grid[p] == '.':
                        grid[p] = 'g'
                        q.append(p)   # 新草留到下一层
    return ''.join(grid)
land = grass_bfs(land, k, m, n)
for i in range(n):
    print(land[m*i:(i+1)*m])

# BFS: 迷宫陷阱
n, K = map(int, input().split())
maze = [list(input().strip()) for _ in range(n)]
# 四种: . # X % 路 墙 坑 宝
# 返回从左上角到右下需要最少步数
def maze_bfs():
    # dist[r][c][t] 表示当前步数，t表示无敌剩余步数<=K
    # -1 表示未访问,访问区域列表初始化
    dist = [[[-1]*(K+1) for _ in range(n)] for _ in range(n)]
    # 起点 (0,0) 如果是 '%'，第一次到达获得无敌
    start_t = 0
    if maze[0][0] == '%':
        start_t = K
        maze[0][0] = '.'  # 道具拿掉
    # 若起点是 X 且无无敌，则无法出发
    if maze[0][0] == 'X' and start_t == 0:
        return -1
    dist[0][0][start_t] = 0
    q = deque()
    q.append((0, 0, start_t))
    # 队列存当前行列号和无敌剩余步数
    dirs = ((-1,0),(1,0),(0,-1),(0,1))
    while q:
        # 局面更新！
        r, c, t = q.popleft()
        d = dist[r][c][t]
        if r == n-1 and c == n-1:
            # 到达出口，返回步数
            return d
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if not (0 <= nr < n and 0 <= nc < n):
                continue # 越界跳过
            cell = maze[nr][nc]
            if cell == '#':
                # 墙，不管它
                continue
            nt = t
            if cell == 'X':
                if t == 0:
                    # 没无敌不能通过陷阱
                    continue
                nt = t - 1
                # 能过，无敌时长-1
            elif cell == '%':
                # 第一次到达还是 '%'，说明之前没被拿过
                # 拿到后无敌时长设为 K，并标记道具消失
                nt = K
                maze[nr][nc] = '.'  
            else:  # '.'
                if t > 0:
                    nt = t - 1
                else:
                    nt = 0
            if dist[nr][nc][nt] == -1:
                # (nr, nc)尚未访问，更新步数
                dist[nr][nc][nt] = d + 1
                q.append((nr, nc, nt))
    return -1
print(maze_bfs())
    
# 模拟:冰雹数,剪枝
# N = int(input())
# ans = 1
# # 结果初始化
# for start in range(1, N + 1):
#     # 遍历从1~N所有的数,找出经过冰雹运算后的最大值
#     # ps:n=1时直接进入下个for循环,不进入while
#     # 当n>=2时,进入while循环并更新ans
#     n = start
#     while n != 1:
#         if n > ans:
#             ans = n          
#             # 记录过程中出现过的最大数
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1
#         # 重点,大量减少了计算量
#         # 剪枝：n 已经小于 start，说明 n 这条链之前作为起点算过，
#         # 它的最大值已被 ans 覆盖，不必继续
#         if n < start:
#             break
# print(ans)
# 通过(注: 看清题意,这里要遍历1~N所有数)
    
# 模拟：电脑查词(队列的应用)
# from collections import deque
# M, N = map(int, input().split())
# # 内存容量与文章词数
# a = list(map(int, input().split()))
# # 数字标记单词，如果整数相同那么单词相同
# # 初始化队列和内存集合
# q = deque()
# s = set()
# # 预设队列 长度为M
# ans = 0
# for x in a:
#     if x in s:
#         continue
#     ans += 1
#     if len(q) >= M: 
#         old = q.popleft()
#         s.remove(old)
#     q.append(x)
#     s.add(x)
# # 输出需要查词典的次数
# print(ans)
# 通过
    
# 奇怪数列,模拟(ps:逻辑很简单)
# 对给定的数字串，从左到右依次统计有几个连续数字
# 将数字个数和数字本身作为变换结果留下
# 初始数字序列和变换次数
# s = input().strip()
# n = int(input())
# for _ in range(n):       
#     # n次变换
#     # 结果串初始化，重置指针
#     result = ""         
#     i = 0               
#     while i < len(s):
#         # 循环，向右遍历
#         # i:连续数字左起索引
#         j = i
#         while j < len(s) and s[j] == s[i]:
#             # 检查数字是否连续，增加计数
#             j += 1
#         # 连续串长 = 总长 - 原索引值
#         count = j - i
#         # 跳出循环说明这里数字连续中断，记录结果
#         result += str(count) + s[i]
#         # 连续长计数，数字本身
#         i = j
#         # 更新起点到下一段开头
#     # 变换每次执行完毕更新用于处理的原串，方便再次变换
#     s = result
# print(s)
        
def main():
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
        
        
        
# 二分法: 分巧克力
# 读输入
# ps: 需要认真思考再手写
# data = sys.stdin.read().split()
# n = int(data[0])
# k = int(data[1])
# chocolates = []
# max_side = 0
# idx = 2
# for _ in range(n):
#     h = int(data[idx]); w = int(data[idx + 1])
#     idx += 2
#     chocolates.append((h, w))
#     max_side = max(max_side, h, w)

# def check(x):
#     total = 0
#     for h, w in chocolates:
#         total += (h // x) * (w // x)
#         if total >= k:
#             return True
#     return False

# left, right = 1, max_side
# ans = 0
# while left <= right:
#     mid = (left + right) // 2
#     if check(mid):
#         ans = mid
#         left = mid + 1
#     else:
#         right = mid - 1
# print(ans)


    

# 2019枚举
# n = int(input())
# ans = 0
# for i in range(1, n+1):
#     r = str(i)
#     if '1' in r or '2' in r or '0' in r or '9' in r:
#         ans += i
# print(ans)
# 通过

# N = 2026060660606202

# def C(x):
#     return x - x//2 - x//1013 + x//2026
# def T(M):
#     s = 0
#     l = 1
#     while l <= M:
#         q = M // l
#         r = M // q
#         s += (C(r) - C(l-1)) * C(q)
#         l = r + 1
#     return s

# ans = 0
# p2 = 1
# alpha = 0
# while p2 <= N:
#     p1013 = 1
#     beta = 0
#     while p2 * p1013 <= N:
#         M = N // (p2 * p1013)
#         ans += (alpha + beta + 1) * T(M)
#         p1013 *= 1013
#         beta += 1
#     p2 *= 2
#     alpha += 1
# print(ans)

# 26进制转换:Excel地址
# n = int(input())
# alphas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
# "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# ans = []
# while n > 0:
#     d = (n - 1) % 26
#     ans.append(alphas[d])
#     n = (n - 1) // 26
# ans = ''.join(reversed(ans))
# print(ans)

# 二叉树节点输出
# n, q = map(int, input().split()) 
# routine = []
# for _ in range(q):
#     S = input()
#     routine.append(S)
# for i in range(q):
#     end = 1
#     Sq = routine[i]
#     for j in range(len(Sq)):
#         r = Sq[j]
#         if r == "L":
#             end = 2 * end - 1
#         elif r == "R":
#             end = 2 * end
#     print(end)

from collections import deque
# 串门: BFS两次求树直径
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    total = 0
    idx = 1
    for _ in range(n - 1):
        v = int(data[idx]); u = int(data[idx+1]); w = int(data[idx+2])
        idx += 3
        adj[v].append((u, w))
        adj[u].append((v, w))
        total += w

    def bfs(start):
        dist = [-1] * (n + 1)
        dist[start] = 0
        q = deque([start])
        far_node, far_dist = start, 0
        while q:
            x = q.popleft()
            for y, w in adj[x]:
                if dist[y] == -1:
                    dist[y] = dist[x] + w
                    q.append(y)
                    if dist[y] > far_dist:
                        far_dist = dist[y]
                        far_node = y
        return far_node, far_dist

    u, _ = bfs(1)          # 第一次 BFS：找最远点 u
    _, diameter = bfs(u)   # 第二次 BFS：从 u 找最远距离 = 直径

    print(2 * total - diameter)

if __name__ == "__main__":
    main()