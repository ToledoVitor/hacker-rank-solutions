def print_pattern(line_number: int, line_size: int, total_lines: int, filler='-'):
    if line_number <= int(total_lines / 2 - 0.5):
        factor = line_number
        factor += (factor - 1)
    else:
        factor = total_lines - line_number + 1
        factor += (factor - 1)

    string = ((".|.") * factor).center(line_size, filler)
    print(string)
    

def print_welcome(line_size: int, filler='-'):
    string = "WELCOME".center(line_size, filler)
    print(string)


def print_doormat(line_size:int, total_lines: int):
    for idx in range(total_lines):
        if idx == int(total_lines / 2 - 0.5):
            print_welcome(line_size=line_size)
            continue
        
        print_pattern(line_number=idx+1, line_size=line_size, total_lines=total_lines)


print_doormat(27, 9)
