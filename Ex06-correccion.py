def find_lost_numbers(original_list:list) -> list:
    lost_numbers = []
    for i in range(1, len(original_list)):
        num_ant = original_list[i-1]
        num = original_list[i]
        if num <= num_ant:
            return "error"
        if num - num_ant > 1:
            lost_numbers.extend(range(num_ant+1, num))
    return lost_numbers