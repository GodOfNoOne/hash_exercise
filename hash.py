import hashlib
import csv
import itertools
def fill_table2(num_of_letters):
    if num_of_letters < 2 or num_of_letters > 6:
        raise ValueError("Number of letters should be between 2 and 6")

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    combinations = []

    for combination in itertools.product(alphabet, repeat=num_of_letters):
        combinations.append(''.join(combination))

    return combinations

def fill_table(start, stop):
    combinations=[]
    for num_of_letters in range(start, stop):
        temp_combinations = fill_table2(num_of_letters)
        combinations+=temp_combinations
    print('YEAHHHHHH BABYYYYYYY')
    return combinations


            

with open ('hash_table.csv','w',newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(['password','md5'])
    csvwriter.writerows(fill_table(6,7))
