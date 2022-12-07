from aoc_utils.funcs import load_text_file


def split_input_from_instructions(data):
    delimiter = ''
    index_pos = data.index(delimiter)
    map = data[:index_pos]
    instructions = data[index_pos+1:]
    return map, instructions

def decode_instruction(instruction):
    temp = instruction.split(' ')
    to_remove = ['move', 'from', 'to']
    [temp.remove(item) for item in to_remove]
    decoded_instruction = {
        "iterations" : int(temp[0]),
        "source" : int(temp[1]),
        "dest" : int(temp[2])
    }
    return decoded_instruction

def decode_all_instructions(instructions):
    return [
        decode_instruction(line) 
        for line in instructions
        ]


def replace_pattern_in_string(line, pattern, new):
    line = line.replace(pattern, new)
    return line

def replace_pattern_in_map(map):

    ### Need to replace withe regex that looks for gap of 2 or more spaces
    ### when rounf replace each point using the patter [" ", "[", " ", "]"]
    ### this will change "[P]     [R]" -> "[P] [ ] [R]" 

    new_map = [
        replace_pattern_in_string(line, pattern="     ", new="[ ]")
        for line in map
    ]

    new_map = [
        replace_pattern_in_string(line, pattern="][", new="],[")
        for line in new_map
    ]

    # new_map = [
    #     replace_pattern_in_string(line, pattern="]", new="")
    #     for line in new_map
    # ]

    # new_map = [
    #     replace_pattern_in_string(line, pattern="[", new="")
    #     for line in new_map
    # ]

    new_map[-1] = replace_pattern_in_string(map[-1], pattern="   ", new=",")
 
    return new_map

def split_and_strip(line):
    return [item.strip() for item in line.split(",")]

def clean_row_data_of_map(map):
    map = replace_pattern_in_map(map)
    map = [split_and_strip(line) for line in map]
    map[-1] = [int(item) for item in map[-1]]
    return map

def build_stack_from_map(map, col_n):
    column = []
    for row in map:
        if (len(row) >= col_n) and (row[col_n - 1]):
            column.append(row[col_n - 1])
    return column
    
    
def convert_map_into_stacks(map):
    map = clean_row_data_of_map(map)
    stack_names = map[-1]
    items_in_map = map[:-1]
    stacks = {
        stack: build_stack_from_map(items_in_map[::-1], stack)
        for stack in stack_names
        }
    return stacks


def perform_instructions(stacks, instructions):
    [action_instruction(stacks, line) for line in instructions]
    return stacks

def action_instruction(stacks, instruction):
    [
        move_item(
            stacks,
            instruction['source'],
            instruction['dest']
            ) 
        for _ in range(instruction["iterations"])
    ]
    
    return stacks

def move_item(stacks, src, dest):
    item = stacks[src][-1]
    stacks[src].pop()
    stacks[dest].append(item)
    return stacks

def read_stacks(stacks):
    return "".join([stack[-1] for name, stack in stacks.items()])


def run():
    address = "input.txt"
    data = load_text_file(address)

    map, instructions = split_input_from_instructions(data)
    stacks = convert_map_into_stacks(map)
    # instructions = decode_all_instructions(instructions)

    # stacks = perform_instructions(stacks, instructions)

    # return read_stacks(stacks)

    

    return replace_pattern_in_map(map)


if __name__ == "__main__":
    print(run())