"搜索专题: BFS与DFS"

import sys
from collections import deque
# 一维青蛙跳杯问题BFS
s1 = input().strip()
s2 = input().strip()
# 算出从s1变成s2需要步数
# *空 W白 B黑
# 青蛙可选：到相邻3个内的空杯子 
def frog_bfs(start, target):
    # start:初始状态, target:目标状态
    if start == target:
        # 如果初始状态就是目标状态,直接返回0步
        return 0
    q = deque([(start, 0)])
    # 队列中存储状态和步数(双端队列)
    visited = {start}
    # 已访问集合，入队标记
    while q:
        # 队列不空，扩展
        s, d = q.popleft()
        # 出队
        e = s.index('*')                
        # 唯一的空杯位置
        for p in range(len(s)):
            # 遍历所有位置，尝试交换
            if s[p] == '*':
                # 跳过空的
                continue
            if 1 <= abs(p - e) <= 3:    
                # 距离 1/2/3 合法,交换 p 和 e
                lst = list(s)
                # 字符换成列表方便交换
                lst[p], lst[e] = lst[e], lst[p]
                # 状态转移
                ns = ''.join(lst)
                # 新局面字符串生成
                if ns == target:
                    # 目标找到，返回结果步数
                    return d + 1
                if ns not in visited:
                    # 更新已访问
                    visited.add(ns)
                    q.append((ns, d + 1))
    return -1   # 不可达（本题一般有解）
print(frog_bfs(s1, s2))

# BFS:AB对换,卡片换位
# 对于二维的 拼成一维处理
# 用e标记空位，只要实现AB位置互换即可
s1 = input().rstrip('\n')
s2 = input().rstrip('\n')
s0 = s1 + s2
def ab_bfs(start):
    q = deque([(start, 0)])
    visited = {start}
    rows = 2
    cols = 3
    a = start.index('A')
    b = start.index('B')
    dirs = ((-1,0), (1,0), (0,-1), (0,1))
    while q:
        s, d = q.popleft()
        e = s.index(' ')
        er, ec = divmod(e, cols) 
        # 输入a,b,返回a对b的商和余数元组.这里用来取空位的行列号
        # 一维变高维,获得空位序列号
        for dr, dc in dirs:
            nr, nc = er+dr, ec+dc
            if not (0 <= nr < rows and 0 <= nc < cols):
                continue # 越界
            p = nr * cols + nc # 邻居的一维下标折算
            if s[p] == ' ': # 空位只有1个
                continue
            lst = list(s)
            lst[e], lst[p] = lst[p], lst[e]
            ns = ''.join(lst)
            if ns[a] == 'B' and ns[b] == 'A':
                # AB完成对换
                return d + 1
            if ns not in visited:
                visited.add(ns)
                q.append((ns, d+1))
    return -1
print(ab_bfs(s0))

# 胖子走迷宫
from collections import deque

n,k = map(int,input().split())
s = [list(input()) for i in range(n)]
q = deque([(2,2,2,0)])
# 用数字012标记胖瘦状态的半径长，最右侧数值标记当前时刻
vir = [[0 for _ in range(n)] for _ in range(n)]
# 标记访问过的位置(x, y)
vir[2][2] = 1
dirs = ((-1,0), (1,0), (0,-1), (0,1))
def f(t):  
    # 检验时间返回状态
    if t < k:
        return 2
    if t < 2 * k:
        return 1
    else:
        return 0
def check(x,y,r): 
    # 检查区域内是否有障碍
    for i in range(x-r,x+r+1):
        # 横向扫,侧向扫
        for j in range(y-r,y+r+1):
            if s[i][j] == '*':
                # 有墙
                return False
    return True
def weigh_bfs():
    while q:
        x,y,r,t = q.popleft()
        if x == n-3 and y == n-3:
            # 目标终点索引n-3
            return t
        if r != 0:
            # 原地等待,体型变瘦,剪枝
            q.append((x,y,f(t + 1),t+1))
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if r <= nx and nx < n - r and r <= ny and ny < n - r and vir[nx][ny] == 0:
                # 完全不越界且未访问
                if check(nx,ny,r) == True:
                    # 无障碍
                    q.append((nx,ny,f(t+1),t+1))
                    vir[nx][ny] = 1
print(weigh_bfs())

# BFS: 传送门期望
n, m = map(int, input().split())
portal = {}
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    portal.setdefault((x1, y1), []).append((x2, y2))
    portal.setdefault((x2, y2), []).append((x1, y1))
    # 传送门邻接表：key = (x, y)，value = [(x2,y2), ...]
from collections import deque
def transfer_maze_bfs():
    total = n * n
    # 期望均值: E = 所有最短步数和 / n^2
    dist = [-1] * total
    # n^2压成一维处理.终点作为起点得到一维索引
    start = (n-1) * n + (n-1)
    dist[start] = 0
    # 反向考虑以终点作为起点算
    dirs = ((-1,0), (1,0), (0,-1), (0,1))
    q = deque([(n, n)])
    while q:
        x, y = q.popleft()
        d = dist[(x - 1) * n + (y - 1)]
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= n:
                # 不按索引,按实际序号
                p = (nx - 1) * n + (ny - 1)
                if dist[p] == -1:
                    # 未访问,更新！
                    dist[p] = d + 1
                    q.append((nx, ny))
        #  传送门,另外尝试
        nbrs = portal.get((x, y))    
        if nbrs:
            for nx, ny in nbrs:
                p = (nx - 1) * n + (ny - 1)
                if dist[p] == -1:
                    dist[p] = d + 1
                    q.append((nx, ny))
    all_sum = sum(dist)
    E = all_sum / total
    return E
    
E = transfer_maze_bfs()
print(f"{E:.2f}")


# BFS: 九宫重排
start = input().rstrip('\n')
target = input().rstrip('\n')
from collections import deque
def magsqu_bfs(start, target):
    # 一维转二维
    if start == target:
        return 0
    r = c = 3
    # start = list(start) 转二维表: [list(s[i*c:(i+1)*c]) for i in range(r)]
    visited = {start}
    q = deque([(start, 0)])
    dirs = ((-1,0), (1,0), (0,-1), (0,1))
    while q:
        s, d = q.popleft()
        e = s.index('.')
        er, ec = divmod(e, c)
        # 调用divmod取行列号
        for dr, dc in dirs:
            nr, nc = er+dr, ec+dc
            if 0 <= nr < r and 0 <= nc < c:
                p = nr * c + nc
                lst = list(s)
                lst[e], lst[p] = lst[p], lst[e]
                ns = ''.join(lst)
                if ns == target:
                    return d+1
                if ns not in visited:
                    visited.add(ns)
                    q.append((ns, d+1))
    return -1
print(magsqu_bfs(start, target))

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
    print(land[i*m:(i+1)*m])

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
    
# BFS:简单迷宫
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
# 迷宫数阵
def simbaze_bfs(maze):
    sx, sy, ex, ey = map(int, input().split())
    dist = [[-1 for _ in range(m)] for _ in range(n)]
    # dist[x][y]初始化-1表示未访问
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q = deque()
    ex -= 1
    ey -= 1
    sx -= 1
    sy -= 1
    q.append((sx, sy, 0))
    # sx, sy表示当前位置, 后面的0是当前步数
    while q:
        # ps: 这里不需要专门检查起终点.
        x, y, d = q.popleft()
        if x == ex and y == ey:
            # 已抵达终点.
            return d
        for dx, dy in dirs:
            xt, yt = x+dx, y+dy
            # 遍历上下左右
            if 0 <= xt < n and 0 <= yt < m:
                cell = maze[xt][yt]
                if cell == 1 and dist[xt][yt] == -1:
                    # 未访问且可通行，试试！
                    dist[xt][yt] = 1
                    q.append((xt, yt, d+1))
    return -1
print(simbaze_bfs(maze))
# 通过

# 无限画布扩散
ans = 0
for i in range(-2020, 4041):
    for j in range(-2020, 4021):
        if any(abs(i - x) + abs(j - y) <= 2020 for x, y in [(0, 0), (2020, 11), (11, 14), (2000, 2000)]):
            ans += 1
print(ans)
        
# 最少操作数BFS
n, k = map(int, input().split())
def cooperate_bfs(n, k):
    q = deque()
    q.append((n, 0))
    visited = {n}
    while q:
        num, cnt = q.popleft()
        if num == k:
            return cnt
        nums = [num + 1, num - 1, num * 2]
        for i in range(3):
            if 1e5 >= nums[i] >= 1 and nums[i] not in visited:
                q.append((nums[i], cnt+1))
                visited.add(nums[i])
    return -1
print(cooperate_bfs(n, k))
        
# 类bfs:扫雷
n, m = map(int, input().split())
old = [list(map(int, input().split())) for _ in range(n)]
dist = [[0 for _ in range(m)] for _ in range(n)]
surround = [(-1, -1), (-1, 0), (-1, 1), 
            (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for i in range(n):
    for j in range(m):
        locat = old[i][j]
        if locat == 1:
            dist[i][j] = 9
            for dr, dc in surround:
                r, c = i+dr, j+dc
                if 0 <= r < n and 0 <= c < m:
                    if old[r][c] == 0:
                        dist[r][c] += 1
for row in dist:
    print(' '.join(map(str, row)))

# 染色Dijkstra问题
# 带边权时BFS失效,本题值得研究
import heapq
n, m = map(int, input().split())
ts = [list(map(int, input().split())) for _ in range(n)]
INF = float('inf')
finish = [[INF] * m for _ in range(n)]
finish[0][0] = ts[0][0]
pq = [(ts[0][0], 0, 0)]
dirs = ((-1,0),(1,0),(0,-1),(0,1))
while pq:
    t, r, c = heapq.heappop(pq)
    if t > finish[r][c]:
        continue
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            nt = t + ts[nr][nc]
            if nt < finish[nr][nc]:
                finish[nr][nc] = nt
                heapq.heappush(pq, (nt, nr, nc))
print(max(finish[r][c] for r in range(n) for c in range(m)))

# 01BFS: 两栖作战
from collections import deque
n = int(input())
land = [input().strip() for _ in range(n)] 
# 0地1水
def amphibious_bfs():
    INF = float('inf')
    # 预设为无穷大，未确定最少切换次数
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = 0
    # dist[r][c] 表示从(0, 0)到(r, c)最少切换次数
    # 起点初始化,代价0
    dq = deque([(0, 0)])
    # 双端队列初始化,只放坐标(r, c)
    dirs = ((-1,0),(1,0),(0,-1),(0,1))
    while dq:
        r, c = dq.popleft()
        d = dist[r][c]
        # 当前格最少切换次数
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                # 不越界, 计算边权(同0异1)
                w = 0 if land[r][c] == land[nr][nc] else 1
                nd = d + w
                # 边权+当前代价
                if nd < dist[nr][nc]:
                    # 当前切换更少,更新(可执行多次)
                    dist[nr][nc] = nd
                    if w == 0:
                        dq.appendleft((nr, nc))   
                        # 代价 0，去队头
                    else:
                        dq.append((nr, nc))       
                        # 代价 1，去队尾
                    # 上面相当于优先做代价0的.
    return dist[n-1][n-1]
print(amphibious_bfs())
# 内存限制，只过7成(Python3),PyPy3可以全过

# BFS: 土豪劫匪问题
import math
from collections import deque
# 获取最小公倍数
def get_lcm(nums):
    res = 1
    for num in nums:
        res = res * num // math.gcd(res, num)
    return res
# BFS 寻路逻辑
def castle_bfs(T, squares, A, B, C):
    # 特判 1x1x1
    if A == 1 and B == 1 and C == 1:
        return 0 if squares[0][0][0] == 0 else -1
    # 特判起点或终点是墙
    if squares[0][0][0] == 1 or squares[A-1][B-1][C-1] == 1:
        return -1
    q = deque([(0, 0, 0, 0)])  # (x, y, z, 步数)
    visited = {(0, 0, 0)}
    dirs = ((-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1))
    while q:
        x, y, z, d = q.popleft()
        # 剪枝：当前步数已达 T，再走一步必超时
        if d >= T:
            continue
        for dx, dy, dz in dirs:
            nx, ny, nz = x + dx, y + dy, z + dz
            # 1. 边界检查
            if not (0 <= nx < A and 0 <= ny < B and 0 <= nz < C):
                continue
            # 2. 墙壁检查（先查墙，再查终点，避免终点是墙）
            if squares[nx][ny][nz] == 1:
                continue
            # 3. 访问检查
            if (nx, ny, nz) in visited:
                continue
            # 4. 到达终点
            if nx == A-1 and ny == B-1 and nz == C-1:
                return d + 1
            q.append((nx, ny, nz, d + 1))
            visited.add((nx, ny, nz))
    return -1
def solve():
    while True:
        try:
            # 读取维度 A B C，跳过空行
            line = input()
            while line.strip() == "":
                line = input()
            A, B, C = map(int, line.split())
            # 读取地图（A 个 B 行 C 列）
            squares = []
            for _ in range(A):
                layer = []
                for _ in range(B):
                    row = list(map(int, input().split()))
                    layer.append(row)
                squares.append(layer)
            T = get_lcm([A, B, C])
            print(castle_bfs(T, squares, A, B, C))
        except EOFError:
            # 读取到文件末尾时退出循环
            break

# BFS: 逃离混境之地
import sys
from collections import deque
data = sys.stdin.read().split()
n = int(data[0])
m = int(data[1])
# 将坐标转换为 0 索引
sx = int(data[2]) - 1
sy = int(data[3]) - 1
ex = int(data[4]) - 1
ey = int(data[5]) - 1
start = (sx, sy)
exit = (ex, ey)
square = []
idx = 6
for _ in range(n):
    line = data[idx:idx+m]
    square.append(line)
    idx += m
# . 通路 # 墙 k 钥匙
def chaos_bfs(start, exit, square):
    sx, sy = start
    ex, ey = exit
    # 如果起点就是终点
    if sx == ex and sy == ey:
        return 0 if square[sx][sy] == 'k' else -1
    q = deque()
    # 判断起点是不是钥匙
    start_key = 1 if square[sx][sy] == 'k' else 0
    q.append((sx, sy, 0, start_key))
    visited = {(sx, sy, start_key)}
    dirs = ((-1,0), (1,0), (0,-1), (0,1))
    while q:
        x, y, t, have_key = q.popleft()
        if x == ex and y == ey and have_key == 1:
            return t
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if square[nx][ny] == '#':
                continue
            nxt_key = have_key
            if square[nx][ny] == 'k':
                nxt_key = 1
            # 终点单独处理
            if nx == ex and ny == ey and nxt_key == 0:
                continue
            if (nx, ny, nxt_key) in visited:
                continue
            q.append((nx, ny, t+1, nxt_key))
            visited.add((nx, ny, nxt_key))
    return -1
        
print(chaos_bfs(start, exit, square))

# 满分版本: 从钥匙出发双向BFS
n, m = map(int, input().split())
A, B, C, D = map(int, input().split())
# 变索引
A, B, C, D = A-1, B-1, C-1, D-1

mp = []
for i in range(n):
    # 字符地图
    mp.append(list(input()))

inf = 10**9
# 大数字预设
dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]
dis1 = [[inf]*m for _ in range(n)]
dis2 = [[inf]*m for _ in range(n)]

def bfs(x, y, dis):
    q = deque()
    q.append([x, y]) # 将起点加入队列
    dis[x][y] = 0 # 记录层数(距离)
    while q:
        x, y = q.popleft() 
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and mp[nx][ny] != '#':
                if dis[nx][ny] > dis[x][y] + 1:
                    dis[nx][ny] = dis[x][y] + 1
                    q.append([nx, ny]) # 加入队列中，以便遍历

bfs(A, B, dis1)
bfs(C, D, dis2)
res = inf
for i in range(n):
    for j in range(m):
        if mp[i][j] == 'k':
            res = min(res, dis1[i][j] + dis2[i][j]) 
            # 一定要走有钥匙的点，取这当中的最小值
            # dis1[i][j] 和 dis2[i][j]已经预处理过了
if res == inf:
    print(-1)
else:
    print(res)
# ===================分界线==================================
import sys
input = sys.stdin.read
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
def lcm_of_three(a, b, c):
    return lcm(lcm(a, b), c)

def bfs(grid, pos, end, visited, size):
    queue = deque([(pos, [pos])])
    while queue:
        (x, y, z), path = queue.popleft()
        if (x, y, z) == end:
            return path
        for dx, dy, dz in dirs:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nx <= size[0] and 0 <= ny <= size[1] and 0 <= nz <= size[2] and (not visited[nx][ny][nz]) and (grid[nx][ny][nz] == 0):
                new_path = path + [(nx, ny, nz)]
                queue.append(((nx, ny, nz), new_path))
                visited[nx][ny][nz] = 1
data = input().strip().splitlines()
ii = 0
while ii < len(data):
    a, b, c = map(int, data[ii].split())
    mp = [[[0]*c for _ in range(b)] for __ in range(a)]
    v = [[[0]*c for _ in range(b)] for __ in range(a)]
    ii += 1
    for i in range(a):
        for j in range(b):
            s = list(map(int, data[ii].split()))
            ii += 1
            mp[i][j] = s
    path = bfs(mp, (0, 0, 0), (a-1, b-1, c-1), v, (a-1, b-1, c-1))
    if path == None:
        print('-1')
    else:
        if lcm_of_three(a, b, c) < len(path):
            print('-1')
        else:
            print(len(path) -1)


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
        v = int(data[idx])
        u = int(data[idx+1])
        w = int(data[idx+2])
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

# ==========================================================================
# ================================= DFS ====================================
# ==========================================================================
# DFS: 海岛淹没问题
def islands_sink():
    input = sys.stdin.readline
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]
    # 速读边长为n的正方形字符网格, '#' 标记陆地连通块
    visited = [[False] * n for _ in range(n)]
    # visited标记对应点是否已被某岛DFS访问
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    ans = 0
    for i in range(n):
        for j in range(n):
            # 双循环扫描
            if grid[i][j] == '#' and not visited[i][j]:
                # 未访问到的陆地且不在某一连通块中
                has_core = False          
                # 岛屿是否有不会被淹的格子
                stack = [(i, j)]
                visited[i][j] = True
                while stack:
                    # 显式栈迭代，LIFO
                    # DFS遍历全岛
                    x, y = stack.pop()
                    # 检查是否四邻全陆地
                    if (0 < x < n-1 and 0 < y < n-1
                            and grid[x-1][y] == '#' and grid[x+1][y] == '#'
                            and grid[x][y-1] == '#' and grid[x][y+1] == '#'):
                        has_core = True
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            if grid[nx][ny] == '#' and not visited[nx][ny]:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                                # 连通块更新
                if not has_core:          
                    # 没有核心 → 完全淹没
                    ans += 1
    print(ans)

# DFS: 数字排队问题
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    # 建邻接矩阵：i,j 不能同队（有倍数关系，含相等）
    conflict = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            # 相等 或 整除关系
            if a[i] == a[j] or a[i] % a[j] == 0 or a[j] % a[i] == 0:
                conflict[i][j] = True
    # 最小着色：DFS 回溯，color[i] = 第几队
    color = [-1] * n
    best = [n]   # 上界：每人一队
    def dfs(idx, used):
        if used >= best[0]:        # 剪枝
            return
        if idx == n:
            best[0] = used
            return
        # 尝试放入已有队 0..used-1
        for c in range(used):
            ok = True
            for j in range(idx):
                if color[j] == c and conflict[idx][j]:
                    ok = False
                    break
            if ok:
                color[idx] = c
                dfs(idx+1, used)
                color[idx] = -1
        # 开新队
        color[idx] = used
        dfs(idx+1, used+1)
        color[idx] = -1

    dfs(0, 0)
    print(best[0])

if __name__ == "__main__":
    main()
     
# DFS: 绕圈挑战 
n = int(input())
Energ = list(map(int, input().split()))
def Energ_dfs():
    states = [0 for _ in range(n)]
    # 对于第i名, 先向右打到第n个
    # 然后继续从1开始打到i-1
    maxe = max(Energ)
    # 先算一个最大值，大于最大直接跳出循环实现剪枝
    for i in range(n):
        e = Energ[i]
        ok = True
        for step in range(1, n):
            j = (i + step) % n
            # 右手边第step个
            if e > maxe:
                states[i] = 1
                break
            if e > Energ[j]:
                e = 2 * e 
            else:
                states[i] = 0
                ok = False
                break
        if ok:
            states[i] = 1
    return states
states = Energ_dfs()
for i in range(n):
    print(states[i])

# DFS: AnotherEightPuzzle
t = int(input())
cases = []
for _ in range(t):
    case = list(map(int, input().split()))
    cases.append(case)

def check(cases):
    ok = False
    multi = True
    # 标记通过或多解情况
    for i in range(t):
        case = cases[i]
        
    
        if not ok:
            print(f"Case {i}: No answer")
        if multi:
            print(f"Case {i}: Not unique")



def solve_case(init):
    adj = [
        [1, 2, 3],             # A=0
        [0, 2, 4, 5],          # B=1
        [0, 1, 3, 4, 5, 6],    # C=2
        [0, 2, 5, 6],          # D=3
        [1, 2, 5, 7],          # E=4
        [1, 2, 3, 4, 6, 7],    # F=5
        [2, 3, 5, 7],          # G=6
        [4, 5, 6]              # H=7
    ]

    pos = [0] * 8          # 每格填的数
    used = [False] * 9     # 数字 1..8 是否已用
    solutions = []         # 收集解（最多收 2 个就够判断）

    # 预填已固定的格子
    for i in range(8):
        if init[i] != 0:
            # 填充数字,标记数字已使用
            pos[i] = init[i]
            used[init[i]] = True

    # 检查预填是否有冲突
    for i in range(8):
        if init[i] == 0:
            continue
        for nb in adj[i]:
            if init[nb] != 0 and abs(init[i] - init[nb]) == 1:
                return "No answer"      # 预填已矛盾
    # 待填格子列表
    empty = [i for i in range(8) if init[i] == 0]
    def dfs(k):
        if len(solutions) >= 2:
            return                       # 已找到 2 个解，剪枝
        if k == len(empty):
            solutions.append(pos[:])     # 找到一个解
            return
        idx = empty[k]
        
        # 尝试所有未用数字
        for v in range(1, 9):
            if used[v]:
                continue
            # 检查与已填邻居是否连续
            ok = True
            for nb in adj[idx]:
                if pos[nb] != 0 and abs(v - pos[nb]) == 1:
                    ok = False
                    break
            if not ok:
                continue
            pos[idx] = v
            used[v] = True
            dfs(k + 1)
            pos[idx] = 0
            used[v] = False
            if len(solutions) >= 2:
                return
    dfs(0)
    if len(solutions) == 0:
        return "No answer"
    elif len(solutions) >= 2:
        return "Not unique"
    else:
        return ' '.join(map(str, solutions[0]))


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    T = int(data[0])
    out = []
    p = 1
    for case in range(1, T + 1):
        init = [int(data[p + i]) for i in range(8)]
        p += 8
        res = solve_case(init)
        
        out.append(f"Case {case}: {res}")

    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == "__main__":
    main()