import hashlib
import csv
def fill_table(start='aaaaaa',stop='zzzzzz'):
    if ord(start[-1])+1<= ord('z'):
        start_list=list(start)
        start_list[-1]=chr(ord(start_list[-1]) + 1)
        start=''.join(start_list)
        print(start)
    
with open ('hash_table.csv','w',newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(['password','md5'])
    fill_table()
    


