def fa(s):
    l = []
    for i in range(len(s)):
         l.append(s[i])
    l.reverse()
    s_new = ''
    for i in range(len(l)):
        s_new += l[i]
    return s_new

def fb(s):
    l1 = []
    for i in range(len(s)):
         l1.append(s[i])
    length = len(l1)
    l2 = []
    l2.append([])
    cnt = 0
    for i in range(length):
        if l1[i] == ' ' :
            cnt += 1
            l2.append([])
        else :
            l2[cnt].append(l1[i])
    s_new = ''
    for i in range(len(l2)):
        l2[i].reverse()
        for j in range(len(l2[i])):
            s_new += l2[i][j]
        s_new += ' '
     
    return s_new 

s = input()
print(fb(s))