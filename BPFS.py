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
# 通过

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
    while q:
        s, d = q.popleft()
        e = s.index(' ')
        er, ec = divmod(e, cols) 
        # 输入a,b,返回a对b的商和余数元组
        # 一维变高维,获得空位序列号
        for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
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
# 通过

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
    
# BFS:简单迷宫
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
# 迷宫数阵
from collections import deque
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
from collections import deque
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
        
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
x1,y1,x2,y2=map(int,input().split())
distance=[(1,0),(0,-1),(0,1),(-1,0)]
q=[]#用队列实现
q.append([x1-1,y1-1,0])#先存起点和当前步数0
while q:
    #print(q)
    now=q.pop(0)
    r,c,s=now[0],now[1],now[2]#当前点的坐标和步数
    arr[r][c]=0#标记
    if r==x2-1 and c==y2-1:#到达终点
        print(s)#打印当前步数，即答案
        break
    for k in range(4):#向4个方向找可行路径
        dx,dy=distance[k]
        x,y=dx+r,dy+c
        if 0<=x<n and 0<=y<m and arr[x][y]==1:#不越界且可走
            arr[x][y]=0#标记该点
            q.append([x,y,s+1])
else:
    print(-1)
        
    
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
# 带边权时BFS失效
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
