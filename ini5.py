import sys


# Version #1:
def write_even_lines(input_file, output_file):
    """Outputs a file with only the even lines of the input file.
    Lines starting at 1.
    """
    with open(input_file) as read_in:
        with open(output_file, 'w') as print_out:
            lines = read_in.readlines()
            for i, line in enumerate(lines):
                if (i + 1) % 2 == 0:
                    print_out.write(line)

# Version #2 after seeing other solutions. It makes more sense outputting to stdout
# than writing to a file. If the user wants to write to a file it can pipe it.
def write_even_lines2(input_file):
    with open(input_file) as f:
        print(''.join(f.readlines()[1::2]))


if __name__ == '__main__':
    try:
        write_even_lines2(sys.argv[1])
    except IndexError:
        print('Please provide filename of input as argument')
