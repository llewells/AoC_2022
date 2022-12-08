from aoc_utils.funcs import load_text_file

def find_marker(signal, size):
    for n, _ in enumerate(signal):
        window = get_window(signal, n, size)
        if is_window_marker(window, size):
            return (n + size)
    return None
    
def is_window_marker(window, size):
    if len(set(window)) == size:
        return True
    return False

def get_window(signal, n, size):
    slice = signal[n:n+size]
    return slice

def run():
    address = "input.txt"
    signals = load_text_file(address)
    answers = [find_marker(signal, size=14) for signal in signals]
    return answers


if __name__ == '__main__':
    print(run())
