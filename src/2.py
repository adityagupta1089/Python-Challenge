with open('../data/3.txt') as f:
    text = f.readlines()
for line in text:
    for cr in line:
        if 'a' <= cr and cr <= 'z':
            print(cr, end='')
print()
