from aoc_utils.funcs import load_text_file, split_list_items

def cast_nested_list_to_int(data):
    if isinstance(data[0], list):
        return [cast_nested_list_to_int(item) for item in data]
    else:
        return [int(item) for item in data]


def check_intersections(range_1, range_2):
    inter = set(range(range_1[0], range_1[1]+1)).intersection(range(range_2[0], range_2[1]+1))
    return inter

def check_range_combinations(pair):
    if check_intersections(pair[0], pair[1]):
        return True
    if check_intersections(pair[1], pair[0]):
        return True
    return False


def run():
    address = "input.txt"
    data = split_list_items(load_text_file(address), delimiter=',')
    data = [split_list_items(item, "-") for item in data]
    data = cast_nested_list_to_int(data)
    
    data = sum([check_range_combinations(pair) for pair in data])


    return data

if __name__ == "__main__":
    print(run())