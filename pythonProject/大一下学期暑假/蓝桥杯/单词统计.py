"""
小蓝正在学习一门神奇的语言，这门语言中的单词都是由小写英文字母组成，有些单词很长，远远超过正常英文单词的长度。小蓝学了很长时间也记不住一些单词，他准备不再完全记忆这些单词，而是根据单词中哪个字母出现得最多来分辨单词。现在，请你帮助小蓝，给了一个单词后，帮助他找到出现最多的字母和这个字母出现的次数。
【输入格式】
输入一行包含一个单词，单词只由小写英文字母组成。
【输出格式】
输出两行，第一行包含一个英文字母，表示单词中出现得最多的字母是哪个。如果有多个字母出现的次数相等，输出字典序最小的那个。
第二行包含一个整数，表示出现得最多的那个字母在单词中出现的次数。
【样例输入】
lanqiao
【样例输出】
a
2
【样例输入】
longlonglongistoolong
【样例输出】
o
6
"""


def word_count(s):
    words = dict()
    i = 97

    # 创建一个字典来统计单词出现的次数，例如{'a':0,'b':1,'c':0}
    while i <= 122:
        words[chr(i)] = 0
        i += 1
    for val in s:
        words[val] += 1
    max_total, max_val = 0, ""
    for element, total in words.items():
        if total > max_total:
            max_total = total
            max_val = element
    print(max_val)
    print(max_total)


word_count("longlonglongistoolong")
