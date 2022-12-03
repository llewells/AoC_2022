from aoc_utils.funcs import load_text_file
import string

PRIORITY = {
    letter: index +1 for 
    index, letter in 
    enumerate(
        string.ascii_lowercase + string.ascii_uppercase
        )
}

def split_bag_into_compartments(bag):
    mid = int(len(bag)/2)
    split_bag = [bag[:mid], bag[mid:]]
    return split_bag

def split_all_bags(bags):
    return [split_bag_into_compartments(bag) for bag in bags]

def get_intersection_of_compartments(bag):
    comp_1, comp_2 = bag
    results = set(comp_1).intersection(comp_2)
    return list(results)

def get_all_intersections_in_bags(bags):
    return [
        get_intersection_of_compartments(bag)
        for bag in bags
        ]

def get_priority(bag):
    return sum([PRIORITY[item] for item in bag])

def get_total_sum_of_priority(bags):
    return sum([get_priority(bag) for bag in bags])



def run():
    address = "input.txt"
    bags = split_all_bags(load_text_file(address))
    result = get_all_intersections_in_bags(bags)
    return get_total_sum_of_priority(result)

if __name__ == "__main__":
    print(run())