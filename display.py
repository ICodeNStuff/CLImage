
def colored_sequence(char, rgb):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, char)
def display(arr, char):
    for i in arr:
        if i != 'n':
            print(colored_sequence(char, i), end='')
        else:
            print('\n', end= '')