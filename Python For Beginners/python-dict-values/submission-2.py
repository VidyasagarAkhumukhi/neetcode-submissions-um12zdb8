from typing import Dict, List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    result_list = []
    for value in age_dict.values():
        result_list.append(value)
    return result_list




# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
