import os
import csv
def read_integer():
    i=int(input())
    return i
def read_file(s):
    if os.path.exists(s):
        return open(s, "r")
    else:
        return 0
def write_file(s):
    if os.path.exists(s):
        return open(s,'a')
    else:
        return 0
def display_all(mode):
    f=read_file("data_set.csv")
    if f==0:
        return "file not found"
    csvreader = csv.reader(f)


    fields = next(csvreader)
    rows = []
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
    print('Field names are:' + ', '.join(field for field in fields))
    for row in rows:
        # parsing each column of a row
        for col in row:
            print(col+" ",end='')
        print()

def search_by_id(val):
    f=read_file("data_set.csv")
    if f == 0:
        return "file not found"

    csv_file = csv.reader(f)

    # loop through the csv list
    for row in csv_file:
        # if current rows 2nd value is equal to input, print that row
        if val == row[0]:
            print("Id:",row[0])
            print("First Name:",row[1])
            print("Last Name:", row[2])
            print("Age:", row[3])
            print("Place of Birth:", row[4])
            print("Address:", row[5])
            print("Caste:", row[6])
            print("Citizenship:",row[7])
            return 1
    return 0



def add():
    id=input()
    temp=search_by_id(id)
    if(temp==1):
        print("Id already exsist")
        return 0
    fn=input()
    ln=input()
    a=input()
    pb=input()
    ad=input()
    ct=input()
    citi=input()
    ll=[id,fn,ln,a,pb,ad,ct,citi]
    temp=write_file("data_set.csv")
    writer = csv.writer(temp)
    writer.writerow(ll)






while(True):
    i=int(input())
    if i==1:
        display_all(0)
    elif i==2:
        temp=input()
        search_by_id(temp)
    elif i==3:
        add()

    else:
        break
