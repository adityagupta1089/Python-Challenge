with open('../data/3.txt') as f:
    text = f.readlines()
for line in text:
    for cr in line:
        if cr == ' ':
            print(' ', end='')
        else:
            print(cr, end='')
