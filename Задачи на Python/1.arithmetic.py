def arithmetic(arg1, arg2, action):
    if action == '+': print (arg1 + arg2)
    elif action == '-': print (arg1 - arg2)
    elif action == '*': print (arg1 * arg2)
    elif action == '/': print (arg1 / arg2)

arg1 = input()
arg2 = input()
action = input()

arithmetic(int(arg1),int(arg2),action)
