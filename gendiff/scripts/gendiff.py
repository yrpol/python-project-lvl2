import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate diff")

    # positional arguments
    parser.add_argument("first_file", type=argparse.FileType('r', encoding='utf-8'), help="first file to compare")
    parser.add_argument("second_file", type=argparse.FileType('r', encoding='utf-8'), help="second file to compare")

    #optional arguments
    parser._optionals.title = "optionals arguments"
    parser.add_argument("-f", "--format", help="set format to output")

    args = parser.parse_args()


if __name__ == '__main__':
    main()
