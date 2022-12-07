from aoc_utils.funcs import load_text_file
import re

# split main data
def split_input_from_instructions(data):
    delimiter = ''
    index_pos = data.index(delimiter)
    map = data[:index_pos]
    instructions = data[index_pos+1:]
    return map, instructions


# get instrcutions
def get_values_from_line(line):
    return re.findall(r"\d+", line)

def decode_instruction(instruction):
    values = get_values_from_line(instruction)
    decoded_instruction = {
        "amount" : int(values[0]),
        "source" : int(values[1]),
        "dest" : int(values[2])
    }
    return decoded_instruction

def decode_all_instructions(instructions):
    return [
        decode_instruction(line) 
        for line in instructions
        ]


# clean and process map data
def add_empty_items(line):
    '''converts space to show the correct number of empty containers'''
    regex = r"(^\s\s+)|(\s\s+)"
    res_str = re.sub(regex, replace_space_with_containers, line)
    return res_str

def replace_space_with_containers(match_obj):
    lookup_1 = [ "[", " ", "]", " "]
    lookup_2 = [ " ", "[", " ", "]"]
    mod = len(lookup_1)
    if match_obj.group(1) is not None:
        return "".join([lookup_1[i % mod] for i, _ in enumerate(match_obj.group())])
    if match_obj.group(2) is not None:
        return "".join([lookup_2[i % mod] for i, _ in enumerate(match_obj.group())])

def get_item_values(line):
    return re.findall(r"\[(.*?)\]", line)

def convert_lines_into_items_arrays(map):
    new_map = [add_empty_items(line) for line in map]
    new_map = [get_item_values(line) for line in new_map]
    return new_map

def remove_whitespace(line):
    return [item.strip() for item in line]


# build stacks from map
def convert_map_into_stacks(map):
    stack_names = get_stack_names(map[-1])
    items_in_map = clean_row_data_of_map(map[:-1])
    stacks = {
        stack: build_stack_from_map(items_in_map[::-1], stack)
        for stack in stack_names
        }
    return stacks

def get_stack_names(line):
    return [int(item) for item in get_values_from_line(line)]

def clean_row_data_of_map(map):
    map = convert_lines_into_items_arrays(map)
    map = [remove_whitespace(line) for line in map]
    return map

def build_stack_from_map(map, col_n):
    column = []
    for row in map:
        if (len(row) >= col_n) and (row[col_n - 1]):
            column.append(row[col_n - 1])
    return column


# perform instructions
def perform_instructions(stacks, instructions):
    [action_instruction(stacks, line) for line in instructions]
    return stacks

def action_instruction(stacks, instruction):
    move_item(
        stacks,
        instruction['source'],
        instruction['dest'],
        instruction["amount"]
        ) 
    return stacks

def move_item(stacks, src, dest, amount):
    items = stacks[src][-amount:]
    stacks[src] = stacks[src][:-amount]
    stacks[dest] += items
    return stacks

def read_stacks(stacks):
    return "".join([stack[-1] for name, stack in stacks.items()])


def run():
    address = "input.txt"
    data = load_text_file(address)

    map, instructions = split_input_from_instructions(data)
    stacks = convert_map_into_stacks(map)
    instructions = decode_all_instructions(instructions)

    stacks = perform_instructions(stacks, instructions)

    return read_stacks(stacks)


if __name__ == "__main__":
    print(run())