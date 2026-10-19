records=[]
for _ in range(int(input())):
    name=input()
    score=float(input())
    records.append([name,score])
grades=sorted(set(student[1] for student in records))
second_lowest=grades[1]
names=sorted(student[0] for student in records if student[1]==second_lowest)

for name in names:
    print(name)
