"""
蓝桥杯测试题: 备赛总纲

刷题不在多而在刷透。真正掌握需要主动复习 + 归纳。

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




# k倍区间问题
"""一开始看到这题标签是暴力，
就想都没想先前缀和再枚举每一区间，
结果超时了，然后看了题解才知道，
前缀和是基本要想到了，但是后面不能暴力枚举，要用用点技巧:加一个数组记录这个余数的前缀区间有几个
然后我们在想一下当两个数除以K的余数相同时，
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
        
        
# 二分法: 分巧克力
# 读输入
# ps: 需要认真思考再手写
data = sys.stdin.read().split()
n = int(data[0])
k = int(data[1])
chocolates = []
max_side = 0
idx = 2
for _ in range(n):
    h = int(data[idx]); w = int(data[idx + 1])
    idx += 2
    chocolates.append((h, w))
    max_side = max(max_side, h, w)

def check(x):
    total = 0
    for h, w in chocolates:
        total += (h // x) * (w // x)
        if total >= k:
            return True
    return False

left, right = 1, max_side
ans = 0
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)

N = 2026060660606202

def C(x):
    return x - x//2 - x//1013 + x//2026
def T(M):
    s = 0
    l = 1
    while l <= M:
        q = M // l
        r = M // q
        s += (C(r) - C(l-1)) * C(q)
        l = r + 1
    return s

ans = 0
p2 = 1
alpha = 0
while p2 <= N:
    p1013 = 1
    beta = 0
    while p2 * p1013 <= N:
        M = N // (p2 * p1013)
        ans += (alpha + beta + 1) * T(M)
        p1013 *= 1013
        beta += 1
    p2 *= 2
    alpha += 1
print(ans)

