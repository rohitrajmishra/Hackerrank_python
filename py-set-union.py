eng_students_roll = []
french_students_roll = []

n = int(input())
set_eng_students_roll = set(input().split(' '))

b = int(input())
set_french_students_roll = set(input().split(' '))

set_union_students_roll = (set_eng_students_roll | set_french_students_roll)
print(len(set_union_students_roll))