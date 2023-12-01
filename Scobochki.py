st = str(input())

correct = True
stack = []

for s in st:
    if s == '(' or s == '[' or s == '{':
        stack.append(s)
    elif s == ')' or s == ']' or s == '}':
        if len(stack) == 0:
            correct = False
            break
        elif (stack[-1] == '(' and s == ')') or (stack[-1] == '[' and s == ']') or (stack[-1] == '{' and s == '}'):
            stack.pop()
        else:
            stack.append(s)

if (correct and len(stack) == 0 and len(st) > 0):
    print('yes')
else:
    print('no')

