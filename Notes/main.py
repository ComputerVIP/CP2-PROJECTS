#Vincent Johnson, Read Notes
import csv

with open("Notes/test.txt", "r") as file:
    content = file.read()
    print(content)
users = {}
with open("Notes\Class CSV sample - Sheet1.csv", "r") as file:
    cnt = csv.reader(file)
    next(cnt)
    for row in cnt:
        print(row)
    for row in cnt:
        users.update[{row[0]:row[1]}]
print(users)