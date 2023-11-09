import hashlib
import pandas as pd 
def get_combinations(start, stop):
    combinations = []
    current = list(start)

    while current != list(stop):
        combinations.append(''.join(current))
        for i in range(len(current) - 1, -1, -1):
            if current[i] < stop[i]:
                current[i] = chr(ord(current[i]) + 1)
                break
            else:
                current[i] = start[i]

    combinations.append(''.join(current))
    return combinations



def get_all_combinations(start, stop):
    combinations = []
    start_len = len(start)
    stop_len = len(stop)
    for i in range(start_len, stop_len + 1):
        if i == len(start):
            combinations += get_combinations(start, stop[0:i])
        else:
            start += "a"
            combinations += get_combinations(start, stop[0:i])
    return combinations


def calculate_md5(input_string):
    md5_hash = hashlib.md5()  
    md5_hash.update(input_string.encode('utf-8'))  
    md5_digest = md5_hash.hexdigest()   
    return md5_digest

def get_md5_list(combinations):
    lst = []
    for c in combinations:
        lst.append(calculate_md5(c))
    return lst


def find_md5_index(md5_list, target_md5):
    for i in range(len(md5_list)):
        if md5_list[i] == target_md5:
            return i
        
    return -1  #Return -1 if the target MD5 is not found in the list


def decrypt(start, stop, md5):
    combinations = get_all_combinations(start, stop)
    md5_list = get_md5_list(combinations)
    print("md5 list is finished")
    index = find_md5_index(md5_list, md5)
    if(index != -1):
        return combinations[index]
    return ''


start = "aaaa"
stop = "zzzz"
md5 = "1b66f47c71f52e1e38434637f52b7c2c"
print(decrypt(start, stop, md5))






























"""
start = "aaa"
stop = "zzz"
combinations = get_all_combinations(start, stop)
md5_list = get_md5_list(combinations)


data = {
    'Combinations': combinations,
    'MD5 Hash': md5_list
}
df = pd.DataFrame(data)

# Specify the file name for the Excel file
excel_file_name = 'D:\Itay\הנדסת תוכנה\סייבר\combinations_and_md5.xlsx'

# Write the DataFrame to an Excel file
df.to_excel(excel_file_name, index=False)

print(f'Excel file "{excel_file_name}" created successfully.')
"""