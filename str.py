"字符串专题"
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

# 杂志拼信问题
mag = input()
let = input()
for r in set(let):
    if let.count(r) > mag.count(r):
        print("NO")
        break
else:
    print("YES")
# 通过