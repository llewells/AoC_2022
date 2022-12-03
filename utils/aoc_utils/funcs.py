def load_text_file(address):
    with open(address) as f:
        data = [line.rstrip() for line in f]
    return data
