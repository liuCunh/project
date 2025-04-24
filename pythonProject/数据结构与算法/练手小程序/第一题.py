"""
给两个字符串s和t，判断t是否为s的重新排列后组成的单词
s='anagram',t='nagaram',return True
s='rat',t='car',return False
"""
# anagram aangram a
def func(s, t):
    tmp = s
    for i in range(len(s)):
        li_tmp = []
        for j in range(len(s)):
            if tmp[i] != s[j]:
                if s[j] not in li_tmp:
                    li_tmp.append(s[j])
                    s = s.replace(s[i], s[j], 1)
                    if s == t:
                        return True
                    else:
                        return False
        li_tmp.clear()
        s = tmp


def isAnagram(s, t):

    # 方法一
    # ss = list(s)
    # tt = list(t)
    # ss.sort()
    # tt.sort()
    # return ss == tt

    # 方法二
    # dict1 = {}
    # dict2 = {}
    # for ch in s:
    #     dict1[ch] = dict1.get(ch, 0) + 1
    # print(f'dict1={dict1}')
    # for ch in s:
    #     dict2[ch] = dict2.get(ch, 0) + 1
    # return dict1 == dict2

    # 方法三
    return sorted(list(s)) == sorted(list(t))


s = "anagram"
t = 'nagaram'
print(isAnagram(s, t))