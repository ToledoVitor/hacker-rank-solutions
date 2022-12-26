# That's not my solution.
# I just find it in hackerrank and found it amazing. Storing here to remember!

if __name__ == '__main__':
    # https://www.hackerrank.com/challenges/python-lists/problem
    N = int(input())
    return_list = []
    command_list = []
    
    for inputs in range(0, N):
        command_list.append(input())
        
    for command in command_list:
        if command == 'print':
            print(return_list)
        else:
            cmdArgs = command.split()
            operation_args = ','.join(cmdArgs[1:])
            exec('return_list.' + cmdArgs[0] + '(' + operation_args + ')')

