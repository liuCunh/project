class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


# 栈的经典操作：括号匹配
def brace_match(s):
    match = {'}': '{', ')': '(', ']': '['}
    stack = Stack()

    # 进栈出栈
    for ch in s:
        if ch in ['{', '[', '(']:
            stack.push(ch)
        else:  # ch in ['}', ']', ')']
            if stack.get_top() == match[ch]:  # 出栈
                stack.pop()
            elif stack.is_empty():  # 空栈
                return False
            else:  # stack.get_top() != match[ch]
                return False
    if stack.is_empty():
        return True
    else:
        return False


# print(brace_match('{()[{}([][{}()])]}'))
print(brace_match(']'))
