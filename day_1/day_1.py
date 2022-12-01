def load_text_file(address):
    with open(address) as f:
        data = [line.rstrip() for line in f]
    return data

def cast_data_to_int(data):
    return [int(item) if item else None for item in data]

def split_data_into_elves(data):
    elves = {}
    count = 0
    sub_list = []

    for item in data:
        if item:
            sub_list.append(item)
        else:
            elves[count] = sum(sub_list)
            count += 1
            sub_list = []
    return elves

def find_elf_with_most_cals(elves):
    highest_cal = 0
    for elf, cals  in elves.items():
        if cals > highest_cal:
            highest_cal = cals
    return highest_cal

def sort_elves_by_cals(elves):
    cal_dict = {}
    for elf, cals in elves.items():
        cal_dict.setdefault(cals, []).append(elf)
    return cal_dict

def sort_call_values(cal_dict):
    return sorted(list(cal_dict.keys()), reverse=True)

def get_top_elves(cal_dict, n):
    ordered_cals = sort_call_values(cal_dict)
    top_cal = ordered_cals[:n]
    total_cals = sum(top_cal)
    return total_cals

def run(address):
    data = load_text_file(address)
    data= cast_data_to_int(data)
    elves = split_data_into_elves(data)
    cals = sort_elves_by_cals(elves)
    total_cals = get_top_elves(cals, n=3)
    return total_cals


if __name__ == '__main__':
    address = "input.txt"
    print(run(address))
