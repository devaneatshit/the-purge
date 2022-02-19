with open('./hitlist.txt', 'r') as f:
    lines = f.readlines()
lines = ['.ban '+line for line in lines]
with open('./commands.txt', 'w') as f:
    f.writelines(lines)