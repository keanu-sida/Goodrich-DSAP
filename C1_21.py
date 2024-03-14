## Write a Python program that repeatedly reads lines from standard input until an EOFError is raised, then outputs these lines in reverse order (user can indicate end of input with ctrl-D).

### initialize empty list of future inputs
ans = []

### run program until EOF command (ctrl-Z or ctrl-D, depending on OS) is entered
while True:
### use try-except block to check for exit command
    try:
        line = input()
### append input to answer list
        ans.append(line)
    except EOFError:
        break
### print answers in reverse order, joined by a new line character to make each line print on a new line
print('\n'.join(reversed(ans)))

