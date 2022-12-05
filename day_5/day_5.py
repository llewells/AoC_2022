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
        "iterations" : temp[0],
        "source" : temp[1],
        "dest" : temp[2]
    }
    return decoded_instruction

def decode_all_instructions(instructions):
    return [
        decode_instruction(line) 
        for line in instructions
        ]



def run():
    address = "test.txt"
    data = load_text_file(address)

    map, instructions = split_input_from_instructions(data)
    instructions = decode_all_instructions(instructions)
    return instructions

if __name__ == "__main__":
    print(run())