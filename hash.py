import hashlib
import csv
def fill_table(start, stop):
    if len(start) != len(stop):
        raise ValueError("Start and stop strings must have the same length")

    def generate_combinations(current, index):
        if index == len(current):
            combinations.append(''.join(current))
            return

        for char in range(ord(start[index]), ord(stop[index]) + 1):
            current[index] = chr(char)
            generate_combinations(current, index + 1)

    combinations = []
    generate_combinations(list(start), 0)

    return combinations

with open ('hash_table.csv','w',newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(['password','md5'])
    comb_list=fill_table("aaaaaa","zzzzzz")
    insert=[]
    for c in comb_list:
        insert.append([c,hashlib.md5(c.encode()).hexdigest()])
    csvwriter.writerows(insert)
