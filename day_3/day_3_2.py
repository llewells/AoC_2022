from aoc_utils.funcs import load_text_file
import string

PRIORITY = {
    letter: index +1 for 
    index, letter in 
    enumerate(
        string.ascii_lowercase + string.ascii_uppercase
        )
}

def split_bags_into_groups(bags, n):
    return [
        bags[index:index+n] 
        for index in range(0, len(bags), n)
        ]

def get_intersection_of_group(group):
    results = set(group[0]).intersection(*group[1:])
    return list(results)

def get_all_intersections_in_groups(groups):
    return [
        get_intersection_of_group(group)
        for group in groups
        ]

def get_priority(bag):
    return sum([PRIORITY[item] for item in bag])

def get_total_sum_of_priority(bags):
    return sum([get_priority(bag) for bag in bags])


def run():
    address = "input.txt"
    groups = split_bags_into_groups(load_text_file(address), n=3)
    result = get_all_intersections_in_groups(groups)
    return get_total_sum_of_priority(result)

if __name__ == "__main__":
    print(run())