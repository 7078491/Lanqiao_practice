"思维训练"
# 思维题：方阵螺旋编号
n, i, j = map(int, input().split())
# 思路： 对边长为n的方阵,右上为n,右下为2n-1,左下为3n-2.
# 方阵每次缩进，边长比相邻大方阵小2 n = n - 2
# 处理考虑： 遍历找到i行j列所在的方阵边长 判断(i, j)所在的边类型及其偏移量

# 层号(算到最近外边界的距离)
k = min(i - 1, j - 1, n - i, n - j)
nk = n - 2 * k              # 当前层边长
start = n * n - nk * nk + 1  # 当前层左上角编号
# 层内相对坐标（1..nk）
r = i - k
c = j - k
if r == 1:                 # 上边
    offset = c - 1
elif c == nk:               # 右边
    offset = (nk - 1) + (r - 1) # 上面走完向下折
elif r == nk:               # 下边
    offset = 2 * (nk - 1) + (nk - c) # 折完走下面
else:                      # 左边
    offset = 3 * (nk - 1) + (nk - r) # 走完下面折回来往上
print(start + offset)
# 通过

# 图书编码与读者需求问题
n, q = map(int, input().split())
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
    print(targets[k])
# 通过

# 26进制转换:Excel地址
n = int(input())
alphas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
"M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ans = []
while n > 0:
    d = (n - 1) % 26
    ans.append(alphas[d])
    n = (n - 1) // 26
ans = ''.join(reversed(ans))
print(ans)