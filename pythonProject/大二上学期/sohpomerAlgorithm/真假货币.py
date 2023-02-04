dicts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0}
# 手动改一下输入顺序，把有问题的后面才输入
use_input = [('ABCD', 'EFGH', 'even'), ('ABIJ', 'EFGH', 'even'), ('ABCI', 'EFJK', 'up')]
problem = []  # 记录假币
for element in use_input:
    # 平衡就把币标记为1
    if element[2] == 'even':
        s = element[0] + element[1]
        for val in s:
            dicts[val] = 1
    elif element[2] == 'up':
        # 计算两边的重量，确定真币处于的位置
        left, right = 0, 0
        for i in range(4):
            # 利用币对应的值确定假币，eg: dicts['A']=1, dicts['B']=0，那就能确定B是有问题的
            if dicts[element[0][i]] > dicts[element[1][i]]:
                problem.append(element[1][i])
            left += dicts[element[0][i]]
            right += dicts[element[1][i]]
        # 处于up状态时，假币在左边则为重，右边则为轻
        # up(右端高) 左边重，正常处于左边，假币就处于轻额一边。
        if left == 3:
            problem.append('重')
        elif right == 3:
            problem.append('轻')

print(f'{problem[0]}是假币并且他比真币{problem[1]}')
# 输出结果： K是假币并且他比真币轻
