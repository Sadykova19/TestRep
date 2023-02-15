

import modul1
import modul2

merged_dict = {**modul1.my_dict, **modul2.my_dict}

with open("merged_dict.txt", "w") as f:
    for key, value in merged_dict.items():
        f.write(f"{key}: {value}\n")

print(merged_dict)