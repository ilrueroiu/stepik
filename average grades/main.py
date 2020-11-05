import re
with open('dataset_3363_4.txt', 'r') as file:
    new_lines = file.read()

cnt, average_grades = 1, []
lines = re.split(r'[;\n]', new_lines)

while cnt + 2 < len(lines):
    average_grades += [str((int(lines[cnt]) + int(lines[cnt + 1]) + int(lines[cnt + 2])) / 3)]
    cnt += 4


maths, phys, rus, new_count, cnt = 0, 0, 0, 0, 1


while cnt < len(lines):
    maths += int(lines[cnt])
    cnt += 4
    new_count += 1
av_maths = maths / new_count
new_count, cnt = 0, 2


while cnt < len(lines):
    phys += int(lines[cnt])
    cnt += 4
    new_count += 1
av_phys = phys / new_count
new_count, cnt = 0, 3


while cnt < len(lines):
    rus += int(lines[cnt])
    cnt += 4
    new_count += 1
av_rus = rus / new_count


average_grades_1 = [str(av_maths)] + [str(av_phys)] + [str(av_rus)]
print(average_grades)
print(average_grades_1)


with open('dataset_3363_4.txt', 'w') as file:
    file.writelines([grade + '\n' for grade in average_grades])
    file.writelines([grade + '\t' for grade in average_grades_1])













































































































