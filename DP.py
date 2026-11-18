"动态规划大专题"
import sys

# 查找最长公共子字符串 dp
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