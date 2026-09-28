from typing import Dict, List

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    age = list(age_dict.values())

    print(age)

# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))
