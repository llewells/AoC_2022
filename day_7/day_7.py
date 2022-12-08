from aoc_utils.funcs import load_text_file


def run():
    address = "test.txt"
    signals = load_text_file(address)
    return signals


if __name__ == '__main__':
    print(run())
