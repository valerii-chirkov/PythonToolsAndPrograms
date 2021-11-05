def str_to_bin():
    filepath = '/Users/valeriichirkov/PycharmProjects/Own Projects/ValeriiChirkovBot/bot.py'
    # filepath = sys.argv[1]
    f = open(filepath, 'r')
    st = f.read()

    # Convert the string to binary
    bin_data = ' '.join(format(ord(x), 'b') for x in st)

    # Display the string
    print(bin_data)


def str_to_bin_func_style(path_to_file):
    bin_data = ' '.join(format(ord(x), 'b') for x in open(path_to_file, 'r').read())
    print(bin_data)
