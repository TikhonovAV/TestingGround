# -*- encode: utf-8 -*-

pathFile = "file"

with open(pathFile, 'r', encoding='utf-8') as f:
    strNumber = sum(1 for i in f)
    print("Количество строк в файле: ", strNumber)
