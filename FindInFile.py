# -*- encode: utf-8 -*-

pathFile = "path"
pattern = "what need to find"

with open(pathFile, 'r', encoding='utf-8') as f:
    for line in f:
        if pattern in line.lower():
            print(line, end='')