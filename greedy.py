# 贪心模拟：品菜问题
t = 1
for _ in range(t):
    n = int(input().strip())
    v = list(map(int, input().split()))
    v1 = [x for x in v if x < 0]
    # 生成负数列表
    s = sum([x for x in v if x >= 0])
    # 非负数求和
    count = len([x for x in v if x >= 0])
    # 非负数总数
    sum1 = sum(v1)
    ans = s * count
    v1.sort(reverse=True)
    p = -1
    for i in range(len(v1)):
        count += 1
        s += v1[i]
        if s * count >= ans:
            ans = s * count
            p = i
            sum1 -= v1[i]
        else:
            break
    ans += sum1
    print(ans)
    
# 贪心算法专题:
# 局部最优求全局最优
# 故障巡检
T = input()
best = 0
# 记录最多走过格子数
for fill in ('L', 'R'):
    # 分别把L,R作为填充内容尝试
    pos = 0
    # 标记机器人位置
    max_left = max_right = 0
    # 机器人位置的最左和最右
    for ch in T:
        # 遍历指令串并先对?替换再检查
        if ch == '?':
            ch = fill
        if ch == 'L':
            # 从原点向左
            pos -= 1
        elif ch == 'R':
            # 从原点向右
            pos += 1
        # 当L比R多时,最远的位置对应数小,反之则大
        # pos 标记一次循环结束时机器人的位置
        max_left = min(max_left, pos)
        max_right = max(max_right, pos)
    # 对比原来的0和向右向左的最远距离
    best = max(best, max_right - max_left + 1)
print(best)
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